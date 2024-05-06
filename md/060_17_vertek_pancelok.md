## Vértek, Páncélok

→ [TODO/ISSUE oldal](https://github.com/kaktusztea/km100/wiki/TODO.ISSUE.vertek.pancelok)

Még vannak nyitott problémák, azokat még ki kell vasalni.

---
Kapcsolódó harci fortély: **[Vértviselet](https://github.com/kaktusztea/km100/blob/master/md/fortelyok.harci/vertviselet.md)**

Egy páncélt három jellemző ír le: a Sebzésfelfogó Érték (**SFÉ**), a Mozgásgátló tényező (**MGT**) és az **Ár**. Ezeket az alábbi jellemzők befolyásolják:

- SFÉ
  - Struktúra (bőr, lánc, lemez, stb)
  - Anyagminőség (alapanyag minősége, hajtogatás, ötvözet minősége)
  - Fémalapanyag (fém vérteknél: milyen fémből készült)

- MGT
  - Struktúra (bőr, lánc, lemez, stb)
  - Fémalapanyag (fém vérteknél: milyen fémből készült)
  - Kidolgozottság (illesztések minősége)
  - Mennyire passzol a vértviselő testére
  - Csatolt elemek száma

- Ár
  - Struktúra (bőr, lánc, lemez, stb)
  - Anyagminőség (alapanyag, hajtogatás, ötvözet minősége)
  - Fémalapanyag (fém vérteknél: milyen fémből készült)
  - Kidolgozottság (illesztések)
  - Csatolt elemek száma

<br />

A fenti jellemzők fordított nézetőpontból:

- Struktúra (bőr, sodrony, stb) → SFÉ-re, Alap-MGT-re hat
- Fémalapanyag  (acél, abbit, mithrill) → SFÉ-re, Alap-MGT-re hat
- Kidolgozottság (illesztések minősége) → MGT-re hat
- Mennyire passzol a vértviselő testére → MGT-re hat
- Csatolt elemek száma → MGT-re és védett területre hat

<br />

---
### Sebzésfelfogó Érték (SFÉ)

Minden páncél rendelkezik **három** úgynevezett Sebzés Felfogó Értékkel (**SFÉ**), amely a páncél nyújtotta védelmet hivatott szimulálni (szúró/vágó/zúzófegyverek ellen). Az SFÉ értéke sebzéskor levonódik a támadás `SP` értékéből (nem a sebzésből!), így jó eséllyel csökkenti a sebzés kategóriáját.

Egy páncélnak **4 fajta SFÉ értéke van**, a támadás jellegétől függ, hogy melyiket kell figyelembe venni, a csapással szembeállítani:

- `Szúró`
- `Vágó`
- `Zúzó`
- `Energia`
  - Villám, Tűz, Fagy támadás tartozik ide.
 	- A fém vértek, ha felforrósódnak, folyamatos sebzést okozhatnak. Erről a KM dönt.
 	- Fém vértet **villámmal** könnyebb eltalálni, mivel az magához vonzza az ilyen energiát. Ilyenkor a támadó számára a Célzás számításánál az Osztó érték `1`-el nő.

Megkülönböztetünk

- páncél Struktúrát (szerkezeti felépítést határozza meg). Például: lánc, sodrony, lemez.
- Fémalapanyag típust. Például: acél, bronz, abbitacél, ...

Az SFÉ független attól, hogy csak egy mellvért-darab, vagy teljes páncélzat borítja testünket – amennyiben azonos anyagból készültek.

#### Páncél struktúrák, Anyagminőség

Az SFÉ értékét a páncél fizikai felépítése, anyaga adja. Az egyes páncél **Struktúrák** különbözőképpen alkalmasak a négy fő támadási típus (szúró/vágó/zúzó/energia) ellen való védekezésre. Sebzéskor a támadó karakter dobás után bemondja végleges SP értékét (példa: "`18, Szúró`”), és az áldozat annak megfelelő (`Szúró`) SFÉ értéket von le belőle.

Az egyes **fém-páncél** példányok struktúrális Anyagminősége erősen eltérhet (függ az alapanyag (ötvözet) összetételétől és a készítő mestertől anyagmegmunkálási ismereteitől is). Lenn a `+/-` oszlopnál jelezzük ennek az SFÉ "mozgástérnek" a kereteit. A jobb anyagminőség viszont nagyon megdobhatja a vért árát - lásd "Ár" oszlop.

| **Struktúra** | **Szúró SFÉ** | **Vágó SFÉ** | **Zúzó SFÉ** | Energia SFÉ | +/- | **Ár** |
| ------------- | :-----------: | :----------: | :----------: | :---------: | :-: | :----: |
| Posztó/Bunda  |      `1`      |     `2`      |     `2`      |     `4`     | `0` | `0.1x` |
| Fegyverkabát  |      `3`      |     `3`      |     `2`      |     `5`     | `0` |  `1x`  |
| Bőr           |      `6`      |     `8`      |     `5`      |    `10`     | `2` |  `1x`  |
| Brigantin     |     `10`      |     `12`     |     `7`      |    `14`     | `2` |  `3x`  |
| Lánc/Sodrony  |      `8`      |     `13`     |     `5`      |    `15`     | `3` | `10x`  |
| Pikkelypáncél |     `12`      |     `13`     |     `6`      |    `15`     | `3` | `50x`  |
| Lemezpáncél   |     `15`      |     `18`     |     `10`     |    `20`     | `4` | `100x` |

⭕TODO: fenti értékek hangolása

A fenti +/- oszlophoz tartozó Ár -szorzó:

| Anyagminőség +SFÉ |    Ár    |
| :---------------: | :------: |
|       `-4`        | `1/10 x` |
|       `-3`        | `1/7 x`  |
|       `-2`        | `1/4 x`  |
|       `-1`        | `1/2 x`  |
|       `+1`        |   `2x`   |
|       `+2`        |   `4x`   |
|       `+3`        |   `7x`   |
|       `+4`        |  `10x`   |

#### Fémalapanyag SFÉ, Ár-szorzó

A különböző fém ötvözetek alapanyagai változtathatnak az SFÉ értékeken és az Ár szorzón. Amihez viszonyítunk az alaphelyzetben az **acél**.

|           |    SFÉ    |    Ár szorzó     |
| --------- | :-------: | :--------------: |
| Acél      |   `+0`    |       `1x`       |
| Bronz     |   `-5`    |      `0,5x`      |
| Abbitacél |   `+5`    |      `10x`       |
| Mithrill  |   `+10`   |      `100x`      |
| Lunír     | ⭕`+10-20` | "a csillagos ég" |

<br />

---
### Mozgásgátló Tényező (MGT)

```
→ Σ MGT = Alap MGT + Csatolt MGT - (Erő x 2)

→ 1 MGT → -0,5 KÉ, -1 TÉ,VÉ
  → MGT értékét csökkenti a Vértviselet fortély (lásd ott)

→ 1 MGT → -1/5 mozgást igénylő képzettségpróbákra (lefele kerekítve)
  → MGT értékét NEM csökkenti a Vértviselet fortély!

→ Tulajdonságpróbákra alapból nem jár MGT-ből származó büntetés,
  de helyzet-függően a KM adhat
```

Harc és mozgás során a vértek, egyes pajzsok, valamint a felszerelés egyes elemei korlátozhatják a karaktereket. Ennek szimulálására van a Mozgásgátló Tényező – röviden **MGT**.

A fenti vérteknek, pajzsoknak és egyes fegyvereknek van MGT értéke. Alapesetben a páncél Struktúráknál leírt MGT alapértékekhez hozzáadjuk a Fémealapanyag (ha van), majd a Kidolgozottság-függő értékeket kapcsolt darabonként, beleértve a torzót védő mellvértet is.

A Képzettségpróbák és Tulajdonságpróbák esetében a fent leírtak az irányadóak, de helyzettől függően a KM dönthet úgy, hogy az MGT adjon büntetést bizonyos próbáknál, míg másoknál ne.

---
#### Alap (mellvért) MGT

Az alábbi alapértékeket csak akkor kell beleszámítani az MGT-be, ha a karakter visel mellvért-darabot.

| **Struktúra** | **Mellvért MGT alap** |
| :------------ | :-------------------: |
| Posztó        |          `3`          |
| Fegyverkabát  |          `3`          |
| Bőr           |          `8`          |
| Brigantin     |         `11`          |
| Lánc/Sodrony  |         `13`          |
| Pikkely       |         `17`          |
| Lemez         |         `18`          |

---
#### Fémalapanyag - MGT

A különböző fém ötvözetek alapanyagai változtathatnak az MGT értékeken. Amihez viszonyítunk az alaphelyzetben az acél.

|           | Alap MGT |
| --------- | :------: |
| Acél      |   `+0`   |
| Bronz     |  ⭕`+6`   |
| Abbitacél |  ⭕`-5`   |
| Mithrill  |  ⭕`-10`  |
| Lunír     |  ⭕`-15`  |

---
#### Erőbónusz MGT csökkentése

```
(Erő x 2) növeli/csökkenti az MGT értékét
```

Aki erősebb, azt kevésbé korlátozza egy nehezebb páncél.

---
#### Csatolt MGT (Vért kidolgozottsága, Csatolt elemek száma)

```
→ Kidolgozottság: a lenti táblázatból megállapított szám.
→ Csatolt MGT = kidolgozottság  x  csatolt elemek száma
  (mellvért darab is beszámít a darabszámba!)
```

| Kat  | Struktúra                  | Pocsék  | **Gyenge munka** | Átlagos | Jó munka | **Mestermunka** |
| ---- | -------------------------- | :-----: | :--------------: | :-----: | :------: | :-------------: |
| I.   | Nem merev, nem fém         |   `3`   |       `2`        |   `1`   |  `0,5`   |       `-`       |
| II.  | Nem merev, fém             |   `4`   |       `3`        |   `2`   |   `1`    |      `0,5`      |
| III. | Merev, fém                 |   `5`   |       `4`        |   `3`   |   `2`    |       `1`       |
|      |                            |         |                  |         |          |                 |
|      | Ár szorzó (kidolgozottság) | `x 0,1` |     `x 0,5`      |  `x 1`  |  `x 10`  |     `x 100`     |

A vért elemek kapcsolódásainak jó **Kidolgozottsága** alapvető fontosságú a gördülékeny mozgáshoz. Egy rossz illesztékekkel készített vértezet rettenetesen nehezíti a mozgást viselője számára, nem minden a nagy SFÉ. Kiváló alapanyagból is lehet hitványul megformált munkát készíteni, fontos tehát a jó készítő mester is.

Minden egyes csatolt tag darab után a táblázatból kinézett MGT érték adódik hozzá az MGT alaphoz, ezt a számértéket a **Kidolgozottság** elnevezéssel illetjük.

**Csatolható tagok** (6 db):
- mellvért
- felkar-tagok
- alkar-tagok
- comb-tagok
- lábszár-tagok
- sisak

Megjegyzések:

- Maga a Mellvért-darab is beleszámít az elemek számába! (így ha csak mellvért-darabot visel a karakter, a minőségi különbség akkor is megjelenik). Ha nincs mellvért-darab, akkor az Alap MGT-t **nem** kell beszámítani, csak a lenti kikeresett számot kell a kapcsolt tagok számával szorozni.
- A páros tagok pl, „felkar-tagok” a számolásban egynek számítanak, aki csak fél párat visel, az is ennyit „fizet” érte, ilyen szinten már felesleges bonyolítás lenne a túlzott differenciálás.

---
#### Erő követelmény MGT értékére

A vértek viselése embert próbáló feladat. Éppen ezért a vértek viselésének követelményeket állítottunk:

| Full MGT  | Erő követelmény |
| :-------: | :-------------: |
| `10`-`20` |      `+1`       |
| `21`-`30` |      `+2`       |
| `31`-`40` |      `+3`       |
| `41`-`50` |      `+4`       |

---
#### Rossz méretű vért viselése – MGT növekedés

```
Kidolgozottság érték módosítható, ha nem passszol a páncél
```

Néha előfordul, hogy a szükség ráviszi a hősöket is, hogy legyőzött ellenfeleik páncéljait tulajdonítsák el, ha épp megszorulnak.

Az ilyen vért azonban sokszor nem passzol új tulajdonosának testalkatához. Túl nagy, túl szűk, nem ott forog el, ahol kényelmes lenne.

Ilyen esetben a KM az adott karakter számára a vért **Kidolgozottság** értékét tetszés szerint leronthatja.

Példa: Endirell a barbár magára ölti imént elhalálozott ellenfele **Átlagos** Kidolgozottsgú acél lemez mellvértjét + a felkar és alkar tagokat is (össz: **3 tag**). Ennek ugye így `3`-as a **Kidolgozottsága** alapesetben (merev, fém vért; átlagos minőség).

Az új páncél viszont úgy áll hősünkön, mint tehénen a gatya. Testalkata ugyanis sajnos nem egyezik az elhunyt ellenségével. A KM szigorú: a páncél **Kidolgozottság** értéket Endirell számára `5`-re rontja le. Alapesetben az **MGT** ugye `27` lenne (`18 + 3x3`), de a büntetés után már `33`-ra ugrik (`18 + 3x5`).

---
#### Egydarabos tag (alkarvédő, lábszárvédő) viselése - MGT
```
Vértviselet fortély nem mérsékli MGT hatásukat!
```

Használd a [Csatolt MGT](#csatolt-mgt-v%C3%A9rt-kidolgozotts%C3%A1ga-csatolt-elemek-sz%C3%A1ma) táblázatot - egy ekkora kis tagnál nem érdemes anyagfüggő részletekbe belemenni.

Használatukról a „**Hárítófegyver használat**” fortély ad útmutatást.

---
#### Sérült vért javítása és MGT módosító hatása
```
Sérülés jellemző: vért sérülése %-ban.
```

Ha megsérül a vért, azt bizony javítani kell és ez bizony nem olcsó mulatság fém vértek esetén.

Az elszenvedett csapások alapján a KM meghatároz egy **az egész vértre** vonatkoztatott sérülés százalékot (**Sérülés jellemző**). A javítás a vért teljes árának annyi százaléka, amennyi a Sérülés értéke.

Ha megsérül a vért, az bizony előbb-utóbb akadályozni fog a mozgásban.

**Opcionális szabály**: az **MGT** az eredetihez képest annyi százalékkal nő, amennyi a vért Sérülés jellemzője.

<br />

---
### Páncél tagok és a védett terület

| **Páncél tag**                          | **Véd**  | **Tulajdonságok, védett helyek**        |
| --------------------------------------- | :------: | --------------------------------------- |
| Mellvért                                |  `50%`   | Csak a torzót védi elöl, hátul, oldalt. |
| + Sisak                                 |  `+10%`  | A fejet védi                            |
| Felkarok / alkarok / combok / lábszárak | `+10%`\* | Tagonként értendő a `+10%`.             |

<br />

---
### Páncéldobás

```
százalékdobás k10-zel
```

Az áldozat dobja `k10`-el ellenfele sebzésdobása után (közben). Tulajdonképpen egy egyszerűsített százalékdobás, hogy a csapás páncéllal fedett területet talált-e el. Minden páncél **X %**-ban védi a testet. **X**-et a fenti táblázatból lehet kiszámolni.

⚡Például: torzót, felkart és alkart védő páncél a test `70%`-át védi (`50+10+10`). Így `k10`-en az `1-7`-es dobás esetén véd a páncél, `8-10`-es esetén nem, mert a csapás fedetlen részt talált el.

<br />

---
### Vértviselet fortély

Ennek a fortélynak az ismerete csökkenti az MGT okozta levonások hatását.

```
1.fok: -15 MGT
2.fok: -30 MGT
3.fok: -35 MGT

- Mellvértnél : VÉ:+5
- Full vértnél: VÉ:+10
```

⭕Képzettségpróbáknál is csökkenjen a büntetés?⭕

<br />

---
### Páncél Ára
```
1x == minden tekintetből átlagos bőr mellvért ára
```

A páncél teljes árát a következőképpen kaphatjuk meg:

```
- Teljes ár = (Mellvért ár) + (Csatolt tagok ára)
- Mellvért ár = (mellvért alapára x Anyagminőség-szorzó x Fémalapanyag-szorzó x Kidolgozottság-szorzó)
- Csatolt tagok ára = 1/5 x (Mellvért ár) x (Csatolt tagok db)
```

- a mellvért-darab árát az **SFÉ** táblázatban találjuk (szorzó) és az Anyagminőségtől is függ.
- a **Kidolgozottság** szorzót a [Vértek kidolgozottsága](#v%C3%A9rt-kidolgozotts%C3%A1ga-csatolt-elemek-sz%C3%A1ma)  táblázat tartalmazza. Érthető módon ha jobb a kidolgozottság, drágább a páncél.
- Ha fém vértről beszélünk és a vért nem hagyományosan acélból készült, akkor a [Fém vértek alapanyagai](#f%C3%A9m-v%C3%A9rtek-alapanyaga---sf%C3%A9) táblázatban található **Fémanyag-szorzó** értéket is be kell vonni (az Acél szorzója: `1`).\
  Például **abbitacél** esetén az értéket `10`-zel kell szorozni.

#### Csatolt tagok ára
```
Csatolt tagok ára = 1/5 x (Mellvért ár) x (Csatolt tagok db)
```

A plusz csatolt tagok egyenként a mellvért-darab `1/5`-ét érik, azaz egy teljes vért a mellvért-darab árának pont a kétszerese.

🔆A "Csatolt tagok db"-ba itt nem számít bele a Mellvért-darab!

#### Miért szorzó érték az „Ár”?

Az SFÉ táblázatban nem véletlenül _szorzó_ értékek szerepelnek arany, vagy más fizetőeszköz helyett. Ennek oka az, hogy tájegységtől függően más-más a vértek ára. Itt csak az egyes típusok közötti ár-arányt adtuk meg. Természetesen ebbe is bele lehet kötni, hogy pl. egy adott országban nem pont ezek az arányok, de ennyire részletes bontásba véleményünk szerint értelmetlen belemenni – felesleges bonyolítás lenne.

<br />

---
### Példa egy páncél leírására

**JK**: „Milyen a páncélja?”

**KM**: „Ez egy Sodrony páncél. Fémalapanyaga acél, Anyagminősége (`-1`)-es (SFÉ-re), Kidolgozottsága Gyenge. Három tagot látsz: mellvért-darabot, felkar-tagot, alkar-tagot. Méretben passzol rád, nem kapsz extra büntetést.”

---
### ⚡Példa 1: Átlagos páncél

A lehető legátlagosabb sodronying, sisakon kívül mindent beborítva.
#### SFÉ
- Struktúra: Sodronying
- Alap SFÉ: `8` / `13` / `5` / `15`
- Anyagminőség átlagos: `+0 SFÉ`
- Fémalapanyag: Acél: `+0 SFÉ`
- **Végső SFÉ**: `8` / `13` / `5` / `15 SFÉ`

#### MGT

- Struktúra: Sodronying
- Kidolgozottság gyenge (nem az alapanyag, az elkészítés gyenge!)
- Alap MGT: `13` (Lánc/Sodrony)
- Kidolgozottság: Nem merev, fém (II.kat) / Gyenge munka → `+3` MGT / tag
- Védett terület: mellkas, felkar, alkarok, combok → `4` db tag
- Karakter Erő tulajdonsága legyen: `+2` → (`2 x 2 = 4` MGT csökkentés)

Összesen tehát: `13  +  (4 x 3)  -  (2 x 2) = 21 MGT`

#### Ár

- Alap:
	- Struktúra: Sodrony: `10x`
	- Anyagminőség átlagos: `1x`
	- Kidolgozottság „gyenge”: `0,5x`
- Mellvért ár : `10x x 1x x 0,5  =  5x`
- Így 1db tag ára: `5x / 5) = 1x`
- Végleges ár: `5x + (3 x 1x) = 8x`, azaz egy átlagos bőr mellvért darab nyolcszorosába kerül a fenti teljes páncél-kombó (csak `3` taggal szoroztunk, mert a mellvért-darabot már beleszámoltuk).

---
### ⚡Példa 2: Legvacakabb teljes lemezvért

... amiben a lehető legnehezebb mozogni (Kidolgozottság: pocsék, Fémalapanyaga: bronz) és még az Anyagminősége is a legvacakabb. Mindent lefed.
#### SFÉ

- Struktúra: Lemezpáncél
- Alap SFÉ: `15 / 18 / 10` / `20`
- Anyagminőség leggyengébb: `SFÉ:-2`
- Fémalapanyag: Bronz: `SFÉ:-3`
- **Végső SFÉ**:  `10 / 13 / 5` / `15`

#### MGT

- Alap MGT:
	- Struktúra: Lemez: `18`
	- Fémalapanyag: Bronz: `6`
- Kidolgozottság: Merev, fém (III.kat) / Pocsék munka → `+5` MGT / tag
- Védett terület: mellkas, felkar, alkarok, combok, lábszárak, fej → `6` db tag
- Karakter **Erő** tulajdonsága legyen: `+1` → (`2 x 1 = 2` MGT csökkentés)

Összesen tehát: `(18 + 6)  +  (6 x 5)  –  (2 x 1) = 52 MGT`

#### Ár

- Alap:
	- Struktúra: Lemez:`100x`
	- Anyagminőség vacak: `0,1x`
	- Kidolgozottság pocsék munka: `0,1x`
	- Fémalapanyag: Bronz: `0,5x`
- Mellvért ár: `100x x 0,1 x 0,1 x 0,5  =  0,5x`
- Így 1 db tag ára: `0,5x / 5 = 0,1x`
- Végleges ár: `0,5x + (0,1 x 5) = 1x`, azaz pontosan egy átlagos bőr mellvért árának megfelelő pénzbe kerül a fenti **teljes** gyatra páncél-kombó (csak 5 taggal szoroztunk mert a mellvért-darabot már beleszámoltuk).
