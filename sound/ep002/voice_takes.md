# Ep. 002 — vocea finală (v2, 23 nov 2026)

Setul complet de replici folosit în mix: `renders:voices/ep002-final/` (113 WAV).
Baza: `voice-tests:lines/ep002-v3` (seed 1). Înlocuite după ASR medium.en (`renders:reports/`):

| Replica | Problema la seed 1 | Luată din |
|---|---|---|
| a8 | „attack as privileged” | seed 2 |
| b3 | „Bitget” → „bitch get” | seed 2 |
| c3 | „Bitget's” neclar | seed 3 |
| g5 | „where the” în loc de „whether” | seed 2 |
| g8 | „Bit gets shut down” | seed 2 |
| h1 | „which gets” | seed 2 |
| l1 | „Bichette” la alt seed; „Bit gets” e pronunția corectă | seed 2 |
| l4 | „Bichette” | seed 2 |
| r2 | „Bitgett / by bit” | seed 2 |
| t3 | „Bitchup” | seed 3 |
| x6 | „bitch get” | seed 2 |
| c6, f10 | modelul adaugă silabe inventate după replicile foarte scurte („Try it.”, „The attacker hadn't.”) la toate seed-urile | seed 1 tăiat în liniștea de după replică (1,30 s / 1,65 s) |

Lecție: ZONOS3 „halucinează” după replici de 2-3 cuvinte → la episoadele viitoare replicile foarte scurte se generează lipite de următoarea sau se taie automat la prima pauză > 0,8 s.
Master: -14,1 LUFS, true peak -2,0 dBTP, 671,6 s.

## v3 (23 nov 2026, seara) — după ASR pe mixul final (large-v3 + medium.en)

Construcție reproductibilă: `sound/ep002/build_final_voices.py` (v3 + fix1 + fix2 + fix3, tăieturile c6/f10).

| Replica | Problema în v2 (mixul final) | Luată din |
|---|---|---|
| t3 | „Bitget” → „Bitchgett” (medium) | fix2 `t3_h6` (textul cu „Bit-get”), curată la ambele modele |
| c3 | „Bitget's” → „Bitjet's” (ambele) | fix2 `c3_h7` („Bit-get's”) |
| x6 | „Bitget” → „bid get” (medium) | fix2 `x6_h7` („Bit-get”) |
| g5 | „whether” → „where the” (large) | fix2 `g5_s9` |
| x4 | „Chainalysis” la începutul frazei, greșit la toate cele 8 variante | **text nou**: „The analysts at Chainalysis, Elliptic and TRM Labs all lean the same way.”, fix3 `x4_s2` |
| z4 | „Siphon Files” acoperit de muzica full de final (varianta curată e auzită corect) | aceeași replică; sub z4 muzica trece pe stratul `pulse`, apoi fade ca înainte |
| g6 | „traced transfer” → „trace transfer” la toate variantele | păstrată: e legătura normală din engleză, nu greșeală |

Master v3: -14,1 LUFS, vârf -2,0 dBFS, 672,6 s (`ffmpeg volume=+4.1dB, alimiter limit=0.77 attack=2 release=60`), AAC 256k → `renders:audio/ep002_audio.m4a`.
