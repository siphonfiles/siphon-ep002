# zh-Hant review (Traditional Chinese, Taiwan)

Method: blind back-translation (`zh-Hant.back.json`) → comparison with `source.json` → full native read. Build: 0 hard, 0 soft. All 9 number notes checked by hand: 4萬枚 = 40,000; 6.3萬 = 63,000; 10萬/20萬; 60億美元 = $6 billion; 3億美元 = $300 million. 3.88億, 2.03億, 2.38億, 1.61億, 15億, 3475萬 USDT, 35,678, 0.84, 0.3%, every time and date match the English.

Taiwan vocabulary confirmed: 資安, 零時差, 伺服器, 惡意套件, 金鑰, 提領, 簽章, 存取, 管線, 執行長, 北韓, 影片說明欄, 旁白, IP位址, 帳 (轉帳/對帳/到帳).

## Meaning
- **53** `認定在9月24日` → `追溯到9月24日`. Mandiant puts the access no earlier than 24 Sep. It did not "determine" that date (same fix as zh-Hans).
- **124** `湮滅痕跡` → `掩蓋痕跡`. 湮滅 means destroying evidence, which is stronger than "covering tracks".
- **138** `約1000個零碎的幣` → `約1000筆零散的小額資金` (about 1,000 small separate pieces, now clear).
- **139** `只用了54個` → `匯集了54筆`. Same counter as 138, and the added "只" is gone.
- **142** `盯著它們` → `留意它們`. The English is "watching for them", not "watching them".
- **168** `親眼看著` → `看著`. 親眼 ("with its own eyes") adds emphasis the English doesn't have, and is odd for a company.
- **181** `都指向` → `指向`. Drops the added "都".

## Uncertain
- 114 `目的地址白名單`: Taiwan uses 位址 for IP/network addresses (kept in 163), but 地址 is normal for wallet addresses (錢包地址). Kept as is.
