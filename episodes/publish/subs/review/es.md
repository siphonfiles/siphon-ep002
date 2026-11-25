# Review: Spanish (Latin American) (`es`)
Method: blind back-translation (`review/es.back.json`), comparison with `source.json`, full native read. Build: 0 hard errors, 0 number notes; remaining soft warnings are short cues ("x1.3–1.5" on 1–2 s cues) where no shorter natural wording exists.

## Meaning (3)
- **19**: «Vuelve al final.» → «Reaparece al final.» — After the imperative 'Recuerda ese préstamo.', 'Vuelve al final' reads as an order to the viewer ('go back to the end'); the English means the loan comes back later.
- **138**: «Cada transferencia robada juntó unos 1.000 fragmentos de moneda.» → «Cada transferencia robada juntó unos 1.000 pequeños fragmentos de moneda.» — Producer clarification: small separate pieces (inputs).
- **174**: «Y el informe de Mandiant no nombra a nadie.» → «Y el informe de Mandiant no nombra absolutamente a nadie.» — Restores the emphasis 'no one at all'.

## Grammar (1)
- **34**: «Controles de riesgo la revisan.» → «Pasa por controles de riesgo.» — Bare plural subject before the verb is unnatural in Spanish; same meaning, natural order.

## Style (3)
- **148**: «Parte del Zcash desapareció en un pool privado, donde no se puede seguir.» → «Parte del Zcash desapareció en un pool privado, donde no se puede rastrear.» — 'seguir' without object is vague; 'rastrear' is the natural term for following funds.
- **156**: «ZachXBT dice que los lavadores pidieron atención al cliente» → «ZachXBT dice que los lavadores pidieron ayuda al soporte» — 'pedir atención al cliente' is unidiomatic; 'pedir ayuda al soporte' is the natural phrasing.
- **173**: «Sobre Bitget, ningún gobierno ha dicho una palabra.» → «Sobre Bitget, ningún gobierno ha dicho ni una palabra.» — Idiomatic negative ('ni una palabra') = 'not a word'.

## Terminology (2)
- **48**: «un día cero, permitió al atacante ejecutar un script oculto.» → «un zero-day, permitió al atacante ejecutar un script oculto.» — 'un día cero' as a bare noun is unclear; 'zero-day' is the term Latin American security press uses.
- **69**: «Bitget dice que las credenciales se robaron mediante el día cero,» → «Bitget dice que las credenciales se robaron mediante el zero-day,» — Consistency with cue 48.

## Still uncertain
- Number format: the file uses 63.000 / 0,84 / 1,5 mil millones (Southern-Cone / RAE style). Mexico and Central America use 63,000 / 0.84. Consistent within the file; change globally only if the target audience is mainly Mexican.
- 50 'felpudo' is understood everywhere but Mexicans/Colombians say 'tapete'. Left as is.
- 31 'billeteras tibias' (warm wallets) is rare in Spanish crypto writing but transparent next to calientes/frías; kept.
- 53 'recién el 24 de septiembre' is idiomatic LatAm for 'not before 24 September'; kept.
