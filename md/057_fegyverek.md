## Fegyverek

⭕Bevezető⭕

### Általános fegyver-harcértékek

Alább alapelveket találhatunk az egyes általános fegyverkategóriákhoz – méret szerint. A lentiek irányadó értékek, az egyes konkrét fegyverek számai ettől eltérnek, viszont új fegyver beillesztése a rendszerbe így gyerekjáték.

| **Kategóriánként** | KÉ | TÉ | VÉ |
| ------------------ | ------ | ------ | ------ |
|                    | **2**  | **4**  | **4**  |
<br />

| **Fegyver példa** | **Kategória** | **Sorszám** | &nbsp;&nbsp;KÉ&nbsp;&nbsp; | &nbsp;&nbsp;TÉ&nbsp;&nbsp; | &nbsp;&nbsp;VÉ&nbsp;&nbsp; |
| ----------------- | ------------- |:-----------:|:--------------------------:|:--------------------------:|:--------------------------:|
| tőr               | rövid         |      1      |             2              |             4              |             4              |
| rövid kard        | fél penge     |      2      |             4              |             8              |             8              |
| hosszú kard       | 1 penge       |      3      |             6              |             12             |             12             |
| másfélkezes kard  | 1,5 penge     |      4      |             8              |             16             |             16             |
| kétkezes kard     | 2 penge       |      5      |             10             |             20             |             20             |
| lándzsa           | szálfegyver   |      6      |             12             |             24             |             24             |


### Elsődleges támadási típus
```
TÉ:-10   - másodlagos támadási típussal
TÉ:-20   - alkalmatlan támadási típussal
```

Minden fegyver rendelkezik egy **elsődleges támadási (sebzési) típussal**, pl. szúrás. Ha emellett más típusú támadásra is alkalmas, az csak másodlagos lehet. Ha a karakter nem jelenti be, hogy milyen típusú támadást akar leadni, akkor mindig az elsődleges támadás típust vesszük megtörténtnek. Például a hosszú kard: vágás/szúrás. Ekkor az alapértelmezett támadási típus a vágás. Ha a karakter bejelenti, hogy szúrni szeretne, akkor azt `TÉ:-10` módosítóval teheti meg. Ha pedig zúzni szeretne (amire a fegyver alkalmatlan), akkor – ha a KM engedi – azt `TÉ-20`-vel teheti meg.

### Különleges fegyver szabály (jelölése: KF)

Egyes – speciális – fegyvereknél van megemlítve ez a szabály. Jelentése: a táblázatban leírt harcértékek csak akkor érvényesek, ha speciális iskolában, vagy onnan származó mestertől megtanulta a karakter a fegyver speciális fogásait. Ez részben előtörténet követelmény, amelyet fel kell tüntetni a karakterlapon. Bánjunk ezzel a követelménnyel szigorúan! Ha ez nincs meg, a KM dönt, hogy milyen – alacsonyabb – harcértékekkel forgathatja a karakter a fegyvert – már ha egyáltalán...

A fegyverek egyedi fogásaihoz viszont követelmény a **Mesterfegyver fortély** `1.` vagy `2.` foka az adott fegyverre. Ezen speciális fogásokat fortélyok formájában tanulhatja meg a harcos. Leírásukat lásd a harci fortélyoknál. Azok a fegyverek számítanak „Speciálisnak”, amelyek komment mezőjében szerepel a „**KT**” jelölés.

### Puszta kéz

A Puszta kéz kiemelt „fegyver”, hiszen mindig „ott van”. Puszta kézzel viszont bármilyen fegyver ellen meglehetősen kellemetlen harcolni, hiszen nincs mivel távol tartani, fenyegetni az ellenfelet. Ezért a Puszta kéz harcértékei mindenkinek a következők:

```
Puszta kéz:  KÉ:-10,  TÉ:-10,  VÉ:-10
```

#### Érintő támadás

Ha a cél csupán az ellenfél megérintése – nem sebzés –, akkor ezt könnyebben megteheti a támadó. Támadó Értékére nem jár levonás:

```
Puszta kéz:  KÉ:-10,  TÉ:0,  VÉ:-10
```

---
### Közelharci fegyverek

(**IV**) Általános szabály íves fegyverekre:

```
- Páncélozatlan ellenfél ellen +2 SP sebzésbónusz
```


