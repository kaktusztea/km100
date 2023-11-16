## Harci helyzetek

|                Szituáció                  |                            Módosító                                   |                                   Megjegyzés                                                                                                                                                                                                                                                                                                                                                                                                                                               | 
|:-----------------------------------------:|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                Meglepetés                 |                              `TÉ:+20`                                 | A támadó kapja a módosítót.<br/>Pajzs VÉ csak akkor számít, ha a csapás nem hátulról jön.                                                                                                                                                                                                                                                                                                                                                                                                  |
|             Támadás hátulról              |                              `TÉ:+20`                                 | A támadó kapja a módosítót.<br/>Pajzs VÉ nem számít.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|            Támadás félhátulról            |                              `TÉ:+10`                                 | Pajzs VÉ csak akkor számít, ha a pajzsot tartó kéz felőli oldalról jön a csapás.                                                                                                                                                                                                                                                                                                                                                                                                           |
|              Készületlenség               |                        Lásd a Meglepetést                             | Ha egy karakter készületlen, akkor támadója a Meglepetés szituációnak megfelelő módosítókkal támadhat rá.                                                                                                                                                                                                                                                                                                                                                                                  |
|         Kábult/megrendült állapot         |                        `KÉ:-10, TÉ:-20, SP:-2`                        | Kábulat, rosszullét, mérgezés esetén ideiglenesen ezek a levonások járnak. A KM – belátása szerint – adhat KT „sebesülést” is<br/>(pl. mérgezésnél)                                                                                                                                                                                                                                                                                                                                        |
|            Észrevétlen támadás            | Áldozat Védő Értéke: mozgás jellegétől függő VÉ |  **Célpont mozgásának jellege, VÉ**<br/>• Álló helyzet / lassan sétáló hátulról: `0 VÉ`<br/>• Lassú egyenletes (séta): `20 VÉ`<br/>• Egyenletes kocogás: `40 VÉ`<br/>• Sprint egyenes vonalon: `60 VÉ`<br/>• Lassú kiszámíthatatlan: `40 VÉ`<br/>• Közepesen gyors, kiszámíthatatlan: `70 VÉ`<br/>• Gyors, kiszámíthatatlan: `100 VÉ`<br/><br/>Követelménye:<br/>• Sikeres „**Lopakodás/rejtőzés**” vs  „**Észlelés**” ellenpróba<br/>• Az Észrevétlen támadás több harci taktika követelménye (pl. Orvtámadás)  |
|        Képzetlen fegyverhasználat         |              `KÉ:-20, TÉ:-30` <br/>`VÉ:-30, CÉ: -30`                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|            Harc puszta kézzel             |                     `KÉ:-10, TÉ:-10, VÉ:-10`                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|              Érintő támadás               |                       `KÉ:0, TÉ:0, VÉ:-10`                            | Érinteni könnyebb, mint megütni, sebezni puszta kézzel.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Harc rosszabbik kézben tartott fegyverrel |                       `KÉ:-10, TÉ:-20, VÉ:-20`                        | Kivétel:<br/><br/>• **Kétkezesség** fortély. Csak annyit ad, hogy rosszabbik kézzel is levonás nélkül tudsz harcolni, de csak 1 fegyverrel!!<br/><br/>• **Kétkezes Harc** fortély                                                                                                                                                                                                                                                                                                              |
|             Harc magasabbról              |                              `TÉ:+10`                                 | A támadó kapja a módosítót.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|             Harc gyűlöletből              |                           `TÉ:+15, VÉ:-30`                            | Aki gyűlöletből harcol, az kevesebbet törődik a védekezéssel, minden erejével ellenfele elpusztítására tör. Az ilyen karakter kötelezően +15TÉ Támadó taktikával harcol (így -30VÉ sújtja).                                                                                                                                                                                                                                                                                                |
|               Fegyverrántás               | Puszta kezes KÉ  <br/>fegyver-függő levonással:<br/><br/>`[0 ;-10] KÉ`| `10`-el túldobott `KÉ` esetén a fegyverrántó támadhat elsőnek azonnal – teljes harcértékével.<br/><br/>Fegyverrántás fortély bónusza:<br/>`1. fok: +5 KÉ`<br/>`2. fok: +10 KÉ` + ha támadhat is:<br/>„**Első vágás**” manőver alkalmazható.                                                                                                                                                                                                                                                        |
|            Harc helyhez kötve             |                     `KÉ:-10, TÉ:-20, VÉ:-20`                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                Közrefogás                 |                        `+10 TÉ` a támadóknak                          | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|             Harc földön fekve             |                     `KÉ:-10, TÉ:-10, VÉ:-10`                          | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|            Beszorított helyzet            |                          Lásd a leírást!                              | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|             Harc félhomályban             |                               ⭕TODO⭕                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|            Félelem harc közben            |    Kötelezően max Védő taktikában kezd harcolni: `VÉ:+15; TÉ:-30`     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|               Lóról leesés                |                           ⭕Ezt ne ide!!!⭕                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|           A védekező takarásban           |                               ⭕TODO⭕                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|              Harc állatokkal              |                          Lásd a leírást!                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

