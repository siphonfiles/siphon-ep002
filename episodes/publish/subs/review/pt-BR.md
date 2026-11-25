# Review: Brazilian Portuguese (`pt-BR`)
Method: blind back-translation (`review/pt-BR.back.json`), comparison with `source.json`, full native read. Build: 0 hard errors, 0 number notes; remaining soft warnings are short cues ("x1.3–1.5" on 1–2 s cues) where no shorter natural wording exists.

## Meaning (3)
- **53**: «Uma ressalva. A Mandiant só situa o acesso privilegiado do atacante em 24 de setembro.» → «Uma ressalva. A Mandiant só data o acesso privilegiado do atacante a partir de 24 de setembro.» — Producer clarification: Mandiant puts the access no earlier than 24 September; 'só situa em' was unclear.
- **138**: «Cada transferência roubada juntou cerca de 1.000 pedaços de moeda.» → «Cada transferência roubada juntou cerca de 1.000 pequenos pedaços de moeda.» — Producer clarification: small separate pieces (inputs).
- **174**: «E o relatório da Mandiant não nomeia ninguém.» → «E o relatório da Mandiant não nomeia absolutamente ninguém.» — Restores 'no one at all'.

## Grammar (2)
- **18**: «Lembre desse empréstimo.» → «Lembre-se desse empréstimo.» — Written standard requires the pronominal form; 'Lembre desse' is colloquial speech.
- **58**: «Deixa eu parar aqui um segundo.» → «Vou parar aqui um segundo.» — 'Deixa eu' is spoken colloquialism, not accepted in written subtitles.

## Style (2)
- **20**: «Em 24 de setembro de 2026, a corretora que veio ajudar virou a roubada.» → «Em 24 de setembro de 2026, a corretora que veio ajudar é que foi roubada.» — 'virou a roubada' is awkward; the cleft 'é que foi roubada' is the natural way to say 'became the one robbed'.
- **173**: «Sobre a Bitget, nenhum governo disse uma palavra.» → «Sobre a Bitget, nenhum governo disse uma palavra sequer.» — Idiomatic emphasis for 'not a word'.

## Terminology (1)
- **34**: «Checagens de risco o analisam.» → «Passa por verificações de risco.» — 'checagens' is informal and the file uses 'verificações' for checks (cue 84); bare plural subject also unnatural.

## Still uncertain
- 31 'carteiras mornas' (warm wallets) is uncommon but transparent next to quentes/frias; kept.
- 150 'design sem permissão' for permissionless: Brazilian crypto press also writes 'permissionless'; kept the translated form.