| **Fegyver**             | Forgatás módja | SP      | Sebzés módja | **Átütés** | **Pengehossz** | KÉ  | TÉ  | VÉ  | Sebesség | Speciális                                                                                                                                                                                                                                                         |
| ----------------------- | -------------- | ------- | ------------ | ---------- | -------------- | --- | --- | --- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Puszta kéz              | egykezes       | -5      | Z            | 0          | 0              | -10 | -10 | -10 | +5       | KT sebesülést okoz.<br />Minden 5-ik KT 1 ÉP elvesztését okozza.<br />Kivéve: harcművészek „Sárkány ököl” fortélya<br />Erőbónusz: Az Erő 1:1-ben beszámít                                                                                                        |
| Tőr                     | egykezes       | +1      | S/V          | 0          | rövid          | 2   | 4   | 4   | +5       | -                                                                                                                                                                                                                                                                 |
| Béltépő                 | egykezes       | +1      | S            | 0          | rövid          | 2   | 4   | 4   | +5       | - Ha minimum 11 SP lett a sebződobás, akkor +5 SP jár.<br />    <br />- Páncélos ellenfélnél minden esetben elakad, ha átment rajta a sebzés.<br />    <br />- Páncéltalan esetén: K6 dobás:  <br />    1-2 a fegyver elakad a testben, ha átment rajta a sebzés. |
| Dzsambia                | egykezes       | +0      | V/S          | 0          | rövid          | 2   | 4   | 4   | +5       | Páncélozott ellenfélnél: SP:0<br />Páncél nélküli ellenfélnél: SP:+2                                                                                                                                                                                              |
| Garott                  | egykezes       | +8 / +4 | V            | 0          | 0              | 0*  | 0*  | 0*  | -        | Csak orvtámadás harci taktikában használható.<br />Erőbónusz: Az Erő 1:1-ben beszámít                                                                                                                                                                             |
| Kés                     | egykezes       | +0      | S/V          | 0          | rövid          | 2   | 3   | 1   | +5       | -                                                                                                                                                                                                                                                                 |
| Kriszkés                | egykezes       | +3/0    | S/V          | 0          | rövid          | 4   | 5   | 2   | +5       | Páncél nélküli ellenfélnél, szúrás esetén sebzése: +3 SP<br />Fegyverrántás szituációban +5 KÉ<br />Páncélszúrásra nem használható.                                                                                                                               |
| Levéltőr                | egykezes       | +1      | S/V          | 0          | rövid          | 2   | 4   | 5   | +5       | -                                                                                                                                                                                                                                                                 |
| Markolatgomb            | egykezes       | +0      | Z            | 0          | 0              | -7  | -7  | -7  | +5       | Ugyanazok az értékei, mint a Vasökölnek.                                                                                                                                                                                                                          |
| Méregfog                | egykezes       | +0      | S            | 0          | rövid          | 1   | 3   | 3   |          | Ha sebzést okoz, befecskendezi a benne tárolt mérget.                                                                                                                                                                                                             |
| Pugoss                  | egykezes       | +1      | S/V          | 0          | rövid          | 2   | 5   | 4   | +5       | Különleges fegyver használata szabály: gorviki klánnal, vagy mesterrel.<br />Ha a karakter nem ismeri a fegyver különleges fogásait akkor harcértékei sima tőré lesznek.                                                                                          |
| Ramiera                 | egykezes       | +2      | S/V          | 0          | rövid          | 3   | 5   | 5   | +5       | KF - Amennyiben ez nincs meg, akkor csak a Rövidkard értékeivel forgatható.<br />Tőrnél nehezebb elrejteni.                                                                                                                                                       |
| Tőr, hárító             | egykezes       | +0      | S            | 0          | rövid          | 2   | 4   | 10  | +5       | Nagyon drága!                                                                                                                                                                                                                                                     |
| Tőr, kígyó              | egykezes       | +2      | S/V          | 0          | rövid          | 2   | 4   | 4   | +5       | Áldozótőr<br />Vágásnál: +0 SP                                                                                                                                                                                                                                    |
| Tőr, ököl               | egykezes       | +0      | S            | 0          | rövid          | -5  | 0   | -5  | +5       |                                                                                                                                                                                                                                                                   |
| ⭕Tőr, páncélszúró⭕    | egykezes       | ⭕+1    | ⭕S          | ⭕         | ⭕1 penge      | ⭕4 | ⭕8 | ⭕4 |          | -                                                                                                                                                                                                                                                                 |
| Tőr, Slan               | egykezes       | +2      | S/V          | 0          | rövid          | 0   | 6   | 2   | +5       |                                                                                                                                                                                                                                                                   |
| Vasököl / páncélkesztyű | egykezes       | +0      | Z            | 0          | 0              | -7  | -7  | -7  | +5       | Erőbónusz: 0 feletti rész 1:1-ben számít be.                                                                                                                                                                                                                      |