---

<br/>

### Képzetlen fegyverhasználat

```
KÉ: -20, TÉ: -30, VÉ: -30, CÉ: -30
```

Ha egy karakter képzetlen az általa forgatott fegyver használatában, akkor harcértékeit a fenti levonások sújtják.

<br/>

---

### Harc puszta kézzel

```
Puszta kéz harcértékei: KÉ: -10, TÉ: -10, VÉ: -10
```

Amennyiben valaki fegyvertelenül, puszta kézzel kénytelen egy felfegyverzett ellenféllel harcolni, akkor alapesetben hátrányban van. Ez a Puszta kéz negatív harcértékeiben mutatkozik meg. A különböző pusztakezes Fortélyok csak mérsékelik ezt a hátrányt. Egyetlen kivétel a harcművészek „**Élő fegyver**” fortélya, amely teljesen megszünteti az említett hátrányokat (`0`-ra „emeli” mindhárom harcértéket).

A fenti levonások kizárólag **belharcban** nem érvényesülnek, ahhoz viszont „**Belharcba kerülés**” Manőver szükséges! Belharcban a Puszta kéz harcértékei `0`-ra emelkednek, valamint járnak a **Belharcból** eredő esetleges módosítók is.

A **Puszta kéz** – mint fegyver – szabály szempontjából „egykezes” fegyvernek számít, tehát **nem** lehet vele **Kétkezes harcot** folytatni!

<br/>

---

### Érintő támadás

```
KÉ: 0, TÉ: 0, VÉ: -10
```

Ha csak meg akarunk érinteni valakit harc közben, az könnyebb, mint puszta kézzel sérülést okozó támadást végbevinni. Az Érintő támadás harcértékei ezért: `KÉ: 0, TÉ: 0, VÉ: -10`\
Tehát a támadásra kisebb a büntetés, mint puszta kézre, a védekezés viszont nem változik.

<br/>

---

### Harc rosszabbik kézben tartott fegyverrel

```
KÉ:-10, TÉ:-20, VÉ:-20
```

Ha – akár sérülés hatására – a harcos kénytelen átvenni fegyverét ügyetlenebb kezébe, akkor csak a következő levonásokkal harcolhat: `KÉ:-10, TÉ:-20, VÉ:-20`\
Kivétel:
- **Kétkezesség** fortély. Csak annyit ad, hogy rosszabbik kézzel is levonás nélkül tudsz harcolni, de csak 1 fegyverrel!!
- **Kétkezes Harc** fortély

<br/>

---

### Támadás hátulról

```TÉ: +10```

Ha a karakter ellenfelére hátulról támad, 👀`+10 TÉ` módosító járul **Támadó Értékéhez**.

<br/>

---

### Meglepetés

```TÉ: +20```

Ha az ellenfél nem számít az őt érő támadásra, de még képes reagálni, akkor Meglepetésről beszélünk. Az ilyen helyzetben a támadó karakter 👀`+20 TÉ` módosítót kap harcértékeire.

<br/>

---

### Készületlenség

Ha egy karakter készületlen, akkor támadója a **Meglepetés** szituációnak megfelelő módosítókkal támadhat rá.

<br/>

---

### Megrendült

```diff
-  -10KÉ, -20TÉ, -2 Sebzés
-  Kell ez? Inkább KT-vel szimulálni, nem?
```

<br/>

---

### Észrevétlen támadás

Ha valaki úgy képes támadást leadni, hogy ellenfele erről az utolsó pillanatig nem tud, tehát egyáltalán nem képes rá reagálni, akkor **Észrevétlen támadásról** beszélünk.

Észrevétlen támadáshoz az alkalmazónak sikeres ellenpróbát kell dobnia **Lopakodás/rejtőzés** képzettségével áldozata **Észlelés** képzettsége ellen.

Ilyenkor ellenfele `Védő Értékét` annak mozgási jellege és mérete határozza meg:


