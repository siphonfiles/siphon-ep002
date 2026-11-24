"""Build the 12 chained 720p LongCat jobs that cover every remaining Thomas line in ep. 002 (24 Nov 2026).
Consecutive lines are covered by clips chained frame-to-frame (continue_from), seams in pauses where
possible, camera alternating M/C at each seam. Writes jobs + 5 s audio windows (24 kHz) to
presenter/clips/inputs/ep002/ and the matching entries to presenter/clips/inputs/ep002_clip_plan.json.
Usage: python3 scripts/ep002_thomas_chains.py <final voices dir>   (sound/ep002/build_final_voices.py)"""
import json, os, sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import resample_poly
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "sound"))
from teaser_mix import load_voice  # noqa: E402
from sting_design import SR  # noqa: E402

VD = sys.argv[1]
tl = json.load(open(os.path.join(ROOT, "graphics/motion/ep002_full.timeline.json")))
ev = [e for e in tl["events"] if e["kind"] == "voice"]
v = {e["id"]: (e["t"], e["t"] + e["dur"]) for e in ev}
N = int((tl["total"] + 2) * SR)
track = np.zeros(N)
for e in ev:
    x = load_voice(os.path.join(VD, e["id"] + ".wav"))
    i = int(e["t"] * SR)
    track[i:i + len(x)] += x[:N - i]

# (group, line ids, lead, seams as absolute episode times, cameras, what he is doing)
G = [
    ("z", ["z1", "z2", "z3"], 0.2, [648.141, 653.02, 657.92], "MCMC", "closing the episode, coming back to the first small transfer"),
    ("d12", ["d1", "d2"], 0.3, [201.82], "MC", "pausing the story to explain how an exchange's security works"),
    ("d4", ["d4"], 0.3, [], "C", "ending the explanation on a short line"),
    ("i5", ["i5"], 0.3, [], "M", "finishing the introduction with a short line"),
    ("l", ["l1", "l2", "l3", "l4", "l5"], 0.3, [601.319, 606.219, 611.08], "MCMC", "recalling the loan Bitget made to Bybit in 2025"),
]
BASE = ("A British man in his early forties with short dark brown hair and light stubble, wearing a plain dark navy cotton "
        "shirt with a soft open collar, sits at a wooden desk in a dim investigation office and speaks calmly and clearly to "
        "the camera, like a documentary presenter {what}. His hands rest still and relaxed on the manila folder on the desk. "
        "Subtle natural head movements, steady eye contact with the lens, natural blinking, composed and serious expression. "
        "Warm amber desk lamp on the right, out-of-focus evidence board and monitor behind him. Static locked-off camera, "
        "soft frontal light, realistic skin texture.")
IN = os.path.join(ROOT, "presenter/clips/inputs/ep002")
plan_p = os.path.join(ROOT, "presenter/clips/inputs/ep002_clip_plan.json")
plan = json.load(open(plan_p))
plan["clips"] = [c for c in plan["clips"] if c["name"] != "thomas_e2_z2_720p"]
for f in ("thomas_e2_z2.json", "thomas_e2_z2.wav"):
    if os.path.exists(os.path.join(IN, f)):
        os.remove(os.path.join(IN, f))
order = []


def rel(t, anchors):
    """time -> [nearest line id at or before t, offset] (keeps working if the timeline shifts later)"""
    k = max((i for i in anchors if v[i][0] <= t + 1e-6), key=lambda i: v[i][0], default=anchors[0])
    return [k, round(t - v[k][0], 3)]


for g, ids, lead, seams, cams, what in G:
    a = v[ids[0]][0] - lead
    end = v[ids[-1]][1] + 0.35
    if g == "z":                      # run straight into the existing z4 clip (no 0.35 s sliver between them)
        end = v["z4"][0] - 0.3
    starts = [a] + seams
    ends = seams + [end]
    prev = None
    for k, (s, e) in enumerate(zip(starts, ends)):
        assert e - s <= 4.95, (g, k, e - s)
        name = f"thomas_e2_{g}{'_' + str(k + 1) if len(starts) > 1 else ''}_720p"
        w = track[int(s * SR): int(s * SR) + 5 * SR]
        w = np.pad(w, (0, 5 * SR - len(w)))
        w = resample_poly(w, 24000, SR)
        w = w / (np.max(np.abs(w)) + 1e-9) * 0.9
        wav = os.path.join(IN, name.replace("_720p", "") + ".wav")
        wavfile.write(wav, 24000, (w * 32767).astype(np.int16))
        spoken = [i for i in ids if v[i][1] > s + 0.05 and v[i][0] < e - 0.05]
        job = dict(name=name, image="presenter/reference/thomas_ref_ep002_1920x1080.png",
                   audio=os.path.relpath(wav, ROOT), line=" | ".join(spoken),
                   prompt=BASE.format(what=what), resolution="720p", seed=42,
                   vocal_mode="Clean speech (fast)", acceleration="DBCache faster",
                   note=f"ep002 chain {g} part {k + 1}/{len(starts)}: episode {s:.3f}-{s + 5:.3f} s of the voice track "
                        f"(final takes, load_voice), 24 kHz; used {s:.3f}-{e:.3f} s")
        if prev:
            job["continue_from"] = dict(clip=f"presenter/clips/ep002/{prev[0]}.mp4", at=round(s - prev[1], 3))
        jp = os.path.join(IN, name.replace("_720p", "") + ".json")
        json.dump(job, open(jp, "w"), indent=2)
        plan["clips"].append(dict(name=name, first=ids[0], last=ids[-1], camera=cams[k],
                                  t0=rel(s, ids), a=rel(s if k else s + lead - min(lead, 0.35), ids), b=rel(e, ids),
                                  chain=g))
        order.append(os.path.relpath(jp, ROOT))
        prev = (name, s)
        print(name, f"{s:.2f}-{e:.2f}", cams[k], spoken, job.get("continue_from", ""))
plan["note"] = plan.get("note", "") + " 24 Nov: 12 chained clips (z, d12, d4, i5, l) cover every remaining Thomas line."
json.dump(plan, open(plan_p, "w"), indent=1)
open(os.path.join(IN, "batch_24nov.txt"), "w").write(",".join(order))
print(",".join(order))
