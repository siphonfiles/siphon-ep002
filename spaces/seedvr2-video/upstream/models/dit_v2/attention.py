# // Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# //
# // Licensed under the Apache License, Version 2.0 (the "License");
# // you may not use this file except in compliance with the License.
# // You may obtain a copy of the License at
# //
# //     http://www.apache.org/licenses/LICENSE-2.0
# //
# // Unless required by applicable law or agreed to in writing, software
# // distributed under the License is distributed on an "AS IS" BASIS,
# // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# // See the License for the specific language governing permissions and
# // limitations under the License.

import torch
import torch.nn.functional as F

from torch import nn

# CHANGED FROM UPSTREAM (Upsampler): flash-attn is imported lazily instead of at
# module scope, and falls back to PyTorch SDPA when it is unavailable.
#
# Upstream ships a prebuilt `apex-0.1-cp310-...whl` and expects a flash-attn
# built against torch 2.4. ZeroGPU runs Python 3.12 on torch 2.8+, where neither
# installs, so the module-scope import took the whole Space down at startup.
try:
    from flash_attn import flash_attn_varlen_func
except ImportError:  # pragma: no cover - depends on the runtime image
    flash_attn_varlen_func = None


def _sdpa_varlen(q, k, v, cu_seqlens_q, cu_seqlens_k, max_seqlen_q, max_seqlen_k, **_):
    """SDPA equivalent of `flash_attn_varlen_func` for this model's usage.

    Only the shape this DiT actually calls is supported, and every one of those
    constraints is asserted rather than assumed: packed `(total_len, heads,
    head_dim)` self-attention, identical q/k segmentation, no causal mask, no
    dropout, and the default softmax scale. Sequences are unpacked from
    `cu_seqlens`, attended independently, and repacked — with a batch of one
    (every request this Space serves) that is a single unmasked SDPA call, so
    the fallback is not a slow path so much as a direct one.
    """
    assert torch.equal(cu_seqlens_q, cu_seqlens_k), (
        "the SDPA fallback assumes self-attention with one segmentation"
    )
    lengths = (cu_seqlens_q[1:] - cu_seqlens_q[:-1]).tolist()
    out = []
    start = 0
    for length in lengths:
        end = start + length
        # (l h d) -> (1 h l d), attend, then back to (l h d).
        segment = [
            x[start:end].transpose(0, 1).unsqueeze(0) for x in (q, k, v)
        ]
        attended = F.scaled_dot_product_attention(*segment)
        out.append(attended.squeeze(0).transpose(0, 1))
        start = end
    return torch.cat(out, dim=0)

class TorchAttention(nn.Module):
    def tflops(self, args, kwargs, output) -> float:
        assert len(args) == 0 or len(args) > 2, "query, key should both provided by args / kwargs"
        q = kwargs.get("query") or args[0]
        k = kwargs.get("key") or args[1]
        b, h, sq, d = q.shape
        b, h, sk, d = k.shape
        return b * h * (4 * d * (sq / 1e6) * (sk / 1e6))

    def forward(self, *args, **kwargs):
        return F.scaled_dot_product_attention(*args, **kwargs)


class FlashAttentionVarlen(nn.Module):
    def tflops(self, args, kwargs, output) -> float:
        cu_seqlens_q = kwargs["cu_seqlens_q"]
        cu_seqlens_k = kwargs["cu_seqlens_k"]
        _, h, d = output.shape
        seqlens_q = (cu_seqlens_q[1:] - cu_seqlens_q[:-1]) / 1e6
        seqlens_k = (cu_seqlens_k[1:] - cu_seqlens_k[:-1]) / 1e6
        return h * (4 * d * (seqlens_q * seqlens_k).sum())

    def forward(self, *args, **kwargs):
        if flash_attn_varlen_func is None:
            return _sdpa_varlen(*args, **kwargs)
        kwargs["deterministic"] = torch.are_deterministic_algorithms_enabled()
        return flash_attn_varlen_func(*args, **kwargs)