| **Célpont mozgásának jellege**      | **VÉ**   |
| ----------------------------------- | :------: |
| Álló helyzet (vagy sétáló hátulról) | 0        |
| Lassú egyenletes (séta)             | 20       |
| Egyenletes kocogás                  | 40       |
| Sprint egyenes vonalon              | 60       |
| Lassú kiszámíthatatlan              | 40       |
| Közepesen gyors, kiszámíthatatlan   | 70       |
| Gyors, kiszámíthatatlan             | 100      |

<br/>

 
| **Célpont mérete** | **VÉ** |
| ------------------ | ------ |
| Óriás              | -30    |
| Ork                | -10    |
| Elfszabású / ember | +0     |
| Goblin             | +20    |
| macska             | +40    |
| egér               | +60    |

<br/>

---

### Harc magasabbról

```
TÉ: +10
```

Ha valaki magasabbról harcol, az előnyben van ellenfelével szemben. Ilyen helyzetben `+10 TÉ` módosító járul Támadó Értékéhez.

<br/>

---

### Harc gyűlöletből

```
TÉ: +15
```

Aki gyűlöletből harcol, az kevesebbet törődik a védekezéssel, minden erejével ellenfele elpusztítására tör. Az ilyen karakter kötelezően `+15 TÉ` Támadó taktikával harcol (így `-30 VÉ` sújtja).

Ebben az állapotban használhatja a **Kezdeményező Taktikát**, de semmilyen defenzív jellegű más taktikát nem (pl. Kiváró, stb).

<br/>

---

### Fegyverrántás

Kapcsolódik: **Fegyverrántás harci fortély** ⭕link⭕

Fegyverrántás szituáción azt értjük, amikor valaki harci kontaktus közben próbálja előkapni fegyverét, hogy ne pusztakezes értékeivel legyen kénytelen küzdeni. Ez igen nehéz feladat, hiszen ellenfele által folyamatosan fenyegetve van.

Fegyverrántásnál pusztakezes `KÉ`-vel történik a kezdeményezés, fegyver-függő módosítóval:

```
KÉ: [0 ;-10]    (Például Tőr: -0 KÉ, Kétkezes csatabárd: -10KÉ)
```

Tehát minél nehezebb előrántani egy fegyvert, annál nagyobb rá a büntetés. A levonás mértékét a KM határozza meg.

Ha a fegyverrántó nyeri a kezdeményezést, akkor sikerült előrántania fegyverét, és teljes – fegyveres – `VÉ`‑je érvényesül, viszont ellenfele dobhat támadást azonnal. A fegyverrántás tehát **1 db** támadást felemésztő cselekedet.

Ha a fegyverrántó elveszti a kezdeményezést, akkor fegyvertelen `VÉ`-jével várja ellenfele támadását.

Viszont ha a fegyverrántó **legalább** `10`-el túldobja ellenfele Kezdeményezését, akkor annyira gyors volt, hogy már ő támadhat elsőnek azonnal – teljes harcértékével. A harc innen a megszokott módon folytatódik. **Megjegyzés**: az ilyen támadást lehet kombinálni **Orvtámadással**, de csak akkor, ha az alkalmazó sikeres „**Első vágás**” manővert tett és ez az első támadása az adott harcban.

**Fegyverrántás** fortély bónuszai fegyverrántás szituációban (alkalmazó oldalán):

```
1.fok:  KÉ:+5
2.fok:  KÉ:+10 + támadásnál (10-el túldobott kezdeményezés esetén) „Első vágás” manőver alkalmazható.
```

#### Meglepetésből, vagy észrevétlen fegyverrántás

Beszélgetek valakivel, váratlanul fegyvert rántok és megszúrom
- A támadás az enyém
- Az áldozat **Észlelés** próbát dob. Ha nincs meg, akkor **Orvtámadásnak** minősül a támadásom.
- Ha megvan, akkor **Meglepetés** szituációvá enyhül a helyzet (`+20 TÉ` módosítót kapok).

#### Mindkét fél fegyverrántást alkalmaz

Ekkor mindkettőjükre érvényesek a fegyverrántásnál leírt módosítók. Az szúr előbb, aki nyeri a `KÉ`-t, ellenfele pedig `Pusztakezes VÉ`-vel védekezhet csak és képtelen előkapni fegyverét. Ha elő akarja húzni, akkor a következő kör elején, támadását feláldozva újra fegyverrántással kell próbálkoznia.

#### ⚡ Példák

