# Review: Hindi (hi)

Method: blind back-translation (`review/hi.back.json`), comparison with source.json, full native read. Build: 0 hard errors.


## Meaning (7)

- **50**: जैसे पायदान के नीचे चिपकाई गई एक अतिरिक्त चाबी। → पायदान के नीचे चिपकी एक अतिरिक्त चाबी। — 'जैसे' (like) added a comparison not in the English; also shorter
- **53**: एक बात ध्यान रखें। Mandiant हमलावर की प्रिविलेज्ड ऐक्सेस सिर्फ़ 24 सितंबर से मानता है। → एक बात ध्यान रखिए। Mandiant के हिसाब से हमलावर की प्रिविलेज्ड ऐक्सेस 24 सितंबर से ही शुरू होती है। — no earlier than 24 Sept (producer note); 'रखिए' consistent with 18/92
- **138**: चोरी के हर ट्रांसफ़र ने कॉइन के करीब 1,000 टुकड़े एक साथ जोड़े। → चोरी के हर ट्रांसफ़र ने कॉइन के करीब 1,000 छोटे-छोटे टुकड़े एक साथ जोड़े। — producer note: about 1,000 small pieces
- **142**: उन पर कोई नज़र नहीं रख रहा था। → उन्हें कोई खोज ही नहीं रहा था। — 'watching for them' = nobody was looking out for them
- **152**: नवंबर में, Bitcoin फिर से आगे बढ़ने लगा। → नवंबर में, वह Bitcoin फिर से हरकत में आया। — 'आगे बढ़ने लगा' can read as the price rising
- **155**: और इसे आगे बढ़ाने वाले ठीक से छिप भी नहीं रहे थे। → और यह पैसा ले जाने वाले लोग ठीक से छिप भी नहीं रहे थे। — 'आगे बढ़ाने वाले' ambiguous (promoters)
- **163**: कहा कि कुछ IP पते एक उत्तर कोरियाई ग्रुप की VPN सर्विस से मेल खाते थे। → कहा कि कुछ IP पते उन VPN सर्विसों से मेल खाते थे जिन्हें एक उत्तर कोरियाई ग्रुप इस्तेमाल करता है। — 'used by' a group, not the group's own service

## Grammar (9)

- **32**: हॉट वॉलेट आपके विदड्रॉल अपने-आप, चौबीसों घंटे चुकाते हैं। → हॉट वॉलेट चौबीसों घंटे, अपने-आप आपके विदड्रॉल का भुगतान करते हैं। — 'विदड्रॉल चुकाते हैं' unidiomatic (one pays a withdrawal out, not 'repays' it)
- **47**: Product A में एक खामी, जो अब तक किसी को नहीं मिली थी, → Product A में एक ऐसी खामी ने, जो अब तक किसी को नहीं मिली थी, — broken sentence across 47/48; subject now carries 'ने'
- **48**: यानी एक ज़ीरो-डे, उसके ज़रिए हमलावर ने एक छिपी स्क्रिप्ट चलाई। → यानी एक ज़ीरो-डे ने, हमलावर को एक छिपी स्क्रिप्ट चलाने दी। — 'let the attacker run' (flaw is the subject), was an anacoluthon
- **70**: और फ़िलहाल उसने किसी अंदरूनी व्यक्ति की संभावना ख़ारिज कर दी है। → और फ़िलहाल उसने किसी अंदरूनी व्यक्ति के शामिल होने की संभावना ख़ारिज कर दी है। — 'possibility of an insider' → of an insider being involved
- **86**: असल में यह काम करता है या नहीं, यह जानने का एक ही तरीका था। → असल में यह काम करेगा या नहीं, यह जानने का एक ही तरीका था। — tense: past narrative frame needs 'करेगा'
- **109**: ग्राहकों के विदड्रॉल रोकना गलत स्विच था। → ग्राहकों के विदड्रॉल रोकना गलत स्विच दबाना था। — 'रोकना गलत स्विच था' (blocking was a switch) → was pressing the wrong switch
- **121**: अब भी यक़ीन नहीं था कि कुंजियाँ ली गई हैं या नहीं। → अब भी यक़ीन नहीं था कि कुंजियाँ ली गई थीं या नहीं। — pluperfect: 'had been taken'
- **141**: उंगलियों के निशान नहीं। → उंगलियों के निशान नहीं मिटे। — elliptical 'निशान नहीं' unclear in Hindi
- **162**: हैक वाली रात, Bitget की CEO, Gracy Chen, ने → हैक वाली रात, Bitget की CEO Gracy Chen ने — comma before 'ने' incorrect

## Style (8)

- **19**: वह आख़िर में फिर आएगा। → आख़िर में यह फिर सामने आएगा। — 'वह ... फिर आएगा' unclear
- **51**: बस पायदान सिक्योरिटी ऑफ़िस के अंदर था। → मगर पायदान सिक्योरिटी ऑफ़िस के अंदर ही था। — 'बस पायदान...' read as 'just the doormat'
- **80**: उसने उसके जवाब जाली बना दिए। → उसने उसके जवाब जाली गढ़ दिए। — 'जाली बना दिए' clumsy; 'forged its answers'
- **144**: और एक नई समस्या: उन्हें बचाए कैसे रखें। → और एक नई समस्या: इसे अपने पास कैसे रखें। — 'बचाए कैसे रखें' unnatural
- **148**: Zcash का एक हिस्सा प्राइवेट पूल में गायब हो गया, जहाँ उसका पीछा नहीं हो सकता। → Zcash का एक हिस्सा प्राइवेट पूल में गायब हो गया, जहाँ उसे ट्रेस नहीं किया जा सकता। — 'पीछा नहीं हो सकता' unnatural; ट्रेस is the usual term
- **175**: जो हमें उसी लोन पर वापस ले आता है। → यही हमें उस लोन पर वापस ले आता है। — sentence opening with 'जो' unnatural
- **187**: खामी ठीक कर दी गई है। → वह खामी ठीक कर दी गई है। — 'the vulnerability' (the one described)
- **189**: और Bitget के मुताबिक, वह सिक्योरिटी वेंडर चुनने के तरीके की समीक्षा कर रहा है। → और Bitget के मुताबिक, वह अपने सिक्योरिटी वेंडर चुनने के तरीके की समीक्षा कर रहा है। — 'its security vendors'

## Terminology (1)

- **129**: Bitget ने मूल वजह ढूँढी और चोरी की रिपोर्ट क़ानूनी एजेंसियों को दी। → Bitget ने मूल वजह ढूँढी और चोरी की सूचना क़ानून प्रवर्तन एजेंसियों को दी। — 'क़ानूनी एजेंसियाँ' = legal agencies; law enforcement = क़ानून प्रवर्तन एजेंसियाँ

## Uncertain / notes
- Large numbers kept in international grouping (100,000 / 200,000 / 35,678) as Ethereum/tech audiences write gas limits; Indian lakh grouping (1,00,000) would also be valid.
- 72 'बगल के रास्ते' for lateral movement kept; some tech YouTubers would say 'लैटरल मूवमेंट'.
- Nukta use (गलत/ग़लत, करीब/क़रीब) follows the file's existing, mostly nukta-less style; no mixed forms introduced except words already written with nukta (क़ानून, यक़ीन).
- FBI treated as masculine, CEO Gracy Chen feminine (की CEO, थीं), ऐक्सेस/रिक्वेस्ट feminine: consistent throughout.
- Soft warnings left (47, 59, 87, 95, 96, 192, 193): low cps or no shorter natural wording.
