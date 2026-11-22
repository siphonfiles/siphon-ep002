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
