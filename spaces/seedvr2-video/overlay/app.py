# SeedVR2-3B VIDEO restoration (Siphon Files), private Space.
#
# Built on the fixed image port Upsampler/seedvr2-3b (Apache-2.0), which itself
# ports ByteDance-Seed/SeedVR2-3B (Apache-2.0). From Upsampler we keep: no apex
# (pure-PyTorch rms/layer norms in configs_3b/main.yaml), no hard flash-attn,
# torch pinned to what ZeroGPU supports, ONE @spaces.GPU entry with a dynamic
# duration (the official Space books three 100 s allocations per request and no
# longer installs on Python 3.12). From the official Space we bring back the
# video path: frame reading, padding to 4n+1 frames, NaResize to a working area,
# wavelet colour fix against the input, video writing.
#
# Nothing touches the GPU at import time: weights are only downloaded to disk,
# the runner is built inside the GPU call.

import os
import random
import tempfile
import time

os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

import gc
from pathlib import Path

import gradio as gr
import imageio.v2 as imageio
import numpy as np
import spaces
import torch
from einops import rearrange
from huggingface_hub import hf_hub_download
from omegaconf import OmegaConf
from torchvision.transforms import Compose, Lambda, Normalize

from common.config import load_config
from common.distributed import init_torch
from common.seed import set_seed
from data.image.transforms.divisible_crop import DivisibleCrop
from data.image.transforms.na_resize import NaResize
from data.video.transforms.rearrange import Rearrange
from projects.video_diffusion_sr.infer import VideoDiffusionInfer

try:
    from projects.video_diffusion_sr.color_fix import wavelet_reconstruction

    USE_COLOR_FIX = True
except ImportError:
    USE_COLOR_FIX = False
    print("color fix unavailable; output will not be wavelet-reconstructed")

WEIGHTS_REPO = "ByteDance-Seed/SeedVR2-3B"
CKPT_DIR = Path("./ckpts")
CKPT_DIR.mkdir(exist_ok=True)


def _fetch(filename: str, target: Path) -> str:
    if target.exists():
        return str(target)
    path = hf_hub_download(repo_id=WEIGHTS_REPO, filename=filename)
    target.symlink_to(path)
    return str(target)


# Disk only (CPU), no GPU: safe at startup.
DIT_CKPT = _fetch("seedvr2_ema_3b.pth", CKPT_DIR / "seedvr2_ema_3b.pth")
VAE_CKPT = _fetch("ema_vae.pth", CKPT_DIR / "ema_vae.pth")
POS_EMB = _fetch("pos_emb.pt", Path("./pos_emb.pt"))
NEG_EMB = _fetch("neg_emb.pt", Path("./neg_emb.pt"))

MAX_FRAMES = 121  # same per-request limit as the official Space
TARGETS = {"1920x1080": 1920 * 1080, "1280x720": 1280 * 720}
MAX_DURATION = 240  # seconds, hard cap on the GPU booking
INPUT_NOISE = float(os.environ.get("SEEDVR2_INPUT_NOISE", 0.0))

os.environ.setdefault("MASTER_ADDR", "127.0.0.1")
os.environ.setdefault("MASTER_PORT", "12355")
os.environ.setdefault("RANK", "0")
os.environ.setdefault("WORLD_SIZE", "1")
os.environ.setdefault("LOCAL_RANK", "0")

_runner = None


def _ensure_runner():
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


def _read_video(path):
    """CPU only. Returns (frames uint8 [T,H,W,3], fps)."""
    reader = imageio.get_reader(path, "ffmpeg")
    fps = float(reader.get_meta_data().get("fps", 25.0))
    frames = []
    for i, fr in enumerate(reader):
        if i >= MAX_FRAMES:
            break
        frames.append(np.asarray(fr)[..., :3])
    reader.close()
    if not frames:
        raise gr.Error("Could not read any frame from the video.")
    return np.stack(frames), fps


def _count_frames(path):
    try:
        reader = imageio.get_reader(path, "ffmpeg")
        n = reader.count_frames()
        reader.close()
        return min(int(n), MAX_FRAMES)
    except Exception:
        return MAX_FRAMES


def _pad_4n1(video):
    """video: c t h w. Pad with the last frame to 4n+1 frames (official cut_videos, sp_size=1)."""
    t = video.size(1)
    if t <= 4:
        need = 5 - t
    elif (t - 1) % 4 == 0:
        return video
    else:
        need = 4 - ((t - 1) % 4)
    pad = video[:, -1:].repeat(1, need, 1, 1)
    return torch.cat([video, pad], dim=1)


