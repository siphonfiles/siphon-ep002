"""Ep. 002 (Bitget) music demos: a new palette, not the ep. 001 heist pieces.

Proprietarul (23 nov 2026): "sunt aceleași melodii ca la episodul 1 ... vino cu altele mai nice".
Ep. 002 looks like a surveillance room (petrol + cyan), so the music leans electronic / cyber-thriller,
still with a pulse (the slow ambient bed was rejected in ep. 001 as "funeral").

  signal_trace     main theme   100 BPM, F# minor. Sequenced 16th arp whose filter slowly opens,
                                 sub bass on 8ths, heartbeat kick, data ticks, a 4-note bell motif.
  inside_the_wall  infiltration  84 BPM, C minor. Low bowed ostinato, sonar ping, muted clicks,
                                 a semitone that never resolves: someone is inside and nobody knows.
  withdrawal_rush  the race      132 BPM, E minor. Broken-beat drums, octave bass, an alarm-like
                                 two-note siren in the synths, risers every 4 bars.
  follow_the_coins laundering    110 BPM, D dorian. Syncopated mallet pattern hopping in stereo,
                                 tight bass, brushed hats: the chase across chains.
  the_loan         ending         76 BPM, A minor -> C. Felt-piano + warm strings, a hopeful lift:
                                 customers got paid back, the loan comes home.

All original, synthesized in code (no samples, no models). Each demo 40 s, ends with a fade.
Run:  python3 sound/ep002/ep002_tracks.py  ->  sound/ep002/demos/<name>.wav
"""
import os
import sys
import numpy as np
from scipy.io import wavfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from sting_design import SR, t_axis, lowpass, highpass, place  # noqa: E402
from heist_design import midi_hz, env, kick, hat, snap, room  # noqa: E402
from heist_tracks import saw, bass_note, tom, string_note, piano_note, brush  # noqa: E402

OUT = os.path.join(HERE, "demos")
rng = np.random.default_rng(202)


# ---------- instruments ----------
def seq_pluck(m, dur, cutoff):
    """Analog-sequencer pluck: detuned saw + square through a low-pass set per note."""
    t = t_axis(dur)
    f = midi_hz(m)
    sq = np.sign(np.sin(2 * np.pi * f * t))
    s = 0.6 * saw(f, dur, (-0.004, 0.004)) + 0.4 * sq
    return lowpass(s, cutoff) * env(dur, 0.11, 0.002)


def sub(m, dur):
    t = t_axis(dur)
    return np.sin(2 * np.pi * midi_hz(m) * t) * env(dur, 0.35, 0.004)


def bell(m, dur=2.5):
    t = t_axis(dur)
    f = midi_hz(m)
    x = (np.sin(2 * np.pi * f * t) + 0.5 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 3)
         + 0.25 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 6))
    return x * env(dur, 0.9, 0.002)


def tick(dur=0.03):
    n = rng.normal(0, 1, int(dur * SR))
    return highpass(n, 5000) * env(dur, 0.004, 0.0003)


def ping(m, dur=3.0):
    """Sonar ping: pure tone, long tail, slight pitch drop."""
    t = t_axis(dur)
    f = midi_hz(m) * (1 - 0.01 * t / dur)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(dur, 0.7, 0.003)


def bowed(m, dur):
    """Low cello-like bowed note: saw stack, slow attack, gentle vibrato."""
    t = t_axis(dur)
    vib = 1 + 0.003 * np.sin(2 * np.pi * 4.8 * t)
    s = saw(midi_hz(m), dur) * vib
    a = np.minimum(1, t / 0.18) * np.minimum(1, (dur - t) / 0.12)
    return lowpass(s, 900) * a


def siren(m1, m2, dur):
    """Two-note alarm figure in a synth, not a literal siren (gentle, musical)."""
    t = t_axis(dur)
    half = dur / 2
    f = np.where(t < half, midi_hz(m1), midi_hz(m2))
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = 0.6 * np.sin(ph) + 0.4 * np.sign(np.sin(ph)) * 0.5
    a = np.minimum(1, t / 0.02) * np.minimum(1, (dur - t) / 0.05)
    return lowpass(s, 2200) * a


