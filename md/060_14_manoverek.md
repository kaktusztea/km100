## Manőverek

- [Szabályok manőverekre](#Szabályok-manőverekre)
- [Manőverek nehézsége](#Manőverek-nehézsége)
- [Manőver végrehajtásának lépései](#Manőver-végrehajtásának-lépései)
	- [Megakasztás (M)](#Megakasztás-M)
	- [Végrehajtás (V)](#Végrehajtás-V)
	- [Ellenpróba (E)](#Ellenpróba-E)
		- [Manőver Pont](#Manőver-Pont)
		- [Célszám](#Célszám)
	- [Vállalás](#Vállalás)
- [Manőverek végrehajtása, képzetlenség](#Manőverek-végrehajtása-képzetlenség)
- [Manőverek fejlesztése, manőver-ismeretek](#Manőverek-fejlesztése-manőver-ismeretek)
- [Manőver lista](#Manőver-lista)
- [Nem fejleszthető manőverek](#Nem-fejleszthető-manőverek)
	- [Átdobás](#%EF%B8%8F%C3%A1tdob%C3%A1s)
	- [Felállás földről](#%EF%B8%8Ffel%C3%A1ll%C3%A1s-f%C3%B6ldr%C5%91l)
	- [Feszítés, Leszorítás / Feszítésből kijövetel](#%EF%B8%8Ffesz%C3%ADt%C3%A9s-leszor%C3%ADt%C3%A1s--fesz%C3%ADt%C3%A9sb%C5%91l-kij%C3%B6vetel)
	- [Kéztörés](#%EF%B8%8Fk%C3%A9zt%C3%B6r%C3%A9s)
	- [Kiegészítő támadás](#%EF%B8%8Fkieg%C3%A9sz%C3%ADt%C5%91-t%C3%A1mad%C3%A1s)
	- [Lábtörés](#%EF%B8%8Fl%C3%A1bt%C3%B6r%C3%A9s)
	- [Leforgatás/Irányítás](#%EF%B8%8Fleforgat%C3%A1sir%C3%A1ny%C3%ADt%C3%A1s)
	- [Nyaktörés](#%EF%B8%8Fnyakt%C3%B6r%C3%A9s)
	- [Öklelés](#%EF%B8%8F%C3%B6klel%C3%A9s)
	- [Pajzzsal öklelés](#%EF%B8%8Fpajzzsal-%C3%B6klel%C3%A9s)
- [Fejleszthető manőverek](#Fejleszthető-manőverek)
	- [Belharcba kerülés](#%EF%B8%8Fbelharcba-ker%C3%BCl%C3%A9s)
	- [Belharcból kibontakozás](#%EF%B8%8Fbelharcb%C3%B3l-kibontakoz%C3%A1s)
	- [Gáncsolás / Lábsöprés (lábbal)](#%EF%B8%8Fg%C3%A1ncsol%C3%A1s--l%C3%A1bs%C3%B6pr%C3%A9s-l%C3%A1bbal)
	- [Kibontakozás/Átsiklás](#%EF%B8%8Fkibontakoz%C3%A1s%C3%A1tsikl%C3%A1s)
	- [Lábkirántás (szálfegyverrel)](#%EF%B8%8Fl%C3%A1bkir%C3%A1nt%C3%A1s-sz%C3%A1lfegyverrel)
	- [Lánccsapda (láncos fegyverekre)](#%EF%B8%8Fl%C3%A1nccsapda--l%C3%A1ncos-fegyverekre)
	- [Lefegyverzés / Fegyvertörés - egy konkrét harcmodorra](#%EF%B8%8Flefegyverz%C3%A9s--fegyvert%C3%B6r%C3%A9s---egy-konkr%C3%A9t-harcmodorra)
	- [Lefejelés](#%EF%B8%8Flefejel%C3%A9s)
	- [Mesterjel](#%EF%B8%8Fmesterjel)
	- [Pajzsrongálás](#%EF%B8%8Fpajzsrombol%C3%A1s)
	- [Területre/Pontra támadás](#%EF%B8%8Fpontra-t%C3%A1mad%C3%A1s) 
	- [Távoltartás](#%EF%B8%8Ft%C3%A1voltart%C3%A1s)
	- [Terelés](#%EF%B8%8Fterel%C3%A9s)
- [Lovas Manőverek](#lovas-man%C5%91verek)
- [Egyszerű példa egy Manőver alkalmazására](#Egyszerű-példa-egy-Manőver-alkalmazására)
- [Összetettebb példa egy Manőver alkalmazására](#Összetettebb-példa-egy-Manőver-alkalmazására)


Harc közben gyakran előfordul, hogy egy karakter speciális húzásokkal próbálkozik, egyedi cseleket vet be, hogy megkönnyítse győzelmét, például kirúgja ellenfele lábát, vagy homokot szór annak szemébe. Sokszor van olyan is, hogy egy karakter különösen jó egy adott csel alkalmazásában és azt előszeretettel veti be minden új ellenfelénél. De ha egyszer olyannal kerül szembe, aki számít rá...

A km100 harcrendszere lehetőséget ad rá, hogy a karakter harc közben ilyen speciális cselekedeteket – manővereket – alkalmazzon. Vannak olyan manőverek is, melyek csak adott fegyverre, vagy harcmodorra jellemzőek, de a legtöbb szabadon, bárki által alkalmazható, amennyiben eleget tesz a leírt követelményeknek. Az alábbiakban látható az egyes manőverek összefoglaló táblázata, mely tömör formában bemutatja, hogy esetükben mire is van szükség végrehajtásukhoz.


---
### Szabályok manőverekre

- Manővert csak az aktuálisan használt harcmodor `3.szintjétől` lehet rendesen használni, alatta a **Manőver Nehézsége** magasabb
  - harcmodor `0.szint` esetén: `+3`
  - harcmodor `1.szint` esetén: `+2`
  - harcmodor `2.szint` esetén: `+1`

- Egy Manőver végrehajtása `1 támadást` emészt fel, nem szükséges hozzá nyert kezdeményezés

- Manővert ellenfél **ellen** alkalmazunk. Így például kiszaltózni az ablakon, vagy leugrani a várfalról **nem** számít Manővernek!

- Ha minden kötelező fázisa (`M E V`) sikeres, akkor az adott Manőver „Hatás” részénél leírtak következnek be

- Végrehajtás fázisa aktuális **fegyveres** `TÉ`-vel történik (kivéve, ha más szerepel a Manőver leírásában.)

- Meglepett, készületlen ellenfél esetén kimarad a **Megakasztás** és az **Ellenpróba** fázis

- Manővereknek lehet:
	- speciális könnyítő/nehezítő körülményei (+/- módosítók a nehézségre)
	- extra végbeviteli követelményei: Ezek nélkül a KM dönt, hogy végrehajtható -e és ha igen, mekkora plusz célszám büntetéssel

- Manőver alkalmazásakor nem folytatható **Védekező harc**, vagy **Védő Taktika**, de **Támadó taktika** igen, kivéve ahol ez az adott Manővernél külön meg van említve.

- **Rohamnál** csak az a manőver hajtható végre, amelyiknél ez külön meg van említve

<br/>

---
### Manőverek nehézsége


| Nehézség     | Érték |
| ------------ |:-----:|
| Mindennapos  |   2   |
| Könnyű       |   4   |
| Átlagos      |   6   |
| Nehéz        |   8   |
| Nagyon nehéz |  10   |

A manőver nehézségét egy számértékkel jellemezzük. Minden manővernek van egy alapnehézsége. Az adott manőver ezzel az értékkel szerepel az **Ellenpróba** **során**. E táblázatban csak irányadó számok szerepelnek, új manőver kitalálásakor hasznos. A manőverek nehézsége ezen értékek közé is eshet.

> **Hasznos tanács** KM részére új (tanulható) manőver létrehozásakor:
> ha úgy érzed, az adott manőver túl tápos, emeld meg a nehézségét és adj több tanulható fokot. Így több MFP szükséges a nehézség csökkentéséhez és így már meglesz az „ára”, ha valaki eséllyel alkalmazni akarja.

<br/>

---
### Manőver végrehajtásának lépései

A játékosnak a kör elején be kell jelentenie, hogy Manővert akar alkalmazni és azt is, hogy melyiket. Ezután a karakterek kezdeményezést dobnak (kivéve pl. a **Meglepetés** szituációt), majd mikor az alkalmazóra kerül a sor, jön a Manőver. Ha a KM úgy látja jónak, megtilthatja adott szituációban a Manőver alkalmazását. Amennyiben a játékos ezt a döntést nem képes kulturáltan kezelni, a KM növelje intenzíven a manőver nehézségét...

Egy Manőver alkalmazása – jellegétől függően – legfeljebb az alábbi három (de nem kötelezően az összes!) alapfázisból állhat. Mindegyik opcionális, hogy melyikre van szükség, azt az adott Manőver leírásánál találjuk. Végrehajtásuk sorrendjében:

- `1.` **Megakasztás** (ha van)\
  ellenfél teszi (Sima támadás - ha sikeres, a Manőver rögtön sikertelen)

- `2.` **Végrehajtás** (manővert végző teszi)\
  Sebzést érő támadás szükséges, `TÉ+20`-al, (aktuális, fegyveres `TÉ` számít), de nem okoz sebet.\
  Mindig ezt dobjuk előbb, mert ez ad leggyorsabban eredményt 🔆

- `3.` **Ellenpróba** (manővert végző teszi)\
  ```Manőver pont vs Célszám```

---
#### Megakasztás (M)

Megelőző támadási forma, melyre az ellenfél jogosult teljes, fegyveres `TÉ`-jével (soron kívüli extra támadás), ha az adott típusú manőver követelményei között ez szerepel (M).

A Megakasztás az első fázis a Manőver végrehajtása során. Ha az így érkező támadás sebző, akkor a Manőver nem sikerült. (Tipikus példa, a harcból való **Kibontakozás**, vagy a **Belharcba kerülés**.)

<br/>

---
#### Végrehajtás (V)

Nem más, mint egy támadás az aktuális, **fegyveres TÉ** értékkel, melyhez `+20 TÉ` módosító járul. Ha ez a támadás sikeres, akkor a Végrehajtás is sikeres (sebzés nincs). (TÉ-be beleszámít a több támadás levonása is!)

Ha a **Végrehajtás** sikertelen, akkor a helyzet megvolt, de nem sikerült kihasználni. A **Végrehajtás** **dobása** után – ha sikeres volt, ha nem – az ellenfél legközelebb már számít az ilyen jellegű támadásra, ezért amennyiben ismét ezt a Manővert kísérli meg a karakter, akkor az **Ellenpróba** során a célszám már **+2-vel** nőni fog (lásd: Ellenpróba lenn) (nem halmozódik). Ilyen lehet még az is, ha a játékos az ellenfelét már látta korábban küzdeni és egy konkrét manővert gyakran alkalmazni.

A fentieken kívül minden **Manővernek** lehetnek egyéni, speciális követelményei, ezeket a saját leírásuknál található meg. A Manőverek fenti (legfeljebb) három „komponense” együtt kezelendő és együtt összesen egy „sima” támadást „emésztenek fel”.

<br/>

---

#### Ellenpróba (E)

```
Manőver pont + k10   vs.  Manőver célszáma
```

<br/>

##### Manőver Pont

| Módosító                                              | Érték                                                             |
| ----------------------------------------------------- | ----------------------------------------------------------------- |
| Harcmodor                                             | Az alkalmazó aktuálisan használt harcmodor képzettségének szintje |
| HM / 10                                               | A nem-távolsági harcmodorokra elköltött **Harcérték Módosítók** (HM) tizede. |
| „Manőver ismeret<br>(az adott manőverre)”<br>(ha van) | Fokonként: `+2`                                                   |
| Vállalás                                              | `+1` pont → `-15 VÉ`<br>(Maximum vállalás: **+ 2**)               |
| + k10                                                 | Dobás `k10`-el                                                    |

<br/>

##### Célszám

| Módosító                                               | Érték                                                                                                                                 |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Manőver Nehézség                                       | Az adott Manőver alapnehézsége                                                                                                        |
| HM / 10                                                | Az ellenfél nem-távolsági harcmodorokra elköltött **Harcérték Módosítóinak** (HM) tizede.                                               |
| Harcmodor                                              | Az ellenfél aktuálisan használt harcmodor képzettségének szintje                                                                      |
| „Manőver ismeret – (az adott manőverre)”  <br>(ha van) | Fokonként: `+2`                                                                                                                         |
| Módosító körülmények                                   | `[-5;+5]` Tetszőleges KM által megadott +/- érték. Körülmény függő nehezítés ill. könnyítés. (Pl. eltérő fegyverméretek, bódulat, stb.) |

Ez a próbadobás nem mást fed, mint hogy a karakter képes -e megteremteni maga számára a lehetőséget, úgymond „megágyazni magának”, hogy egyáltalán megkísérelhesse a **Manővert**. A harcban ez helyezkedést, „pozícióba kerülést” jelent, amelynek sikere függ a karakter és ellenfele által aktuálisan használt harcmodor szintjétől, a **Manőver** alap nehézségétől, attól, hogy a karakter mennyire „bevállalós”, valamint az általa és ellenfele által forgatott fegyverméretektől és egyéb módosító körülményektől.

Az **Ellenpróba** dobása során a KM meghatározza a próba célszámát, a játékos, pedig ún. Manőver pontját és dob hozzá k10-el. Ha a végső érték eléri a célszámot, akkor az **Ellenpróba** **sikeres volt.**

Ha csak az **Ellenpróba** az adott Manőver követelménye, akkor annak sikere esetén az egész **Manőver** automatikusan sikeresnek tekinthető.

- Ha a körben a manőver az utolsó „támadás”, akkor rontott Végrehajtás esetén Vállalásának VÉ levonása „átcsúszik” a következő körre.

- A KM a körülményektől és szituációtól függően adhat pozitív/negatív célszám módosítót [+5;-5] értékhatáron belül. Sőt, a KM dönthet úgy, hogy a feltételei adottak, nincs szükség Ellenpróbára.


#### Vállalás

A karakter – **Ellenpróba** során – dönthet úgy, hogy `VÉ`-je egy részéért cserébe pluszokat rak Manőver pontjaira. Ez veszélyeket is rejt, hiszen így kiszolgáltatottabbá válik ellenfele támadásaival szemben.

- A Vállalás legfeljebb `+2` lehet. Minden pont `-15 VÉ`-t ideiglenes levonást okoz (`1` visszatámadás)

- Ha a Manőver sikeres, akkor az ellenfél következő visszatámadásakor már nincs levonás

<br/>

---
### Manőverek végrehajtása, képzetlenség

A manőverek végrehajtásával bárki próbálkozhat, aki az adott manővernél leírt **Végbevitel-követelményeket** teljesíti. Amennyiben nem teljesíti, akkor is nekifuthat, de az

```
... Ellenpróba dobásánál a célszám az ő számára 3-al megemelkedik.
```

### Manőverek fejlesztése, manőver-ismeretek

A manővereket „**Fejleszthető**” és „**Nem fejleszthető**” csoportokba soroljuk.(lásd lejjebb a két elkülönített fejezetet). Alkalmazásaik szabályai nem különböznek.

Egy karakter összes **nem-távolsági Harcmodor** képzettségeinek minden `3. szintje` után automatikusan kap egy-egy ún. „**Manőverfejlesztő pontot**” (MFP), amelyekből az említett „Fejleszthető” manőverekhez **Manőver-ismeret** fokokat lehet felvenni. **1 fok tanulása 1 MFP-be kerül**, továbbá a fokok tanulásának követelményeit is teljesíteni kell (lásd az adott manőverek leírásánál).

> Ha a karakter nem elégszik meg az MFP-k által felvehető manőver-ismeretek számával, akkor `15 KP`-ért vehet további fokokat, melyek később nem „válthatóak vissza” akkor sem, amikor magasabb szinten ismét lesz elkölthető MFP-je.

A **Manőver-ismeretek**, az adott **konkrét** Manőver alkalmazása esetén fokonként `+2` módosítót adnak az alkalmazó Manőver pontjaihoz az **Ellenpróba** dobásánál.

```
Manőver-ismeret fokonként +2 módosítót ad az „Ellenpróba” dobásnál
```


Ilyen ismeret lehet például a **Manőver – Gáncsolás** megtanulása, melynek bónuszát kizárólag **Gáncsolás** manőver esetén kapja meg a karakter. Az, hogy egy Manőver ismeretnek hány foka van, az az adott manőver leírásánál található meg.

<br/>

---
### Manőver lista

Az alábbiakban bemutatjuk a km100 által ismert manővereket. A KM bármikor rögtönözhet új manővert, mindössze az alábbiakat kell megtennie: meghatározni a Manőver alap nehézségét, végbevitelének követelményeit, szükséges fázisait (MEV), hatását, valamint az esetleges speciális követelményeket (képzettségpróba, stb). Amennyiben az új manőver fejleszthető, akkor az egyes tanulható fokok követelményeit is rögzíteni kell.

😑 Nem fejleszthető Manőverek\
💪 Fejleszthető Manőverek\
🤼‍♂️ Belharcos Manőverek


<br />

---
---
### 😑 Nem fejleszthető manőverek

#### 😑 Felállás földről

- Nehézség: `6`
- Fázisok: `M E`
- Végbevitel követelménye: -
- Speciális: Manőver-pontokhoz **Akrobatika** `1/3`-a hozzáadható (lefele kerekítve)
- Hatás: Sikerült harc közben a földről feltápászkodnod, folytathatod a harcot, immár levonások nélkül.

---
#### 😑 Kiegészítő támadás

 ⭕TODO⭕ KELL EZ?⭕
- Nehézség: `7`
- Fázisok: `E V`
- Végbevitel követelménye:
	- Közelharc – `4.szint`
	- Forgatott fegyverre: Mesterfegyver – `1.fok`
- Hatás: Harc közben egy támadásod helyett valamilyen csalafinta, alattomos húzást vetsz be ellenfeled ellen. Ilyen lehet például, hogy öklöddel váratlanul az arcába csapsz, vagy térden rúgod, esetleg a vállába bokszolsz, stb. Ennek a támadásodnak a sebzése `k20+1`. (Természetesen az esetleges „kiegészítők”, mint *vaskesztyű*, *szegecsek* és az **Erőbónusz** szintén beleszámítanak a sebzésbe.) Ha a sebzés legalább `5`, akkor a fentieken kívül ellenfeled elveszíti következő támadását.

---
#### 😑 Öklelés

- Nehézség: `⭕?⭕`
- Fázisok: `⭕M⭕  E V`
- Végbevitel követelménye:
	-  ⭕TODO⭕
- Hatás: ⭕TODO⭕

---
#### 😑 Pajzzsal öklelés

- Nehézség: `7` ± **Erő** különbség + (Ellenfél minden **Pajzshasználat** foka után `+2` (ha használ épp pajzsot ő is))
- Fázisok: `E V`
- Végbevitel követelménye:
	- Pajzshasználat – `2.fok`
	- Nagy és Közepes pajzzsal lehet csak
- Hatás: Pajzsoddal sikeresen feldöntötted ellenfeled, aki ettől kezdve (míg fel nem képes állni) a „**Harc földön fekve**” helyzet módosítóival harcol.

<br/>

---
---
### 💪  Fejleszthető manőverek

```
+2 Manőver Pont jár tanult fokonként
```

Az alábbiakban Manőverfejlesztő Pontokból (`MFP`) fejleszthető Manőverek listáját találhatjuk.

#### 💪 Belharcba kerülés

- Nehézség: `9`
- Fázisok: `M E`
- Max fok: `2`
- Végbevitel követelménye:
	- Belharcos fegyver használata
	- **Közelharc** harcmodor
- &#8291;1. fok követelmény: **Belharc** fortély - `1.fok`
- &#8291;2. fok követelmény: **Belharc** fortély - `1.fok`
- Speciális:
	- `4`-el túldobott célszám esetén (Ellenpróbánál) sebző **Megakasztás** támadást elszenvedve is bekerülhet a karakter.
	- Ellenfél háttal áll: célszámra: `-4`
	- A fegyver-méretek eltérése is kiemelten érvényesül!!
	  ⭕TODO: mennyi legyen kategóriánként?)⭕
- Hatás: Sikeresen bekerültél belharcba, megkapod a Belharci szituációnál leírt módosítókat.
- Kijövetel: Sikeres [Kibontakozás/Átsiklás](#%EF%B8%8Fkibontakoz%C3%A1s%C3%A1tsikl%C3%A1s) manőver. Lásd ott.
- Megjegyezés: Ha az ellenfél úgy dönt, hogy szándékosan beengedi belharcba a karaktert, akkor nincs szükség a Manőverre, dobás nélkül megtörténik a bekerülés, amelyet kezdeményezés követ, majd a harc – immár a Belharc szabályainak megfelelően.

---
#### 💪 Belharcból kibontakozás

Lásd: [Kibontakozás/Átsiklás](#%EF%B8%8Fkibontakozásátsiklás) manőver.

---
#### 💪🤼‍♂️ Gáncsolás / Lábsöprés (lábbal)
- Nehézség: `8/5`
- Fázisok: `E V`
- Max fok: `1`
- Végbevitel követelménye: -
- **1. fok** követelmény: Közelharc - `5.szint`, Aktuális harcmodor: - `5.szint`
- Speciális:
	- Belharci szituációban a nehézség csak `5`
	- Súlyos ellenfélnél: opcionális **Erőpróba** (KM dönt). Gondoljunk a nagy, páncélos ellenfelekre!
	- Csak kétlábú ellenfelek ellen alkalmazható, több lábbal rendelkező ellenfélnél **Ökleléssel** kell próbálkoznod.
- Hatás: Sikeresen kikaszáltad ellenfeled lábát, aki a földre zuhan. Felállnia csak sikeres „**Felállás földről**” manőver alkalmazásával sikerülhet. A továbbiakban a **Harc földön fekve** módosítói vonatkoznak rá.

---
#### 💪Kibontakozás/Átsiklás

- Nehézség: `5` ± `2`  (`1` penge különbségenként)
- Fázisok: `E M`
	- Ez speciális manőver, mert itt először dobjuk az Ellenpróbát, csak aztán a Megakasztás(oka)t.
	- A **Megakasztás** kreatív figyelemeltereléssel kiváltható/megúszható, de a KM ne legyen vajszívű!
- Max fok: `2`
- **1.fok** követelménye: `Ügyesség: 0`
- **2.fok** követelménye: `Ügyesség: +1`
- Végbevitel követelménye: -
- Speciális:
	- A harcolók fegyver-méret különbsége számít! Penge különbségenként `2`-vel csökken/nő a **Nehézség**.
	- Ha Ellenpróbánál a dobás `2`-vel meghaladja a célszámot, akkor egy ellenfél nem jogosult **Megakasztásra**. Ez további `+2`-enként további egy ellenfélre igaz.
	- Kibontakozásnál nem folytatható Védekező harc, de **Védő taktika** igen.
- Hatás: Sikerül a harcból kibontakoznod, ellenfele(i)d már nem támadhat(nak) rád. Most jön a futás... Ha üldöznek, akkor támadóddal **Gyorsaság** ellenpróbát kell dobnotok, amelyet, ha te nyertél, akkor kereket oldottál, ha viszont az üldöződ nyerte, akkor utolért és leadhat rád egy támadást hátulról (`+10 TÉ`), amely ellen puszta kezes harcértékeiddel védekezhetsz.
- Több támadó:
	- A célszámba a legmagasabb ellenfél-harcmodor-szint számít be
	- Minden további ellenfél után `+2` járul a célszámhoz.
	- A fegyverméret kategória különbségnél is a legnagyobb fegyverű ellenfél fegyveréhez kell viszonyítani.
- Kibontakozás belharcból:
	- Ugyanúgy dobandó, mint ha harcból akarnánk kibontakozni.
	- Ha az ellenfélnek Belharc fortélya van, akkor fokonként `+2`-vel nő a nehézség Ellenpróbánál
	- Ha az alkalmazónak Belharc fortélya van, akkor dobására fokonként `+2` pontot kap Ellenpróbánál
	
```diff
-   TODO
-   1. Ha belharci szituációban a belharcos sebesülést szenved és elrontja fájdalomtűrés próbáját
-   (már nincs Fájdalomtűrés dobás sebesüléskor,... de itt esetleg dobhatunk...), akkor
-   ellenfele – ha akarja – automatikusan megszüntetheti a belharci szituációt,
-   kibontakozhat belőle.
-
-   2. Sérülést bevállalva mindenképpen kijönni hogy lehessen?
```

---
#### 💪Lábkirántás (szálfegyverrel)

- Nehézség: `6`
- Fázisok: `E V`
- Max fok: `1`
- **1.fok** követelménye: Lándzsavívás – `6.szint`
- Végbevitel követelménye: szálfegyver használata
- Speciális:
	- Kifejezetten lábkirántásra alkalmas fegyverre: `+2` Manőver Pont
	- Súlyos ellenfélnél: opcionális Erőpróba (KM dönt). Gondoljunk a nagy, páncélos ellenfelekre! Ez a tényező kevésbé hangsúlyos, mint a sima **Gáncsolásnál**.
	- Csak kétlábú ellenfelek ellen alkalmazható, több lábbal rendelkező ellenfélnél **Ökleléssel** kell próbálkoznod.
- Hatás: Sikeresen kihúztad szálfegyvereddel ellenfeled lábát, aki a földre zuhan. Felállnia csak sikeres „**Felállás földről**” manőver alkalmazásával sikerülhet. A továbbiakban a **Harc földön fekve** módosítói vonatkoznak rá.

---
#### 💪Lánccsapda  (láncos fegyverekre)

- Nehézség: `9`
- Fázisok: `E V`
- Max fok: `2`
- **1.fok követelménye**: Kétkezes harc – `2.fok`, Láncos fegyverre: Mesterfegyver fortély – `1.fok`
- **2.fok követelménye**: Kétkezes harc – `2.fok`, Láncos fegyverre: Mesterfegyver fortély – `2.fok`
- Végbevitel követelménye:
	-  a balkezes fegyvernek láncnak, vagy lánccal felszereltnek kell lennie
	- az alkalmazó kétkezes harcot folytat
	- az ellenfél fegyvere csak egykezes lehet
- Hatás: Jobbkezes fegyvereddel elvezeted, bal kezedben tartott láncos fegyvereddel pedig foglyul ejted ellenfeled pengéjét, vagy fegyvertartó kezét, melyet a továbbiakban nem tud használni, amíg ki nem szabadítja azt. Amennyiben ellenfeled `0,5` pengénél nagyobb fegyvert forgat, dönthet:
	- elengedi a fegyvert, mellyel gyakorlatilag sikeres lefegyverzéssé változik a manőver
	- továbbra is kezében tartja
	  (`0,5` pengénél kisebb fegyver tartása esetén kötelezően kézben marad). Ha kézben tartja, akkor az ellenfelet **Harc helyhez kötve** módosítói sújtják, elveszít minden bónuszt az adott fegyverre (Mf, stb), kétkezes harc esetén a továbbiakban a másik kezében tartott fegyver harcértékeivel küzd. Ha másik keze üres, akkor sújtják a **Harc puszta kézzel** fejezetben leírt levonások is, melyek minden pusztakezes harcosra vonatkoznak.
- Hatás 2: a foglyul ejtett fegyverre a Lefegyverezés manőver csak `5`-ös nehézségű


---
#### 💪Lefegyverzés / Fegyvertörés - egy konkrét harcmodorra

Ha meg akarod fosztani ellenfeledet fegyverétől, vagy kiütve kezéből, vagy annak eltörésével, akkor lefegyverezés manővert kell alkalmaznod.

- Nehézség: `10`
- Fázisok: `E V`
- Max fok: `3`
- **1.fok követelménye**: Harcmodor képzettség – `5.szint`
  Ha bármely más harcmodorban eléri az 5.szintet, akkor onnantól kezdve abban a harcmodorban is jár a bónusz, nem szükséges újra pontot költeni a manőverre.
- **2.fok követelménye**: 1.fok megléte, Harcmodor képzettség – `7.szint` és  Mesterfegyver fortély (választott fegyver) – `1.fok`
  Amint egy újabb fegyverre felveszed a Mesterfegyver fortélyt (az adott harcmodorra) legalább `1.fokon`, akkor onnan kezdve arra is tudod használni a `2.fokú` lefegyverzést.
- **3.fok**: Követelmény: 2.fok megléte, Harcmodor képzettség – `9.szint` és Mesterfegyver fortély (választott fegyver) – `2.fok`
- **Plusz módosító**: a használt fegyver mennyire alkalmas a másik fegyver elvételére. A KM dönt: `[-2;+4]` (Kétkezes harc sok esetben megkönnyíti a lefegyverzést)
- Végbevitel követelménye: -
- **Speciális**:
  - fából készült **szálfegyverek** törése alapból `2`-vel kisebb Nehézségű (`8`)
  - Hogy fegyvercsellel, végtagsebzéssel, vagy fegyvertöréssel fosztja meg ellenfelét a karakter, arról a KM dönt és az esetleges módosítókat is ő határozza meg.
  - Karmok és szarvak ellen nem használható a Manőver, ott **Csonkolás** szükséges
- Hatás: A lefegyverzés sikeres. Ellenfeled kezéből kihullik a fegyver, vagy eltörik.

---
#### 💪Lefejelés
⭕Belharcot előbb!⭕

- Nehézség: `8/5`
- Fázisok: `E V`
- Max fok: `1`
- Végbevitel követelménye:
	-  xyz
- Speciális:
	- Belharcban a nehézség csak 5
	- Nem szükséges Belharc fortély
	- ⭕Ellenfél képzett belharcos: lásd leírás⭕
	- ⭕TODO: állatoknak általában van Belharcuk! (KM dönt)⭕
- Hatás: Arcon fejelted áldozatodat.

---
#### 💪Mesterjel

- Nehézség: `10+12`🍁
- Fázisok: `E V`
- Max fok: `2`
- **1.fok követelmény**: Mesterfegyver – `2.fok`
- **2.fok követelmény**: Mesterfegyver – `3.fok`
- Speciális követelmény: A használt fegyver csak valamilyen (legfeljebb 1 penge hosszú) hegyes szúrófegyver lehet
- Végbevitel követelménye: -
- Hatás: Sikeres manőver esetén képes vagy mesterjeledet belekarcolni ellenfeled ruhájába/bőrébe. 🍁A nehézség a jel bonyolultságától függ.


---
#### 💪Pajzsrongálás

Szándékosan rongálod ellenfeled pajzsát, csökkentve annak Védő Értékét.

- Nehézség: `6`
- Fázisok: `E V`
- Max fok: `1`
- **1. fok követelménye**: Aktuális harcmodor - `6.szint`, `Erő: +1`
- Végbevitel követelménye: Aktuális harcmodor - `4.szint`
- Speciális: Ez ellen a manőver ellen nem számít a pajzs adta Védő Érték!
- Hatás: Sebzést dobsz. Zúzó- és kétkezes fegyverek sebzése (SP) `1:1`-ben csökkenti ellenfeled pajzsának **Védő Értékét** (véglegesen).

---
#### 💪Páncélszúrás

- Nehézség: `Lásd a leírást`
- Fázisok: `E V`
- Max fok: `2`
- **1. fok követelménye**: Aktuális harcmodor - `6.szint`
- **2. fok követelménye**: Aktuális harcmodor - `9.szint`
- Nehézség: vért lefedésétől függ %-ban: `1-10` (példa: Mellvért: `5`, teljes vért: `10`)
- 
- Végbevitel követelménye:
	-  Erre alkalmas fegyver (KM dönt), melynek pengéje befér az ellenfél páncéljának illesztékei közé
	- Csak **Közelharc** vagy **Kardvívás** harcmodorban használható
- Hatás: Képes vagy megtalálni ellenfeled páncélján a rést, ahol megkerülheted a vért adta védelmet. Ha fegyvereddel be tudtál szúrni az illesztékek között (a manőver sikerült), akkor dobj rendes sebzést, mely ellen áldozatodnak csak a vértezet alatt viselt további védelmei adnak **SFÉ**-t. Ne feledjük, hogy a teljes vértezet alatt sokszor láncinget viselnek!
  Sikeres Páncélszúrás esetén az áldozat nem jogosult **Páncéldobásra**.

---
#### 💪 Területre/Pontra támadás

- Nehézség:
    - `1-9`: páncéllal nem fedett területre támadni. A célpont páncéllal való lefedettségétől függ. 60%-ban fedett áldozat esetén a **Nehézség**: `6`, 90%-nál `9` , és így tovább.
    - `8`: egy adott végtagra támadni
    - `10`: egy adott (nagy érme méretű) pontra támadás
        - Csak Szúrófegyverrel
        - [Harci Anatómia](fortelyok.harci/harci_anatomia.md) harci fortély **SP bónusza** csak itt használható - ha vértmentes pont a cél.
        - [Kínokozás](fortelyok.harci/kinokozas.md) harci fortély **Fájdalomtűrés hatása** csak itt használható - ha vértmentes pont a cél.
    - `12`: Szemkiszúrás
- Fázisok: `E V`
- Max fok: `2`
- **1. fok követelménye**: Aktuális harcmodor - `6.szint`
- **2. fok követelménye**: Aktuális harcmodor - `9.szint`
- Speciális:
	- Végrehajtás (támadás) során **nem kapja meg a +20 TÉ módosítót**! Ha az Ellepróba fázis sikeres, sima támadást dobsz aktuális harcértékeiddel.
	- Meglepetés esetén is kell **Ellenpróbát** dobni

- Hatás: Az általad kiszemelt területre sikerül leadnod a támadásod. Sebezz, ahogy szoktál, az Harci Anatómia ismerete 
-Nyakra, szemre, lágyékra és különösen sérülékeny, apró pontokra támadhatsz vele. Ha sikeres a támadás, akkor dobj rendes sebzést és hozzáadhatod a "**Harci anatómiánál**" leírt bónusz sebzéseket. Ha célod egy apró szerv, mint a szem, fül, vagy ujj kiszúrása/levágása, akkor siker esetén sebzésed **Közepes**(⭕?⭕) és megszabadítottad ellenfeledet egy fent leírt testrésztől.
- Megjegyzés: A „**Pontra támadás**” **nem** használható együtt a **Páncélszúrás** manőverrel! A testrésznek páncél által fedetlennek kell lennie.



---
#### 💪Távoltartás⭕

Nem támadsz, hanem ⭕TODO⭕

- Nehézség: `5`
- Fázisok: `M E`
- Max fok: `⭕TODO⭕`
- Végbevitel követelménye:
	-  ⭕todo⭕
- Hatás: ⭕todo⭕


---
#### 💪Terelés

- Nehézség: `8`🍁
- Fázisok: `E`
- Max fok: `1`
- **1.fok követelménye:** Aktuális harcmodor - `6.szint`
- Végbevitel követelménye: Aktuális harcmodor - ⭕`6.szint`⭕
- Speciális:
	- Alkalmazható egyszerre, csoportosan is.
	- Csoportot terelni nehezebb. Ilyenkor emelkedik a a nehézség (KM dönt).
- Nehézség🍁: Harci alakzatban használva jelentősen csökkenthetik a nehézséget. Az alakzatok jellemzőit ismerve a KM dönt `[-4;+2]`. Ez csökkenheti a végbevitel harcmodor követelményét is.
- Hatás: arra tereli az ellenfelet, amerre akarja. Hátrálásnál nem kell használni, az megy magától!

<br/>

---
---
### 🤼‍♂️ Belharcos Manőverek

#### 🤼‍♂️ Átdobás

- Nehézség: `5` + (Ellenfél minden **Belharc** foka után `+2`)
- Fázisok: `E V`
- Végbevitel követelménye:
	- Közelharc – `4 .szint`
	- Belharc – `1.fok`
	- Belharci szituáció
- Speciális: súlyos ellenfélnél opcionális **Erőpróba** (KM dönt)
- Hatás: Belharc közben fogást találsz ellenfeleden és átdobod a vállad felett. Innentől kezdve a [Harc földön fekve](060_10_harci_helyzetek.md#harc-f%C3%B6ld%C3%B6n-fekve) módosítói szerint kell számolni harcértékeit.

---
#### 🤼‍♂️ Belharcba kerülés (x)

[Lásd fenn](#%EF%B8%8Fbelharcba-ker%C3%BCl%C3%A9s).

---
#### 🤼‍♂️ Feszítés, Leszorítás / Feszítésből kijövetel

- Nehézség: `6` ± **Erő** különbség + (Ellenfél minden **Belharc** foka után `+2`)
- Fázisok: `E V`
- Végbevitel követelménye:
	- Belharci szituáció
	- Belharc – `1.fok` (kijövetelhez nem kell)
	- Közelharc – `4.szint`
	- Kijövetelhez: sikeres **Fájdalomtűrés** próba `15`-ös célszám ellen (körönként dobandó). Ha nincs meg, képtelen visszatámadni és mágiát, pszít használni
- Speciális:
	- Belharcos fegyverrel együtt is lehet alkalmazni
- Hatás:
	- Sikeresen lefeszítetted ellenfeledet, aki alig bír mozdulni / Kiszabadultál a feszítésből
	- Amíg feszítve van, addig nem tud fegyverrel támadni és `TÉ/VÉ:-25` (`KÉ`-t elveszíti automatikusan)

---
#### 🤼‍♂️💪 Gáncsolás / Lábsöprés (lábbal)

[Lásd fenn](#%EF%B8%8Fg%C3%A1ncsol%C3%A1s--l%C3%A1bs%C3%B6pr%C3%A9s-l%C3%A1bbal).

---
#### 🤼‍♂️ Kéztörés

- Nehézség:  `6` ± **Erő** különbség + (Ellenfél minden **Belharc** foka után `+2`)
- Fázisok: `E V`
- Végbevitel követelménye
	- Belharci szituáció
	- Belharc – `1.fok`
	- Közelharc – `6 .szint`
- Hatás: kitörted ellenfeled kezét, ⭕`5 ÉP`⭕ sebzés, a sérült kezét nem  használhatja harcra, amíg meg nem gyógyul.
- ⭕Páncél nehezítsen?⭕

---
#### 🤼‍♂️ Lábtörés

- Nehézség: `8` ± **Erő** különbség + (Ellenfél minden **Belharc** foka után `+2`)
- Fázisok: `E V`
- Végbevitel követelménye:
	- Belharci szituáció
	- Belharc – `⭕2⭕.fok`
- Hatás: kitörted ellenfeled lábát, ⭕`6 ÉP`⭕ sebzés

---
#### 🤼‍♂️ Leforgatás/Irányítás

- Nehézség: `8 / 4` (Lefeszített ellenfél ellen a nehézség csak `4`)
- Fázisok: `E V`
- Végbevitel követelménye:
	-  Belharci szituáció
- Hatás: Képes vagy ellenfeledet a számodra kedvező irányba forgatni/terelni miközben összeakaszkodtok. Legfeljebb `5 méternyi` távot tetethetsz meg vele.

---
#### 🤼‍♂️ Nyaktörés

- Nehézség: `9`
- Fázisok: `E V`
- Végbevitel követelménye:
	- Belharci szituáció
	- Belharc – `2.fok`
	- Harci anatóma – `1.fok`
	- ⭕TODO: páncél akadályozzon – legyen nehezebb⭕
- Hatás: Kitörted ellenfeled nyakát. Amennyiben humanoid anatómiájú egyedről van szó, 1 körön belül meghal.

<br />

---
---
### Lovas Manőverek

A lóval és ló ellen végbevihető Manőverek a [Harc lóhátról](060_15_harc_lohartol.md#lovas-man%C5%91verek) fejezetben találhatóak.

<br/>

---
### ⚡Egyszerű példa egy Manőver alkalmazására

**Rühes** külön ismeret nélkül megpróbálja lefegyverezni ellenfelét. Mindkettőjüknél hosszú kard van, Rühes kicsivel jobb vívó, és `MFP`-ből fejlesztette a **Lefegyverzés/Fegyvertörés** manővert `1.fokra`.

Rühes értékei:
- Kardvívás: `7.szint`
- KÉ: `15`
- TÉ: `55 / 45`
- VÉ: `125`
- Lefegyverzés/Fegyvertörés manőver - `1.fok`
- `HM/10`: `37/10 = 3`

Ellenfelének értékei:
- Kardvívás: `6.szint`
- `HM/10`: `32/10 = 3`
- VÉ: `115`

A Lefegyverzés manőver nehézsége: `10`\
A Lefegyverezés fázisai: sikeres Végrehajtás (`V`) és Ellenpróba (`E`) szükséges.

1. **Végrehajtás**  (`V`)
   Rühes `+20`-al leadja támadását: `55+20+k100 = 132`, ez nagyobb mint ellenfele `VÉ`-je
   → Sikeres Végrehajtás

2. Ellenpróba  (`E`)
- Tetves dobása:  `10` (kardvívás + HM/10) + `2` (Lefegyverzés:`1.fok`) + `k10`
- Célszám: `6 + 3 + 10 = 19` (ellenfél kardvívása + HM/10 + Lefegyverzés nehézsége)


```
A próbadobás így:   (12 + k10)  vs.  19
```

Tehát ha Rühes legalább  `7`-et dob  `k10`-en, akkor az **Ellenpróba** is sikeres és így az egész manőver is, ellenfele kardja kihullik annak kezéből. Látható, hogy a **Lefegyverzés** külön ismeret nélkül nem könnyű művelet.

Ha Rühes megtanulná a Lefegyverezést  `2.fokon` Manőverfejlesztő Pontjaiból ( `MFP`), akkor már `+4` járna a próbadobására ( `14+k10`) és így már `5`-ös dobással is sikert érhetne el. Ha viszont ellenfele is jártas lenne – mondjuk csak `1.fokon` – Lefegyverzésben, akkor az ő `+2` bónusza mérsékelné Rühes `+4`-es bónuszát és ismét csak a `7`-es dobással(vagy felette) lenne eredményes.

<br/>

---
### ⚡Összetettebb példa egy Manőver alkalmazására

Tetves **Gáncsolást** akar alkalmazni. Ellenfelénél kard van, nála tőr és rendelkezik „Gáncsolás” Manőver ismerettel (`1 fok`). Bejelenti, hogy ezen kívül `2 pontot` vállal (lásd [Vállalás](#v%C3%A1llal%C3%A1s)) a cél érdekében → `VÉ:-20`

Tetves értékei:
- Közelharc: `7.szint`
- KÉ: `15`
- TÉ: `55`
- VÉ: `125` ; A Vállalás miatt csak: `105`
- Manőver ismeret – Gáncsolás – `1.fok`
- `HM/10`: `37/10 = 3`

Ellenfelének értékei:
- Kardvívás: `6.szint`
- `HM/10`: `32/10 = 3`
- VÉ: `140`
- Nincs „**Gáncsolás**” Manőver ismerete

A Gáncsolás manőver nehézsége: `8` (belharcban `5` lenne, de ez most nem áll fenn)\
Gáncsolás fázisai: sikeres Végrehajtás (`V`) és Ellenpróba (`E`) szükséges.

1. Végrehajtás: Tetves leadja támadását. `55+20+k100 = 142`, ez nagyobb mint ellenfele `VÉ`-je
    → Sikeres Végrehajtás

2. Ellenpróba
- Tetves manőver pontjai: `7+3+2+2 = 14`
    (közelharc + „Gáncsolás” manőver ismeret bónusza + vállalás)

- Célszám: `8+3+6+2=19`
  (ellenfél kardvívása + HM/10 + Gáncsolás nehézsége + a fegyverméretek különbözősége miatt a KM megnöveli `2`-vel a célszámot)

```
A próbadobás így:  (14 + k10)   vs.  19
```

Tehát ha Tetves legalább `5`-öt dob `k10`-en, akkor az **Ellenpróba** (`E`) is sikeres és így az egész manőver is az, kikaszálta ellenfele lábát. Ha nem sikerült volna a manőver, akkor ellenfele következő rendes visszatámadása ellen Tetves `-20 VÉ` büntetés szenvedett volna el (a Vállalás miatt).