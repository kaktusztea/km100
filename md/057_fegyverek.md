## Fegyverek

⭕Bevezető⭕

### 1.3.1 Általános fegyver-harcértékek

Alább alapelveket találhatunk az egyes általános fegyverkategóriákhoz – méret szerint. A lentiek irányadó értékek, az egyes konkrét fegyverek számai ettől eltérnek, viszont új fegyver beillesztése a rendszerbe így gyerekjáték.

| **Kategóriánként** | **KÉ** | **TÉ** | **VÉ** |
| ------------------ | ------ | ------ | ------ |
|                    | **2**  | **4**  | **4**  |
<br />

| **Fegyver példa** | **Kategória** | **Sorszám** | &nbsp;&nbsp;**KÉ**&nbsp;&nbsp; | &nbsp;&nbsp;**TÉ**&nbsp;&nbsp; | &nbsp;&nbsp;**VÉ**&nbsp;&nbsp; |
| ----------------- | ------------- |:-----------:|:------------------------------:|:------------------------------:|:------------------------------:|
| tőr               | rövid         |      1      |               2                |               4                |               4                |
| rövid kard        | fél penge     |      2      |               4                |               8                |               8                |
| hosszú kard       | 1 penge       |      3      |               6                |               12               |               12               |
| másfélkezes kard  | 1,5 penge     |      4      |               8                |               16               |               16               |
| kétkezes kard     | 2 penge       |      5      |               10               |               20               |               20               |
| lándzsa           | szálfegyver   |      6      |               12               |               24               |               24               |


### 1.3.2 Elsődleges támadási típus
```
TÉ:-10   - másodlagos támadási típussal
TÉ:-20   - alkalmatlan támadási típussal
```

Minden fegyver rendelkezik egy **elsődleges támadási (sebzési) típussal**, pl. szúrás. Ha emellett más típusú támadásra is alkalmas, az csak másodlagos lehet. Ha a karakter nem jelenti be, hogy milyen típusú támadást akar leadni, akkor mindig az elsődleges támadás típust vesszük megtörténtnek. Például a hosszú kard: vágás/szúrás. Ekkor az alapértelmezett támadási típus a vágás. Ha a karakter bejelenti, hogy szúrni szeretne, akkor azt `TÉ:-10` módosítóval teheti meg. Ha pedig zúzni szeretne (amire a fegyver alkalmatlan), akkor – ha a KM engedi – azt `TÉ-20`-vel teheti meg.

### 1.3.3 Különleges fegyver szabály (jelölése: KF)

Egyes – speciális – fegyvereknél van megemlítve ez a szabály. Jelentése: a táblázatban leírt harcértékek csak akkor érvényesek, ha speciális iskolában, vagy onnan származó mestertől megtanulta a karakter a fegyver speciális fogásait. Ez részben előtörténet követelmény, amelyet fel kell tüntetni a karakterlapon. Bánjunk ezzel a követelménnyel szigorúan! Ha ez nincs meg, a KM dönt, hogy milyen – alacsonyabb – harcértékekkel forgathatja a karakter a fegyvert – már ha egyáltalán...

A fegyverek egyedi fogásaihoz viszont követelmény a **Mesterfegyver fortély** `1.` vagy `2.` foka az adott fegyverre. Ezen speciális fogásokat fortélyok formájában tanulhatja meg a harcos. Leírásukat lásd a harci fortélyoknál. Azok a fegyverek számítanak „Speciálisnak”, amelyek komment mezőjében szerepel a „**KT**” jelölés.

### 1.3.4 Puszta kéz

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
### 1.3.6 Közelharci fegyverek

(**IV**) Általános szabály íves fegyverekre:

```
- Páncélozatlan ellenfél ellen +2 SP sebzésbónusz
```


