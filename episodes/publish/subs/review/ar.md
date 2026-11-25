# Review: ar

Method: blind back-translation (`review/ar.back.json`) written before opening source.json, then comparison, then a full native read.

Total changes: 22 (grammar 7, terminology 4, meaning 6, style 5)


## Meaning

- **19**: سيعود في النهاية. → وسنعود إليه في النهاية. — 'سيعود في النهاية' read as 'it will be repaid'; EN = it comes back in the story at the end
- **53**: تحفّظ واحد: تؤرّخ Mandiant الوصول المميّز للمهاجم بيوم 24 سبتمبر فقط. → تحفّظ واحد: لا تُرجع Mandiant وصول المهاجم بصلاحيات مميّزة إلى ما قبل 24 سبتمبر. — producer note: no earlier than 24 September; 'بيوم 24 سبتمبر فقط' was unclear
- **71**: عثرت Mandiant على web shell في الجهاز B، وعلى قناة تعود إلى المهاجم. → عثرت Mandiant على web shell في الجهاز B، وعلى قناة اتصال تصل إلى المهاجم. — 'قناة تعود إلى المهاجم' = a channel belonging to the attacker; EN = a channel back to the attacker
- **109**: كان إيقاف سحوبات العملاء هو المفتاح الخطأ. → كان إيقاف سحوبات العملاء هو الزر الخطأ. — 'المفتاح' also means 'key', confusing in an episode about keys; producer note: wrong lever
- **138**: كل تحويل مسروق جمع نحو 1,000 قطعة من العملة. → كل تحويل مسروق جمع نحو 1,000 قطعة صغيرة من العملة. — producer note: small separate pieces
- **145**: خرجت العملات المستقرة أولًا، لأن العملات المستقرة يمكن تجميدها. → تخلّص من العملات المستقرة أولًا، لأن العملات المستقرة يمكن تجميدها. — 'خرجت العملات المستقرة أولًا' = 'left first' (ambiguous); EN = they were got rid of first

## Grammar

- **11**: لنفهم لماذا يؤلم هذا الحادث، لنعد 19 شهرًا إلى الوراء. فبراير 2025. → لكي نفهم لماذا يؤلم هذا الحادث بالذات، لنعد 19 شهرًا إلى الوراء. فبراير 2025. — avoid doubled 'لـ' construction; 'this one' rendered with بالذات
- **13**: يتهم FBI كوريا الشمالية. → يتهم الـFBI كوريا الشمالية. — Arabic usage takes the article: الـFBI
- **103**: 19:14. طوارئ من أعلى مستوى. → 19:14. حالة طوارئ من أعلى مستوى. — 'طوارئ' alone needs 'حالة'
- **116**: لمدة 2 ساعة و39 دقيقة بعد التنبيه الأول. → لمدة ساعتين و39 دقيقة بعد التنبيه الأول. — '2 ساعة' ungrammatical; dual form (same value)
- **135**: في الأيام الـ8 السابقة، أرسلت تلك المحافظ 35,678 معاملة. → في الأيام الثمانية السابقة، أرسلت تلك المحافظ 35,678 معاملة. — 'الأيام الـ8' unnatural; number word (same value)
- **172**: سمّى FBI اللصوص: مجموعة TraderTraitor الكورية الشمالية. → سمّى الـFBI اللصوص: مجموعة TraderTraitor الكورية الشمالية. — article with FBI
- **178**: حمّل FBI كوريا الشمالية مسؤولية تلك السرقة. → حمّل الـFBI كوريا الشمالية مسؤولية تلك السرقة. — article with FBI

## Style

- **101**: فهذا ما رأيته: سحبك توقف. → فهذا ما رأيته: توقّف سحبك. — natural verb-first order
- **125**: التقارير لا تقول. → التقارير لا توضّح ذلك. — 'لا تقول' alone is incomplete in Arabic
- **126**: أمران مزيفان على Bitcoin أعادا رسائل خطأ. → أمران مزيّفان بعملة Bitcoin أعادا رسائل خطأ. — 'على Bitcoin' unclear
- **137**: وعلى Zcash، كان الأمر أوضح. → وعلى Zcash، كانت البصمة أوضح. — 'الأمر' vague; the trace/fingerprint is meant
- **195**: وعندما انطلق الإنذار أخيرًا، منعت المنصة عملاءها، → وعندما انطلق الإنذار أخيرًا، أغلقت المنصة الباب في وجه عملائها، — 'منعت عملاءها' (forbade its customers) incomplete; idiom for 'locked out', echoing the door image

## Terminology

- **17**: بلا فائدة. بلا ضمان. → بلا فائدة. بلا ضمانات. — collateral = ضمانات
- **150**: فرفضت THORChain، متذرعةً بتصميمها غير المشروط بالإذن. → فرفضت THORChain، متذرعةً بتصميمها الذي لا يتطلب إذنًا. — 'غير المشروط بالإذن' unnatural rendering of permissionless
- **156**: يقول ZachXBT إن غاسلي الأموال طلبوا الدعم الفني → يقول ZachXBT إن غاسلي الأموال طلبوا دعم العملاء — customer support = دعم العملاء, not technical support
- **177**: بلا فائدة. بلا ضمان. → بلا فائدة. بلا ضمانات. — see 17

## Still uncertain / notes

- 116 and 135 trigger number notes by design: ساعتين = 2 and الثمانية = 8, checked by hand.
- 'web shell' (71) left in English, as Arabic security writing commonly does.
- Decimal/thousand separators kept Western (0.84, 40,000, 35,678) as in the original file.
