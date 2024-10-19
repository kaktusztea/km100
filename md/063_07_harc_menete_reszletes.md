
## A harc menete – részletes leírás

A fentiekben kifejtettük az egyes harcértékek kiszámításának módját. Most lássuk, a fentieket hogyan alkalmazza a harcos, mikor küzdelemre kerül sor.

A számolás jelentős része karakteralkotáskor történik, így a játékmenet kellően gyors marad.

---
### Harci kör

A harcot körökre osztjuk, ebben cselekedhet mindenki a kezdeményezés által meghatározott sorrendben.

Mindenki leadja támadásait, aztán ugyanebben a sorrendben a több támadással rendelkező karakterek újra - egészen addig, míg van valaki, akinek még van támadása.

---
### Akció

Lásd : [Akciók fogalma](063_02_akcio_fogalma.md#akció-fogalma).

---
### Kezdeményezés

```
Harci KÉ + k10
```

Minden kör elején van kezdeményező dobás, ami csak a cselekvési sorrend meghatározására szolgál, nem foglalja magába a harci dominanciát, a harc irányítását.

A játékosok kezdeményezéskor `k10`-el dobnak és a kapott értéket hozzáadják aktuális **Kezdeményező Értékükhöz**. Aki a magasabb eredményt kapja, az kezdi a támadást. Amennyiben a dobás `10`-es, akkor a játékos újra dobhat és az új dobását is hozzáadhatja az előző – `10`-et érő – dobásához.

Ha két karakter azonos kezdeményezést ért el, és egymással harcolnak, akkor egyszerre támadnak, csapásuk egyszerre érkezik, vagy ha a KM-nek jobban tetszik, ilyenkor összeakadhatnak a fegyverek, egymásnak feszülnek a küzdők... egymás szemébe meredve próbálják továbbgördíteni a harc menetét...


---
### Varázslás kezdeményezése

```
Varázslás KÉ + k10
```

### Speciális szituáció: Harc ÉS Varázslás egy körben

Ha olyan speciális helyzet áll elő, hogy harcolni ÉS varázsolni is szeretnél körön belül váltva, akkor:
- KÉ dobás előtt válassz: melyik KÉ értékedet használod: "Harci KÉ", vagy "Varázslás KÉ".
- Ha a magasabb értékűt választod, akkor mindenképpen az annak megfelelő típusú támadást kell először kell használnod (harc, varázslás).
- Ha mire sorra kerülsz mégis váltanál a másik támadási formára (mágia→harci; harci→mágia), akkor automatikusan átváltasz az alacsonyabb KÉ-típus értékére - ezzel vállalva, hogy rögtön hátrébb is eshetsz a sorrendben
- Viszont ha az alacsonyabb KÉ-típus értéket választod, akkor **bármelyik** támadási formát (mágia/harci) válaszhatod mikor rád kerül a sor
- Többet is támadhatsz AKKOR ha a választott KÉ-típusban már többet tudsz támadni
- Támadás/kör: a választott KÉ-típus által adott. Ha támadás típust váltasz, de azzal a típussal nem lenne meg az újabb támadás, akkor természetesen nem is kapod meg.


---
### Támadás, Védő Érték csökkentése

```
Támadó dobás = Támadó Érték + k100
```

```
Minden újabb támadás a körben
  TÉ:-10 levonással megy
  2.tám: -10 TÉ,  3.tám: -20 TÉ, ...
```

Harcban, támadáskor a játékos dob `k100`-al, majd a kapott értéket hozzáadja aktuális **Támadó Értékéhez**. Ennek értéke lesz a **Támadó dobás**. Amennyiben a támadónak több támadása van a körben, akkor minden egyes plusz támadás `TÉ:-10` módosítóval történik.

A harc, a védekezés komolyan igénybe veszik az áldozat figyelmét, állóképességét. Ha a támadás nem érte el a megtámadott **Védő Értékét** (azaz a találatot), akkor az áldozat Védő Értékére ideiglenes csökkenést szenved el. Ha a támadás eléri, vagy meghaladja a `VÉ`-t, akkor pedig sebző támadásról (**találatról**) beszélünk. Hogy harc közben a védekezőnek milyen jellemzője csökken, azt az alábbi táblázat mutatja:

| Támadó dobás eredménye | Hatás                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :--------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      **TÉ < VÉ**       | VÉ csökkentés<br/>• Alaphelyzetben (nincs előnyös-hátrányos helyzet):<br/>&nbsp;&nbsp;mindkét fél `nagykocká`-val csökkent (k100)<br/><br/>• Legalább 1 penge fegyverméret különbségnél:<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Előnyös helyzetű támadó: `nagykocka`-val csökkent (k100)<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Hátrányos helyzetű támadó: `kiskocka`val csökkent (k100)<br/><br/>• 2 penge, vagy nagyobb méretkülönbségnél:<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Előnyös helyzetű támadó:  `nagykocka+1`-el csökkent (k100)<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Hátrányos helyzetű támadó: `kiskocka`-val csökkent (k100) |
|      **TÉ >= VÉ**      | Találat → Sebzés dobás<br/>• A sebzéshez az Erőbónusz/Erőhiány és mágiából adódó bónuszok hozzáadódnak<br/>• Többszörös találat: `+20`-anként `+3 SP`  (max +9 SP)<br/>• Páncéldobás (opcionális): `k10`-el dob az áldozat<br/>• VÉ csökkentés: ÉP sebtől függő VÉ csökkenés (lásd a [Sebzés](#sebz%C3%A9s) táblázatot) (csak!)                                                                                                                                                                                                                                                                                                     |

**Megjegyzés**: a Harci anatóma ÉP bónusza csak akkor adható hozzá, ha az alap sebzés átment a páncélon! ⭕TODO: ez változhat⭕

🔆 A VÉ csökkenést kizárólag a [Harcos Elme](fortelyok.harci/harcos_elme.md) fortély tanulása képes mérsékelni.

A rendszer előnye, hogy a több támadó okozta fenyegetés sokkal fajsúlyosabb lesz, hiszen többen, sokkal gyorsabban “leverik” a karakter VÉ-jét. A támadások száma is sokat számít, részben a VÉ csökkentés szempontjából, másrészt a sokkal erősebb, több támadással rendelkező karakternek jó esélye van az első körben elintéznie gyengébb ellenfelét, még ha annak magas is a **Védő Értéke** (első egy/két támadás VÉ-t csökkent, aztán találat).

Megnő a [támadó/védő taktika](064_02_harci_taktikak.md#támadó-taktika) jelentősége is. Egy sebesült harcos ellen jó lehet a támadó **taktika**, bár megvannak a veszélyei is, váratlan vereséghez is vezethet. A harc elején pedig – ha az idő engedi – hasznos lehet a védekezést preferáló taktikát választani kivéve, ha nagyon sietős az ellenfél elintézése. A megfelelő harcmodorok kombinálása színessé, izgalmassá teszi a küzdelmet.

---
#### Találat

```
TÉ >= VÉ
```
Találatnak nevezzük azt a támadást, amelynek értéke eléri, vagy meghaladja a Védő Értékét. Ilyenkor a támadó [Sebzésdobást](#sebz%C3%A9s) tesz, a védekező pedig [Páncéldobást](#p%C3%A1nc%C3%A9ldob%C3%A1s-tal%C3%A1lat-helye).

**Figyelem**: az SP nem azonos az okozott ÉP sebbel! (lásd [Sebzés](#sebz%C3%A9s) fejezet).

#### Többszörös találat

```
TÉ >= VÉ + 20  / 40   / 60 
          +3SP / +6SP / +9SP
```

Amennyiben a találat olyan sikeres lett, hogy további `20`-al nagyobb az ellenfél Védő értékénél, akkor a támadó `+3 SP` bónuszt (nem ÉP!) kap. Ez ismétlődhet, tehát minden további `+20` után jár a `+3 SP`. Példa: `TÉ=175, VÉ=100`. Ekkor `140`-nél és `160`-nál kap bónuszt a támadó, tehát `+6 SP` extra jár sebzésére. A **Többszörös találat** által adható maximum sebzésbónusz: `+9`.

#### 00-ás (100-as) támadó dobás

```
Áldozat: SFÉ=0
Támadó: +5 SP
```

A `00`-ás (100-as) támadó dobás kiemelt jelentőséggel bír. Ez szimbolizálja a „tökéletes csapást”, mely csak rendkívül ritkán következik be. Ilyenkor nem számít az ellenfél vértjének SFÉ-je (`SFÉ=0`), a támadó pedig `+5 SP` bónuszt adhat sebzéséhez. A fentiek alól kivételt képez a Slan „Aranyharang” technika használata és az Elemi Erő aura, de ott is érvényes a `+5` sebzés. 

Fontos viszont megemlíteni, hogy amennyiben a `00`-ás dobás ellenére sem sikerült az ellenféllel szemben **Találatot** elérni, akkor az okozott sebzés kimerül a jutalomként kapott `+5` SP-ben (`1ÉP + 5 VÉ csökkentés`) SFÉ természetesen ez esetben sincs.

```
"Fárasztó taktika" alkalmazásakor
 00 dobás esetén további +5 VÉ csökkentés
 bónuszt kap a támadó.
```

#### 01-es támadó dobás (balsiker)

A `01`-es támadó dobás szintén kiemelt, de ezúttal negatív felhanggal. Ilyenkor a támadó csapása biztosan sikertelen, sőt olyan malőrt vétett, ami egyenesen nevetséges és amely hibából ellenfele előnyt kovácsolhat. Nincs általános szabály a konkrét eseményre, ilyenkor a KM dönt szituációtól függően (pl. elejti a kardot). Általában az „ítélet” egy - az ellenfél által leadott - extra támadás.

---
### Sebzés

```
SP = k20
   + Fegyver-sebzés
   + módosítók
   + bónuszok
   – (aktuális SFÉ)

Módosítók:
   - Mesterfegyver fortély
   - Erőbónusz
   - Támadás erőből fortély

Bónuszok:
   - Többszörös találat
   - Roham

SFÉ: páncéltól, támadási típustól 
     és a fegyver Átütésétől függ
```

| **SP** | **ÉP Sebzés** | **VÉ csökkentés** |
| :----: | :-----------: | :---------------: |
| ...-0  |     0 ÉP      |      -10 VÉ       |
|  1-5   |     1 ÉP      |      -10 VÉ       |
|  6-10  |     3 ÉP      |      -10 VÉ       |
| 11-15  |     6 ÉP      |      -15 VÉ       |
| 16-20  |     10 ÉP     |      -20 VÉ       |
| 21-25  |     15 ÉP     |      -30 VÉ       |
| 26-30  |     21 ÉP     |      -40 VÉ       |
| 31-35  |     28 ÉP     |      -50 VÉ       |
| 36-40  |     36 ÉP     |      -60 VÉ       |
| 41-45  |     45 ÉP     |      -70 VÉ       |
| 46-50  |     55 ÉP     |      -80 VÉ       |

```
Az 1-es dobás (k20):
  mindig 1 ÉP seb
  (bónuszoktól függetlenül)

(amennyiben az SP dobás
átment a páncél SFÉ-n)
```

Amennyiben a korábban leírt módon sikeres [Találatot](063_07_harc_menete_reszletes.md#tal%C3%A1lat) értünk el, akkor ezt követően **Sebző Dobást** tehetünk `k20`-al, melyhez hozzáadódik a fegyver sebzése, a [Mesterfegyver](fortelyok.harci/mesterfegyver.md) fortélyból és az [Erőbónuszból](#er%C5%91b%C3%B3nusz-%C3%A9s-er%C5%91hi%C3%A1ny) adódó módosítók, valamint a [Többszörös találatból](#t%C3%B6bbsz%C3%B6r%C3%B6s-tal%C3%A1lat), [Rohamból](064_02_harci_taktikak.md#harci-taktikák) és egyes fortélyokból (pl. [Támadás Erőből](fortelyok.harci/tamadas_erobol.md)) adódó extra értékek. Az így kapott `SP` értéket bemondja a támadó a támadás típusával együtt (pl. Szúrás).

A védő levonja a számból a támadás típusának (pl. szúrás) megfelelő `SFÉ` értékét (pl. szúrás elleni), amely a vértjénél szerepel. A kapott, csökkentett `SP` értékhez rendelt `ÉP` értéket (lásd **ÉP Sebzés** oszlopot) levonja aktuális Életerő Pontjai számából, a `VÉ` csökkenést pedig aktuális **Védő Értékéből**.

Sebzés esetén nincs kis/nagykocka `VÉ` csökkentés, csak a táblázatban levő érték!

Ha az `SP` érték a páncél `SFÉ` levonása után `0`-ra csökken, a VÉ csökkentés akkor is fixen `-10`.

---
#### Harcérték csökkenés

Ha valakit találat ért és átkerül másik sebesülés-kategóriába, `TÉ levonást` kap, melyet mérsékel a [Fájdalomtűrés képzettség](kepzettsegek.fizikai/fajdalomtures.md) és [Önuralom tulajdonságok](014_tulajdonsagok.md#-önuralom-%EF%B8%8F) összege.

Bővebben lásd: [Fájdalomtűrés fejezetet](061_03_sebesules.md#f%C3%A1jdalomt%C5%B1r%C3%A9s-harc-k%C3%B6zben)!

Ez azért előnyös, mert megint csak karakteralkotás időben számítjuk ki a fenti értékeket.

---
#### Támadás jellege, páncél SFÉ

```
Szúró, Vágó és Zúzó támadás
```

Támadáskor fontos momentum annak jellegének meghatározása, valamint az ellenfél vértjének aktuális **Sebzés Felfogó Értéke**, az **SFÉ**, amely mérsékelheti a sebesülést. Ez utóbbi (SFÉ) nem állandó érték, pont a támadás jellegétől és a fegyver esetleges átütéséből adódik.

A harcban használt fegyverek igen sokszínűek, a **km100** rendszere különbséget tesz az általuk leadott támadás jellege szerint: **szúró, vágó és zúzó** támadás.

Egyes fegyverek többféle támadási formát is lehetővé tesznek, gondoljunk csak a jól ismert hosszú kardra, amellyel szúrni is, vágni is lehet.

---
#### Elsődleges támadási típus

```
TÉ:-10 - másodlagos támadási típussal
TÉ:-20 - alkalmatlan támadási típussal

Jelölése "/" jellel: például "V/S"
V: Vágás;  S: Szúrás;  Z: Zúzás
```

Majdnem minden fegyver rendelkezik egy **elsődleges támadási (sebzési) típussal**, pl. szúrás. Ha emellett más típusú támadásra is alkalmas, az legtöbbször másodlagos lehet (kivételeket lásd lejjebb az "Egyenjogú támadási típus" bekezdésben). Ha a karakter nem jelenti be, hogy milyen típusú támadást akar leadni, akkor mindig az elsődleges támadás típust vesszük megtörténtnek. Például a hosszú kard: vágás/szúrás (V/S). Ekkor az alapértelmezett támadási típus a vágás. Ha a karakter bejelenti, hogy szúrni szeretne, akkor azt `TÉ:-10` módosítóval teheti meg. Ha pedig zúzni szeretne (amire a fegyver alkalmatlan), akkor – ha a KM engedi – azt `TÉ-20`-vel teheti meg.

A Harcrendszer végén található **Fegyvertáblázatban** minden fegyver támadási típusa megtalálható.

---
#### Egyenjogú támadási típus

```
Jelölése "+" jel: például "S+V"

Nincs levonás egyik támadás típusnál sem
```

Egyes fegyverekkel többféle támadási típust lehet használni anélkül, hogy a forgató hátrányba kerülne és levonást szenvedne el a TÉ-ből. Ilyen fegyvereknél az egyes támadási típusokat "+" jellel választjuk el.

---
#### Átütés

```
Aktuális SFÉ = Vért SFÉ - Átütés
```

Fontos szerep jut még azoknak a fegyvereknek, amelyek rendelkeznek Átütés értékkel (a legtöbb fegyver `Átütés értéke: 0`), mivel a támadott vért megfelelő SFÉ-jének kiválasztása után annak értékéből még le kell vonni az **Átütést** is, így kapjuk meg a vért végleges aktuális SFÉ-jét. Átütéssel olyan fegyverek rendelkeznek, amelyek kifejezetten alkalmasak vértek átlyukasztására legtöbbször azon okból, hogy kis területre koncentrálnak nagy erőt.\
Például: csákány...

---
#### Páncéldobás (találat helye)

```
k10 (x10)   vs.  fedett terület %
```
Természetesen nem mindegy, hogy egy támadás hol találta el az ellenfelet, hiszen lehet, az adott testrészt nem fedi vért (`SFÉ: 0`). Ha a KM úgy határoz, hogy az ő partijánál ezt is kidobják harc közben, akkor a találati hely megállapítására az áldozat Páncéldobást tesz `k10`-el, amely egy kvázi százalékdobás. Attól függően, hogy a páncél mekkora területet fed le (hány %-ot), egyre nagyobb esélye van, hogy oda kapott be találatot, ahol testét óvja a vért. Ha a védett érték alá, vagy egyenlőt dob, olyankor számít az SFÉ. Pl. egy mellvértet visel, ami `50%`-ban fed, olyankor ha `1-5`-ig dob, akkor szerencséje volt, páncélt talált a csapás.

⚡ Például Tetves olyan bőrből készült vértet visel, amely csak a torzóját védi. Ez `50%`-ban fed, tehát ha` 1-5`-ig dob `k10`-en, akkor szerencséje volt, és aktív az SFÉ, ha e fölé, akkor SFÉ-je `0`-nak számít. Ha Tetves felvesz egy sisakot (`+10%`), akkor már `60%` az esélye, hogy védett pontot talált el ellenfele.

---
#### Erőbónusz és Erőhiány

```
Az Erő tulajdonság 1:1-ben
hozzáadódik az SP értékhez.

Ha értéke negatív, akkor 
értelemszerűen levonódik belőle.
```

Egyes fegyverek forgatása esetén a karakter fizikai ereje megnöveli az okozott sebzés. Tipikusan azok a fegyverek ezek, amelyek használata során a plusz erő használata felgyorsítja azt, jól kivezethető ívű csapások végezhetők vele. Továbbá számos fegyver van, melynek forgatása Erő követelményhez kötött, azaz csak megfelelő fizikumú karakter használhatja. Erről az egyes fegyverek egyéni leírásában találhatunk részleteket, de általánosságban a fenti szabályok az irányadóak.

---
#### Élőholtak sebzése

```
Élőholt VÉ visszaáll
minden kör elején
```

Mivel nem fáradnak szellemileg, legfeljebb ideiglenes hátrányos harci pozícióba kerülnek, ezért az élőholtak VÉ-je **minden** kör elején visszaáll eredeti értékére. Ezen kívül a különböző támadási módok ellen különféleképpen ellenállóak, azok sebzése a következőképpen alakul:

- Szúrófegyverek sebzése: negyed SP sebzés (lefele kerekítve) + nincs Erőbónusz
- Vágófegyverek sebzése: fele SP sebzés (lefele) + van Erőbónusz. Csonkoláskor normál sebzés.
- Zúzófegyverek sebzése: rendes sebzés + Erőbónusz

---
### Vérzés

A súlyos sebek intenzíven vérezhetnek. A szúrt, vágott, zúzott sebek mind máshogy.

Abban, hogy a karakter aktuális sebesülési állapotában milyen ütemben veszít folyamatosan újabb Életerő Pontokat, az a szituációtól és így gyakorlatilag a KM szavától függ.

---
### Védő Érték regenerálódása

A karakternek minimum `1 kör`, zavartalan, ellazult, nyugodt testi ÉS szellemi pihenésre van szüksége, hogy visszanyerje Védő Értékét.

Ha például üldözik és ő megbújik egy kis beugróban, akkor Védő Értéke NEM regenerálódik, mert bármikor rajtaüthetnek, nem engedhet ki, figyelme továbbra is ki van hegyezve.

**Győzelmi szabály**: Ha a karakter végzett egy nagyjából hasonló tudású, vagy erősebb ellenfelével (úgy hiszi, legyőzte), akkor **Védő Értékéhez** visszatér `+10 pont` (a siker hatása a szervezetre + heroizmus).

---
### Zuhanás, megégés, zúzódás, varázslatok sebzése

⭕TODO: [Irányelvek kidolgozása](https://github.com/kaktusztea/km100/wiki/TODO.ISSUE.harcrendszer#nem-harci-sebz%C5%91d%C3%A9sek)

Természetesen nem csak fegyverek okozhatnak sérülést, hanem egy mágikus tűzgolyó, zuhanás a tetőről, stb. A mágikus hatások sebzéseit a [Mágia](090_magiarendszer.md) fejezetben tárgyaljuk, bővebben lásd ott.

Zuhanás, zúzódás, egyéb fizikai sérülések esetén a KM meghatároz egy sebzés értéket ugyanúgy, akár egy fegyver esetében. Pl. `K20+5`. Az **SFÉ** ilyen esetekben legtöbbször nem számít, vagy csak igen mérsékelten. Ha számít, akkor általában a **zúzó SFÉ** értéket használjuk, de KM dönt, mivel ahány eset annyiféle.

---

### Példák sebzésre

```diff
- TODO: Egy harmadik,
- páncélos példa (páncéldobással!)
```


⚡Példa 1

- Tetves Edzettsége: `+2` → így `16 ÉP`-je van
- Ősi ellenfele (Rühes) hosszú karddal (`SP: +3`) támad rá. Eltalálja, sebez.
- Rühes dob: `k20+4` (hosszú kard)
- `7`-et dob, így az eredmény: `7+4=11`
- A `11 SP` seb-kategóriájához `6 ÉP` veszteség tartozik
- Tetves levon `6 ÉP`-t `16 ÉP`-jéből, marad `10 ÉP`-je.

⚡Példa 2

- Cobaq Ereje: `+5`, Kétkezes kardot (`+8`) forgat
- Így sebzésdobása: `k20+13`, tehát minimum `14 SP`-t sebez, ami már `6 ÉP`.
- Ha `7`-nél nagyobbat dob (`65%`), akkor már `15 ÉP` sebet okoz, ami sokszor már halálos

---
