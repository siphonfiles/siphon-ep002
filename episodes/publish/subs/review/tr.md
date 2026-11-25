# Review: tr

Method: blind back-translation (`review/tr.back.json`) written before opening source.json, then comparison, then a full native read.

Total changes: 28 (grammar 8, meaning 7, style 11, terminology 2)


## Meaning

- **11**: Bunun neden bu kadar acıttığını anlamak için 19 ay geri gidelim. Şubat 2025. → Bunun neden acıttığını anlamak için 19 ay geri gidelim. Şubat 2025. — dropped added intensifier 'bu kadar' (EN: why this one hurts)
- **19**: Sonunda geri dönecek. → Sonda yeniden karşımıza çıkacak. — 'Sonunda geri dönecek' read as 'it will eventually be repaid'; EN = it comes back at the end of the story
- **32**: Sıcak cüzdanlar çekimlerini otomatik olarak, günün her saati öder. → Sıcak cüzdanlar senin çekimlerini günün her saati otomatik olarak öder. — 'çekimlerini' was ambiguous (their/your); made 'your' explicit
- **53**: Bir çekince: Mandiant, saldırganın ayrıcalıklı erişimini yalnızca 24 Eylül'e tarihliyor. → Bir çekince: Mandiant, saldırganın ayrıcalıklı erişimini en erken 24 Eylül'e tarihliyor. — 'yalnızca 24 Eylül'e tarihliyor' unclear; producer note: no earlier than 24 September
- **124**: İzleri örtmek için ya da daha fazlası için. → İz örtmek mi, daha fazlası mı? — 'ya da daha fazlası için' was incomplete; now 'covering tracks, or more?' as two possibilities, answered by 125
- **138**: Çalınan her transfer yaklaşık 1.000 coin parçasını bir araya getirdi. → Çalınan her transfer yaklaşık 1.000 küçük coin parçasını bir araya getirdi. — producer note: small separate pieces (inputs)
- **172**: FBI hırsızların adını verdi: Kuzey Kore'nin TraderTraitor'ı. → FBI hırsızların adını verdi: Kuzey Kore'nin TraderTraitor grubu. — producer note: TraderTraitor is a group; made explicit

## Grammar

- **10**: Kayıtlarda. Tarihi 24 gün öncesi. → Kayıtlarda. 24 gün öncesine ait. — 'Tarihi 24 gün öncesi' is ungrammatical as a sentence; natural form
- **33**: «Çek» tuşuna bastığında bir talep işlem hattına girer. → “Çek” düğmesine bastığında bir talep işlem hattına girer. — Turkish quotation marks; button = düğme in an app
- **100**: O anda Bitget'te paran varsa, → O anda Bitget'te paran vardıysa, — past conditional needed (EN: if you had money)
- **144**: Ve yeni bir sorun: onu nasıl elde tutacaktı. → Ve yeni bir sorun: Parayı nasıl elinde tutacaktı? — fragment read ungrammatically; now a proper question
- **153**: 11 günde yaklaşık 161 milyon dolar, çoğu CoinJoin üzerinden; → 11 günde yaklaşık 161 milyon dolar, çoğu CoinJoin üzerinden. — semicolon + dangling appositive replaced
- **154**: birçok kişinin coin'lerini tek bir işlemde karıştıran bir yöntem. → Bu yöntem, birçok kişinin coin'lerini tek bir işlemde karıştırıyor. — see 153
- **165**: Bunun, dediğine göre, ön göstergelere dayandığını söyledi. → Bunun ön göstergelere dayandığını söyledi. — redundant 'dediğine göre ... söyledi'
- **182**: Bitget'te paran varsa, onu kaybetmedin. → Bitget'te paran vardıysa, onu kaybetmedin. — past conditional (EN: if you had money)

## Style

- **21**: O dönem yılın en büyük kripto hırsızlığıydı. → O sırada yılın en büyük kripto hırsızlığıydı. — 'O dönem' → 'O sırada' (at the time)
- **51**: Yalnız paspas güvenlik odasının içindeydi. → Ne var ki paspas güvenlik odasındaydı. — more natural 'except' connector
- **80**: Onun yanıtlarını sahteledi. → Onun yanıtlarını taklit etti. — 'sahteledi' is not natural Turkish
- **84**: sistem, kontrollerin geçildiği konusunda talep sahibinin sözüne düpedüz güvendi. → sistem, kontrollerin geçildiğine dair talep edenin sözüne öylece güvendi. — 'düpedüz' (downright) wrong nuance; smoother word order
- **96**: Böylece denemeyi bıraktılar. → Bu yüzden denemeyi bıraktılar. — 'Böylece' (thereby) → 'Bu yüzden' (so)
- **109**: Müşteri çekimlerini engellemek yanlış şalterdi. → Müşteri çekimlerini engellemek, yanlış şalteri indirmekti. — 'yanlış şalterdi' unidiomatic
- **117**: İki ayrı tahmin, alarmdan sonra → İki ayrı tahmine göre alarmdan sonra — 'tahmin ... buluyor' awkward; split kept
- **118**: çıkan parayı yaklaşık 238 milyon dolar buluyor. → çıkan para yaklaşık 238 milyon dolar. — see 117
- **125**: Raporlar bunu söylemiyor. → Raporlar söylemiyor. — fits the question in 124
- **155**: Ve onu taşıyanlar pek iyi saklanmıyordu. → Ve parayı taşıyanlar pek iyi saklanmıyordu. — 'onu' (it) unclear → 'parayı'
- **196**: ve imza makinesini çalışır hâlde bıraktı. → imza makinesini ise çalışır hâlde bıraktı. — avoid 've ... bıraktı / ve ... bıraktı' repetition

## Terminology

- **72**: Oradan yana doğru, üretimdeki cüzdan iş sunucusuna geçtiler. → Oradan yanal hareketle üretimdeki cüzdan iş sunucusuna geçtiler. — 'yana doğru' → security term 'yanal hareket' (lateral movement)
- **156**: ZachXBT'ye göre aklayıcılar, kullandıkları servislerin → ZachXBT'ye göre parayı aklayanlar, kullandıkları servislerin — 'aklayıcılar' is rare; 'parayı aklayanlar' natural

## Still uncertain / notes

- 143 stays a soft length warning (17 cps); no shorter natural wording.
- 'ılık cüzdan' for warm wallet is the term used in Turkish crypto media but less common than sıcak/soğuk; kept.
- 150 keeps '(permissionless)' once, as allowed by the rules.
