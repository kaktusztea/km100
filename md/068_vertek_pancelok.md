## Vértek, Páncélok

→ [TODO/ISSUE oldal](https://github.com/kaktusztea/km100/wiki/TODO.ISSUE.vertek.pancelok)

Még vannak nyitott problémák, azokat még ki kell vasalni.

---
Kapcsolódó harci fortély: **[Vértviselet](https://github.com/kaktusztea/km100/blob/master/md/fortelyok.harci/vertviselet.md)**

Egy páncélt három jellemző ír le: a Sebzésfelfogó Érték (**SFÉ**), a Mozgásgátló tényező (**MGT**) és az **Ár**. Ezeket az alábbi jellemzők befolyásolják:

- SFÉ
  - választott struktúra (bőr, sodrony, stb)
  - anyagminőség
  - alapanyag típus (fém vérteknél: milyen fémből készült)

- MGT
  - választott struktúra (bőr, sodrony, stb)
  - alapanyag típus (fém vérteknél: milyen fémből készült)
  - vért kidolgozottsága (illesztések)
  - mennyire passzol a vértviselő testére
  - csatolt elemek száma

- Ár
  - választott struktúra (bőr, sodrony, stb)
  - anyagminőség
  - alapanyag típus (fém vérteknél: milyen fémből készült)
  - vért kidolgozottsága (illesztések)

<br />

A fenti jellemzők fordított nézetőpontból:

- választott struktúra (bőr, sodrony, stb) → SFÉ-re, Alap-MGT-re hat
- alapanyag (fém vérteknél: milyen fémből készült) → SFÉ-re hat
- alapanyag típus (acél, abbit, mithrill) → SFÉ-re, Alap-MGT-re hat
- kidolgozottság (illesztések minősége) → MGT-re hat
- mennyire passzol a vértviselő testére → MGT-re hat
- csatolt elemek száma → MGT-re és védett területre hat

<br />

---
### Sebzésfelfogó Érték (SFÉ)

Minden páncél rendelkezik **három** úgynevezett Sebzés Felfogó Értékkel (**SFÉ**), amely a páncél nyújtotta védelmet hivatott szimulálni (szúró/vágó/zúzófegyverek ellen). Az SFÉ értéke sebzéskor levonódik a támadás `SP` értékéből (nem a sebzésből!), így jó eséllyel csökkenti a sebzés kategóriáját. Természetesen a támadás jellege (`Szúró`/`Vágó`/`Zúzó`) határozza meg, hogy mely SFÉ értéket kell a csapással szembeállítani.

Megkülönböztetünk

- páncél struktúrát (szerkezeti felépítést határozza meg). Például: lánc, sodrony, lemez.
- alapanyag típust. Például: acél, bronz, abbitacél, ...

Az SFÉ független attól, hogy csak egy mellvért-darab, vagy teljes páncélzat borítja testünket – amennyiben azonos anyagból készültek.

#### Páncél struktúrák, alapanyag minősége

Az SFÉ értékét a páncél fizikai felépítése, anyaga adja. Az egyes páncél struktúrák különbözőképpen alkalmasak a három fő támadási típus (szúró/vágó/zúzó) ellen való védekezésre. Sebzéskor a támadó karakter dobás után bemondja végleges SP értékét (példa: „18, Szúró”), és az áldozat annak megfelelő (szúró) SFÉ értéket von le belőle.

Az egyes **fém-páncél** példányok struktúrális minősége erősen eltérhet (függ az anyagtól és a készítő mestertől is). Lenn SFÉ határokkal jelezzük ezt a jelenséget. Például "Szúró 10-12-14" azt jelenti, hogy 10-14-es intervallumon belül lehet az ilyen anyagú vért, az átlagos struktúrális-minőség a 12-es.\
A jobb minőség nagyon megdobhatja a vért árát.

| **Páncél struktúra** | **Szúró SFÉ** | **Vágó SFÉ** | **Zúzó SFÉ** | +/- |      **Ár**       |
| -------------------- | :-----------: | :----------: | :----------: | :-: | :---------------: |
| Posztó/Bunda         |       1       |      2       |      2       |  0  |        ⭕?%        |
| Fegyverkabát         |       3       |      3       |      2       |  0  |        ⭕?%        |
| Bőr                  |       6       |      8       |      5       |  2  |        ⭕?%        |
| Brigantin            |      10       |      12      |      7       |  2  |        ⭕?%        |
| Lánc/Sodrony         |       8       |      13      |      5       |  2  |  ?% - 60% - ⭕?%   |
| Pikkelypáncél        |      12       |      13      |      6       |  2  |  ⭕?% - ?% - ⭕?%   |
| Lemezpáncél          |      15       |      18      |      10      |  2  | 70% - 160% - 250% |
⭕TODO: fenti értékek hangolása

---
#### Fém vértek alapanyaga - SFÉ

A különböző fém ötvözetek alapanyagai változtathatnak az SFÉ értékeken. Amihez viszonyítunk az alaphelyzetben az az acél.

|           |   SFÉ    | Ár (anyag-szorzó) |
| --------- |:--------:|:-----------------:|
| Acél      |    +0    |        1x         |
| Bronz     |    -5    |       0,5x        |
| Abbitacél |    +5    |        10x        |
| Mithrill  |   +10    |       100x        |
| Lunír     | ⭕+10-20 | "a csillagos ég"  |

<br />

---
### Mozgásgátló Tényező (MGT)

```
→ 1 MGT → -0,5 KÉ, -1 TÉ,VÉ
→ 1 MGT → -1/5 mozgást igénylő képzettségpróbákra (lefele kerekítve)
```

Harc és mozgás során a vértek, egyes pajzsok, valamint a felszerelés egyes elemei korlátozhatják a karaktereket. Ennek szimulálására van a Mozgásgátló Tényező – röviden **MGT**. A fenti vérteknek, pajzsoknak és egyes fegyvereknek van MGT értéke. Alapesetben a páncél struktúráknál leírt MGT alapértékekhez hozzáadjuk a kategória- és minőségfüggő értékeket kapcsolt darabonként, beleértve a torzót védő mellvértet is.

KM dönt, de például kézügyességet érintő Ügyességpróbára nyilván nem jár levonás, ha nincs páncélkesztyűben a játékos.

---
#### Alap (mellvért) MGT

Az alábbi alapértékeket akkor kell beleszámítani az MGT-be, ha a karakter visel mellvért-darabot.

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
#### Fém vértek alapanyagai - MGT

A különböző fém ötvözetek alapanyagai változtathatnak az MGT értékeken. Amihez viszonyítunk az alaphelyzetben az az acél.

|           | Alap MGT |
| --------- | :------: |
| Acél      |   `+0`   |
| Bronz     |  ⭕`+6`   |
| Abbitacél |   ⭕-?    |
| Mithrill  |   ⭕-?    |
| Lunír     |   ⭕-?    |

---
#### Erőbónusz MGT csökkentése

```
(Erő x 2) növeli/csökkenti az MGT értékét.
```

Aki erősebb, azt kevésbé korlátozza egy nehezebb páncél.

---
#### Vért kidolgozottsága, csatolt elemek száma

```
→ Kidolgozottság: a lenti táblázatból megállapított szám.
→ Σ Plusz MGT = (kidolgozottság x csatolt elemek száma (mellvért darab is beszámít!))
```

| Kat  | Struktúra                  | Pocsék  | **Gyenge munka** | Átlagos | Jó munka | **Mestermunka** |
| ---- | -------------------------- | :-----: | :--------------: | :-----: | :------: | :-------------: |
| I.   | Nem merev, nem fém         |   `3`   |       `2`        |   `1`   |  `0,5`   |       `-`       |
| II.  | Nem merev, fém             |   `4`   |       `3`        |   `2`   |   `1`    |      `0,5`      |
| III. | Merev, fém                 |   `5`   |       `4`        |   `3`   |   `2`    |       `1`       |
|      |                            |         |                  |         |          |                 |
|      | Ár szorzó (kidolgozottság) | `x 0,1` |     `x 0,5`      |    -    |  `x 10`  |     `x 100`     |

A vért elemek kapcsolódásainak jó kidolgozottsága alapvető fontosságú a gördülékeny mozgáshoz. Egy rossz illesztékekkel készített vértezet rettenetesen nehezíti a mozgást viselője számára, nem minden a nagy SFÉ. Kiváló alapanyagból is lehet hitványul megformált munkát készíteni, fontos tehát a jó készítő mester is.

Minden csatolt tag után a táblázatból kinézett MGT érték adódik hozzá az MGT alaphoz, ezt a számértéket a **Kidolgozottság** elnevezéssel illetjük.

**Csatolható tagok** (6 db):
- mellvért
- felkar-tagok
- alkar-tagok
- comb-tagok
- lábszár-tagok
- sisak

Megjegyzések:

- maga a Mellvért-darab is beleszámít az elemek számába!** (így ha csak mellvért-darabot visel a karakter, a minőségi különbség akkor is megjelenik). Ha nincs mellvért-darab, akkor az Alap MGT-t **nem** kell beszámítani, csak a lenti kikeresett számot kell a kapcsolt tagok számával szorozni.
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

Példa: Endirell a barbár magára ölti imént elhalálozott ellenfele **Átlagos** megmunkáltságú acél lemez mellvértjét + a felkar és alkar tagokat is (össz: **3 tag**). Ennek ugye így `3`-as a **Kidolgozottsága** alapesetben (merev, fém vért; átlagos minőség).

Az új páncél viszont úgy áll hősünkön, mint tehénen a gatya. Testalkata ugyanis sajnos nem egyezik az elhunyt ellenségével. A KM szigorú: a páncél **Kidolgozottság** értéket Endirell számára `5`-re rontja le. Alapesetben az **MGT** ugye `27` lenne (`18 + 3x3`), de a büntetés után már `33`-ra ugrik (`18 + 3x5`).

---
#### Egydarabos tag (alkarvédő, lábszárvédő) viselése - MGT

⭕TODO: külön értékük legyen (anyagfüggő!!), vagy használjuk erre is a táblázatot simán?⭕

**Vértviselet fortély nem mérsékli MGT hatásukat!**

Használatukról a „**Hárítófegyver használat**” fortély ad útmutatást.

---
#### Sérült vért javítása és MGT módosító hatása
```
Sérülés jellemző: vért sérülése %-ban.
```

Ha megsérül a vért, azt bizony javítani kell és ez bizony nem olcsó mulatság fém vértek esetén.

Az elszenvedett csapások alapján a KM meghatároz egy **az egész vértre** vonatkoztatott sérülés százalékot (**Sérülés jellemző**). A javítás a vért teljes árának annyi százaléka, amennyi a Sérülés értéke.

Ha megsérül a vért, az bizony előbb-utóbb akadályozni fog a mozgásban.

⭕**Opcionális szabály**: az **MGT** az eredetihez képest annyi százalékkal nő, amennyi a vért Sérülés jellemzője.⭕

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

⭕A Tulajdonság- és Képzettségpróbáknál is csökkenjen a büntetés?⭕

<br />

---
### Páncél Ára

A páncél teljes árát a következőképpen kaphatjuk meg:

```
Teljes ár = (Mellvért ár) + (Csatolt tagok ára)
Mellvért ár = (mellvért alapára  x  kidolgozottság-szorzó  x  anyag-szorzó)
```

- a mellvért-darab árát az **SFÉ** táblázatban találjuk (%), anyagminőségtől is függ.
- a **Kidolgozottság** szorzót a [Vértek kidolgozottsága](#v%C3%A9rt-kidolgozotts%C3%A1ga-csatolt-elemek-sz%C3%A1ma)  táblázat tartalmazza. Érthető módon ha jobb a kidolgozottság, drágább a páncél.
- Ha fém vértről beszélünk és a vért nem hagyományosan acélból készült, akkor a [Fém vértek alapanyagai](#f%C3%A9m-v%C3%A9rtek-alapanyaga---sf%C3%A9) táblázatban található **anyag-szorzó** értéket is be kell vonni. (az Acél szorzója: `1`) Pl. abbitacél esetén az értéket `10`-zel kell szorozni.

#### Csatolt tagok ára
```
Csatolt tagok ára = 1/5 x (Mellvért ár) x (Csatolt tagok db)
```

A plusz csatolt tagok egyenként a mellvért-darab `1/5`-ét érik, azaz egy teljes vért a mellvért-darab árának pont a kétszerese.

🔆A "Csatolt tagok db"-ba itt nem számít bele a Mellvért-darab!

#### Miért százalék érték az „Ár”?

Az SFÉ táblázatban nem véletlenül _százalék_ értékek szerepelnek arany, vagy más fizetőeszköz helyett. Ennek oka az, hogy tájegységtől függően más-más a vértek ára. Itt csak az egyes típusok közötti ár-arányt adtuk meg. Természetesen ebbe is bele lehet kötni, hogy pl. egy adott országban nem pont ezek az arányok, de ennyire részletes bontásba véleményünk szerint értelmetlen belemenni – felesleges bonyolítás lenne.

<br />

---
### Példa egy páncél leírására

**JK**: „Milyen a páncélja?”

**KM**: „Ez egy Sodrony páncél. Anyaga acél, anyagminősége (`-1`)-es (SFÉ-re), kidolgozottsága Gyenge. Három tagot látsz: mellvért-darabot, felkar-tagot, alkar-tagot. Méretben passzol rád, nem kapsz extra büntetést.”

---
### Példa átlagos páncélra

#### MGT

- Sodronying, gyenge kidolgozottságú (nem az alapanyag, az elkészítés gyenge!)
- Védett terület: mellkas, felkar, alkarok, combok (összesen: `4` tag).
- Alap MGT: `15` (Sodrony)
- Nem merev, fém (II.kat) / Gyenge munka → `+3` MGT / tag (Kidolgozottság)
- Karakter Erő tulajdonsága legyen: `+2` → (`2 x 2 = 4` jön le)

Összesen tehát: `15 + (4 x 3) - (2 x 2) = 23 MGT`

#### SFÉ

- Alapanyag minősége átlagos (nincs SFÉ módosulás)
- Acélból van: (nincs SFÉ módosulás)
- Alap SFÉ: `12` / `9` / `4`
- Összesen: `12` / `9` / `4 SFÉ`

#### Ár

- Alap: `100%` (sodrony, átlagos anyag), de a kidolgozottság „gyenge” (`0,5x`) → Mellvért ár : 50%
- Így 1db tag ára: `(50 / 5) = 10%`
- Végleges ár: `50% + (3 x 10%) = 80 %`, azaz egy átlagos acél mellvért darab `80%`-ába kerül a fenti teljes páncél-kombó. (csak `3` taggal szoroztunk, mert a mellvért-darabot már beleszámoltuk!)

---
### Példa egy vértre, amiben a lehető legnehezebb mozogni...

… és még az anyagminősége is a legvacakabb.

#### MGT

- Lemezvért, pocsék kidolgozottságú, anyaga: bronz
- Alap MGT: `18` (lemez) + `6` (bronz)
- Merev, fém (III.kat) / Pocsék munka → `+5` MGT / tag (**Kidolgozottság**)
- Védett terület: mellkas, felkar, alkarok, combok, lábszárak, fej (összesen: 6 tag).
- Karakter **Erő** tulajdonsága legyen: `+1` → (`2 x 1 = 2` jön le)

Összesen tehát: `18 + 6 + (6 x 5) – (2 x 1) = 52 MGT`

#### SFÉ

- Alap SFÉ: `12 / 14 / 9`
- Alapanyag minősége: leggyengébb (`SFÉ:-2`)
- Bronzból van: (`SFÉ:-3`)
- Összesen: `7 / 9 / 4` SFÉ

#### Ár

- Alap: `70%` (lemez, vacak anyag), a **Kidolgozottság** is „vacak” (`0,1x`) és bronzból van: (`0,5x`)
- Mellvért ár: `70% x 0,1 x 0,5 = 3,5%`
- Így 1db tag ára: `(3,5% / 5) = 0,7 %`
- Végleges ár: `3,5% + (5 x 0,7%) = 7 %`, azaz egy átlagos acél mellvért darab `80%`-ába kerül a fenti teljes gyatra páncél-kombó. (csak 5 taggal szoroztunk mert a mellvért-darabot már beleszámoltuk!)
