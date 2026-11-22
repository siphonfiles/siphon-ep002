# SeedVR2-3B image restoration, Upsampler v3 recipe.
#
# Ported from ByteDance-Seed/SeedVR2-3B. What changed and why:
#
# 1. Image only. The upstream Space serves video and images from one entry
#    point, carrying the sequence-parallel plumbing, frame cutting and video
#    writing along with it. This Space backs an image tool, so that is all gone.
# 2. ONE @spaces.GPU entry. Upstream decorates configure_runner,
#    generation_step AND generation_loop, so a single request booked three GPU
#    allocations of 100s each. ZeroGPU checks the requested duration against the
#    visitor's remaining quota, and an unauthenticated visitor has 120 seconds a
#    day in total, so the upstream shape cannot serve an anonymous user at all.
#    Everything now runs inside one call with a measured dynamic duration.
# 3. No apex. Upstream installs a prebuilt `apex-0.1-cp310-...whl` and selects
#    `fusedrms` / `fusedln` norms in configs_3b/main.yaml. ZeroGPU runs Python
#    3.12, where that wheel does not install, so every norm layer then failed.
#    The config now selects the `rms` / `layer` paths that the same source file
#    already implements in pure PyTorch, with identical parameter names and
#    shapes so the checkpoint loads unchanged.
# 4. No hard flash-attn dependency. See models/dit_v2/attention.py.
#
# The model restores at a fixed working resolution regardless of input size (it
# was trained at high res and NaResize scales the input to meet it), so GPU cost
# per request is essentially constant and no tiling is involved. See WORK_AREA.

# Must precede the torch import: the allocator reads this at initialization.
#
# Fragmentation insurance, NOT the fix for the NVML assert this Space used to
# die on. That was measured: the ZeroGPU worker printed
# 'expandable_segments:True' on the runs that still crashed, so the setting was
# applied the whole time and made no difference. What actually decides it is
# WORK_AREA below. Kept because it costs nothing and reduces fragmentation.
import os
import random
import tempfile

os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

import gc

import mimetypes
from pathlib import Path

import gradio as gr
import spaces
import torch
import torch.nn.functional as F
from einops import rearrange
from omegaconf import OmegaConf
from PIL import Image
from huggingface_hub import hf_hub_download
from torchvision.transforms import Compose, Lambda, Normalize
import torchvision.transforms as T

from upsampler_theme import UPSAMPLER_CSS, UPSAMPLER_THEME, footer_html, header_html

from data.image.transforms.divisible_crop import DivisibleCrop
from data.image.transforms.na_resize import NaResize
from data.video.transforms.rearrange import Rearrange
from common.config import load_config
from common.distributed import init_torch
from common.seed import set_seed
from projects.video_diffusion_sr.infer import VideoDiffusionInfer

try:
    from projects.video_diffusion_sr.color_fix import wavelet_reconstruction

    USE_COLOR_FIX = True
except ImportError:
    USE_COLOR_FIX = False
    print("color fix unavailable; output will not be wavelet-reconstructed")

# Weights come from the official ByteDance repo rather than a re-upload. It is
# the canonical source for these files and is Apache-2.0, so there is no mirror
# in the chain that could change under us.
WEIGHTS_REPO = "ByteDance-Seed/SeedVR2-3B"
CKPT_DIR = Path("./ckpts")
CKPT_DIR.mkdir(exist_ok=True)


def _fetch(filename: str, target: Path) -> str:
    if target.exists():
        return str(target)
    path = hf_hub_download(repo_id=WEIGHTS_REPO, filename=filename)
    target.symlink_to(path)
    return str(target)


DIT_CKPT = _fetch("seedvr2_ema_3b.pth", CKPT_DIR / "seedvr2_ema_3b.pth")
VAE_CKPT = _fetch("ema_vae.pth", CKPT_DIR / "ema_vae.pth")
# The text branch is conditioned by two fixed embeddings shipped with the
# weights, so this Space runs no text encoder at all.
POS_EMB = _fetch("pos_emb.pt", Path("./pos_emb.pt"))
NEG_EMB = _fetch("neg_emb.pt", Path("./neg_emb.pt"))

