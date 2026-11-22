"""LivePortrait on Kaggle's free T4: "Thomas at work" shots from the three-quarter angle
(Siphon Files ep. 001, proprietarul 22 nov 2026). The approved still
presenter/reference/thomas_ref_threequarter_final.png is animated with the head pose and the eyes
(blinks, gaze) of Thomas's own LongCat clips; the mouth stays closed (lips are NOT transferred),
because in these shots he is reading the file while the narration continues.

Licensing: LivePortrait code + weights MIT. Its InsightFace face detector (non-commercial models)
is replaced by OpenCV YuNet (MIT, opencv_zoo); LivePortrait's own 203-point landmark model (MIT)
does the fine landmarks. Inputs: job.json, source.png, driving_*.mp4. Output: /kaggle/working/out.
"""
import os, sys, json, time, glob, subprocess, shutil

T0 = time.time()
LOG, done = [], []
OUT = "/kaggle/working/out"
os.makedirs(OUT, exist_ok=True)


def log(*a):
    m = f"[{time.time() - T0:7.1f}s] " + " ".join(str(x) for x in a)
    print(m, flush=True)
    LOG.append(m)


def save_log(extra=None):
    d = {"log": LOG, "elapsed_s": round(time.time() - T0, 1)}
    d.update(extra or {})
    json.dump(d, open(os.path.join(OUT, "run_log.json"), "w"), indent=2)