```
KÉ alap: 26 → Puszta kezes KÉ: 16  (Mivel a Puszta kéz KÉ értéke: -10)
Tőrrel KÉ: 28 (Tőr KÉ:+2)
• Puszta kezes KÉ (16) számít
• Egy tőrt könnyű előrántani (0 KÉ büntetés). Így a KÉ: 16
    • 2.fokú fegyverrántás fortéllyal: 16+10=26 (ez már csak 2-vel marad el a tőrös KÉ-től)
• Ha kardot akarnék rántani, azt már nehezebb (-4 KÉ büntetés). Így fortély nélkül KÉ: 12
    • 2.fokú fegyverrántás fortéllyal: 12+10=22
• Kétkezes csatabárdot „rántani” szinte lehetetlen (-10KÉ). Így fortély nélkül KÉ: 6
    • 2.fokú fegyverrántás fortéllyal: pont kiegyenlíti a -10 KÉ büntetést. Így KÉ=16
```

**Szálfegyverek**, nagy kétkezes fegyverek esetén értelmetlen a fegyverrántás, hiszen vagy kézben vannak, vagy olyan módon tárolva, ahonnan lehetetlen fegyverrántással előhúzni.

<br/>

---

### Harc helyhez kötve

```
KÉ:-10, TÉ:-20, VÉ:-20
```

Ha a karakter helyhez kötve kénytelen harcolni, akkor `-10 KÉ, -20 TÉ és -20 VÉ` büntetés jár harcértékeire.

<br/>

---

### Beszorított helyzet

Beszorított helyzeten azt értjük, ha az adott fegyverrel a harcos helyhiány miatt nem képes annak technikáit maradéktalanul alkalmazni. Ez nagyon szűk helyeken egészen szélsőséges hátrányokat is okozhat fegyver-típustól függően.

Mivel nem lehet általános szabályt alkotni minden szituáció és fegyver-típus kapcsolatából, ezért csak irányelveket fektetünk le, a KM határozza meg az adott helyzet ismeretében, hogy épp milyen levonások járnak.

„**Rövid**” fegyverekre (max 0,5 pengehossz) nem jár levonás. Puszta kéz értékei nem módosulnak.

Szobában, bútorok közt:
- 2 kezes és szálfegyverek harcértéke `0`-ra zuhan
- egykezes fegyverek harcértéke **feleződik**

Szűk sikátorban:
- Fontos, hogy milyen irányból érkezik a támadás. Egy lándzsa technikáit például nem lehet itt alkalmazni, viszont a két oldalról való védettség folytán szinte lehetetlen hozzáférni. Ilyenkor a szúró szálfegyverek `+15 TÉ/VÉ` módosítót kapnak, viszont a hátulról érkező támadások ellen teljesen védtelen ilyenkor a harcos. Abba az irányba fegyverének harcértékei `0`-nak számítanak és még **további** `-15 TÉ/VÉ` csökkenést szenved el.

**Megjegyzés**: a **Támadó- és Védő** taktikák **Beszorított helyzetben** továbbra is használhatóak.

<br/>

---

### Harc földön fekve

```
KÉ: -10, TÉ: -10, VÉ: -10
```

<br/>

---

### Harc félhomályban

```diff
- TODO (PROB_HARC_#51)
```

<br/>

---

### Félelem harc közben
Ha valaki nem bírja a stresszt, vagy kezdő a harcban, vagy meg lett félemlítve (KM dönt), akkor automatikusan **Védekező taktikában** kezd harcolni, mégpedig a legerősebb (`VÉ:+15; TÉ:-30`) módon. Ha akarja, ha nem.

<br/>

---

### Lóról leesés

Ha leesel a lóról, **Esés** képzettség próbát kell dobnod, melynek nehézségét a KM határozza meg a körülmények ismeretében. Ha a próba...
- Sikertelen: ló sebességétől és talajtól függően: `[k6 - 4k6] ÉP` sebesülés
- Sikeres: ló sebességétől és talajtól függően: `[0 - k6] ÉP` sebesülés

<br/>

---

### A védekező takarásban

```diff
- TODO (PROB_HARC_#51)
```

<br/>

---

### Harc állatokkal

Sokféle állat van, ezért nem lehet egységes szabályt alkotni azok harcmodoráról, viszont kimondható, hogy az állatok nagy része általában olyan harcmodort folytat, ami a **Belharcnak** felel meg leginkább. Így harci „képzettségeik” és értékeik is e szerint legyenek meghatározva.