def riser(dur):
    """Noise swell that brightens: a crossfade from a dark band to a bright band (no filter steps, no clicks)."""
    t = t_axis(dur)
    n = rng.normal(0, 1, len(t))
    dark = highpass(lowpass(n, 700), 200)
    bright = highpass(lowpass(n, 7000), 2000)
    x = t / dur
    return (dark * (1 - x) + bright * x) * x ** 1.5


def mallet(m, dur=0.6):
    t = t_axis(dur)
    f = midi_hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t * 25)
    return x * env(dur, 0.18, 0.001)


def felt_piano(m, dur=4.0, vel=1.0):
    return lowpass(piano_note(m, dur, vel), 2200)


# ---------- stereo helpers ----------
def pan(x, p):
    """p in [-1, 1]; equal-power."""
    a = (p + 1) * np.pi / 4
    return np.stack([x * np.cos(a), x * np.sin(a)], 1)


def finish_st(st, seconds, fade=5.0):
    n = int(seconds * SR)
    st = st[:n].copy()
    f = int(fade * SR)
    st[-f:] *= (0.5 * (1 + np.cos(np.linspace(0, np.pi, f))))[:, None]
    st /= np.max(np.abs(st)) + 1e-9
    return st * 10 ** (-1 / 20)


def buf(seconds):
    return np.zeros(int((seconds + 4) * SR))


