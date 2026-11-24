"""Mix the chosen ep. 002 effects quietly under the voice, at their anchor lines.
Usage: python3 sound/ep002/sfx/add_sfx.py <mix.wav> <timeline.json> <out.wav>
- reads sound/ep002/sfx/chosen.json (file, anchors, gain_db = peak level in dBFS before the master)
- each effect is peak-normalised, faded in/out, then placed:
  short hits land 0.25 s before the line starts (in the breath before the words);
  beds (hum, alarm, wind) start 0.4 s before the line and fade over 0.6 s
- the timeline is not changed
"""
import json, os, subprocess, sys
import numpy as np
from scipy.io import wavfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SR = 44100  # same rate as the episode mix (sound/episode_mix.py)
BEDS = {"server_hum": 7.0, "building_alarm": 5.5, "night_wind_city": 6.0, "vault_open": 4.2}


def load(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.join(ROOT, path), "-ac", "1", "-ar", str(SR),
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).astype(np.float64)


def main(mix_path, tl_path, out_path):
    sr, mix = wavfile.read(mix_path)
    assert sr == SR, sr
    mix = mix.astype(np.float64) / 32768.0
    tl = json.load(open(tl_path))
    start = {e["id"]: e["t"] for e in tl["events"] if "id" in e and "t" in e}
    chosen = json.load(open(os.path.join(ROOT, "sound/ep002/sfx/chosen.json")))["effects"]
    layer = np.zeros(len(mix))
    log = []
    for name, c in chosen.items():
        x = load(c["file"])
        if name in BEDS:
            x = x[:int(BEDS[name] * SR)]
        x = x / (np.abs(x).max() + 1e-9)
        n = len(x)
        fi, fo = int((0.6 if name in BEDS else 0.005) * SR), int((0.6 if name in BEDS else 0.05) * SR)
        x[:fi] *= np.linspace(0, 1, fi)
        x[n - fo:] *= np.linspace(1, 0, fo)
        x *= 10 ** (c["gain_db"] / 20)
        lead = 0.4 if name in BEDS else 0.25
        for a in c["anchors"]:
            t = start[a["line"]] - lead + c.get("offset_s", 0.0)
            i = max(0, int(t * SR)); j = min(len(layer), i + n)
            layer[i:j] += x[:j - i]
            log.append((round(t, 2), name, a["line"]))
    out = mix + layer[:, None] if mix.ndim == 2 else mix + layer
    wavfile.write(out_path, SR, (np.clip(out, -1, 1) * 32767).astype(np.int16))
    for row in sorted(log):
        print(*row)


if __name__ == "__main__":
    main(*sys.argv[1:4])
