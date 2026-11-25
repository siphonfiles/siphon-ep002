"""Ep. 002 (Bitget) sound plan: same engine and same rules as ep. 001 (sound/episode_mix.py).

Pattern copied from ep. 001 (approved by proprietarul, 20-22 nov 2026):
  - teaser: heist piece in full, ~13 dB under the voice, a bass hit on every cut, black + sub drop + title
  - narration: music only in places (pulse/drums), every stop a smooth fade that ends before the key line
  - Thomas on camera: dry
  - T-minus cards: bass hit + card
  - the race (Locked out): 'vault_run' at the 'key' level, cut to silence before "19:16"
  - Afterwards: 'memory_piano', then the heist piece returns for the close and fades on the end card

Usage: python3 sound/ep002/ep002_mix.py <voice_dir> <out.wav>   (writes <out>.timeline.json too)
"""
import json
import os
import sys

import numpy as np
from scipy.io import wavfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
import episode_mix as EM  # noqa: E402
from sting_design import SR  # noqa: E402

V = lambda i, p=0.5: [("voice", i), ("pause", p)]
M = lambda *s: list(s)
SECTION = 1.2
FADE = ("music", "fade:4.0", -2.8)    # starts 2.8 s before the end of the previous line, ends before the next

P = []
# ---------------- TEASER ----------------
P += [("level", "teaser"), ("music", "full"), ("pause", 1.2)]
P += [("voice", "t1"), ("hit",), ("pause", 0.9), ("card", 2.6)]          # block explorer line
P += [("voice", "t2"), ("hit",), ("pause", 0.9), ("card", 3.0)]          # "Nobody stole a key."
P += [("voice", "t3"), ("hit",), ("pause", 0.9)]
P += [("voice", "t4"), ("pause", 0.25), ("hit",), ("music", "fade")]
P += [("pause", 1.4), ("drop",), ("card", 4.0)]                          # title
# ---------------- THE RESCUER ----------------
P += [("card", 1.5)] + V("r1", .7) + M(("level", "narration"), ("music", "pulse@3")) + V("r2", .7) + V("r3", .6)
P += [("voice", "r4")] + M(FADE) + [("hit",), ("card", 2.2), ("pause", .4)]          # $388M
P += V("i1", .5) + V("i2", .6) + V("i3", .6) + V("i4", .5) + [("voice", "i5"), ("hit",), ("pause", SECTION + .4)]
# ---------------- HOW AN EXCHANGE PAYS YOU ----------------
P += [("card", 1.5)] + M(("music", "pulse@3")) + V("p1", .6) + V("p2", .7) + V("p3", .6) + V("p4", .8) + [("voice", "p5")] \
    + M(FADE) + [("pause", .8)] + [("voice", "p6"), ("hit",), ("pause", SECTION)]
# ---------------- T-MINUS 24 DAYS ----------------
P += [("hit",), ("card", 2.0)] + M(("music", "pulse@3")) + V("a1", .6) + V("a2", .7) + V("a3", .6) + V("a4", .6) \
    + V("a5", .6) + [("voice", "a6")] + M(FADE) + [("pause", .9)] + [("voice", "a7"), ("hit",), ("pause", 1.2)] \
    + V("a8", .9) + V("a9", .6) + [("voice", "a10"), ("hit",), ("pause", SECTION)]
# ---------------- BRIDGE (Thomas, dry) ----------------
P += V("d1", .5) + V("d2", .5) + V("d3", .5) + V("d4", SECTION)
# ---------------- T-MINUS 2 HOURS 24 MINUTES ----------------
P += [("hit",), ("card", 2.0)] + M(("music", "drums@3")) + V("b1", .6) + V("b2", .5) + V("b3", .8) + V("b4", .7) \
    + V("b5", .6) + [("voice", "b6")] + M(FADE) + [("pause", .8)] + V("b7", .7) + [("voice", "b8"), ("hit",), ("pause", SECTION)]
# ---------------- T-MINUS 42 MINUTES ----------------
P += [("hit",), ("card", 2.0)] + M(("music", "pulse@3")) + V("c1", .6) + V("c2", .6) + V("c3", .7) + V("c4", .6) \
    + [("voice", "c5")] + M(FADE) + [("pause", .9)] + [("voice", "c6"), ("hit",), ("pause", SECTION)]
