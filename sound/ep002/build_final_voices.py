"""Rebuild the exact set of 113 voice takes used in the ep. 002 mix (see voice_takes.md).
Usage: python3 sound/ep002/build_final_voices.py <voice-tests checkout dir> <out_dir>
<voice-tests checkout dir> holds lines/ep002-v3, lines/ep002-fix1, lines/ep002-fix2, lines/ep002-fix3."""
import os, shutil, sys
from scipy.io import wavfile
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
L = lambda d: os.path.join(src, "lines", d)
for f in os.listdir(L("ep002-v3")):
    if f.endswith(".wav"): shutil.copy(os.path.join(L("ep002-v3"), f), os.path.join(out, f))
FIX1 = {"a8": 2, "b3": 2, "g8": 2, "h1": 2, "l1": 2, "l4": 2, "r2": 2}          # ASR round 1
FIX2 = {"t3": "h6", "c3": "h7", "x6": "h7", "g5": "s9"}                           # ASR round 2 (23 Nov evening)
FIX3 = {"x4": "s2"}                                                                         # x4 rephrase, filled in after round 3
for k, s in FIX1.items(): shutil.copy(os.path.join(L("ep002-fix1"), f"{k}_s{s}.wav"), os.path.join(out, f"{k}.wav"))
for k, v in FIX2.items(): shutil.copy(os.path.join(L("ep002-fix2"), f"{k}_{v}.wav"), os.path.join(out, f"{k}.wav"))
for k, v in FIX3.items(): shutil.copy(os.path.join(L("ep002-fix3"), f"{k}_{v}.wav"), os.path.join(out, f"{k}.wav"))
for k, t in (("c6", 1.30), ("f10", 1.65)):           # ZONOS invents syllables after very short lines: cut in the silence
    sr, a = wavfile.read(os.path.join(L("ep002-v3"), f"{k}.wav")); wavfile.write(os.path.join(out, f"{k}.wav"), sr, a[:int(t * sr)])
print("voices ready:", len([f for f in os.listdir(out) if f.endswith('.wav')]))