def _chunks(n, size):
    if not size or size >= n:
        return [(0, n)]
    size = max(5, (int(size) - 1) // 4 * 4 + 1)  # keep 4n+1
    return [(s, min(n, s + size)) for s in range(0, n, size)]


def _duration(video, target="1920x1080", chunk_frames=0, seed=0, progress=None) -> int:
    """Estimate only (no measurement yet). Latent frames = (T-1)/4+1; cost scales with
    latent frames x working area, plus a fixed overhead for building the runner.
    Calibrate from the logged real time of the first runs and tighten."""
    n = _count_frames(video) if video else MAX_FRAMES
    latent = (n - 1) // 4 + 1
    area = TARGETS.get(target, TARGETS["1920x1080"]) / (1280 * 720)
    est = 25 + 2.2 * latent * area
    return int(min(MAX_DURATION, max(30, est)))


@spaces.GPU(duration=_duration)
@torch.no_grad()
def restore_video(video, target="1920x1080", chunk_frames=0, seed=0, progress=gr.Progress(track_tqdm=True)):
    if not video:
        raise gr.Error("Upload a video first.")
    t0 = time.time()
    frames, fps = _read_video(video)
    n = frames.shape[0]
    area = TARGETS.get(target, TARGETS["1920x1080"])
    print(f"[in] {n} frames {frames.shape[2]}x{frames.shape[1]} @ {fps} fps, target area {target}", flush=True)

    runner = _ensure_runner()
    runner.config.diffusion.cfg.scale = 1.0
    runner.config.diffusion.cfg.rescale = 0.0
    runner.config.diffusion.timesteps.sampling.steps = 1
    runner.configure_diffusion()
    chosen = int(seed) or random.randrange(1, 2**31)
    set_seed(chosen, same_across_ranks=True)
    print(f"[seed] {chosen}", flush=True)

    transform = Compose(
        [
            NaResize(resolution=area**0.5, mode="area", downsample_only=False),
            Lambda(lambda x: torch.clamp(x, 0.0, 1.0)),
            DivisibleCrop((16, 16)),
            Normalize(0.5, 0.5),
            Rearrange("t c h w -> c t h w"),
        ]
    )
    text_embeds = {
        "texts_pos": [torch.load(POS_EMB).to("cuda")],
        "texts_neg": [torch.load(NEG_EMB).to("cuda")],
    }

    out_frames = []
    for s, e in _chunks(n, chunk_frames):
        clip = torch.from_numpy(frames[s:e]).permute(0, 3, 1, 2).float().div_(255.0)  # t c h w
        cond = transform(clip.to("cuda"))  # c t h w
        length = cond.size(1)
        reference = rearrange(cond, "c t h w -> t c h w")
        latents = runner.vae_encode([_pad_4n1(cond)])
        noise = [torch.randn_like(x) for x in latents]
        aug = [torch.randn_like(x) for x in latents]

        def _add_noise(x, a):
            tt = torch.tensor([1000.0], device="cuda") * INPUT_NOISE
            shape = torch.tensor(x.shape[1:], device="cuda")[None]
            return runner.schedule.forward(x, a, runner.timestep_transform(tt, shape))

        conditions = [
            runner.get_condition(nz, task="sr", latent_blur=_add_noise(lt, ag))
            for nz, ag, lt in zip(noise, aug, latents)
        ]
        with torch.autocast("cuda", torch.bfloat16, enabled=True):
            videos = runner.inference(noises=noise, conditions=conditions, dit_offload=False, **text_embeds)
        sample = videos[0]
        sample = rearrange(sample[:, None], "c t h w -> t c h w") if sample.ndim == 3 else rearrange(sample, "c t h w -> t c h w")
        sample = sample[:length]
        if USE_COLOR_FIX:
            sample = wavelet_reconstruction(sample.to("cpu"), reference[: sample.size(0)].to("cpu"))
        else:
            sample = sample.to("cpu")
        sample = rearrange(sample, "t c h w -> t h w c").clip(-1, 1).mul_(0.5).add_(0.5).mul_(255).round().to(torch.uint8).numpy()
        out_frames.append(sample)
        del latents, conditions, videos, cond
        gc.collect()
        torch.cuda.empty_cache()
        print(f"[chunk] frames {s}-{e} done at {time.time() - t0:.1f}s", flush=True)

    result = np.concatenate(out_frames, axis=0)
    out_dir = tempfile.mkdtemp(prefix="seedvr2-")
    path = os.path.join(out_dir, "restored.mp4")
    writer = imageio.get_writer(
        path, fps=fps, codec="libx264", quality=None, macro_block_size=16,
        ffmpeg_params=["-crf", "12", "-preset", "slow", "-pix_fmt", "yuv420p"],
    )
    for fr in result:
        writer.append_data(fr)
    writer.close()
    print(f"[out] {result.shape[0]} frames {result.shape[2]}x{result.shape[1]} @ {fps} fps, gpu fn {time.time() - t0:.1f}s", flush=True)
    return path


with gr.Blocks(title="SeedVR2-3B video restore (private)") as demo:
    gr.Markdown("### SeedVR2-3B video restore\nMax 121 frames per request. Output keeps the input fps.")
    with gr.Row():
        with gr.Column():
            video_in = gr.Video(label="Video")
            target = gr.Radio(list(TARGETS), value="1920x1080", label="Working area")
            chunk = gr.Number(value=0, precision=0, label="Frames per chunk (0 = all)")
            seed = gr.Number(value=0, precision=0, visible=False)
            run = gr.Button("Restore", variant="primary")
        with gr.Column():
            video_out = gr.Video(label="Result")
    run.click(restore_video, inputs=[video_in, target, chunk, seed], outputs=[video_out], api_name="restore_video")

demo.launch(ssr_mode=False, show_error=True)