---
### Kardvívó fegyverek harcértékei

(**MK**) Általános szabály Másfélkezes fegyverekre, ha egy kézzel forgatják őket:

```
- KÉ:-3,  TÉ:-5,  VÉ:-5
- Átütés megszűnik (ha volt)
- Erőbónuszra -3 büntetés, azaz a Sebzésre -3 büntetés
- Sebesség, marad
```

(**IV**) Általános szabály íves fegyverekre:

```
- Páncélozatlan ellenfél ellen +2 SP sebzésbónusz
```


| **Fegyver**          | Forgatás módja | SP  | Sebzés módja | **Átütés** | **Pengehossz**                          | KÉ  | TÉ  | VÉ  | Sebesség | Speciális                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | -------------- | --- | ------------ | ---------- | --------------------------------------- | --- | --- | --- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kard, dzsenn szablya | egykezes       | +4  | V/S          | 0          | 1 penge                                 | 8   | 15  | 15  | 5        | **(IV)** fegyver                                                                                                                                                                                                                                                                                                                                                                             |
| Kard, emrelin        | egykezes       | +4  | V/S          | 0          | 1 penge                                 | 7   | 13  | 13  | 6        |                                                                                                                                                                                                                                                                                                                                                                                              |
| Kard, fejvadász      | egykezes       | +3  | V/S          | 0          | 0,5 penge                               | 5   | 9   | 11  | 5        | KF: gorviki klánnal, vagy mesterrel.<br />Ha a karakter nem ismeri a fegyver különleges fogásait akkor harcértékei sima rövidkardé lesznek.<br />Hárítófegyverként is használható.                                                                                                                                                                                                           |
| Kard, handzsár       | egykezes       | +4  | V            | 0          | 1 penge                                 | 4   | 13  | 10  | 6        | **(IV)** fegyver<br />Erő követelmény: +2                                                                                                                                                                                                                                                                                                                                                    |
| Kard, hiequar        | egykezes       | +4  | S/V          | 2          | 1 penge                                 | 4   | 12  | 8   | 6        | Elfek használják. Előtörténet!                                                                                                                                                                                                                                                                                                                                                               |
| Kard, hosszú         | egykezes       | +4  | V/S          | 0          | 1 penge                                 | 6   | 12  | 12  | 6        | Nem éri meg, mert a másfélkezes sokkal jobb mindenben és nincs hátránya                                                                                                                                                                                                                                                                                                                      |
| Kard, jatagán        | egykezes       | +1  | V/S          | 0          | ⭕1 penge<br />vagy 0,5 penge? (Márk)⭕ | ⭕4 | ⭕8 | ⭕8 | 6        | **(IV)** fegyver                                                                                                                                                                                                                                                                                                                                                                             |
| Kard, kétkezes       | kétkezes       | +8  | V/S          | 0          | 2 penge                                 | 10  | 20  | 15  | 8        | Ha közrefogják a forgatót, fegyverének VÉ-je 0-ra zuhan.<br />Erő követelmény: +2<br />Edzettség követelmény: +1                                                                                                                                                                                                                                                                             |
| Kard, khossas        | egykezes       | +4  | V/S          | 0          | 1 penge                                 | 4   | 11  | 10  | 6        | Elfek használják. Előtörténet!                                                                                                                                                                                                                                                                                                                                                               |
| Kard, kígyó          | egykezes       | +3  | V/S          | 0          | 1 penge                                 | 5   | 11  | 11  | 6        | Szúró sebzés: +5 SP                                                                                                                                                                                                                                                                                                                                                                          |
| Kard, Lagoss         | egykezes       | ⭕  | ⭕           | 0          | ⭕                                      | ⭕  | ⭕  | ⭕  | ⭕       | KF: Amennyiben ez nincs meg, akkor csak a Hosszúkard értékeivel forgatható.                                                                                                                                                                                                                                                                                                                  |
| Kard, lovag          | egykezes       | +6  | V/S          | 1          | 1 penge                                 | 7   | 15  | 12  | 7        | Erő követelmény: +2                                                                                                                                                                                                                                                                                                                                                                          |
| Kard, másfélkezes    | kétkezes       | +5  | V/S          | 0          | 1,5 penge                               | 8   | 16  | 16  | 7        | (MK), továbbá:<br />- 2 kézre fogva: alap <br />- 1 kézre fogva:  <br />&nbsp;&nbsp;• -3 KÉ, -5 TÉ, -5 VÉ<br />&nbsp;&nbsp;• Átütés megszűnik (ha volt)<br />&nbsp;&nbsp;• Erőbónuszra -3 büntetés, azaz a SP: -3 büntetés<br />&nbsp;&nbsp;• Sebesség, marad <br />- +1-es Erő alatt forgatva:<br />&nbsp;&nbsp;• 1 pontonként -10 minden harcértékre<br />&nbsp;&nbsp;• 1:1 levonás SP-ből |
| Kard, mesterkard     | kétkezes       | +5  | V/S          | 0          | 1,5 penge                               | 9   | 18  | 13  | 7        | (MK), továbbá:<br />⭕TODO⭕                                                                                                                                                                                                                                                                                                                                                                 |
| Kard, Pugoss         | egykezes       | ⭕  | ⭕           | 0          | 0,5 penge                               | ⭕  | ⭕  | ⭕  | ⭕       | (KF)                                                                                                                                                                                                                                                                                                                                                                                         |
| Kard, rövid          | egykezes       | +2  | S/V          | 0          | 0,5 penge                               | 4   | 8   | 8   | 6        | -                                                                                                                                                                                                                                                                                                                                                                                            |
| Kard, Slan           | kétkezes       | +6  | V/S          | 2          | 1,5 penge                               | 9   | 19  | 13  | 7        | (MK), továbbá: (spec)<br />Nagyon ritka, rendkívül nehéz hozzájutni, legtöbbször személyre szabott.<br />Fegyverrántásban képzett karakter fegyverrántó szituációban +5 KÉ-t kap.                                                                                                                                                                                                            |
| Kard, Slan rövid     | egykezes       | +4  | V/S          | 0          | 0,5 penge                               | 5   | 11  | 5   | 5        | Lásd Slan kard (de nem (MK))                                                                                                                                                                                                                                                                                                                                                                 |
| Kard, Slan csatakard | kétkezes       | +9  | V/S          | 2          | 2 penge                                 | 9   | 23  | 17  | 8        | Hihetetlen drága és ritka.<br />Csak két kézzel forgatható.  <br />(spec)                                                                                                                                                                                                                                                                                                                    |
| Kard, szablya        | egykezes       | +3  | V/S          | 0          | 1 penge                                 | 6   | 12  | 12  | 6        | **(IV)** fegyver                                                                                                                                                                                                                                                                                                                                                                             |
| Mara-sequor          | kétkezes       | ⭕  | ⭕           | ⭕         | ⭕                                      | ⭕  | ⭕  | ⭕  |          | (MK), (KF) továbbá:                                                                                                                                                                                                                                                                                                                                                                          |
| Meneth               | egykezes       | ⭕  | ⭕           | 0          | ⭕                                      | ⭕  | ⭕  | ⭕  | ⭕       |                                                                                                                                                                                                                                                                                                                                                                                              |
| Predoci egyeneskard  | egykezes       | ⭕  | ⭕           | 0          | ⭕                                      | ⭕  | ⭕  | ⭕  | ⭕       |                                                                                                                                                                                                                                                                                                                                                                                              |
| Sequor               | egykezes       | ⭕  | ⭕           | 0          | ⭕                                      | ⭕  | ⭕  | ⭕  | ⭕       | (KF):                                                                                                                                                                                                                                                                                                                                                                                        |
| Tőrkard              | egykezes       | +2  | S            | 0          | 1 penge                                 | 6   | 12  | 12  | 5        | - Az áldozat páncéldobás során -1 büntetést szenved el<br /> - Pontra támadás manővernél: a manőver nehézsége 1-el csökken <br />- Ha az ellenfél is tőrkarddal harcol, mindketten kapnak +10 VÉ bónuszt.                                                                                                                                                                                    |

