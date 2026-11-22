# Episodul 002: Paznicul era ușa (traducere în română, pentru verificare)

Originalul, în engleză, e în `002-the-guard-was-the-door.md`, cu sursele [S#] și notele editoriale. Aici e doar textul vorbit și cartoanele, ca să-l poți verifica ușor. Thomas = în cadru, VO = vocea peste imagini.

---

## 0:00 · Teaser
**VO:** N-au furat nicio cheie. N-au spart blockchain-ul. Au intrat prin singurul lucru care trebuia să-i oprească—
**Carton:** „Nobody stole a key.” („Nimeni n-a furat vreo cheie.”) — analiza DFNS
**VO:** La 19:05 a sunat alarma. Bitget a blocat retragerile tuturor clienților. Și banii au continuat să plece încă—
**VO:** Și primul semn că cineva era înăuntru? E în loguri. Datat cu douăzeci și patru de zile—
*(negru, bas, titlul: SIPHON FILES · THE GUARD WAS THE DOOR)*

## 0:30 · Rezultatul
**VO:** Pe 24 septembrie 2026, 387 de milioane și jumătate de dolari au ieșit de pe exchange-ul crypto Bitget. Au plecat din portofelele hot și warm, cele care plătesc clienții în fiecare zi. Portofelele cold n-au fost atinse.
**Thomas:** Sunt Thomas Archer, naratorul AI al Siphon Files. Fiecare afirmație din episod are o sursă, toate sunt în descriere. Partea ciudată: firma de investigații a Bitget, Mandiant, n-a găsit nicio dovadă că ar fi fost compromisă vreo cheie privată. Deci cum furi 387 de milioane fără chei? Pui exchange-ul să semneze în locul tău.

## 1:05 · Cum te plătește un exchange
**VO:** Ca să înțelegi cum, trebuie să știi unde își ține un exchange banii. Cei mai mulți stau în portofele cold: offline, lente, greu de atins. Apoi sunt portofelele warm, care țin rezerva ce reumple nivelul următor. Și portofelele hot, care plătesc retragerile automat, non-stop.
**VO:** Când apeși „withdraw”, cererea intră într-un circuit. Verificările de risc se uită la ea. Apoi un serviciu de semnare pune pe ea o semnătură criptografică, și banii pleacă. Semnătura e tot ce contează. Fără ea, nu pleacă nimic. Cu ea, pleacă orice.
**VO:** Ține minte asta. Atacatorul n-a avut nevoie de secretul semnăturii. Doar de mașina care o folosește.

## 2:00 · Cu 24 de zile înainte
**Carton:** T-MINUS 24 DAYS
**VO:** 31 august. E cea mai veche activitate malițioasă găsită de anchetatori în loguri. Nu era în portofele. Era într-un produs de securitate, unul dintre cele două unelte ale altor firme care rulau în mediul de producție al Bitget.
**VO:** Anchetatorii le spun simplu Produsul A și Produsul B. Producătorul n-a fost numit. Nu există un număr public de vulnerabilitate. Pe Produsul A, o breșă pe care n-o știa nimeni, un zero-day, l-a lăsat pe atacator să ruleze un script ascuns.
**VO:** Zero-day înseamnă exact asta: cei care fac produsul au avut zero zile s-o repare, pentru că nu știu că există. Scriptul a citit o parolă de bază de date. Stătea în clar, într-o variabilă de mediu.
**VO:** Gândește-te la o cheie de rezervă lipită sub preș, doar că preșul era în biroul pazei. Cu parola aceea, scriptul s-a conectat direct la baza de date.
**VO:** Aceeași activitate a apărut pe a doua mașină pe 23 septembrie, și pe a treia pe 25.
**VO:** O precizare: Mandiant datează accesul privilegiat al atacatorului pe 24 septembrie. Logurile SlowMist merg înapoi până la 31 august. Cele două rapoarte nu au fost încă puse de acord.

## 3:05 · Puntea
**Thomas:** Să mă opresc o secundă. Firmele cumpără produse de securitate ca să supravegheze ușile. Le dau acces adânc, pentru că doar așa văd totul. Ceea ce înseamnă că, dacă cineva preia paznicul, nu mai are nevoie să spargă vreo ușă. E deja pe fiecare hol.

## 3:25 · Cu 2 ore și 24 de minute înainte
**Carton:** T-MINUS 2 HOURS 24 MINUTES · 24 SEP · 16:07 UTC
**VO:** La 16:07 UTC, cineva s-a logat în consola Produsului B.
**VO:** Produsul B e descris ca o platformă de management, genul de unealtă cu care administratorii rulează sarcini pe multe mașini. Au folosit identitatea unui angajat real al Bitget. Cum au obținut-o e încă sub investigație.
**VO:** Au încercat trei injecții de comenzi. Apoi au trimis cod printr-un punct de execuție web. Mandiant a găsit ce a urmat: un web shell și un canal de comandă și control înapoi spre atacator.
**VO:** De acolo s-au mutat lateral, pe serverul de producție care construiește tranzacțiile de retragere. Au instalat pe el pachete malițioase.

## 4:25 · Cu 42 de minute înainte
**Carton:** T-MINUS 42 MINUTES · 17:49 UTC
**VO:** La 17:49, o unealtă a pornit pe serverul portofelelor. SlowMist a recuperat-o mai târziu din fișiere șterse. Făcea trei lucruri: falsifica rezultatele verificărilor de risc, construia cereri de retragere și le împingea în procesul normal de retragere al Bitget.
**VO:** Asta e tot trucul. Verificările de risc erau raportate de cel care făcea cererea. Deci unealta spunea pur și simplu că verificările au trecut, verificări care nu rulaseră niciodată. Iar semnatarul a semnat. A produs semnături valide fără să verifice cine cere de fapt.

## 5:15 · Ora zero: 18:31
**Carton:** 18:31 UTC — în Asia e două și jumătate noaptea.
**VO:** 18:31. Două transferuri minuscule: 93 TRX, apoi 0,84 ETH. Teste. Destul de mici cât să rămână sub pragurile de alertă. Și nicio alarmă nu a sunat.
**VO:** Apoi, nimic. Aproape o jumătate de oră.
**VO:** 18:58. 34,75 milioane USDT pleacă într-un singur transfer.

## 5:55 · Vârful
**VO:** 19:01. Șapte transferuri. Cinci blockchain-uri. Cincisprezece secunde.
**VO:** 19:05. Reconcilierea Bitget observă în sfârșit diferența. Controlul de risc blochează retragerile pentru toți clienții platformei. 19:14: urgență de cel mai înalt nivel.
*(liniște 1 s)*
**VO:** 19:16. Cinci transferuri. Cinci blockchain-uri. Nouă secunde. Aproximativ 203 milioane de dolari, mai ales din portofelele warm.
**VO:** Clienții fuseseră blocați cu unsprezece minute înainte. Atacatorul, nu.
**VO:** De ce portofelele warm? Pentru că acolo stă rezerva mai mare, cea care reumple portofelele hot. Două portofele pe care Bitquery le consideră warm au trimis aproximativ 55% din tot ce s-a furat. Și pe acel nivel nu exista niciun pas de aprobare în plus între cerere și semnătură. Nicio a doua persoană. Nicio listă de destinații permise. Pe fiecare blockchain de tip Ethereum, banii au mers la o singură adresă nouă.

## 6:50 · De ce nu s-a oprit
**VO:** Blocarea retragerilor clienților a fost butonul greșit. Cererile falsificate nu erau retrageri de clienți. Serviciul de semnare a continuat să meargă 2 ore și 39 de minute după prima alertă. După o estimare, aproximativ 60% din bani au plecat după ce alarma sunase deja.
**VO:** La 20:40, Bitget a început să mute fondurile în portofelele cold. În acel moment încă nu putea exclude că fuseseră furate chei. Ultimul transfer urmărit a plecat la 21:23. După 21:22, atacatorul a încercat să rescrie înregistrările de retragere direct în baza de date. Două comenzi false de Bitcoin au dat eroare. La 21:44, Bitget a oprit serviciile de retragere, inclusiv semnarea.
**VO:** A doua zi dimineață, la 08:43, Bitget spune că a găsit cauza. La 13:42 a raportat furtul autorităților. A anunțat o recompensă de recuperare: 5% din orice se recuperează sau se îngheață, pentru cine ajută. Și a adus două echipe din afară: Mandiant, parte din Google Cloud, și firma de securitate blockchain SlowMist.

## 7:45 · Amprenta pe care n-o urmărea nimeni
**VO:** Exista un semn, la vedere. Fiecare transfer pe blockchain fixează o limită de „combustibil”, gas. Plățile normale către clienți ale Bitget foloseau cam 63 de mii. Transferurile atacatorului foloseau exact 100 de mii sau 200 de mii. Din 35.678 de tranzacții din săptămâna aceea, nicio altă tranzacție nu făcea asta.
**VO:** Și fiecare comandă falsificată era ștearsă după fiecare transfer.

## 8:15 · Unde s-au dus banii
**VO:** Stablecoin-urile au plecat primele, pentru că stablecoin-urile pot fi înghețate. Toți cei 34,75 milioane USDT au fost schimbați pe ETH în 20 de minute. XRP-ul, peste 40% din pradă, a fost mutat în Bitcoin prin THORChain. O parte din Zcash a intrat într-un fond privat, unde nu mai poate fi urmărit.
**VO:** ETH-ul a fost parcat în opt portofele. Șase dintre ele aveau exact câte 10.000 ETH. În câteva zile, cea mai mare parte a început să se miște: în THORChain pentru Bitcoin și prin alte punți spre alte blockchain-uri. BNB și TRX au fost transformate în Bitcoin într-o zi.
**VO:** Bitget a cerut THORChain să blocheze adresele. THORChain a refuzat, invocând faptul că e o rețea fără permisiuni.
**VO:** În final, au fost înghețate aproximativ 1,1 milioane de dolari. Sub 0,3%.
**Carton (parafrază):** CEO-ul Bitget a spus că nu se așteaptă să recupereze mare lucru. — CNBC

## 8:55 · Cine?
**VO:** Deci cine a făcut asta? În noaptea atacului, CEO-ul Bitget, Gracy Chen, a spus că tiparul seamănă cu ce face Coreea de Nord. A invocat adrese IP care se potrivesc cu servicii VPN folosite înainte de un grup nord-coreean.
**Carton:** „The pattern looks very much like what the North Korean team did before.” („Tiparul seamănă foarte mult cu ce a făcut echipa nord-coreeană înainte.”) — Gracy Chen, livestream pe X
**VO:** Patru zile mai târziu a fost mai prudentă. Ce spusese, a explicat ea, se baza pe indicii preliminare.
**VO:** Firmele de analiză blockchain înclină în aceeași direcție. Chainalysis leagă furtul de actori asociați cu Coreea de Nord. Elliptic spune că e foarte probabil. TRM Labs spune că e probabil. O parte din spălare a trecut prin portofele care mutaseră înainte bani furați de la Bybit.
**VO:** Investigatorul ZachXBT a raportat că unul dintre cei care au spălat banii mutase și fonduri din atacul asupra Kelp DAO din aprilie. Kelp, Drift, Bitget: trei furturi mari în mai puțin de șase luni, toate înclinând în aceeași direcție în rapoartele analiștilor.
**VO:** Dar niciun guvern nu a atribuit atacul asupra Bitget. Iar raportul Mandiant nu face nicio atribuire.

## 9:35 · Tiparul
**Thomas:** Iată ce putem spune. În 2025, Bybit a pierdut un miliard și jumătate de dolari. FBI a dat vina pe Coreea de Nord. Iar metoda pornea de la aceeași idee: nu furi cheia, ci schimbi ce crede semnatarul că semnează. La o lună după Bitget, Binance a pierdut peste șase miliarde. FBI a numit grupul nord-coreean TraderTraitor în câteva zile. Pentru Bitget, confirmarea asta n-a venit.

## 10:00 · Final
**VO:** Clienții n-au pierdut bani. Bitget a acoperit pierderea din fondul său de protecție. Fondul ăsta e motivul pentru care povestea nu e despre clienți ruinați. Pierderea a căzut pe firmă, nu pe oamenii care aveau bani pe exchange. Retragerile de Bitcoin s-au redeschis pe 28 septembrie. Totul a revenit până pe 2 octombrie. Vulnerabilitatea e reparată, iar funcția producătorului e oprită.
**VO:** Bitget spune că a restrâns accesul intern, a adăugat verificare independentă pentru retrageri și a întărit monitorizarea activității neobișnuite. Operațiunile critice cer acum mai multe aprobări. Cu alte cuvinte, o cerere singură n-ar mai trebui să fie de ajuns. Producătorul tot n-a fost numit.
**Thomas:** Bitget a cumpărat unelte ca să-i păzească ușa. Timp de cel puțin douăzeci și patru de zile, le ținea altcineva în mână. Și când alarma a sunat în sfârșit, exchange-ul și-a blocat clienții, dar a lăsat mașina de semnat să meargă. Sunt Thomas Archer. Ați urmărit Siphon Files.
