# Episodul 002: Paznicul era ușa (traducere în română, pentru verificare) · DRAFT v2

Originalul, în engleză, e în `002-the-guard-was-the-door.md`, cu sursele [S#], notele editoriale și lista schimbărilor față de v1. Aici sunt doar textul vorbit și cartoanele, ca să le poți verifica ușor. Thomas = în cadru, VO = vocea peste imagini.

**Titlul (ales):** Inside the $388M Bitget Hack · **Thumbnail:** NO KEY WAS STOLEN · înainte de publicare: Test & Compare cu 3 variante.

---

## 0:00 · Teaser
**VO:** N-au furat nicio cheie. N-au spart blockchain-ul. Au intrat prin singurul lucru care trebuia să-i oprească—
**Carton:** „Nobody stole a key.” („Nimeni n-a furat vreo cheie.”) — analiza DFNS
**VO:** La 19:05 a sunat alarma. Bitget a blocat retragerile tuturor clienților. Și banii au continuat să plece încă—
**VO:** Și primul semn că cineva era înăuntru? E în loguri. Datat cu douăzeci și patru de zile—
*(negru, bas, titlul: SIPHON FILES · THE GUARD WAS THE DOOR)*

## 0:30 · Rezultatul
**VO:** Pe 24 septembrie 2026, aproximativ 388 de milioane de dolari au ieșit de pe exchange-ul crypto Bitget. Au plecat din portofelele hot și warm, cele care plătesc clienții în fiecare zi. Portofelele cold n-au fost atinse. La momentul acela, era cel mai mare furt crypto al anului.
**Thomas:** Sunt Thomas Archer, naratorul AI al Siphon Files. Fiecare afirmație din episod are o sursă, toate sunt în descriere. Partea ciudată: Bitget spune că nu a fost compromisă nicio cheie privată. Deci cum furi 388 de milioane de dolari fără chei? Pui exchange-ul să semneze în locul tău.

## 1:05 · Cum te plătește un exchange
**VO:** Un exchange își ține cei mai mulți bani în portofele cold: offline, lente, greu de atins. Portofelele warm țin o rezervă. Portofelele hot plătesc retragerile automat, non-stop.
**VO:** Când apeși „withdraw”, cererea intră într-un circuit. Verificările de risc se uită la ea. Apoi un serviciu de semnare pune pe ea o semnătură criptografică, și banii pleacă. Fără semnătura asta, nu pleacă nimic. Cu ea, pleacă orice.
**VO:** Ține minte asta. Atacatorul n-a avut nevoie de secretul semnăturii. Doar de mașina care o folosește.

## 1:50 · Cu 24 de zile înainte
**Carton:** T-MINUS 24 DAYS
**VO:** 31 august. E cea mai veche activitate malițioasă găsită de anchetatori în loguri. Nu era în portofele. Era într-un produs de securitate, unul dintre cele două unelte ale altor firme care rulau în sistemele Bitget.
**VO:** Anchetatorii le spun simplu Produsul A și Produsul B. Producătorul n-a fost numit. Nu există un număr public de vulnerabilitate. Pe Produsul A, o breșă pe care n-o descoperise nimeni încă, un zero-day, l-a lăsat pe atacator să ruleze un script ascuns.
**VO:** Scriptul a citit o parolă de bază de date. Stătea în clar, într-o variabilă de mediu. Gândește-te la o cheie de rezervă lipită sub preș, doar că preșul era în biroul pazei.
**VO:** Același script ascuns a apărut pe a doua mașină pe 23 septembrie. Și pe a treia, în noaptea furtului.
**VO:** O precizare: Mandiant datează accesul privilegiat al atacatorului pe 24 septembrie. Logurile SlowMist merg înapoi până la 31 august. Cele două rapoarte nu au fost puse de acord.
**VO:** Oricum ar fi, timp de mai bine de trei săptămâni nu s-a întâmplat nimic din ce să observe cineva.

## 2:50 · Puntea
**Thomas:** Să mă opresc o secundă. Firmele cumpără produse de securitate ca să supravegheze ușile. Le dau acces adânc, pentru că doar așa văd totul. Ceea ce înseamnă că, dacă cineva preia paznicul, nu mai are nevoie să spargă vreo ușă. E deja pe fiecare hol.

## 3:10 · Cu 2 ore și 24 de minute înainte
**Carton:** T-MINUS 2 HOURS 24 MINUTES · 24 SEP · 16:07 UTC
**VO:** La 16:07 UTC, cineva s-a logat în platforma de management a Produsului B. A folosit identitatea unui angajat real al Bitget. Bitget spune că datele de logare au fost furate prin același zero-day. Și spune că, deocamdată, a exclus pe oricine din interior.
**VO:** Au încercat trei injecții de comenzi. Apoi au trimis cod printr-un punct de execuție web. Mandiant a găsit un web shell pe dispozitivul B și un canal de comandă și control înapoi spre atacator.
**VO:** De acolo s-au mutat lateral, pe serverul de producție care construiește tranzacțiile de retragere. Au instalat pe el pachete malițioase.

## 4:05 · Cu 42 de minute înainte
**Carton:** T-MINUS 42 MINUTES · 17:49 UTC
**VO:** La 17:49, pe serverul portofelelor a pornit o unealtă. SlowMist a recuperat-o mai târziu din fișiere șterse. A falsificat rezultatele verificărilor de risc. A construit cereri de retragere. Și le-a împins în fluxul normal de retrageri al Bitget.
**VO:** Asta e tot trucul. Potrivit unei analize, sistemul pur și simplu l-a crezut pe cuvânt pe cel care trimitea cererea că verificările trecuseră. Și semnatarul a semnat.

## 4:50 · Ora zero: 18:31
**Carton:** 18:31 UTC · În Asia e două și jumătate noaptea.
**VO:** 18:31. Două transferuri minuscule. 93 TRX. Apoi 0,84 ETH. Teste. CEO-ul Bitget spune că erau sub pragul de risc, așa că nu s-a declanșat nicio alertă.
**VO:** Apoi, nimic. Aproape o jumătate de oră.
**VO:** 18:58. 34,75 milioane de USDT pleacă într-un singur transfer.

## 5:30 · Vârful
**VO:** 19:01. Șapte transferuri. Cinci blockchain-uri. Cincisprezece secunde.
**VO:** 19:03. Încă un test mic, dintr-un alt portofel. Două minute mai târziu, alarma.
**VO:** 19:05. Reconcilierea Bitget observă în sfârșit diferența. Controlul de risc blochează retragerile pentru toți clienții platformei. 19:14. Urgență de cel mai înalt nivel.
**VO:** 19:16. Cinci transferuri. Cinci blockchain-uri. Nouă secunde. Aproximativ 203 milioane de dolari.
**VO:** Clienții fuseseră blocați cu unsprezece minute înainte. Atacatorul nu.
**VO:** Potrivit unei analize, nimic nu stătea între o cerere și o semnătură la portofelele warm. Niciun al doilea om. Nicio listă de destinații permise.

## 6:15 · De ce nu s-a oprit
**VO:** Blocarea retragerilor clienților a fost întrerupătorul greșit. Cererile falsificate nu erau retrageri de clienți. Serviciul de semnare a mers încă 2 ore și 39 de minute după prima alertă. Două estimări separate pun banii plecați după alarmă la aproximativ 238 de milioane de dolari. Mai mult de jumătate.
**VO:** La 20:40, Bitget a început să mute fondurile în cold storage. În acel moment încă nu putea exclude că fuseseră luate chei. Ultimul transfer urmărit a plecat la 21:23. Apoi atacatorul a încercat să rescrie direct în baza de date înregistrările retragerilor. Două comenzi false de Bitcoin au dat erori. La 21:44, Bitget a oprit serviciile de retragere, inclusiv semnarea.
**VO:** A doua zi dimineață, Bitget a găsit cauza. În aceeași după-amiază a raportat furtul la autorități. A adus Mandiant, parte din Google Cloud, și firma de securitate blockchain SlowMist. Și a oferit o recompensă: 5 la sută din orice sumă înghețată sau recuperată, pentru cine ajută.

## 7:10 · Amprenta pe care n-a urmărit-o nimeni
**VO:** Exista un semn, la vedere. Fiecare transfer pe Ethereum își fixează o limită de „combustibil”, gazul. Plățile normale ale Bitget către clienți foloseau cam 63 de mii. Transferurile atacatorului foloseau exact 100 de mii sau 200 de mii. În cele opt zile dinaintea furtului, acele portofele au trimis 35.678 de tranzacții. Nicio plată către clienți n-a făcut așa.
**VO:** Pe Zcash a fost și mai vizibil. Fiecare dintre cele două transferuri furate a adunat aproape o mie de bucăți separate de monedă. Până atunci, cea mai mare tranzacție a portofelului folosise 54.
**VO:** Și comenzile falsificate au fost șterse după fiecare transfer.

## 7:40 · Unde au ajuns banii
**VO:** Stablecoin-urile au plecat primele, pentru că stablecoin-urile pot fi înghețate. Toți cei 34,75 milioane de USDT au fost schimbați în ETH în 20 de minute. XRP-ul, cam două cincimi din pradă, a ajuns în Bitcoin prin THORChain. O parte din Zcash a dispărut într-un fond privat, unde nu mai poate fi urmărită.
**Pe ecran:** ETH parcat în opt portofele, șase cu exact 10.000 ETH fiecare.
**VO:** Bitget a cerut THORChain să blocheze adresele. THORChain a refuzat, invocând faptul că e deschis tuturor, fără permisiuni. În final, au fost înghețați aproximativ 1,1 milioane de dolari. Sub 0,3 la sută.
**VO:** Apoi, luna asta, Bitcoin-ul a început să se miște din nou. În unsprezece zile, aproximativ 161 de milioane de dolari au plecat din portofelele etichetate drept ale hackerului Bitget, cei mai mulți prin CoinJoin, o metodă care amestecă monedele mai multor oameni într-o singură tranzacție. Pe 16 noiembrie, acele portofele mai aveau cam 35 de bitcoini.
**VO:** Și cei care mutau banii nu se ascundeau prea bine. ZachXBT spune că spălătorii au cerut ajutor la serviciul clienți în chaturile publice de Discord și Telegram ale serviciilor pe care le foloseau. Schimburi eșuate. Plăți lipsă. El spune că erau spălători de bani chinezi, care lucrau pentru atacatori.
**Carton:** CEO-ul Bitget a spus că nu se așteaptă să recupereze mare lucru. — CNBC *(parafrază pe ecran, nu citat)*

## 8:35 · Cine?
**VO:** Deci cine a făcut asta? În noaptea atacului, CEO-ul Bitget, Gracy Chen, a spus că niște adrese IP se potriveau cu servicii VPN folosite de un grup nord-coreean.
**Carton:** „The pattern looks very much like what the North Korean team did before.” („Tiparul seamănă foarte mult cu ce a făcut echipa nord-coreeană înainte.”) — Gracy Chen, livestream pe X
**VO:** Patru zile mai târziu, a fost mai prudentă. Ce spusese, a explicat, se baza pe indicii preliminare.
**VO:** Firmele de analiză blockchain înclină în aceeași direcție. Chainalysis leagă furtul de actori asociați cu Coreea de Nord. Elliptic spune că e foarte probabil. TRM Labs spune că e probabil. Elliptic spune că Bitget a împins furturile nord-coreene suspectate din 2026 peste un miliard de dolari. Iar ZachXBT spune că unul dintre acei spălători a mutat și bani din exploit-ul Kelp DAO din aprilie.
**VO:** Apoi a venit Binance. La cinci săptămâni după Bitget, Binance a pierdut peste șase miliarde de dolari. Iar Chainalysis a văzut banii furați de la Binance întâlnindu-se pe blockchain cu banii de la Bitget. În timp real. ZachXBT spune că ambii au ajuns, prin THORChain, la aceeași adresă.
**VO:** La două zile după furtul de la Binance, FBI a numit hoții: grupul nord-coreean TraderTraitor. Pentru Bitget însă, niciun guvern n-a spus nimic. Iar raportul Mandiant nu numește pe nimeni.

## 9:35 · Împrumutul
**Thomas:** Mai e un detaliu. În februarie 2025, Bybit a pierdut un miliard și jumătate de dolari. FBI a dat vina pe Coreea de Nord. În aceeași zi, Bitget i-a împrumutat lui Bybit 40.000 de ether, ca să-i țină retragerile în funcțiune. Fără dobândă. Fără garanții. Nouăsprezece luni mai târziu, banii plecau de la Bitget. Iar analiștii arată în aceeași direcție.

## 10:00 · Final
**VO:** Clienții n-au pierdut bani. Bitget spune că a acoperit pierderea din fondul de protecție. Fondul ăsta e motivul pentru care povestea nu e despre clienți ruinați. Pierderea a căzut pe companie. Fondul a fost refăcut la puțin peste 300 de milioane de dolari. Tot mai puțin decât înainte de furt.
**VO:** Toate retragerile au revenit până pe 2 octombrie. Vulnerabilitatea e reparată, iar funcția furnizorului e oprită. Operațiunile critice la Bitget cer acum mai mult de o aprobare. Cu alte cuvinte, o cerere singură n-ar mai trebui să fie de ajuns. Și spune că revizuiește modul în care își alege produsele de securitate de la alte firme. Furnizorul tot n-a fost numit.
**Thomas:** Bitget a cumpărat unelte ca să păzească ușa. Timp de cel puțin douăzeci și patru de zile, s-ar putea ca altcineva să le fi ținut în mână. Iar când alarma a sunat în sfârșit, exchange-ul și-a blocat clienții și a lăsat mașina de semnat să meargă. Sunt Thomas Archer. Acesta a fost Siphon Files.

---

## Ce s-a schimbat față de v1 (pe scurt)
1. „Mandiant n-a găsit dovezi că s-a compromis vreo cheie” → **„Bitget spune că nu a fost compromisă nicio cheie”**. În raport, Mandiant notează doar că Bitget n-a observat așa ceva.
2. Suma vorbită: 387,5 → **„aproximativ 388 de milioane”**, cifra finală Bitget, aceeași cu titlul.
3. Scoase cifra „55% din portofelele warm” și „mai ales din warm”: împărțirea hot/warm nu e în datele Bitquery.
4. Adăugat: angajatul nu e suspect, iar datele de logare au fost furate prin zero-day (CEO-ul, la AMA).
5. Adăugate: legătura cu Binance, împrumutul către Bybit, urma CoinJoin din noiembrie, spălătorii care cer ajutor în chaturi publice, amprenta de pe Zcash, testul de la 19:03.
6. Formulate ca analiză sau ca afirmație a sursei: deducțiile DFNS și legătura cu Kelp DAO („ZachXBT spune”).
7. Finalul: „altcineva le ținea” → **„s-ar putea ca altcineva să le fi ținut”**, pentru că Mandiant datează accesul mai târziu decât SlowMist.