# ---------- tracks ----------
def signal_trace(seconds=40):
    bpm = 100
    s16 = 60 / bpm / 4
    bar = 16 * s16
    drums, bass, arpL, arpR, bells, ticks = (buf(seconds) for _ in range(6))
    prog = [(42, [54, 57, 61, 64]), (38, [50, 54, 57, 61]), (45, [57, 61, 64, 68]), (40, [52, 56, 59, 64])]  # F#m D A E
    pat = [0, 2, 1, 3, 2, 1, 0, 2, 3, 1, 2, 0, 1, 3, 2, 1]
    bars = int(seconds / bar) + 1
    for b in range(bars):
        root, ch = prog[(b // 2) % 4]
        t0 = b * bar
        cut = 500 + 2600 * min(1.0, b / 10)               # the filter opens over ~10 bars
        for i in range(16):
            m = ch[pat[i]] + (12 if i % 8 == 7 else 0)
            target = arpL if i % 2 == 0 else arpR
            place(target, 0.32 * seq_pluck(m, s16 * 1.4, cut), t0 + i * s16)
            if b >= 2 and i % 2 == 0:
                place(ticks, 0.08 * tick(), t0 + i * s16 + s16 * 0.5)
        for i in range(8):
            place(bass, 0.5 * sub(root - 12 + 12, s16 * 1.8), t0 + i * 2 * s16)
        if b >= 4:
            place(drums, 0.9 * kick(), t0)                  # heartbeat: da-dum
            place(drums, 0.6 * kick(), t0 + 3 * s16)
            place(drums, 0.9 * kick(), t0 + 8 * s16)
            place(drums, 0.6 * kick(), t0 + 11 * s16)
            place(drums, 0.35 * snap(), t0 + 12 * s16)
        if b >= 6 and b % 4 == 2:                          # 4-note motif, every 4 bars
            for k, m in enumerate([73, 69, 68, 66]):
                place(bells, 0.22 * bell(m), t0 + k * 4 * s16)
    L = room(arpL, mix=0.3) + 0.4 * room(arpR, mix=0.3)
    R = room(arpR, mix=0.3) + 0.4 * room(arpL, mix=0.3)
    mono = bass + drums
    st = np.stack([L, R], 1) + mono[:, None] + pan(room(bells, seconds=2.4, mix=0.45), 0.25) + pan(ticks, -0.5)
    return finish_st(st, seconds)


def inside_the_wall(seconds=40):
    bpm = 84
    beat = 60 / bpm
    bar = 4 * beat
    low, pings, clicks, high, drums = (buf(seconds) for _ in range(5))
    ost = [36, 36, 39, 36, 38, 36, 35, 36]               # C C Eb C D C B C (8ths)
    bars = int(seconds / bar) + 1
    for b in range(bars):
        t0 = b * bar
        for i in range(8):
            place(low, 0.4 * bowed(ost[i] + (0 if b % 4 < 2 else -2 if i % 2 else 0), beat * 0.48), t0 + i * beat / 2)
        for i in range(16):
            if rng.random() < 0.55:
                place(clicks, 0.06 * tick(0.02), t0 + i * beat / 4)
        if b % 2 == 0:
            place(pings, 0.25 * ping(84 if b % 4 == 0 else 79, 3.2), t0 + beat * 0.5)
        if b >= 4:                                        # the unresolved semitone, high and thin
            place(high, 0.07 * string_note(72, bar * 0.95), t0)
            place(high, 0.06 * string_note(73, bar * 0.95), t0 + 0.02)
            place(drums, 0.7 * kick(0.4), t0)
            place(drums, 0.4 * tom(80, 0.6), t0 + 2.5 * beat)
    st = pan(room(low, seconds=1.6, mix=0.25), 0) + pan(room(pings, seconds=3.0, mix=0.55), -0.35) \
        + pan(clicks, 0.45) + pan(room(high, seconds=2.5, mix=0.5), 0.1) + pan(drums, 0)
    return finish_st(st, seconds)


def withdrawal_rush(seconds=40):
    bpm = 132
    s16 = 60 / bpm / 4
    bar = 16 * s16
    drums, bass, syn, fx = (buf(seconds) for _ in range(4))
    roots = [40, 40, 36, 38]                               # E E C D
    kicks = (0, 3, 6, 10, 11)
    bars = int(seconds / bar) + 1
    for b in range(bars):
        t0 = b * bar
        root = roots[(b // 2) % 4]
        for i in range(16):
            place(bass, 0.45 * bass_note(root + (12 if i % 2 else 0), s16 * 0.85, cutoff=900, decay=0.07), t0 + i * s16)
            place(drums, 0.16 * hat(accent=1.0 if i % 2 == 0 else 0.45), t0 + i * s16)
        for i in kicks:
            place(drums, 0.85 * kick(), t0 + i * s16)
        for i in (4, 12):
            place(drums, 0.55 * snap(), t0 + i * s16)
        if b % 4 == 3:
            for k, i in enumerate((8, 10, 12, 13, 14, 15)):
                place(drums, 0.45 * tom(150 - 14 * k), t0 + i * s16)
        if b >= 2:                                         # siren figure on the off-bars
            place(syn, 0.2 * siren(root + 31, root + 32, bar * 0.5), t0 + bar * 0.5 if b % 2 else t0)
        if b % 4 == 2:
            place(fx, 0.25 * riser(bar), t0 + bar * 0.0)
    st = pan(drums + bass, 0) + pan(room(syn, mix=0.3), -0.2) + 0.6 * pan(syn, 0.4) + pan(fx, 0.2)
    return finish_st(st, seconds)


def follow_the_coins(seconds=40):
    bpm = 110
    s16 = 60 / bpm / 4
    bar = 16 * s16
    drums, bass, mL, mR = (buf(seconds) for _ in range(4))
    prog = [(38, [62, 65, 69, 71]), (43, [62, 67, 71, 74]), (36, [60, 64, 67, 71]), (43, [62, 67, 71, 74])]  # Dm9 G C G
    rhythm = [0, 3, 6, 8, 10, 13]                         # syncopated 3-3-2-2-3-3
    bars = int(seconds / bar) + 1
    for b in range(bars):
        root, ch = prog[b % 4]
        t0 = b * bar
        for k, i in enumerate(rhythm):
            m = ch[(k + b) % 4] + (12 if k == 4 else 0)
            place(mL if k % 2 == 0 else mR, 0.3 * mallet(m), t0 + i * s16)
        for i in (0, 3, 6, 10, 14):
            place(bass, 0.55 * bass_note(root - 12 + (7 if i == 10 else 0), s16 * 1.6, cutoff=700, decay=0.12), t0 + i * s16)
        for i in range(16):
            place(drums, 0.12 * brush(0.12) if i % 2 else 0.1 * hat(accent=0.6), t0 + i * s16)
        if b >= 2:
            place(drums, 0.75 * kick(), t0)
            place(drums, 0.55 * kick(), t0 + 7 * s16)
            place(drums, 0.45 * snap(), t0 + 4 * s16)
            place(drums, 0.45 * snap(), t0 + 12 * s16)
    st = pan(drums + bass, 0) + pan(room(mL, mix=0.3), -0.55) + pan(room(mR, mix=0.3), 0.55)
    return finish_st(st, seconds)


def the_loan(seconds=40):
    bpm = 76
    beat = 60 / bpm
    bar = 4 * beat
    keys, low, strings, clock = (buf(seconds + 4) for _ in range(4))
    prog = [(33, [57, 60, 64, 69]), (29, [57, 60, 65, 69]), (36, [60, 64, 67, 72]), (31, [59, 62, 67, 71])]  # Am F C G
    figure = [(0.0, 0), (0.5, 1), (1.0, 2), (2.0, 3), (2.5, 2), (3.0, 1)]
    bars = int(seconds / bar) + 2
    for b in range(bars):
        root, ch = prog[b % 4]
        t0 = b * bar
        place(low, 0.45 * felt_piano(root + 12, 6.0, 0.8), t0)
        lift = 12 if b >= 8 else 0                         # the melody lifts an octave in the second half
        for at, k in figure:
            place(keys, 0.38 * felt_piano(ch[k] + lift * (k == 3), 3.0, 0.7), t0 + at * beat)
        if b >= 4:
            for m in ch[:3]:
                place(strings, 0.07 * string_note(m, bar * 1.02), t0)
        for i in range(4):
            place(clock, 0.04 * hat(accent=0.5), t0 + i * beat)
    st = pan(room(keys + low, seconds=2.6, mix=0.38), 0) + pan(room(strings, seconds=3.0, mix=0.5), 0.15) + pan(clock, -0.3)
    return finish_st(st, seconds, fade=4.0)


TRACKS = {"signal_trace": signal_trace, "inside_the_wall": inside_the_wall, "withdrawal_rush": withdrawal_rush,
          "follow_the_coins": follow_the_coins, "the_loan": the_loan}

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in TRACKS.items():
        st = fn(40)
        path = os.path.join(OUT, f"{name}.wav")
        wavfile.write(path, SR, (st * 32767).astype(np.int16))
        print("wrote", path, round(len(st) / SR, 1), "s")


def withdrawal_rush_v2(seconds=20, toms=False):
    """Owner (23 nov 2026): keep only what plays in the first 3 s of withdrawal_rush
    (octave bass + kick/snap/hats), no siren synth, no riser; ~20 s long.
    toms=True adds the drum fill every 4th bar (still only drums + bass)."""
    bpm = 132
    s16 = 60 / bpm / 4
    bar = 16 * s16
    drums, bass = buf(seconds), buf(seconds)
    roots = [40, 40, 36, 38]
    kicks = (0, 3, 6, 10, 11)
    bars = int(seconds / bar) + 1
    for b in range(bars):
        t0 = b * bar
        root = roots[(b // 2) % 4]
        for i in range(16):
            place(bass, 0.45 * bass_note(root + (12 if i % 2 else 0), s16 * 0.85, cutoff=900, decay=0.07), t0 + i * s16)
            place(drums, 0.16 * hat(accent=1.0 if i % 2 == 0 else 0.45), t0 + i * s16)
        for i in kicks:
            place(drums, 0.85 * kick(), t0 + i * s16)
        for i in (4, 12):
            place(drums, 0.55 * snap(), t0 + i * s16)
        if toms and b % 4 == 3:
            for k, i in enumerate((8, 10, 12, 13, 14, 15)):
                place(drums, 0.45 * tom(150 - 14 * k), t0 + i * s16)
    return finish_st(pan(drums + bass, 0), seconds, fade=3.0)
