# ja — independent review

Method: blind back-translation (`ja.back.json`), then a comparison with source.json, then a full native read. Build: 0 hard, 0 soft. I checked all 30 number notes by hand: 3億8800万=388M, 2億300万=203M, 2億3800万=238M, 1億6100万=161M, 60億=6B, 3億=300M, 15億=1.5B, 4万=40,000, 6万3000=63,000, 10万/20万, 3万5678, 3475万=34.75M. All match.

## Meaning
- 53: 攻撃者の特権アクセスの時期を9月24日としか特定していない → 攻撃者の特権アクセスを9月24日までしかさかのぼっていない. The old version was ambiguous. The new one says plainly that Mandiant's evidence goes back no earlier than 24 September.
- 109: 顧客の出金を止めたのは、間違ったスイッチだった → 顧客の出金停止は、押すべきスイッチではなかった. The old version could read as "what stopped customer withdrawals was the wrong switch". The new one says blocking them was the wrong lever.
- 116: 最初の警報から2時間39分。 → 最初の警報から2時間39分にわたって。 The old version only gave a point in time. The new one gives the duration: the service kept running for 2 h 39 min after the first alert.
- 69–70: Bitgetによれば…盗まれ、／…排除したという → Bitgetによると、認証情報はゼロデイ脆弱性で盗まれたもので、／内部の人間の関与は、現時点では排除されている。 The attribution to Bitget now covers both halves, and the split reads cleanly. "For now" is kept (現時点では).
- 138: 約1000個のコインの断片を寄せ集めていた → 約1000個の小さなコインの断片をまとめていた (producer clarification: small pieces/inputs).

## Grammar
- 63: 同じスクリプトは広がっていた → 同じスクリプトが広がっていた (が fits new information here).

## Style
- 11: この件の痛さを知るには → なぜこれが痛手なのかを知るには (more natural, and closer to "why this one hurts").
- 54: 食い違いは、まだ解消されていない → 内容は、まだすり合わされていない ("reconciled": the reports have not been brought into line).
- 142: 誰もそれを見張っていなかった → 誰もそれに目を光らせていなかった ("watching for them").

## Terminology / numbers
- 135: 35,678件 → 3万5678件, to match the 万 style used everywhere else (6万3000, 4万).

## Still uncertain
- 197: the sign-off 以上、Siphon Filesでした uses です/ます while the narration is plain form. This is a conventional broadcast sign-off, so I kept it.
- 34 リスク審査 ("risk checks") and 76/79/102 リスク管理 ("risk control") are kept as distinct terms because the English uses distinct terms.