def sh(cmd, cwd=None, timeout=1800):
    """Run a command, streaming its output into the log (so a hang is visible), with a timeout."""
    log("$", cmd)
    p = subprocess.Popen(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
    out, t0 = [], time.time()
    import threading
    def reader():
        for line in p.stdout:
            line = line.rstrip()
            out.append(line)
            if line and not line.startswith("\r"):
                log("   |", line[-300:])
    th = threading.Thread(target=reader, daemon=True)
    th.start()
    try:
        p.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        p.kill()
        raise RuntimeError(f"timeout after {timeout}s: {cmd}")
    th.join(5)
    save_log({"status": "running", "done": done})
    if p.returncode != 0:
        raise RuntimeError(f"command failed ({p.returncode}): {cmd}")
    return "\n".join(out)


FACE = r'''
import json, os, types
import numpy as np
import cv2
from .human_landmark_runner import LandmarkRunner

_DIR = os.path.join(os.path.dirname(__file__), "../../pretrained_weights")
_FACES = json.load(open(os.path.join(_DIR, "faces.json")))


class FaceAnalysisDIY:
    """Drop-in for LivePortrait's InsightFace wrapper (non-commercial models). The face boxes + 5 points
    were found beforehand with OpenCV YuNet (MIT) on the exact source image and on the first frame of each
    driving clip (camera locked, so the box is stable); here we only pick them by image size and refine
    with LivePortrait's own 203-point landmark model (MIT). No OpenCV DNN at run time (it killed the
    Kaggle session three times)."""
    def __init__(self, *a, **k):
        self.lmk = LandmarkRunner(ckpt_path=os.path.join(_DIR, "liveportrait/landmark.onnx"), onnx_provider="cpu", device_id=0)

    def prepare(self, *a, **k):
        pass

    def warmup(self):
        pass

    def get(self, img_bgr, flag_do_landmark_2d_106=True, direction="large-small", max_face_num=0, **k):
        h, w = img_bgr.shape[:2]
        cand = [v for v in _FACES.values() if v["shape"] == [h, w]]
        if not cand:   # scaled input: rescale the closest entry
            v = min(_FACES.values(), key=lambda v: abs(v["shape"][1] / v["shape"][0] - w / h))
            sx, sy = w / v["shape"][1], h / v["shape"][0]
            cand = [{"bbox": [v["bbox"][0] * sx, v["bbox"][1] * sy, v["bbox"][2] * sx, v["bbox"][3] * sy],
                     "pts5": [[x * sx, y * sy] for x, y in v["pts5"]]}]
        f = cand[0]
        rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        pts5 = np.array(f["pts5"], dtype=np.float32)
        l = self.lmk.run(rgb, pts5)
        l = self.lmk.run(rgb, l)
        return [types.SimpleNamespace(bbox=np.array(f["bbox"], dtype=np.float32), kps=pts5, det_score=0.93,
                                      landmark_2d_106=l)]
'''

import threading
def _heartbeat():
    while True:
        time.sleep(30)
        try:
            m = subprocess.run("free -m | awk 'NR==2{print $3\"/\"$2\" MB RAM\"}'; nvidia-smi --query-gpu=memory.used,utilization.gpu --format=csv,noheader | tr '\\n' ' '",
                               shell=True, capture_output=True, text=True, timeout=20).stdout.strip()
            log("heartbeat:", m)
        except Exception as e:
            log("heartbeat error", repr(e))
threading.Thread(target=_heartbeat, daemon=True).start()

try:
    jf = glob.glob("/kaggle/input/**/job.json", recursive=True)
    assert jf, "job.json missing"
    IN = os.path.dirname(jf[0])
    job = json.load(open(jf[0]))
    log(len(job["shots"]), "shots; inputs in", IN)
    log(sh("nvidia-smi --query-gpu=name,memory.total --format=csv,noheader"))
    if not shutil.which("ffmpeg"):
        sh("pip install -q imageio-ffmpeg && ln -sf $(python -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())') /usr/local/bin/ffmpeg")
    W = "/tmp/lp"
    sh(f"git clone -q https://github.com/KwaiVGI/LivePortrait {W}")
    sh(f"git -C {W} log -1 --format=%H")
    sh("pip install -q tyro pykalman rich ffmpeg-python scikit-image imageio imageio-ffmpeg 2>&1 | tail -2")
    try:
        import onnxruntime  # noqa
    except Exception:
        sh("pip install -q onnxruntime 2>&1 | tail -2")
    # weights (MIT); the InsightFace folder is NOT downloaded
    from huggingface_hub import snapshot_download
    snapshot_download("KwaiVGI/LivePortrait", local_dir=f"{W}/pretrained_weights",
                      allow_patterns=["liveportrait/base_models/*", "liveportrait/retargeting_models/*",
                                      "liveportrait/landmark.onnx"])
    shutil.copy(os.path.join(IN, "faces.json"), f"{W}/pretrained_weights/faces.json")
    open(f"{W}/src/utils/face_analysis_diy.py", "w").write(FACE)
    # new animation region "eyes_pose": head pose + eyes from the driver, mouth stays as in the still
    for f in (f"{W}/src/config/argument_config.py", f"{W}/src/config/inference_config.py"):
        s = open(f).read().replace('Literal["exp", "pose", "lip", "eyes", "all"]', 'Literal["exp", "pose", "lip", "eyes", "all", "eyes_pose"]')
        open(f, "w").write(s)
    p = f"{W}/src/live_portrait_pipeline.py"
    s = open(p).read()
    s = s.replace('inf_cfg.animation_region == "pose"', 'inf_cfg.animation_region in ("pose", "eyes_pose")')
    s = s.replace('inf_cfg.animation_region == "eyes"', 'inf_cfg.animation_region in ("eyes", "eyes_pose")')
    open(p, "w").write(s)
    log("patched: YuNet detector, eyes_pose region")
    src = os.path.join(IN, job["source"])
    for n, sh_ in enumerate(job["shots"]):
        name = sh_["name"]
        drv = os.path.join(IN, sh_["driving"])
        od = f"/tmp/lp_out/{name}"
        log(f"[{n + 1}/{len(job['shots'])}] {name}: driving {sh_['driving']}")
        t = time.time()
        sh(f"python -u -X faulthandler -c \"import faulthandler,sys,runpy; faulthandler.dump_traceback_later(60, repeat=True); sys.argv=sys.argv[1:]; runpy.run_path('inference.py', run_name='__main__')\" inference.py -s {src} -d {drv} -o {od} --animation_region eyes_pose "
           f"--driving_option expression-friendly --driving_multiplier {sh_.get('multiplier', 1.0)} "
           f"--source_max_dim 1344 --flag_crop_driving_video", cwd=W, timeout=1200)
        vids = [v for v in glob.glob(f"{od}/*.mp4") if "_concat" not in v]
        assert vids, "no output video for " + name
        shutil.copy(vids[0], os.path.join(OUT, name + ".mp4"))
        sh(f"ffmpeg -v error -y -i {OUT}/{name}.mp4 -vf select='eq(n\\,50)' -frames:v 1 {OUT}/{name}_f50.png")
        done.append({"name": name, "seconds": round(time.time() - t, 1)})
        log(f"{name} OK in {time.time() - t:.0f}s")
        save_log({"status": "running", "done": done})
    save_log({"status": "ok", "done": done})
    log("DONE", len(done))
except Exception as e:
    import traceback
    log("FAILED:", repr(e))
    log(traceback.format_exc()[-3000:])
    save_log({"status": "failed", "error": repr(e), "done": done})
    sys.exit(1)