# The resolution the model restores at, as an area. Upstream hardcodes
# 2560*1440 for images with `downsample_only=False`, meaning small inputs are
# scaled UP to it and large inputs down, because the model was only trained at
# high resolution.
#
# THIS is what decides whether the VAE decode survives on ZeroGPU. The
# decoder's peak contiguous allocation scales with it, and that allocation is
# what trips "NVML_SUCCESS == r INTERNAL ASSERT FAILED" in the caching
# allocator. Measured: 2560x1440 (the upstream value) fails, 1920x1080 passes
# in 14.7s. Left overridable so the ceiling can be probed without a code
# change, but do not raise the default without re-testing a real run.
#
# The cost is honest to state: the model was trained at high resolution, so
# restoring at 2MP rather than 3.7MP gives up some of its headroom on very
# large outputs. It still upscales ~4.9x from a 360x240 input.
WORK_AREA = int(os.environ.get("SEEDVR2_WORK_AREA", 1920 * 1080))
# 0 = a fresh random seed per request (the premium worker does the same);
# any other value pins it, for probes.
DEFAULT_SEED = int(os.environ.get("SEEDVR2_SEED", 0))
# Strength of the noise added to the conditioning latent before the SR pass,
# as a fraction of the 1000-step schedule. 0.0 matches upstream's image
# inference script (projects/inference_seedvr2_3b.py, cond_noise_scale) and
# the premium worker (the ComfyUI node's latent_noise_scale, which is this
# same step, runs at 0.0 there). The first port of this Space wrote 0.1,
# which put 12-22 single-token bright blemishes on every result (measured
# 2026-10-14, three seeds; 0.05 left 0-1, 0.0 left none, with no loss of
# detail or JPEG deblocking). Env override for probes.
INPUT_NOISE = float(os.environ.get("SEEDVR2_INPUT_NOISE", 0.0))
# Upstream runs under bf16 autocast; fp16 is an override for artifact probes.
AUTOCAST_DTYPE = {"bf16": torch.bfloat16, "fp16": torch.float16}[
    os.environ.get("SEEDVR2_AUTOCAST", "bf16")
]

# Single-process "distributed" context. The model code routes every device
# placement through common.distributed, which reads these.
os.environ.setdefault("MASTER_ADDR", "127.0.0.1")
os.environ.setdefault("MASTER_PORT", "12355")
os.environ.setdefault("RANK", "0")
os.environ.setdefault("WORLD_SIZE", "1")
os.environ.setdefault("LOCAL_RANK", "0")

_runner = None


def _ensure_runner():
    """Build the runner once, inside a GPU context.

    Deliberately NOT done at module scope, even though ZeroGPU prefers that for
    placement: `init_torch` ends in `dist.init_process_group(backend="nccl")`
    and `torch.cuda.set_device`, which need a real device rather than the CUDA
    emulation that applies outside `@spaces.GPU`. Memoized because
    `init_process_group` raises if called twice, and because a warm worker
    should not reload 3B parameters per request.
    """
    global _runner
    if _runner is not None:
        return _runner

    if not torch.distributed.is_initialized():
        init_torch(cudnn_benchmark=False)

    runner = VideoDiffusionInfer(load_config(os.path.join("./configs_3b", "main.yaml")))
    OmegaConf.set_readonly(runner.config, False)
    runner.configure_dit_model(device="cuda", checkpoint=DIT_CKPT)
    runner.configure_vae_model()
    if hasattr(runner.vae, "set_memory_limit"):
        runner.vae.set_memory_limit(**runner.config.vae.memory_limit)

    _runner = runner
    return _runner


def _transform():
    return Compose(
        [
            NaResize(resolution=WORK_AREA**0.5, mode="area", downsample_only=False),
            Lambda(lambda x: torch.clamp(x, 0.0, 1.0)),
            DivisibleCrop((16, 16)),
            Normalize(0.5, 0.5),
            Rearrange("t c h w -> c t h w"),
        ]
    )


def _duration(image, steps=1, seed=0, progress=None) -> int:
    """Every request restores at the same working resolution (WORK_AREA), so cost
    tracks the step count and little else. Measured on a cold worker, then
    given headroom; kept as small as honesty allows, because the request is
    checked against the visitor's remaining quota and a smaller one also ranks
    higher in the ZeroGPU queue."""
    # Scaled by the working area: the measured 12 s/step was at the default
    # 2 MP, and a bigger area (SEEDVR2_WORK_AREA override) runs longer.
    area_scale = WORK_AREA / (1920 * 1080)
    return int(min(90, 14 + 12 * int(steps) * area_scale))


# Gradio saves a PIL or array result as WebP at Pillow's default quality of 80,
# which throws away exactly the fine detail the model just produced (and that
# file is what the free tool hands the visitor to download). Write the result
# ourselves at quality 95 and return the path: Gradio serves a path as is.
OUTPUT_WEBP_QUALITY = 95
WEBP_MAX_SIDE = 16383  # libwebp's hard limit; larger results fall back to PNG


def save_result(image):
    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)
    out_dir = tempfile.mkdtemp(prefix="upsampler-result-")
    if max(image.size) > WEBP_MAX_SIDE:
        path = os.path.join(out_dir, "upscaled.png")
        image.save(path, "PNG")
    else:
        path = os.path.join(out_dir, "upscaled.webp")
        image.save(path, "WEBP", quality=OUTPUT_WEBP_QUALITY, method=4)
    return path


