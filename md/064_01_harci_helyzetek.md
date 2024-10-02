## Harci helyzetek

Fontos: A "Meglepetés", "Támadás hátulról", "Észrevétlen támadás" egymást kizáró, "vagy-vagy" harci helyzetek, nem vonhatóak össze.

|                 Szituáció                 |                                Módosító                                | Megjegyzés                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :---------------------------------------: | :--------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                Meglepetés                 |                                `TÉ:+20`                                | A támadó kapja a módosítót.<br/>Pajzs VÉ csak akkor számít, ha a csapás nem hátulról jön.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|             Támadás hátulról              |                                `TÉ:+20`                                | A támadó kapja a módosítót.<br/>Pajzs VÉ nem számít.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|            Támadás félhátulról            |                                `TÉ:+10`                                | Pajzs VÉ csak akkor számít, ha a pajzsot tartó kéz felőli oldalról jön a csapás.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|              Készületlenség               |                           Lásd a Meglepetést                           | Ha egy karakter készületlen, akkor támadója a Meglepetés szituációnak megfelelő módosítókkal támadhat rá.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|     Kábult/bódult/megrendült állapot      |                        ⭕`KÉ:-10, TÉ:-20, SP:-2`                        | Kábulat, rosszullét, mérgezés esetén ideiglenesen ezek a levonások járnak. A KM – belátása szerint – adhat KT „sebesülést” is<br/>(pl. mérgezésnél)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|            Észrevétlen támadás            |            Áldozat Védő Értéke: mozgás jellegétől függő VÉ             | **Célpont mozgásának jellege, VÉ**<br/>• Álló helyzet / lassan sétáló hátulról: `0 VÉ`<br/>• Lassú egyenletes (séta): `20 VÉ`<br/>• Egyenletes kocogás: `40 VÉ`<br/>• Sprint egyenes vonalon: `60 VÉ`<br/>• Lassú kiszámíthatatlan: `40 VÉ`<br/>• Közepesen gyors, kiszámíthatatlan: `70 VÉ`<br/>• Gyors, kiszámíthatatlan: `100 VÉ`<br/><br/>Követelménye:<br/>• Sikeres „**Lopakodás/rejtőzés**” vs  „**Észlelés**” ellenpróba<br/>• Az Észrevétlen támadás több harci taktika követelménye (pl. Orvtámadás)                                                                                                                                   |
|            Belharci szituáció             |                            Lásd a leírást!                             | • Bekerülni: [Belharcba kerülés](065_03_altalanos_manoverek.md#belharcba-ker%C3%BCl%C3%A9s) manőverrel<br/>• Kijönni: [Belharcból kibontakozás](065_03_altalanos_manoverek.md#belharcb%C3%B3l-kibontakoz%C3%A1s) manőverrel<br/>• Mindenki a saját Harcmodorának módosítóival küzd<br/>• [Belharc fortély](fortelyok.harci/belharc.md) bónuszai: `KÉ:+2`, `TÉ/VÉ:+3` fokonként. Csak **Közelharc** harcmodorban jár.<br/>• A `rövid (0)` pengénél nagyobb fegyverek értékei: `0`-ra esnek, sebzésük max: `+1 SP`,  „**Harckeret**” csökken `5`-el. **Erőbónusz** és **MF** fortély bónuszai maradnak.<br/>• Puszta kéz értékei `0`-ra emelkednek |
|        Képzetlen fegyverhasználat         |                `KÉ:-20, TÉ:-30` <br/>`VÉ:-30, CÉ: -30`                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|            Harc puszta kézzel             |                        `KÉ:-10, TÉ:-10, VÉ:-10`                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|              Érintő támadás               |                          `KÉ:0, TÉ:0, VÉ:-10`                          | Érinteni könnyebb, mint megütni, sebezni puszta kézzel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Harc rosszabbik kézben tartott fegyverrel |                        `KÉ:-10, TÉ:-20, VÉ:-20`                        | Kivétel:<br/><br/>• **Kétkezesség** fortély. Csak annyit ad, hogy rosszabbik kézzel is levonás nélkül tudsz harcolni, de csak 1 fegyverrel!!<br/><br/>• **Kétkezes Harc** fortély                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|             Harc magasabbról              |                                `TÉ:+10`                                | A támadó kapja a módosítót.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|             Harc gyűlöletből              |                            `TÉ:+15; VÉ:-30`                            | Aki gyűlöletből harcol, az kevesebbet törődik a védekezéssel, minden erejével ellenfele elpusztítására tör. Az ilyen karakter kötelezően maximális, `TÉ:+15` [Támadó taktikával](064_02_harci_taktikak.md#támadó-taktika) harcol (így `VÉ:-30` sújtja).                                                                                                                                                                                                                                                                                                                                                                                          |
|               Fegyverrántás               | Puszta kezes KÉ  <br/>fegyver-függő levonással:<br/><br/>`[0 ;-10] KÉ` | `10`-el túldobott `KÉ` esetén a fegyverrántó támadhat elsőnek azonnal – teljes harcértékével.<br/><br/>Fegyverrántás fortély bónusza:<br/>`1. fok: +5 KÉ`<br/>`2. fok: +10 KÉ`                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|            Harc helyhez kötve             |                        `KÉ:-10, TÉ:-20, VÉ:-20`                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|             Harc földön fekve             |                        `KÉ:-10, TÉ:-10, VÉ:-10`                        | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|            Beszorított helyzet            |              Lásd a [leírást](#beszor%C3%ADtott-helyzet)!              | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|             Harc félhomályban             |                                 ⭕TODO⭕                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|            Félelem harc közben            |                            `VÉ:+20; TÉ:-40`                            | Aki erős félelem alatt harcol, az kevesebbet törődik a támadással, minden erejével védekezni próbál. Az ilyen karakter kötelezően maximális, `VÉ:+20` [Támadó taktikával](064_02_harci_taktikak.md#védő-taktika) harcol (így `TÉ:-40` sújtja).                                                                                                                                                                                                                                                                                                                                                                                                   |
|               Lóról leesés                |                            ⭕Ezt ne ide!!!⭕                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|           A védekező takarásban           |                                 ⭕TODO⭕                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|              Harc állatokkal              |                            Lásd a leírást!                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |


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

### Kábult / Bódult / Megrendült

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
### Belharc, Belharci szituáció

```diff
- PROB_HARC_#46
```

Ha a képzett harcosnak sikerül ellenfele fegyvere „mögé”, testközelébe kerülni, akkor ebből előnyt kovácsolhat.

#### Belharci szituáció

Bejutottál ellenfeled fegyverének fenyegető vége mögé, testközelbe, de nem szükségszerűen érintésbe. Ha az általad épp forgatott fegyverre van tanult [Belharc fortélyod](fortelyok.harci/belharc.md), harcérték bónuszokat kapsz (lásd a fortély leírását). Belharci szituációban eddig tiltott manőverek végrehajtását is megpróbálhatod, melyek végbevitelének követelménye a Belharci szituáció: úgy is mint Átdobás, Feszítés/kijövetel, Kéztörés, Lábtörés, Nyaktörés.

```diff
- Átnézni ezeket a fortélyokat. Belharc fortély is kell hozzájuk?
```

Továbbá pár manőver könnyebbé válik Belharci szituációban: [Gáncsolás/lábsöprés](065_04_belharcos_manoverek.md#g%C3%A1ncsol%C3%A1s--l%C3%A1bs%C3%B6pr%C3%A9s-l%C3%A1bbal) (belharcban `+2` Ellenpróbánál)

#### Belharcba kerülés manőver

A Belharci szituációba kerüléshez ezt a (fejleszthető) manővert kell sikerrel végrehajtani. Csak Közelharc harcmodor alkalmazása közben lehet megpróbálni.

Bővebben lásd a [manőver leírását](065_03_altalanos_manoverek.md#belharcba-ker%C3%BCl%C3%A9s).

#### Kibontakozás/Átsiklás manőver

A **Belharci szituációból** kijövetelre ennek sikeres végrehajtására van szükség.
Nehézsége alapesetben `5`-ös. Persze csak akkor kell a próba, ha valamelyik fél benn akarja tartani a másikat.

- Ha az ellenfélnek Belharc fortélya van, akkor fokonként `+2`-vel nő a nehézség Ellenpróbánál
- Ha az alkalmazónak Belharc fortélya van, akkor dobására fokonként `+2` pontot kap Ellenpróbánál
- Ha belharci szituációban a belharcos sebesülést szenved és elrontja fájdalomtűrés próbáját
```diff
- (már nincs **Fájdalomtűrés dobás** sebesüléskor,... de itt esetleg dobhatunk...)
```
... akkor ellenfele – ha akarja – automatikusan megszüntetheti a belharci szituációt, kibontakozhat belőle.

```diff
- Sérülést bevállalva **mindenképpen** kijönni hogy lehessen?
```

#### Belharcos-fegyverek

Minden `rövid (0)` pengehosszú fegyver, kivéve ezek közül azokat a fegyvereket, melyek leírásánál külön meg van említve, hogy nem lehet velük belharcot folytatni (pl. rövidkard, csatabárd, …)

#### Belharc fortély
Legfeljebb `2.fokon` tanulható fortély, amelyet **egy konkrét, választott belharcos-fegyverre** lehet felvenni. Így többször is felvehető más-más fegyverekre. Belharci szituációban az adott fegyvert forgatva fokonként `KÉ:+2`, `TÉ/VÉ:+3` bónuszt ad. A bónuszok csak akkor élnek, ha az alkalmazó Belharci szituációban **Közelharc** harcmodort alkalmaz. Bővebben lásd a [Belharc fortély](fortelyok.harci/belharc.md) leírásánál.

#### Általános szabályok belharci szituációra

- Belharci szituációban a nem-belharcos fegyverek harcértékei `0`-ra zuhannak, sebzésük `+1 SP`, ⭕(ha alacsonyabb volt, akkor `-5 SP`)⭕, a forgató **Harckeret** értéke `5`-el csökken, továbbá **Hátrányos szituációba** kerül, a belharcos pedig **Előnyösbe**. A **Mesterfegyver** és az **Erőbónusz** értékei mindkét félnél megmaradnak.
- A Puszta kéz értékei `0`-ra emelkednek.
- Belharcban az áldozat abban a harcmodorban harcol, amiben előtte is. (De a **Belharc** fortély bónuszaihoz követelmény a **Közelharc** használata). Például egy szablyás harcoshoz bekerül egy belharcos, akkor ő továbbra is kardvívás harcmodorának értékeivel küzd, igaz szablyájának harcértékeit elveszíti annak mérete miatt.
- A Belharc 1:1 elleni szituációban használható leghatékonyabban, külső, harmadik fél ellen viszont kiszolgáltatottabb.

```diff
- TODO: Ez még vitatható, mert Attila szerint olyan, mint harcolók közé lőni.
```

Amennyiben a belharcban levő harcost egy harmadik (vele nem belharcban levő) fél támadja, akkor a belharcos a **Harc helyhez kötve** szituáció VÉ büntetéseit szenvedi el, visszatámadni pedig nem tud, hiszen össze van akaszkodva másik ellenfelével. Kivétel: Sikeres **Leszorítás** (manőver) alkalmazása után, a leszorított áldozatot beforgathatja maga és a támadó közé, kvázi patthelyzetet okozva.


⭕**TODO: Átnézendő:**

```diff
- Manőverek, amik megkövetelik a belharci szitut (és amiket ezzel kapcsolatban át kell nézni): Átdobás, Feszítés/kijövetel, Kéztörés, Lábtörés, Nyaktörés
-	    Ezek natív végrehajtásához követelmény a Belharci szituáció.
```


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
TÉ: +15, VÉ: -30
```

Aki gyűlöletből harcol, az kevesebbet törődik a védekezéssel, minden erejével ellenfele elpusztítására tör. Az ilyen karakter kötelezően `+15 TÉ` Támadó taktikával harcol (így `-30 VÉ` sújtja).

Ebben az állapotban használhatja a **Kezdeményező Taktikát**, de semmilyen defenzív jellegű más taktikát nem (pl. Kiváró, stb).

<br/>

---

### Fegyverrántás

Kapcsolódik: [Fegyverrántás](fortelyok.harci/fegyverrantas.md) harci fortély

Fegyverrántás szituáción azt értjük, amikor valaki harci kontaktus közben próbálja előkapni fegyverét, hogy ne pusztakezes értékeivel legyen kénytelen küzdeni. Ez igen nehéz feladat, hiszen ellenfele által folyamatosan fenyegetve van.

Fegyverrántásnál pusztakezes `KÉ`-vel történik a kezdeményezés, fegyver-függő módosítóval:

```
KÉ: [0 ;-10]    (Például Tőr: -0 KÉ, Kétkezes csatabárd: -10KÉ)
```

Tehát minél nehezebb előrántani egy fegyvert, annál nagyobb rá a büntetés. A levonás mértékét a KM határozza meg.

Ha a fegyverrántó nyeri a kezdeményezést, akkor sikerült előrántania fegyverét, és teljes – fegyveres – `VÉ`‑je érvényesül, viszont ellenfele dobhat támadást azonnal. A fegyverrántás tehát **1 db** támadást felemésztő cselekedet.

Ha a fegyverrántó elveszti a kezdeményezést, akkor fegyvertelen `VÉ`-jével várja ellenfele támadását.

Viszont ha a fegyverrántó **legalább** `10`-el túldobja ellenfele Kezdeményezését, akkor annyira gyors volt, hogy már ő támadhat elsőnek azonnal – teljes harcértékével. A harc innen a megszokott módon folytatódik. **Megjegyzés**: az ilyen támadás lehet természetesen [Manőver](065_00_manoverek.md) is.

**Fegyverrántás** fortély bónuszai fegyverrántás szituációban (alkalmazó oldalán):

```
1.fok:  KÉ:+5
2.fok:  KÉ:+10
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

Ha leesel a lóról, [Akrobatika](kepzettsegek/akrobatika.md) képzettség próbát (esésre) kell dobnod, melynek nehézségét a KM határozza meg a körülmények ismeretében. Ha a próba...
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

