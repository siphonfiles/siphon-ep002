"""Generate SFX candidates with Stable Audio Open Small on CPU. Usage: python scripts/sfx_gen.py jobs.json out_dir
Each clip is decoded only as long as it needs to be (sample_size trimmed to its seconds, multiple of 2048)
and written right away, so a timeout still leaves the finished clips."""
import json, math, os, sys, time, torch
import soundfile as sf
from einops import rearrange
from stable_audio_tools import get_pretrained_model
from stable_audio_tools.inference.generation import generate_diffusion_cond
torch.set_num_threads(os.cpu_count() or 2)
jobs = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
model, cfg = get_pretrained_model("stabilityai/stable-audio-open-small")
model = model.eval().float()
sr, nmax = cfg["sample_rate"], cfg["sample_size"]
log = []
for name, secs, prompt in jobs["items"]:
    n = min(nmax, math.ceil((secs + 0.25) * sr / 2048) * 2048)
    for seed in (11, 22, 33):
        t = time.time()
        with torch.inference_mode():
            a = generate_diffusion_cond(model, steps=8, cfg_scale=1.0, sampler_type="pingpong", device="cpu", seed=seed,
                                        conditioning=[{"prompt": prompt, "seconds_total": secs}], sample_size=n)
        a = rearrange(a, "b d n -> d (b n)").to(torch.float32)[:, : int(secs * sr)]
        a = (a / a.abs().max().clamp(min=1e-6) * 0.89).clamp(-1, 1)
        sf.write(f"{out}/{name}_s{seed}.wav", a.T.numpy(), sr)
        log.append({"name": name, "seed": seed, "seconds": round(time.time() - t, 1)}); print(log[-1], flush=True)
        json.dump(log, open(f"{out}/log.json", "w"), indent=1)