---
### Pusztító fegyverek harcértékei
     
| **Fegyver**                               | Forgatás módja | SP  | Sebzés módja           | **Átütés** | **Pengehossz** | KÉ  | TÉ  | VÉ  | Sebesség | Speciális                                                                      |
| ----------------------------------------- | -------------- | --- | ---------------------- | ---------- | -------------- | --- | --- | --- | -------- | ------------------------------------------------------------------------------ |
| ⭕Balta                                   | egykezes       |     |                        | 0          |                |     |     |     |          |                                                                                |
| ⭕Bot, rövid                              | egykezes       |     |                        | 0          |                |     |     |     |          |                                                                                |
| ⭕Bot, furkós                             | egykezes       |     |                        | 0          |                |     |     |     |          |                                                                                |
| Buzogány, egykezes                        | egykezes       | 5   | Z                      | 0          | 1 penge        | 4   | 12  | 8   | 7        |                                                                                |
| ⭕Buzogány, kétkezes                      | kétkezes       |     |                        | 0          |                |     |     |     |          |                                                                                |
| ⭕Buzogány, láncos                        | egykezes       |     |                        |            |                |     |     |     |          | Pajzs VÉ a fele! (?)                                                           |
| ⭕Buzogány, shadleki                      | ??             |     |                        |            |                |     |     |     |          |                                                                                |
| ⭕Buzogány, tollas                        | egykezes       |     |                        | !          |                |     |     |     |          |                                                                                |
| ⭕Buzogány, tüskés  <br />_csatacsillag_? | egykezes       |     |                        | !!         |                |     |     |     |          |                                                                                |
| Csatabárd, egykezes                       | egykezes       | +4  | V  <br />(néha szúrás) | ??         | 0,5 penge      | 4   | 8   | 8   |          |                                                                                |
| Csatabárd, kétkezes                       | kétkezes       | +8  | ??                     | ??         | 1,5 penge      | 8   | 16  | 16  |          |                                                                                |
| Csatacsákány                              | egykezes       | +3  | S?                     | 10 !       | 1 penge        | 4   | 8   | 8   |          | Nagyon vérzik<br />50% az esély, hogy beragad és nem lehet kihúzni harc közben |
| ⭕Cséphadaró                              | kétkezes       |     |                        | 0          |                |     |     |     |          | EZ NEM SZÁLFEGYVER?                                                            |
| ⭕Harci kalapács                          | ??             |     |                        |            |                |     |     |     |          |                                                                                |

