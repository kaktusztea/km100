# Képzettségrendszer

▲ [Nyitóoldal](start.md)\
→ [TODO/ISSUE képzettségrendszer](https://github.com/kaktusztea/km100/wiki/ISSUE.TODO.kepzettsegek)


- [Képzettségek kategóriái](#képzettségek-kategóriái)
- [Képzettségek növelése](#képzettségek-növelése)
- [Képzettségek pontigényei](#képzettségek-pontigényei)
  - [Képzettségek követelményei](#képzettségek-követelményei)
  - [Karakter Pontok elosztása](#karakter-pontok-elosztása)
- [Képzettségpróba](#képzettségpróba)
  - [Vállalás](#vállalás)
  - [Próba biztos tudásból](#próba-biztos-tudásból)
  - [Próba képzetlenül](#próba-képzetlenül)
  - [Összetett képzettségpróba, Másodlagos próbadobások](#összetett-képzettségpróba-másodlagos-próbadobások)
  - [Összhangok](#összhangok)
  - [Képzettség párok](#képzettség-párok)
  - [Sérülés hatása képzettségpróbára](#sérülés-hatása-képzettségpróbára)

Mikor a játékos megalkotja karakterét, amellyel Ynev világán kalandozni fog, meghatározza azokat az ismereteket, jártasságokat, amelyeket az - addigi élete során - elsajátított. A km100 rendszere a fentieket a képzettségek és fortélyok tanulásával szimulálja. Ebben a fejezetben a Képzettségekkel fogunk foglalkozni. Minden Képzettséget egy számértékkel jellemzünk, amelyből kiderül, tulajdonosa mennyire jártas az adott témában.

Ez az érték a karakter életútja során - a megszerzett tapasztalatoknak hála -, növekedhet, amely fejlődést a játékos Karakteralkotó Pontjai (`KP`) elosztásával jelenít meg.

## Képzettségek kategóriái

A képzettségeket kategóriákra bontjuk aszerint, mennyire átfogóak, mekkora ismeretanyagot ölelnek fel, tehát **nem** tanulásuk „nehézsége" szerint próbálunk különbséget tenni! Három kategóriát különbözetünk meg:

> 🔴 Átfogó, 🔵 Átlagos, 🟢 Specializált/Könnyű

A Képzettségeket és egymáshoz való viszonyukat legjobban halmazokkal tudnánk szemléltetni, melyek közül a legnagyobb (`Átfogó`) több kisebbet (`Átlagos`) tartalmaz, amelyek további még kisebb (`Specializált`) halmazokat foglalnak magukban. A „`Könnyű`" képzettségek nem tartoznak egyik felsorolt halmazba sem, önmagukban állnak, kezelésük viszont szinte mindenben megegyezik a Specializált képzettségekével (lásd később).

| Képzettség kategória | Például |
| ----------- | :----------- |
| 🔴 **Átfogó** | Történelemismeret - Ynev |
| 🔵 **Átlagos** | Történelemismeret - Pyarroni államszövetség,<br />vagy Történelemismeret - Kyria |
| 🟢 **Specializált / Könnyű** | Történelemismeret - Predoc |

Az `Átfogó` képzettségek jellemzője, hogy általános, mindenre kiterjedő tudást nyújtanak az adott területen. Éppen ezért tanulásuk is tovább tart, ami meg is látszik a magasabb `KP` igényen. Ennek következménye, hogy magába foglal több konkrétabb Képzettséget, amelyeket az `Átlagos`, vagy `Specializált` kategóriákban találunk. Az ide tartozó képzettségeket tekinthetjük a legnagyobb halmaznak. Ilyen Átfogó képzettség például az általános történelemismeret : "`Történelemismeret - Ynev`".

Az `Átlagos` képzettségek már jóval konkrétabb, - így gyorsabban tanulható - tudást takarnak (így KP igényük is alacsonyabb), egy konkrét feladatkörrel foglalkoznak, viszont azon belül mindennel, például a „`Történelemismeret - Pyarroni államszövetség`" képzettség kizárólag a nevéből adódó terület történelmét foglalja magában.

Végére maradtak a `Specializált` képzettségek, amelyek egy adott terület egy konkrét, szűk problémakörével foglalkoznak. Könnyen megtanulhatóak, de viszonylag szűk, gyakorlatias tudást takarnak. A fenti példánál maradva a „`Történelemismeret - Predoc`" kizárólag Predoc állam történelmének ismeretét nyújtja, ha tágabb tudásra vágyunk, ahhoz már legalább Átlagos Képzettséget kell felvennünk.

Természetesen a karakter egy bizonyos szinten túl nem fejlődhet egy adott specializált képzettségben, szüksége van az átfogóbb tudásra is. Szabály, hogy:

```
A Specializált és az őt magába foglaló Átlagos képzettség közti különbség legfeljebb 3 lehet.
```

A Specializált képzettségekkel együtt és azonos módon kezeljük a „`Könnyű`" képzettségeket, melyek azért kerültek ebbe a csoportba, mert tanulásuk során hamar el lehet érni a maximumot, így KP igényük is alacsony. Egyetlen különbség a Specializált képzettségekhez képest, hogy egy `Könnyű` képzettségnek nincsen felsőbb halmaza (Átlagos, vagy Átfogó), amibe beletartozna, így a maximum 3-as különbség limit itt nem is értelmezhető.

Amennyiben a karakter rendelkezik olyan Képzettséggel, amely egy általa szintén ismert Képzettség alá tartozik (része), akkor ha a „magasabb kategóriájú" Képzettséget növeli, akkor az alá tartozó „alacsonyabb kategóriájú" képzettség értéke nem változik.

> Példa

A karakter rendelkezik `6-os szintű` „Történelemismeret - Predoc" (**Specializáció**) és `3-as szintű` „Történelemismeret - Pyarroni államszövetség" (**Átlagos**) képzettséggel. Mivel Predoc a Pyarroni államszövetsége része, ezért a fenti, **Átlagos** képzettség tudásanyagába ez is beletartozik. Ekkor ha a karakter mondjuk `+2-vel` növeli az **Átlagos** képzettségét (`3+2=5`), attól a **Specializált** képzettsége továbbra is `6` marad, a növelés nem „tolta" maga előtt az alsóbb képzettséget.

Ha az `Átlagos` képzettség értéke „beéri" a `Specializáltét`, akkor „magába olvasztja" azt. Természetesen bármikor „kinöveszthető" újra egy `Specializáció` az `Átlagos` képzettségből. Ugyanez igaz természetesen az `Átfogó` és az alá tartozó `Átlagos` képzettségekre is.

> Összefoglalva

A képzettségeket három kategóriába sorolhatjuk. Ezek a következőek:

- 🔴 Átfogó
- 🔵 Átlagos
- 🟢 Specializáció, illetve „Könnyű" képzettségek

A „`Könnyű`" képzettségekben hamar el lehet érni a maximumot (ilyen pl az Úszás, Futás, Nyelvismeret).

Az `Átfogó` csoport alá a nagyobb, átfogóbb képzettségek tartoznak, mint pl. a Történelemismeret, Sebgyógyítás, stb. Olyanok, amelyekben egy életen keresztül is lehet fejlődni.

---
## Képzettségek növelése

A karakterek fejlődése természetesen nem lehet ugrásszerű, meg kell őriznünk a folyamatosság illúzióját szintlépéskor, el kell kerülnünk, hogy egy 3. szintű karakter 12-13-as értékekkel rohangáljon. Ugyanakkor fontos színesítő, ha egy 1. szintű karakter egyes területeken kitűnik társai közül. Általános szabályok:

- A harci és misztikus képzettségek szintje legfeljebb (`szint+3`) lehet
- A többi képzettség értéke pedig legfeljebb (`szint+8`) lehet
- Szintlépéskor legfeljebb `2-vel` növelhetőek a képzettségek, kivéve, ha 0-ról akar valaki egy képzettséget tanulni. Ilyenkor szintlépéskor maximum `3.szintre` növelheti egy lépésben az ilyen képzettséget.
- Egy Átlagos, vagy Specializáció képzettség `legfeljebb 3-al lehet magasabb`, mint az őt magába foglaló Átfogó, vagy Átlagos képzettség.  Ha nincs fölé tartozó képzettség (pl. Nyelvismeret esetén), akkor természetesen nincs felső korlát.
- A képzettségek egyes kiemelt szintjeinek is lehetnek követelményei!  Magas szinten főleg.

---
## Képzettségek pontigényei

A fejlődés Karakter Pontba (`KP`) kerül. A KP szimulálja az egyes képzettségek elsajátítására fordított tanulás „egységnyi mennyiséget". Hogy a korábban ismertetett három kategóriának (Átfogó, Átlagos, Spec/Könnyű) adott szinten mekkora a KP igénye, azt az alábbi táblázat adja meg:

| Fokozat | Képzettség Szint | 🔴 Átfogó |       | 🔵 Átlagos |       | 🟢 Spec /<br />Könnyű |       |
| ------- | :--------------: | :----: | :---- | :------: | :---- | :---------: | :---- |
|             | 1  | 6   | +6KP  | 4   | +4KP  | 2  | +2KP |
|             | 2  | 10  | +4KP  | 6   | +2KP  | 3  | +1KP |
| Novícius    | 3  | 16  | +6KP  | 9   | +3KP  | 5  | +2KP |
|             | 4  | 24  | +8KP  | 13  | +4KP  | 7  | +3KP |
|             | 5  | 34  | +10KP | 18  | +5KP  | 10 | +3KP |
| Kismester   | 6  | 46  | +12KP | 24  | +6KP  | 13 | +4KP |
|             | 7  | 60  | +14KP | 31  | +7KP  | 17 | +4KP |
|             | 8  | 76  | +16KP | 39  | +8KP  | 21 | +5KP |
| Mester      | 9  | 94  | +18KP | 48  | +9KP  | 26 | +5KP |
|             | 10 | 114 | +20KP | 58  | +10KP | 31 | +6KP |
|             | 11 | 136 | +22KP | 69  | +11KP | 37 | +6KP |
| Nagymester  | 12 | 160 | +24KP | 81  | +12KP | 43 | +7KP |
|             | 13 | 186 | +26KP | 94  | +13KP | 50 | +7KP |
|             | 14 | 214 | +28KP | 108 | +14KP | 57 | +8KP |
| Élő legenda | 15 | 244 | +30KP | 123 | +15KP | 65 | +8KP |

A `KP igény` fokozatosan nő, tehát `1`-ről `2`-re sokkal könnyebb fejlődni, mint mondjuk `4`-ről `5`-re. Átfogó és Átlagos képzettségben hagyományos tanulással `legfeljebb 13`-ig lehet fejlődni. `14`-es és `15`-ös szintre csak úgy juthat el a karakter, ha a képzettséggel kapcsolatos, nagyon ritka titkos tudásra tesz szert. Ez kaland alapja is lehet!! Pl. megszerezni a "Gyógyító Érintés Tudományának Titkos Fóliását" (Sebgyógyításhoz).

A másik felső korlát lehet az adott kultúra fejletlensége, vagy korlátai. Például egy primitív nomád törzs kuruzslója nem fejlődhet Sebgyógyításban `6`-os érték fölé, mert nincs olyan forrás, ahonnan a hatékonyabb módszereket megtanulhatná. A KM mindig vegye figyelembe az adott körülményeket és fejlődési lehetőségeket.

---
### Képzettségek követelményei

Nem csak a Fortélyoknak, a Képzettségek egyes szintjeinek is lehetnek követelményei. Ez persze nem minden Képzettségre igaz, de van, ahol szükséges.

Ha egy képzettség egy bizonyos fokának eléréséhez szükség van valamilyen teljesítendő követelményre, akkor azt az adott képzettség leírásánál részletezzük.

---
### Karakter Pontok elosztása

A karakteralkotás fejezetben ismerettük a Karakter Pontok értékének
számítását. A képzettségek „vásárlása" is ezekből történik.

---
## Képzettségpróba

Vesszük az adott szituációban épp szükséges Tulajdonság értékét (KM mondja meg, hogy melyiket), hozzáadjuk a Képzettség értékét, majd dobunk `k10`-es kockával és a fentieket összeadjuk. Ha a kapott szám nagyobb, vagy egyenlő a Célszámmal, akkor a próba sikerült.

```
Tulajdonság + Képzettség + k10   vs.  Célszám
```

| Képzettségpróba<br /><sub>(dobás k10-el)</sub> | Célszám  |
| ------ | :-----: |
| Könnyű          | 6  |
| Átlagos         | 9  |
| Nehéz           | 12 |
| Nagyon nehéz    | 15 |
| Rendkívül nehéz | 18 |
| Emberfeletti    | 21 |

Ha a KM úgy látja, hogy az adott próbánál több Tulajdonság is szerepet játszik, akkor a szükséges Tulajdonságok átlagával kell számolni.

---
### Vállalás

A Vállalás azt jelenti, hogy (ha a KM is beleegyezik) képzettségpróba esetén kaphatsz legfeljebb `+3` bónuszt a próbára - Te döntöd el mennyit. Minél többet vállalsz, annál nagyobb veszélynek teszed ki magad. Ugyanis a próba előtt „Vállalás próbát" kell dobni:

```
k6 vs. (a vállalás értéke)
```

> **Fontos**: a Vállalás értéke nem haladhatja meg képzettséged aktuális értékét!

Ha `k6`-on a Vállalás értékével megegyezőt, vagy kisebbet dobsz, akkor kritikus, halálos hibát vétesz és természetesen nem dobhatsz képzettségpróbát se. Ebből látszik, hogy vállalni csak nagyon fontos, ritka esetben van értelme. Úgy foglalhatjuk össze, hogy mikor vállalsz, olyankor megpróbálkozol valami olyan dologgal, ami hatékonyabb, mint jelenlegi tudásod, de még nem gyakoroltad be rendesen (pl. csak ellested a mesteredtől), így a rontásra is nagyobb az esélyed.

A fenti példánál maradva egy 2-es Vállalás esetén már a következőképpen fest a próba:

```
2 (Ügyesség) + 5 (Mászás) + 2 (Vállalás)+ k10   vs.  15 (Nagyon nehéz)

Azaz: (9+k10)  vs  15
```

Ez sokat dob az esélyeken, de megvan a rizikója is: ha a fenti karakter a dobás előtt a Vállalás-próbánál k6-on 1-et, vagy 2-t dob, akkor Halálos hibát vét!

> **Fontos**: összetett, több dobást igénylő képzettségpróbánál nem alkalmazható Vállalás! (pl. megmászni a nagy hegyet).

---
### Próba biztos tudásból

Bizonyos képzettségeket csak biztos tudásból lehet megpróbálni, nincs lehetőség képzettségpróba dobására. Tipikusan a „Tudok-e valamit róla?"-jellegű határozottan eldönthető esetekben. Ilyenkor a KM dönti el, hogy az adott képzettségszinttel az adott feladat megoldható, avagy sem.

---
### Próba képzetlenül

Ha a karakter egyáltalán nem jártas az adott képzettségben (vonatkozó értéke nulla), akkor -- ha a képzettség leírásánál engedélyezett a képzetlen dobás -- ugyanúgy próbát dob, mint bárki, de a `célszám 3-al emelkedik`. Egyes képzettségek esetén képzetlenség esetén **nem jár** a 3-as, célszám emelő büntetés. Ilyenek tipikusan az alapvető fizikai képzettségek (`mászás, esés, ugrás`), valamint az olyanok, melyeket minden ember tud legalább minimális szinten, még ha soha nem is foglalkozott
vele.

Hogy mely képzettségek esetén lehet képzetlenül is próbát tenni, azt az összefoglaló táblázatban találod. Ha az adott képzettséget nem lehet képzetlenül megpróbálni, akkor a KM egyszerűen megtagadja a próbát, automatikusan sikertelennek véve azt.

⭕ PROB_KEPZETTSEGEK\_#11. (összhang) ⭕

---
### Összetett képzettségpróba, Másodlagos próbadobások

Ha a karakternek egy olyan összetett feladatot kell elvégeznie, ami nem intézhető el 1db dobással (pl. megmászni egy hegyet, vagy rettentő magas várfalat, esetleg órákon keresztül verset szavalni), akkor igazságtalan lenne a maximális nehézséget többször megdobatni vele, hiszen így drasztikusan lecsökken az esélye a sikerre. Ilyenkor a következő módszert használjuk:

- A játékos dob egy próbát az indokolt maximális nehézségre (pl. „Nagyon nehéz" (`Célszám:12`))
- Ezután dob több (a KM dönti el, hány) próbát **1 fokozattal (-3 célszám) alacsonyabb nehézség ellen**. Pl. (`2db Nehéz próbát`). Így a siker eloszlása sokkal fokozatosabb és a biztos tudást is jobban jutalmazzuk, valamint elkerüljük, hogy egy kezdő - csak azért, mert szerencséset dobott - egy hosszú, részletes, tudását jóval meghaladó feladatot „véletlenül" megcsinálhasson.
- Hogy a másodlagos dobásból hány kell, az főleg attól függ, hogy a feladat „milyen hosszú", mennyire „többlépcsős".
- Ha nagyon finom bontást akarunk, akkor `akár 2 fokozattal` (-6  célszám) alacsonyabb nehézségre is dobathatunk akár így is: Nagyon nehéz (1db), Nehéz(1db), Átlagos (1db).

> Példa ⚡ Megmászni egy 200 ynevi láb magas, omladékos hegyet

- Tetves, a tolvaj `Mászás képzettsége: 7`, `Ügyessége: +2` , így `8+2=9`-re dob majd rá `k10`-el.
- A próba „Nagyon nehéz" (`Célszám: 15`)
- Mivel az út hosszú, nem intézhető el a dolog 1db dobással, a KM `2db Másodlagos próbát` ír elő.
- Ekkor a próbák célszámai: `15`, `12`, `12` (azaz `50%`, `80%` és `80%` esély a sikerre). Ezzel kb. `30%`-a van a teljes feladat sikerére (`0.5 x 0.8 x 0.8`). Látható, hogy az összetettebb feladatok nagyobb fokú biztos tudást igényelnek.
- Tehát a próbák:

```
- 1x Nagyon nehéz (15)
- 2x Nehéz        (12)
```

⭕ **TODO**: Kidolgozni továbbiakat!⭕

---
### Összhangok

Vannak olyan esetek, amikor egyes képzettségek ismerete segítséget nyújthat más képzettségek használatakor. Az ilyet nevezzük Összhangnak. Természetesen a két érték nem adható össze, az aránytalansághoz vezetne.

Ilyen esetekben attól függően, hogy mennyire kapcsolódik, a „kiegészítő" képzettség az adott feladathoz, annak `1/3`-a, vagy `1/5`-e adható hozzá képzettségpróbánál az elsődleges képzettség értékéhez. Tehát:

```
- Ha erősen kapcsolódik: 1/3-a adható hozzá
- Ha közepesen kapcsolódik: 1/5-e adható hozzá
```

Például a karakter dulakodás nyomait találja egy erdei tisztáson. Valamilyen állat is ott volt. Ekkor `Nyomolvasás` képzettségpróbát kell dobnia, de mivel nagy segítséget jelentene, ha tudná, hogy milyen állat is volt jelen, ezért ebben az esetben a `Természetjárás` képzettség kiegészítő képzettségként működik. Mivel a jelen próbához a `Természetjárás` erősen kapcsolódik, ezért annak `1/3`-a hozzáadható a karakter Nyomolvasás képzettségéhez (a próba idejére).

---
### Képzettség párok

Bizonyos képzettségek „függésben" vannak egymással, azaz az adott képzettség legfeljebb egy meghatározott szinttel lehet magasabb a másik, kapcsolódó képzettségnél. Az ilyen egyedi függéseket jelezzük az adott képzettség leírásánál.

---
### Sérülés hatása képzettségpróbára

Ha megsérül a karakter, képzettségpróbáira levonások járnak. Hogy mennyi, az attól függ, hogy melyik sebesülés kategóriában van, illetve hogy fizikai mozgást igénylő, vagy nem igénylő képzettségét teszi próbára:

|      | S1  | S2 | S3 | S4 |
| ---- | :----: | :----: | :----: | :----: |
| **fizikai** | -  | -2 | -4 | -6 |
| **egyéb**   | -  | -  | -1 | -3 |

---
