"""Restore/upscale one short clip with SeedVR2-3B on ZeroGPU (HF_TOKEN).
Default target: the owner's private Space <account>/siphon-seedvr2-video (account from whoami,
never written to the repo). Also supports the official ByteDance-Seed/SeedVR2-3B (broken on ZeroGPU since 2026).
Usage: python scripts/seedvr2_clip.py <input.mp4> <fps> [space] [target]
  space:  "own" (default) | "ByteDance-Seed/SeedVR2-3B" | any "<owner>/<name>"
  target: "1920x1080" (default) | "1280x720"   (own Space only)
-> out/<name>_seedvr2.mp4 + out/log.json"""
import json, os, shutil, sys, time
from gradio_client import Client, handle_file
from huggingface_hub import HfApi

src, fps = sys.argv[1], float(sys.argv[2])
space = sys.argv[3] if len(sys.argv) > 3 else "own"
target = sys.argv[4] if len(sys.argv) > 4 else "1920x1080"
os.makedirs("out", exist_ok=True)
tok = os.environ["HF_TOKEN"]
if space == "own":
    user = HfApi(token=tok).whoami()["name"]
    print(f"::add-mask::{user}", flush=True)
    space = f"{user}/siphon-seedvr2-video"
c = Client(space, token=tok)
t = time.time()
if space.startswith("ByteDance-Seed/"):
    res = c.predict(video_path=handle_file(src), seed=666, fps_out=fps, api_name="/generation_loop")
else:
    res = c.predict(video={"video": handle_file(src)}, target=target, chunk_frames=0, seed=0, api_name="/restore_video")
sec = round(time.time() - t, 1)
print("seconds:", sec, flush=True)
name = os.path.splitext(os.path.basename(src))[0]
outs = []
for item in (res if isinstance(res, (list, tuple)) else [res]):
    p = item.get("video") if isinstance(item, dict) else item
    if isinstance(p, dict): p = p.get("path")
    if isinstance(p, str) and os.path.exists(p) and p.endswith(".mp4"):
        dst = f"out/{name}_seedvr2.mp4"; shutil.copy(p, dst); outs.append(dst); break
json.dump({"input": src, "target": target, "seconds_wall": sec, "outputs": outs}, open("out/log.json", "w"), indent=2)
if not outs: sys.exit("no video in result")