---
### Lándzsavívó fegyverek harcértékei
 
| **Hegy**      | SP  | Sebzés módja | **Átütés** | Speciális                                                                                                                                                                                                                                                                                |
| ------------- | --- | ------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Keskeny hegyű | +2  | S            | 4          | Kis területet roncsol, de páncélokat jól üti át                                                                                                                                                                                                                                          |
| Széles hegyű  | +4  | S            | 0          | Nagy területet roncsol, de nehezebben megy át a páncélokon                                                                                                                                                                                                                               |
| Szigony       | +4  | S            | 0          | - Ha minimum 11 SP lett a sebződobás (SFÉ lejön!), akkor +5 SP jár. <br />- Páncélos ellenfélnél: K6 dobás: 1-3 értéknél a fegyver elakad a testben, ha átment rajta a sebzés.<br /> - Páncéltalan esetén: K6 dobás: 1-es értéknél a fegyver elakad a testben, ha átment rajta a sebzés. |
| Alabárd fej   |     |              |            |                                                                                                                                                                                                                                                                                          |

⭕Méret: MGT bejön nagy méretnél⭕

| **Fegyver**         | Forgatás módja | SP  | Sebzés módja | **Átütés** | **Pengehossz** | KÉ  | TÉ  | VÉ  | Sebesség | Speciális                        |
| ------------------- | -------------- | --- | ------------ | ---------- | -------------- | --- | --- | --- | -------- | -------------------------------- |
| ⭕Alabárd           | kétkezes       |     |              |            |                |     |     |     |          | Talán a legjobb a páncélok ellen |
| ⭕Bot, hosszú       | kétkezes       |     | Z            | 0          |                |     |     |     |          |                                  |
| Lándzsa             | kétkezes       |     | S            |            | 3 penge        | 12  | 24  | 24  |          |                                  |
| ⭕Pika              | kétkezes       |     | S            |            |                |     |     |     |          |                                  |
| ⭕Szigony, egykezes | egykezes       |     |              |            |                |     |     |     |          |                                  |
| ⭕Szigony, kétkezes | kétkezes       |     |              |            |                |     |     |     |          |                                  |

