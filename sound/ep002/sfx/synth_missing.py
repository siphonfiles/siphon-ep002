"""Effects that Stable Audio Open Small did not reach before the 240-min CPU timeout (run 45235356430),
synthesized in code (100% original, same toolkit as sound/sfx_layer.py).
Usage: python3 sound/ep002/sfx/synth_missing.py <out_dir>
Writes 48 kHz mono WAVs: barrier_drop, stamp_thud, transfer_whoosh, phone_buzz, vault_close, scan_beep, night_wind_city.
"""
import os, sys
import numpy as np
from scipy.io import wavfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import sfx_layer as L  # noqa: E402

SR = L.SR
rng = np.random.default_rng(24)


def norm(x, peak=0.89):
    return x / (np.abs(x).max() + 1e-9) * peak


def thud(dur, f0, f1, decay, noise_hi=2500, noise_gain=0.35):
    n = int(dur * SR); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t * 30)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * L.env(n, 0.002, decay)
    click = L.bp(rng.standard_normal(n), 300, noise_hi) * L.env(n, 0.001, 0.012) * noise_gain
    return body + click


def barrier_drop():
    # short metallic swing, then a hollow clunk as the arm lands
    swing = L.bp(rng.standard_normal(int(0.45 * SR)), 1800, 5000) * np.linspace(0, 1, int(0.45 * SR)) ** 2 * 0.15
    clunk = thud(0.9, 160, 70, 0.18, 4000, 0.6)
    ring = np.sin(2 * np.pi * 410 * np.arange(len(clunk)) / SR) * L.env(len(clunk), 0.002, 0.25) * 0.18
    return norm(np.concatenate([swing, clunk + ring]))


def stamp_thud():
    a = thud(0.6, 220, 90, 0.08, 3000, 0.8)
    paper = L.bp(rng.standard_normal(len(a)), 2000, 7000) * L.env(len(a), 0.001, 0.03) * 0.25
    return norm(a + paper)


def transfer_whoosh():
    return norm(L.whoosh(1.1) * 0.9 + L.lp(L.whoosh(1.1), 600) * 0.6)


def phone_buzz():
    # two vibration pulses on a desk (~170 Hz with rattle)
    n = int(0.42 * SR); t = np.arange(n) / SR
    pulse = (np.sign(np.sin(2 * np.pi * 172 * t)) * 0.5 + np.sin(2 * np.pi * 172 * t)) * L.env(n, 0.01, 0.6)
    pulse = L.lp(pulse, 1800) * np.minimum(1, (n - np.arange(n)) / (0.03 * SR))
    gap = np.zeros(int(0.18 * SR))
    return norm(np.concatenate([pulse, gap, pulse, np.zeros(int(0.3 * SR))]))


def vault_close():
    # heavy door: low rumble swell, then a deep slam and a bolt click
    sw = int(0.8 * SR)
    rumble = L.lp(rng.standard_normal(sw), 180) * np.linspace(0, 1, sw) ** 2 * 0.4
    slam = thud(1.6, 90, 38, 0.45, 1500, 0.5)
    bolt = np.zeros(len(slam)); k = int(0.35 * SR)
    b = L.bp(rng.standard_normal(int(0.05 * SR)), 1200, 6000) * L.env(int(0.05 * SR), 0.001, 0.01)
    bolt[k:k + len(b)] = b * 0.5
    return norm(np.concatenate([rumble, slam + bolt]))


def scan_beep():
    n = int(0.6 * SR); t = np.arange(n) / SR
    s = np.zeros(n)
    for start, f in ((0.0, 1760.0), (0.16, 2093.0)):
        k = int(start * SR); m = int(0.11 * SR)
        s[k:k + m] += np.sin(2 * np.pi * f * t[:m]) * L.env(m, 0.003, 0.05)
    return norm(s, 0.8)


def night_wind_city():
    # 6 s of soft wind (slow band-pass sweep) over distant low traffic rumble
    n = int(6.0 * SR); noise = rng.standard_normal(n)
    out = np.zeros(n); B = 1024
    for i in range(0, n, B):
        p = i / n
        f = 420 + 160 * np.sin(2 * np.pi * (p * 1.3 + 0.1)) + 70 * np.sin(2 * np.pi * p * 3.7)
        seg = noise[max(0, i - 4096):i + B]
        out[i:i + B] = L.bp(seg, f * 0.6, f * 1.6)[-len(out[i:i + B]):]
    traffic = L.lp(rng.standard_normal(n), 120) * 0.6
    fade = np.minimum(1, np.minimum(np.arange(n), n - np.arange(n)) / (1.0 * SR))
    return norm((out + traffic) * fade, 0.7)


EFFECTS = dict(barrier_drop=barrier_drop, stamp_thud=stamp_thud, transfer_whoosh=transfer_whoosh,
               phone_buzz=phone_buzz, vault_close=vault_close, scan_beep=scan_beep,
               night_wind_city=night_wind_city)

if __name__ == "__main__":
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for name, fn in EFFECTS.items():
        x = fn().astype(np.float32)
        wavfile.write(os.path.join(out, f"{name}_synth.wav"), SR, x)
        print(name, f"{len(x)/SR:.2f}s")
