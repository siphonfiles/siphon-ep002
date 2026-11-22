"""Restore/upscale one short clip with SeedVR2-3B (Space ByteDance-Seed/SeedVR2-3B, ZeroGPU, HF_TOKEN).
The Space keeps max 121 frames per call and resizes video to ~1280x720 area. Usage:
python scripts/seedvr2_clip.py <input.mp4> <fps_out>  -> out/<name>_seedvr2.mp4 + out/log.json"""
import json, os, shutil, sys, time
from gradio_client import Client, handle_file
src, fps = sys.argv[1], float(sys.argv[2])
os.makedirs("out", exist_ok=True)
c = Client("ByteDance-Seed/SeedVR2-3B", token=os.environ["HF_TOKEN"])
t = time.time()
res = c.predict(video_path=handle_file(src), seed=666, fps_out=fps, api_name="/generation_loop")
sec = round(time.time() - t, 1)
print("result:", res, "seconds:", sec, flush=True)
name = os.path.splitext(os.path.basename(src))[0]
outs = []
for item in (res if isinstance(res, (list, tuple)) else [res]):
    p = item.get("video") if isinstance(item, dict) else item
    if isinstance(p, dict): p = p.get("path")
    if isinstance(p, str) and os.path.exists(p) and p.endswith(".mp4"):
        dst = f"out/{name}_seedvr2.mp4"; shutil.copy(p, dst); outs.append(dst); break
json.dump({"input": src, "seconds_wall": sec, "outputs": outs, "raw": str(res)}, open("out/log.json", "w"), indent=2)
if not outs: sys.exit("no video in result")