<br />

---
### Lovas fegyverek harcértékei
     
| **Fegyver**            | Forgatás módja | SP  | Sebzés módja | **Átütés** | **Pengehossz** | KÉ  | TÉ  | VÉ  | Sebesség | Speciális |
| ---------------------- | -------------- | --- | ------------ | ---------- | -------------- | --- | --- | --- | -------- | --------- |
| ??? Kopja, könnyű      |                |     |              |            |                |     |     |     |          |           |
| ??? Kopja, lovas       |                |     |              |            |                |     |     |     |          |           |
| ??? Kopja,, nehézlovas |                |     |              |            |                |     |     |     |          |           |

<br />

---
### Hajítófegyverek harcértékei

A Hajítófegyverek sebzése általánosságban **Szúró** jellegű. Ahol ez másként van, ott az adott fegyver leírásánál a „Speciális/Megjegyzés” oszlopban ezt külön feltüntetjük.

#### Hajító szálfegyverek (Hajítás)
| Fegyver         | Forgatás módja | SP  | Sebzés módja | Átütés | KÉ  | CÉ  | Osztó | Hatótáv | Sebesség | Speciális / Megjegyzés                                                                     |
| --------------- | -------------- |:---:|:------------:|:------:|:---:|:---:|:-----:| -------:|:--------:| ------------------------------------------------------------------------------------------ |
| ⭕Könnyű kopja  |                |     |              |        |     |     |   1   |     60m |          | Követelmény: Erő `+3`                                                                      |
| ⭕Lándzsa  (?)  |                |     |              |        |     |     |   1   |     60m |          | Követelmény: Erő `+2`                                                                      |
| ⭕Dárda, hajító |                |     |              |        |     |     |   2   |     60m |          | Követelmény: Erő `+0`<br />Pajzsba dobva csökkenti annak Védő Értékét a dobott SP értékkel |

<br />

#### Hajítófegyverek (Hajítás)
| Fegyver        | Forgatás módja | SP  | Sebzés módja | Átütés | KÉ  | CÉ  | Osztó | Hatótáv | Sebesség | Speciális / Megjegyzés                                                                                                                                                                                 |
| -------------- | -------------- |:---:|:------------:|:------:|:---:|:---:|:-----:| -------:|:--------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ⭕Bola         | egykezes       |     |              |        |     | +2  |   1   |     20m |          |                                                                                                                                                                                                        |
| ⭕Hajítóbárd   | egykezes       |     |              |        |     | +4  |   1   |  ⭕20m* |          | Maximális hatótávolsága:  <br />`20+(Erő x 4)` méterben<br />Pajzsba dobva csökkenti annak Védő Értékét a dobott **SP** értékkel                                                                       |
| ⭕Hajítótőr    | egykezes       | +0  |      S       |        |     | +4  |   2   |     15m |          | Automatikusan jár rá a **Közeli lövés** fortélynál leírt `CÉ:+10` bónusz ha a célpont Cellaszáma 1.<br />Erőbónusz: **Erő** `1:1`-ben beszámít<br />⭕**SFÉ** bónusz még ellene esetleg.. (dupla SFÉ?) |
| ⭕kő, alma     | egykezes       |     |              |        |     | +0  |   1   |    20m* |          | Maximális hatótávolsága: <br />`20+(Erő x 5)` méterben                                                                                                                                                 |
| ⭕Parittya     | egykezes       |     |              |        |     | +4  |   2   |     70m |          | Lehet nagy sebzése, de az SFÉ duplán számítson ellene (vagy SFÉ bónusz)                                                                                                                                |
| ⭕Ramiera (?)  | egykezes       |     |              |        |     | +1  |   1   |     10m |          |                                                                                                                                                                                                        |
| ⭕Slan csillag | egykezes       |     |              |        |     | +3  |   1   |     15m |          |                                                                                                                                                                                                        |
| ⭕Tőr          | egykezes       |     |              |        |     | +2  |   2   |     10m |          |                                                                                                                                                                                                        |

<br />

#### Egyéb távolsági fegyverek (Hajítás)