# ---------------- 18:31 ----------------
P += [("hit",), ("card", 2.0)] + M(("music", "drums@2")) + V("e1", .6) + V("e2", .6) + V("e3", .9) \
    + V("e4", .8) + V("e5", .6) + V("e6", .6) + [("voice", "e7"), ("pause", .3)]
# ---------------- LOCKED OUT (the race, vault_run) ----------------
P += [("track", "vault_run"), ("level", "key"), ("music", "full"), ("hit",), ("card", 1.6)]
P += V("f1", .6) + V("f2", .5) + V("f3", .7) + V("f4", .6) \
    + [("voice", "f5"), ("music", "fade:2.9", -1.7), ("pause", 1.3)] \
    + [("voice", "f6"), ("hit",), ("pause", .6)] + V("f7", .6) + [("voice", "f8"), ("hit",), ("pause", 1.0)] \
    + V("f9", .7) + [("voice", "f10"), ("hit",), ("pause", SECTION + .4)]
# ---------------- WHY DIDN'T IT STOP? ----------------
P += [("card", 1.5)] + V("g1", .6) + V("g2", .7) + V("g3", .9) + [("hit",), ("card", 1.6)] \
    + M(("track", "heist"), ("level", "narration"), ("music", "pulse@3")) + V("g4", .7) + V("g5", .6) + V("g6", .6) \
    + V("g7", .6) + [("voice", "g8")] + M(FADE) + [("pause", .9)] + V("g9", .7) + V("g10", SECTION)
# ---------------- THE TELL ----------------
P += [("card", 1.5)] + V("h1", .6) + V("h2", .8) + V("h3", .9) + V("h4", .8) + V("h5", .6) \
    + [("voice", "h6"), ("hit",), ("pause", 1.0)] + V("h7", SECTION)
# ---------------- WHERE DID IT GO? ----------------
P += [("card", 1.5)] + M(("music", "pulse@3")) + V("w1", .6) + V("w2", .7) + V("w3", .6) + V("w4", .8) \
    + [("voice", "w5")] + M(FADE) + [("pause", .9)] + V("w6", .6) + V("w7", .6) + V("w8", SECTION)
# ---------------- WHO? ----------------
P += [("card", 1.5)] + V("x1", .6) + V("x2", .5) + [("card", 3.4)] + V("x3", .6) + V("x4", .9) \
    + [("voice", "x5"), ("hit",), ("pause", .8)] + V("x6", .6) + V("x7", .6) + V("x8", .9) + V("x9", .7) + V("x10", SECTION)
# ---------------- THE LOAN (Thomas, dry) ----------------
P += V("l1", .5) + V("l2", .6) + V("l3", .6) + V("l4", .6) + V("l5", SECTION)
# ---------------- AFTERWARDS ----------------
P += [("card", 1.5)] + M(("track", "memory_piano"), ("level", "feature"), ("music", "full@3")) \
    + V("k1", .6) + V("k2", .7) + V("k3", .8) + V("k4", .6) + [("voice", "k5")] + M(FADE) + [("pause", SECTION)]
P += V("z1", .7) + V("z2", .7) + [("pause", .3)] + V("z3", 1.0) + V("z4", 0) \
    + [("track", "heist"), ("level", "key"), ("music", "full@1"), ("pause", 1.2),
       ("music", "fade"), ("pause", EM.END_FADE + 0.5)]
# 25 Nov 2026 (owner): no music under Thomas while he speaks (it came in under z3 at 10:57) ->
# the closing heist piece starts after z4, over the end card, then fades as before; timeline unchanged
# 23 Nov 2026: under the full heist piece both ASR models heard "Siphoned Files" in z4 (the clean take is
# heard right) -> the sign-off sits on the thinner pulse layer, then the piece fades as before

PLAN = P

if __name__ == "__main__":
    mix, total = EM.render(sys.argv[1], PLAN)
    wavfile.write(sys.argv[2], SR, (np.stack([mix, mix], 1) * 32767).astype(np.int16))
    json.dump(EM.LAST_TIMELINE, open(os.path.splitext(sys.argv[2])[0] + ".timeline.json", "w"), indent=1)
    print("wrote", sys.argv[2], f"{total:.1f}s")