@spaces.GPU(duration=_duration)
@torch.no_grad()
def upscale_image(image, steps=1, seed=0, progress=gr.Progress(track_tqdm=True)):
    if image is None:
        raise gr.Error("Upload an image first.")

    # The allocator config has to be read by the process that actually owns the
    # CUDA context. ZeroGPU runs this function in its own worker, so an env var
    # exported at import time in the parent is not proof it applied here —
    # print what the worker sees, and set it directly as well.
    print(f"[alloc] PYTORCH_CUDA_ALLOC_CONF={os.environ.get('PYTORCH_CUDA_ALLOC_CONF')!r}", flush=True)
    try:
        torch.cuda.memory._set_allocator_settings("expandable_segments:True")
        print("[alloc] expandable_segments set at runtime", flush=True)
    except Exception as exc:  # older/newer torch may not expose this
        print(f"[alloc] runtime allocator setting unavailable: {exc}", flush=True)
    print(f"[alloc] work area {WORK_AREA} px", flush=True)

    runner = _ensure_runner()

    runner.config.diffusion.cfg.scale = 1.0
    runner.config.diffusion.cfg.rescale = 0.0
    runner.config.diffusion.timesteps.sampling.steps = int(steps)
    runner.configure_diffusion()
    # Random seed per request by default, like the premium worker, so a
    # blemish that lands on a face in one run is elsewhere in the next. The
    # API takes an explicit seed (hidden in the UI) so artifacts can be
    # checked across seeds without a redeploy.
    chosen = int(seed) or DEFAULT_SEED or random.randrange(1, 2**31)
    print(f"[seed] {chosen}", flush=True)
    set_seed(chosen, same_across_ranks=True)

    img = Image.open(image).convert("RGB") if isinstance(image, str) else image.convert("RGB")
    tensor = T.ToTensor()(img).unsqueeze(0)  # (t=1, c, h, w)

    cond = _transform()(tensor.to("cuda"))
    original = cond
    latents = runner.vae_encode([cond])

    text_embeds = {
        "texts_pos": [torch.load(POS_EMB).to("cuda")],
        "texts_neg": [torch.load(NEG_EMB).to("cuda")],
    }

    noise = [torch.randn_like(latent) for latent in latents]
    aug_noise = [torch.randn_like(latent) for latent in latents]

    def _add_noise(x, aug):
        t = torch.tensor([1000.0], device="cuda") * INPUT_NOISE
        shape = torch.tensor(x.shape[1:], device="cuda")[None]
        return runner.schedule.forward(x, aug, runner.timestep_transform(t, shape))

    conditions = [
        runner.get_condition(n, task="sr", latent_blur=_add_noise(latent, a))
        for n, a, latent in zip(noise, aug_noise, latents)
    ]

    with torch.autocast("cuda", AUTOCAST_DTYPE, enabled=True):
        videos = runner.inference(
            noises=noise, conditions=conditions, dit_offload=False, **text_embeds
        )

    sample = videos[0]
    sample = (
        rearrange(sample[:, None], "c t h w -> t c h w")
        if sample.ndim == 3
        else rearrange(sample, "c t h w -> t c h w")
    )
    reference = (
        rearrange(original[:, None], "c t h w -> t c h w")
        if original.ndim == 3
        else rearrange(original, "c t h w -> t c h w")
    )
    if USE_COLOR_FIX:
        sample = wavelet_reconstruction(sample.to("cpu"), reference[: sample.size(0)].to("cpu"))
    else:
        sample = sample.to("cpu")

    sample = rearrange(sample, "t c h w -> t h w c")
    sample = sample.clip(-1, 1).mul_(0.5).add_(0.5).mul_(255).round().to(torch.uint8).numpy()

    del latents, conditions, videos
    gc.collect()
    torch.cuda.empty_cache()

    return save_result(sample[0])


with gr.Blocks(css=UPSAMPLER_CSS, theme=UPSAMPLER_THEME) as demo:
    gr.HTML(
        header_html(
            "SeedVR2 3B Image Upscaler",
            "One-step diffusion restoration that rebuilds real detail in blurry, "
            "compressed, and low-resolution photos.",
        )
    )

    with gr.Row():
        with gr.Column():
            image_in = gr.Image(label="Image", type="filepath")
            steps = gr.Slider(1, 4, value=1, step=1, label="Steps")
            # API-only: 0 keeps the fixed default seed.
            seed = gr.Number(value=0, precision=0, visible=False)
            run = gr.Button("Upscale Image", variant="primary")
        with gr.Column():
            image_out = gr.Image(label="Result", type="filepath")

    # No leading slash: gradio prefixes it, and "/upscale_image" here would
    # publish the endpoint as "//upscale_image".
    run.click(
        upscale_image,
        inputs=[image_in, steps, seed],
        outputs=[image_out],
        api_name="upscale_image",
    )

    gr.HTML(
        footer_html(
            "SeedVR2-3B is ByteDance's one-step diffusion model for image and video "
            "restoration. It rebuilds genuine texture in photos that are blurry, "
            "heavily compressed, or simply too small, restoring at high resolution "
            "rather than smoothing detail away the way a conventional upscaler does.",
            "https://upsampler.com/free-image-upscaler-no-signup",
            "free image upscaler",
        )
    )

demo.launch(ssr_mode=False, show_error=True)