| Fegyver    | Forgatás módja | SP  | Sebzés módja | Átütés | KÉ  | CÉ  | Osztó | Hatótáv | Sebesség | Speciális / Megjegyzés                  |
| ---------- | -------------- | --- | ------------ |:------:|:---:|:---:|:-----:|:-------:| -------- | --------------------------------------- |
| ⭕Dobóháló |                |     |              |        |     | +0  |   1   |   4m*   |          | Maximális hatótávolsága: 4+Erő méterben |
| ⭕Köpeny   | egykezes       |     |              |        |     | +0  |   1   |   4m    |          |                                         |
| ⭕Lasszó   | egykezes       |     |              |        |     | +0  |   1   |   10m   |          |                                         |


<br />

---
### Lőfegyverek harcértékei
`TODO_HARC_#36.`

A Lőfegyverek sebzése általánosságban **Szúró** jellegű. Ahol ez másként van, ott az adott fegyver leírásánál a „**Speciális/Megjegyzés**” oszlopban ezt külön feltüntetjük.  

A Sebzést és Átütést a nyílhegy is meghatározza! ⭕TODO ⭕

1 helyen rögzített „lengő” anyagok könnyen megfoghatják a lövedékeket (pl. száradó ruha)⭕.


#### Íjász lőfegyverek

| Fegyver           | Forgatás módja | SP  | Sebzés módja | Átütés | KÉ  | CÉ  | Osztó  | Hatótáv | Sebesség | Speciális / Megjegyzés                                                                             |     |
| ----------------- | -------------- |:---:|:------------:|:------:|:---:|:---:|:------:| -------:|:--------:| -------------------------------------------------------------------------------------------------- | --- |
| ⭕Rövid íj        | kétkezes       |     |              |        |     | +10 |   2    |         |          | Az Erőbónusz csak akkor számít ha az íj erre az Erő értékre lett tervezve!                         |     |
| ⭕Hosszú íj       | kétkezes       |     |              |        |     | +12 |   3    |         |          | Az Erőbónusz csak akkor számít ha az íj erre az Erő értékre lett tervezve!                         |     |
| ⭕Visszacsapó íj  | kétkezes       |     |              |        |     | +10 |   3    |         |          | Az Erőbónusz csak akkor számít ha az íj erre az Erő értékre lett tervezve!                         |     |
| ⭕Elf íj          | kétkezes       |     |              |        |     | +13 | 3(4\*) |         |          | \Csak a készítője (és egyben birtokosa) kezében, egyébként hagyományos íjként működik. Osztója: 3. |     |
| ⭕Fúvócső, kicsi  | egykezes       |     |              |        |     | +8  |   1    |         |          | k20 dobásnál: 20-as dobás: 1 ÉP, különben 0 ÉP                                                     |     |
| ⭕Fúvócső, vadász | kétkezes       |     |              |        |     | +10 |   1    |         |          |                                                                                                    |     |


#### Lövész lőfegyverek


| Fegyver          | Forgatás módja | SP  | Sebzés módja | Átütés | KÉ  |  CÉ  | Osztó | Hatótáv | Sebesség | Speciális / Megjegyzés                                                         |
| ---------------- | -------------- |:---:|:------------:|:------:|:---:|:----:|:-----:| -------:|:--------:| ------------------------------------------------------------------------------ |
| Kézi nyílpuska   | egykezes       |     |      S       |        |     | +10* |   3   |     20m |    ⭕    | * A kézi nyílpuska kevésbé pontos fegyver kis mérete miatt.                    |
| Nyílpuska        | kétkezes       | +6  |      S       |  ⭕10  |     | +16  |   4   |     50m |    ⭕    | Nem páncéltörő ?? A nehézvértet átviszi, vagy nem?<br />Távolság-függő Átütés. |
| Nehéz nyílpuska  | kétkezes       | +14 |      S       |  ⭕10  |     | +16  |   4   |     80m |    ⭕    | Páncéltörő Ez átviszi a nehézvértet is!                                        |
| Shad. páncéltörő | kétkezes       |     |      Z       |  ⭕??  |     |  +4  |   4   |  ⭕120m |    ⭕    | * Újratöltés: 1 emberrel: 3 kör, 2 emberrel: 1 kör<br />** Páncéltörő          |
| Khar. nyílpuska  | kétkezes       |     |      S       |        |     | +14  |   4   |     50m |    ⭕    | * Míg ki nem fogy a tár. Újratöltés: 1 kör                                     |