| **Fegyver**             | **Forgatás módja** | **SP**  | **Sebzés módja** | **Átütés** | **Pengehossz** | **KÉ** | **TÉ** | **VÉ** | **Sebesség** | **Speciális**                                                                                                                                                                                                                                           |
| ----------------------- | ------------------ | ------- | ---------------- | ---------- | -------------- | ------ | ------ | ------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Puszta kéz              | egykezes           | -5      | Z                | 0          | 0              | -10    | -10    | -10    | 5            | KT sebesülést okoz.<br><br>Minden 5-ik KT 1 ÉP elvesztését okozza.<br><br>Kivéve: harcművészek „Sárkány ököl” fortélya<br><br>Erőbónusz: Az Erő 1:1-ben beszámít                                                                                        |
| Tőr                     | egykezes           | +1      | S/V              | 0          | rövid          | 2      | 4      | 4      | 5            | -                                                                                                                                                                                                                                                       |
| Béltépő                 | egykezes           | +1      | S                | 0          | rövid          | 2      | 4      | 4      | 5            | - Ha minimum 11 SP lett a sebződobás, akkor +5 SP jár.<br>    <br>- Páncélos ellenfélnél minden esetben elakad, ha átment rajta a sebzés.<br>    <br>- Páncéltalan esetén: K6 dobás:  <br>    1-2 a fegyver elakad a testben, ha átment rajta a sebzés. |
| Dzsambia                | egykezes           | +0      | V/S              | 0          | rövid          | 2      | 4      | 4      | 5            | Páncélozott ellenfélnél: SP:0<br><br>Páncél nélküli ellenfélnél: SP:+2                                                                                                                                                                                  |
| Garott                  | egykezes           | +8 / +4 | V                | 0          | 0              | 0*     | 0*     | 0*     | -            | Csak orvtámadás harci taktikában használható.<br><br>Erőbónusz: Az Erő 1:1-ben beszámít                                                                                                                                                                 |
| Kés                     | egykezes           | +0      | S/V              | 0          | rövid          | 2      | 3      | 1      | 5            | -                                                                                                                                                                                                                                                       |
| Kriszkés                | egykezes           | +3/0    | S/V              | 0          | rövid          | 4      | 5      | 2      | 5            | Páncél nélküli ellenfélnél, szúrás esetén sebzése: +3 SP<br><br>Fegyverrántás szituációban +5 KÉ<br><br>Páncélszúrásra nem használható.                                                                                                                 |
| Levéltőr                | egykezes           | +1      | S/V              | 0          | rövid          | 2      | 4      | 5      | 5            | -                                                                                                                                                                                                                                                       |
| Markolatgomb            | egykezes           | +0      | Z                | 0          | 0              | -7     | -7     | -7     | 5            | Ugyanazok az értékei, mint a Vasökölnek.                                                                                                                                                                                                                |
| Méregfog                | egykezes           | +0      | S                | 0          | rövid          | 1      | 3      | 3      |              | Ha sebzést okoz, befecskendezi a benne tárolt mérget.                                                                                                                                                                                                   |
| Pugoss                  | egykezes           | +1      | S/V              | 0          | rövid          | 2      | 5      | 4      | 5            | Különleges fegyver használata szabály: gorviki klánnal, vagy mesterrel.<br><br>Ha a karakter nem ismeri a fegyver különleges fogásait akkor harcértékei sima tőré lesznek.                                                                              |
| Ramiera                 | egykezes           | +2      | S/V              | 0          | rövid          | 3      | 5      | 5      | 5            | KF - Amennyiben ez nincs meg, akkor csak a Rövidkard értékeivel forgatható.<br><br>Tőrnél nehezebb elrejteni.                                                                                                                                           |
| Tőr, hárító             | egykezes           | +0      | S                | 0          | rövid          | 2      | 4      | 10     | 5            | Nagyon drága!                                                                                                                                                                                                                                           |
| Tőr, kígyó              | egykezes           | +2      | S/V              | 0          | rövid          | 2      | 4      | 4      | 5            | Áldozótőr<br><br>Vágásnál: +0 SP                                                                                                                                                                                                                        |
| Tőr, ököl               | egykezes           | +0      | S                | 0          | rövid          | -5     | 0      | -5     | 5            |                                                                                                                                                                                                                                                         |
| Tőr, páncélszúró        | egykezes           | +1      | S                | 8          | 1 penge        | 4      | 8      | 4      |              | -                                                                                                                                                                                                                                                       |
| Tőr, Slan               | egykezes           | +2      | S/V              | 0          | rövid          | 0      | 6      | 2      | 5            |                                                                                                                                                                                                                                                         |
| Vasököl / páncélkesztyű | egykezes           | +0      | Z                | 0          | 0              | -7     | -7     | -7     | 5            | Erőbónusz: 0 feletti rész 1:1-ben számít be.                                                                                                                                                                                                            |

