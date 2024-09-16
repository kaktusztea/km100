# Távolsági harcrendszer

⚜️ [Nyitóoldal](start.md)

→ [TODO/ISSUE távharc](https://github.com/kaktusztea/km100/wiki/TODO.ISSUE.tavharc)

A távolsági lő- és hajítófegyverekkel végzett harc során a támadott fél nem saját Védő Értékével vesz részt a harcban, hanem ugyanolyan “céltárgynak” minősül, mint egy szalmabábú, vagy egy agyaggalamb. 
Ugyanakkor az alábbiak befolyásolják a találat esélyeit:

- Támadó Célzó Értéke
- Használt fegyver
- Célpont Távolsága
- Célpont Mozgásának jellege
- Célpont Mérete
- Célpont Láthatósága, sötétben hangossága
- Látási viszonyok
- Szél hatása
- Egyéb körülmények, fortély módosítók

Lásd még: [Szándékos kitérés lövés elől](070_tavolsagi_harc.md#sz%C3%A1nd%C3%A9kos-kit%C3%A9r%C3%A9s-l%C3%B6v%C3%A9s-el%C5%91l) fejezetet. 

---
## Távolsági harcmodor képzettségek

- Hajítás
- Íjászat
- Lövészet
- Ostromlövészet
- Mágikus lövészet

<br />

---
## Célzó Érték kiszámolása

Mikor a támadó lövést, vagy hajítást végez, a Célzó Értékét állítja szembe a célpont távolsági Védő Értékével. A Célzó Érték kiszámolása a következőképpen történik - még karakteralkotási időben.

```
Támadó CÉ = -30 + CM + Harcmodor CÉ + (2 x Önuralom/Erő) + Fegyver CÉ + Mf-bónusz
```


Alapból mindenki konstans `-30`-as értékkel kezd, amihez hozzájönnek a **Célzó Harcérték** módosítók (`CM`), majd a karakter ⚪**Önuralom** VAGY ⚪**Erő** Tulajdonsága kétszerese ([fegyvertől függ](#er%C5%91b%C5%91l--%C3%BCgyess%C3%A9gb%C5%91l-forgatott-fegyverek)), utána a fegyver egyedi CÉ-je és az esetlegesen, az adott fegyverre felvett **Mesterfegyver** fortélyból adódó bónusz (`CÉ:+3/fok`).

Bővebben:

|     **Összeadandó értékek**     | **Leírás**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :-----------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              `-30`              | Konstans. Ez az érték gyakorlatilag a célpont Védő Érték alapját adná, de mivel itt csak 1x (karakteralkotáskor) kell vele számolni, ezért a számolás meggyorsítása miatt átkerült ide.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|               CM                | Célzóérték Módosító. Szintenként legfeljebb `4` vehető fel. `1 CM = 2 KP`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|          Harcmodor CÉ           | Harcmodor képzettség szintje által kapott bónusz (lásd a [Harcmodor képzettségeket](062_02_harcmodor_kepzettsegek.md#harcmodor-képzettségek)!)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `2x` Önuralom<br>/<br> `2x` Erő | Az Önuralom vagy Erő kétszerese ([fegyvertől függ](#er%C5%91b%C5%91l--%C3%BCgyess%C3%A9gb%C5%91l-forgatott-fegyverek))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Fegyver CÉ<br>(kategória függő) | Különbséget teszünk a fegyverkategóriák közt attól függően, hogy alapesetben milyen könnyű velük célba találni. Az alábbi értékek csak irányszámok, a konkrét fegyver értékek ettől eltérhetnek.<br> • Hajító szálfegyverek: `CÉ:+0`<br> • Apró hajítófegyverek: `CÉ:+4`<br> • Íjak: `CÉ:+10`<br> • Nyílpuskák: `CÉ:+16`<br> (A fentiek irányadó számok, egyes speciális fegyverek ezen értéke eltérhet ettől. Lásd a [Távolsági fegyverek harcértékei](067_fegyverek.md#hajítófegyverek-harcértékei) fejezetet!)                                                                                                                                                                                                           |
|               Mf                | Mesterfegyver fortély után járó bónusz, amennyiben a használt fegyverre felvette a karakter. Fokonként `CÉ:+3` bónusz.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|             Célzás              | `CÉ:+10` módosító 1 célzással eltöltött kör után (nem additív)<br>`CÉ:⭕+20` [Képzett célzás](fortelyok.harci/kepzett_celzas.md) fortély megléte esetén. <br> 🔆Figyelem: íjnál csak 1 körig lehet kitartani!! 1 kör után nem jár bónusz és körönként `CÉ:-10` büntetés!                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|              Egyéb              | • Képzetlenségből adódó levonás: `CÉ:-40`<br>• Hirtelen lövés: `CÉ:-30`<br> • Az egyes [Fortélyokból](#fort%C3%A9lyok---t%C3%A1vols%C3%A1gi-harc) adódó bónuszok.<br><br> • Nem “belőtt” lőfegyver: `CÉ-30` (íjak) / `CÉ:-15` (nyílpuskák)<br> Ha a támadó most lő először a fegyverrel, akkor íjak esetében `CÉ:-30`, nyílpuskák használatánál pedig `CÉ:-15` módosító sújtja. Ha legalább fél órát töltött el a “belövéssel”, ez a módosító megszűnik. Egyébiránt a használat során folyamatosan tűnik el a hátrány (negyed óra után már csak `CÉ:-15` / `CÉ:-8` és így tovább).<br><br>• Álló cél "belövése" (gyakorlás) min. negyed órán át: `+10-30 CÉ` <br>• A fegyverek minősége befolyásolhatja azok Célzó értéket. |

<br />

---
## (Célzott) Támadó dobás

```
CÉ + k100
```

<br />

---
## Célpont Védő Értékének kiszámolása

A célpont Védő értéke reprezentálja a célpont eltalálásának nehézségét. Ugyanolyan célszámként viselkedik, mint a rendes Védő érték, azaz, ha a lövést/hajítást végző karakter Célzó Értékkel együtt számított Támadó dobása eléri, vagy meghaladja ezen értéket, akkor találatról beszélünk. Amennyiben az érték alatta marad, a támadás célt téveszt.

A célpont **Védő Értékét**  az ún. Szorzó és a Cellaszám szorzataként kapjuk meg.

```
Célpont VÉ = Szorzó  x  Cellaszám
```

\-

| **Szorzó** |                     | Univerzális szorzó, mely az alábbi módosítók összegéből (❗) áll                                   |
| ---------- | ------------------- | ------------------------------------------------------------------------------------------------- |
|            | Mozgás módosító     | A célpont mozgásának jellegéből adódó alap szorzó                                                 |
|            | Méret módosító      | A célpont méretéből adódó módosító                                                                |
|            | Láthatóság módosító | A célpont láthatóságától és sötétben való zajosságától függő módosító                             |
|            | Egyéb módosítók     | Lővész mozgása,<br /> Szél hatása\*, Szürkület\*, Célpont zajossága* (sötétben)<br />\*Opcionális |

\-

**Cellaszám**
A célpont Távolságának és a fegyver Osztójának hányadosa felfelé kerekítve.

$$ Cellaszám = {cél\ távolsága\ (m) \over fegyver\ Osztó} → felfelé\ kerekítve $$

\-

**Fegyver osztó**
```
Nem hajítós tárgyak   - 1
Apró hajítófegyverek  - 2
Íjak                  - 3
Nyílpuskák            - 4
```

---

Az alábbiakban kifejtjük a fenti **Szorzó** táblázatban foglalt egyes értékek jelentését.

<br />

---
### Szorzó

A Szorzó a célpont Védő értékének kiszámolásában játszik szerepet. Az alábbi módosítók **összege** adja meg értékét:

- Mozgás módosító (a célpont és a lövész mozgása is számít)
- Méret módosító
- Láthatóság módosító (zajossággal együtt)
- Fényviszonyok
- Szél ereje

---
#### Szorzó - Mozgás módosító

Ha a célpont mozog, jóval nehezebb eltalálni. A távolság növekedésével ez a nehézség nem lineárisan, hanem exponenciálisan nő, éppen ezért érthető, hogy a mozgás is a Távolsági szorzó része. Alább az egyes mozgás típusokhoz tartozó módosítókat olvashatjuk.


| Célpont mozgásának jellege | Módosító | Megjegyzés                                                                                                                                                                      |
| :------------------------: | :------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|            Álló            |   `3x`   | A célpont mozdulatlan                                                                                                                                                           |
|     Lassú, egyenletes      |   `5x`   | Lassú séta, léptetés lovon.<br><br>⭕Többen harcolnak, bármelyik fél eltalálása jó. (Közéjük lövés)⭕<br><br>⭕(Vagy: 3x (álló), méret bónusz (-1/2x). Aztán k6, h kit talált el)⭕ |
|     Gyors, egyenletes      |   `8x`   | Egyenletesen futó ember, vágtató lovas                                                                                                                                          |
|      Kiszámíthatatlan      |  `15x`   | A célpont ugrál össze-vissza, cikk-cakkban fut.                                                                                                                                 |
|      Harcoló célpont       |  `20x`   | Csak egy konkrét harcoló fél eltalálása jó.                                                                                                                                     |

Természetesen a lövést végző személy mozgása is befolyásolja a találati esélyeket, hiszen könnyebb állva célozni, mint mondjuk futásból. A lövész mozgása az alábbiak szerint módosíthatja a **Szorzót**:

| Lövész mozgása                     | Módosító | Megjegyzés |
| ---------------------------------- | :------: | ---------- |
| Mozdulatlan / Álló lövész          | `+0x` ⭕  |            |
| A lövész lassan egyenletesen sétál | `+2x`  ⭕ |            |
| A lövész lassan fut                | `+5x`  ⭕ |            |
| A lövész rohan                     | `+10x` ⭕ |            |

---
#### Szorzó - Méret módosító

| Célpont mérete           | Módosító | Megjegyzés |
| ------------------------ | :------: | ---------- |
| Pénzérme                 |   +7x    |            |
| Alma                     |   +5x    |            |
| Fej, Dinnye, Macska      |   +4x    |            |
| Törpe, gyerek            |   +1x    |            |
| Átlagos ember/elf méretű |   +0x    |            |
| Ló oldalról, Ogre        |   -1x    |            |
| Lovas                    |   -2x    |            |
| ⭕TODO⭕                   |          |            |
| ⭕TODO⭕                   |          |            |

→ 🔺ISSUE: [Túl kicsi a fej szorzója](https://github.com/kaktusztea/km100/wiki/TODO.ISSUE.tavharc#l%C3%B6v%C3%A9szet-haj%C3%ADt%C3%A1s-kaland-tapasztalatok)

→ 🔺ISSUE: [Ha a szorzó 0-ra, vagy az alá csökkenne](https://github.com/kaktusztea/km100/wiki/TODO.ISSUE.tavharc#km100-c%C3%A9lz%C3%A1s-szorz%C3%B3).

---
#### Szorzó - Láthatóság és hangosság módosító

A látási viszonyok erősen meghatározzák a távolsági harcot, hiszen például félhomályban sokkal nehezebb eltalálni valakit, mint fényes nappal. Viszont... könnyebb valakit eltalálni sötétben, ha zajt ad ki. Ezeknek megfelelően a fenti körülmények is módosítják a Szorzó értékét. A fentieket az alábbi táblázatokban foglalhatjuk össze.

| Környezeti fényviszonyok | Szorzó Módosító |
| ------------------------ | :-------------: |
| Szürkületben             |      `+2x`      |
Szürkületben nehezebb a távolság becslése.


| A célpont láthatósága és hangossága        |            Szorzó Módosító            | Példa                                                           |
| ------------------------------------------ | :-----------------------------------: | :-------------------------------------------------------------- |
| **Jól kivehető kontúr**<br>                |                 `+0x`                 | Nappali célpont; napnyugtakor háztetőn álldogáló célpont        |
| **Homályos kontúr**                        |                 `+3x`                 | Félhomályban mozgó alaké;<br>testközelben levő célpont sötétben |
| **Éppen kivehető kontúr (zajos)**          |                 `+6x`                 | Sötétben moccanó, neszező árnyak                                |
| **Éppen kivehető kontúr (csendes)**        |                `+15x`                 | Sötétben, csendben lapuló árnyak                                |
| **Háttérrel egybeolvadó kontúr (zajos)**   |                `+15x*`                | Vaksötétben harcoló ellenfél;  <br>távoli célpont sötétben      |
| **Háttérrel egybeolvadó kontúr (csendes)** | Lehetetlen. Csak 100-as dobás esetén. | Lopakodó, némán osonó fejvadász                                 |
\* Csak speciális mentális gyakorlat segítségével.

---
#### Szorzó - Szél hatása

Amennyiben erős szél fúj, akkor az is módosíthatja a célpont Védő Értékét, mivel az erős széllökések eltéríthetik a lövedéket.

| Szél ereje  |  Szorzó módosító   |
| ----------- | :----------------: |
| Nagyon erős |        +4x         |
| Viharos     |        +8x         |
| Orkán erejű | A lövés lehetetlen |


---
### Osztó

Az fegyver **Osztó** szintén méterben megadott távolságérték és fegyverenként változik. Azt mutatja meg, hogy hány méterenként nő **az adott fegyverrel szemben** a célpont **Védő Értéke**. Gyakorlatilag azt befolyásolja, hogy a cél távolságának növekedésével milyen ütemben romlik találati esélyünk.

Érthető, hogy egy nyílpuska **Osztója** nagyobb, mint egy dobótőré, hiszen az előbbivel jó eséllyel támadhatunk akár `30-40` méterre levő célpontot is, míg egy dobótőr esetében ez már a lehetetlen kategóriába tartozik. A fentieket alább, a **Cellaszám** tárgyalásánál érthetjük meg.

⚡Példa: a **Könnyű nyílpuska** **Osztója** `4`. Tehát `4` méterenként nő vele szemben a célpont Védő Értéke.

### Cellaszám

$$ Cellaszám = {cél\ távolsága\ (m) \over fegyver\ Osztó} → felfelé\ kerekítve $$

Ez a szám adja meg, hogy a fegyver **Osztójához** viszonyítva hányadik távolság “cellában” található a célpont. A Védő Érték kiszámításánál ezzel a számmal lesz beszorozva a **célpont szorzója**, amelyet a mozgás, méret, láthatóság, stb módosíthatnak (lásd alább).

Például ha egy hosszú íjjal (melynek **Osztója** `3`) lövünk egy `7` méterre levő célra, annak Cellaszáma: `3`.  `7/3 → 3` mivel a `7` osztva `3`-al, felfelé kerekítve egyenlő `3`-al.

Az egyszerűség kedvéért álljon erről itt egy ábra, melyről megérthetőek a fentiek.

![](images/06_cellaszam.png)

Ha a fegyver Osztója nem `3`, hanem mondjuk `2` lenne, akkor következésképpen a célpont **Cellaszáma** `4` lenne (`7/2`).

Alább az egyes fegyver-kategóriák tipikus **Osztó** értékét látjuk. Ettől csak rendkívül kevés esetben tér el egyik-másik konkrét fegyver, azok is csak nagyon indokolt esetben. Látható, hogy minél pontosabb egy fegyver, annál nagyobb az **Osztó** értéke.


| Fegyverkategória                    | Osztó | Példa fegyverek                                        | Speciális                                                                                                                         |
| ----------------------------------- |:-----:| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| **Nem hajításra készített tárgyak** |  `1`  | Kard, zsámoly, söröskorsó                              | Maximális Hatótávjukhoz hozzáadható:  <br>(`Erő x Osztó`)                                                                         |
| **Apró hajítófegyverek**            |  `2`  | Tőr, dobótőr, hajítóbárd, kő                           | -                                                                                                                                 |
| **Íjak**                            |  `3`  | Rövid íj, hosszú íj,  <br>+ Kézi nyílpuska,  <br>dárda | Sebzés bónusz: Erő tulajdonság  <br>(ha erre az Erőre lett tervezve)                                                              |
| **Nyílpuskák**                      |  `4`  | Minden nyílpuska  <br>kivéve Kézi és Kharei            | A kézi nyílpuskától felfelé Páncéltörőnek számítanak:<br><br>`SFÉ = a vért rétegeinek száma`<br>(mágikus vértek esetén a KM dönt) |

🔆**Megjegyzés**: Javasoljuk a KM-nek, hogy ha esetleg mágikus, vagy kifejezetten jó minőségű fegyver értékeit akarja az alapértékhez képest módosítani, akkor az Osztó értékét lehetőleg **ne** módosítsa, inkább a fegyver **Célzó Értékét** változtassa.

<br />

### Sebzés bónusz hiánya

Távolsági fegyverek esetén NINCS **Többszörös találatból** adódó plusz sebzés.


---
## Harci körülmények, taktikák

### Szándékos kitérés lövés elől

Ha valaki látja és van ideje felkészülni a rá leadott lövésre/hajításra, valamint rendelkezik elegendő hellyel a kitérésre és bejelenti, hogy megpróbálja elkerülni végzetét, akkor Gyorsaságpróbát kell dobnia, melynek nehézsége függ a lövést leadó személy távolságától, valamint az általa használt fegyvertől.


| Gyorsaságpróba célszám | Dobófegyverek,<br />Mágikus lövedék I. | Íjak,<br />Mágikus lövedék II. | Nyílpuskák,<br />Mágikus lövedék III. |
|:----------------------:| --------------------------------------:| ------------------------------:| -------------------------------------:|
|           8            |                      1m&nbsp;-&nbsp;3m |                        0m - 5m |                              0m - 10m |
|           7            |                                4m - 6m |             6m&nbsp;-&nbsp;10m |                   11m&nbsp;-&nbsp;20m |
|           6            |                      7m&nbsp;-&nbsp;9m |            11m&nbsp;-&nbsp;15m |                   21m&nbsp;-&nbsp;30m |
|           5            |                    10m&nbsp;-&nbsp;12m |            16m&nbsp;-&nbsp;20m |                   31m&nbsp;-&nbsp;40m |
|           4            |                           Testközelben |                                |                                       |

Lásd: [Elemi mágia - Formulák - Őselem idézése](magia.arkanumok/elemi_magia.md#őselem-idézése)\
⭕(lehet h ki kéne szedni általános "Mágikus lövedék" szekcióba)⭕

🔆**Megjegyzés**: A próbához `+2` járul, ha a karakter rendelkezik [Kitérés lövés elől](fortelyok.harci/kiteres_loves_elol.md) harci fortéllyal.

---
### Páros, kétkezes hajítás

Egyszerre két kézzel 1-1 fegyvert elhajítani. Ebben a szituációban `2`db célzó dobást tesz a karakter `CÉ:-30` módosítóval. Természetesen ha mindkettő talál, mindkettő sebez is.

A fegyver méretének az **Erő** Tulajdonság és a KM józan esze szab határt.

[Kétkezesség](fortelyok.harci/ketkezesseg.md) fortély megléte esetén csak `CÉ:-15` büntetés sújtja az alkalmazót.

---
### Egyéb körülmények

| Körülmény                                                           |                    CÉ módosító                     | Megjegyzés                                                                                                                                                                                                                           |
|:------------------------------------------------------------------- |:--------------------------------------------------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A célpont fekszik, guggol                                           |                       nincs                        | A védekező megváltozott mérete számít.                                                                                                                                                                                               |
| `+1` kör Célzás                                                     |                      `CÉ:+10`                      | [Képzett célzás](fortelyok.harci/kepzett_celzas.md) fortély megléte esetén: `CÉ:+20`<br>Íjjal legfeljebb `1` körig lehet a **Célzást** használni, hosszabb ideig való kitartása körönként `CÉ:-10` büntetést okoz.                   |
| Hirtelen lövés:  <br>a célpont hirtelen tűnik fel, rögtön lőni kell |                      `CÉ:-30`                      | -                                                                                                                                                                                                                                    |
| A lövész képzetlen az adott fegyver használatában                   |                      `CÉ:-40`                      | -                                                                                                                                                                                                                                    |
| Nem “belőtt” lőfegyver                                              | `CÉ:-30`&nbsp;(íjak)<br>`CÉ:-15`&nbsp;(nyílpuskák) | Egy lőfegyvert a karakternek „be kell lőni”, azaz kitapasztalni egyedi jellemzőit. Ez kb. fél óra gyakorlást jelent. Amíg a fegyver új használója ezt nem teszi meg, addig az adott fegyverre az itt leírt CÉ levonások vonatkoznak. |

<br />


---
## Távolsági fegyverek

### Távolsági fegyver kategóriák, Fegyverek Célzó Értéke

A távolsági fegyverek több kategóriába sorolhatóak attól függően, hogy általánosságban mennyire könnyű kezelni őket, mennyire alkalmasak messzi célok leküzdésére. Ezek szerint az alábbi módosítók járulnak ****minden**** karakter Célzó Értékéhez, aki a felsorolt fegyverek valamelyikét kezébe veszi. A lentiek csak irányadó számok a konkrét fegyverek Célzó Értéke és egyedi jellemzőik eltérhetnek ezen értékektől, de nagyjából ebben a skálán mozognak.


|            Fegyverkategória            |  CÉ   | Fegyverek                                              | Speciális                                                                                                                             |
|:--------------------------------------:|:-----:| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Hajító szálfegyverek,<br>Egyéb tárgyak | `+0`  | Kard, zsámoly, korsó, hajításra nem alkalmas fegyverek | Maximális Hatótávjukhoz hozzáadható:  <br>(ERŐ x Osztó)                                                                               |
|          Apró hajítófegyverek          | `+4`  | Tőr, dobótőr, hajítóbárd, dárda, lándzsa, kő           | -                                                                                                                                     |
|                  Íjak                  | `+10` | Íjak                                                   | Sebzés bónusz: ERŐ Tulajdonság 1:1<br>(**ha** erre az Erőre lett tervezve)                                                            |
|               Nyílpuskák               | `+16` | Nyílpuskák                                             | A kézi nyílpuskától felfelé **Páncéltörőnek** számítanak:<br>SFÉ = a vért rétegeinek száma<br>(mágikus vértek esetén a KM szava dönt) |

🔆**Megjegyzés**: Amennyiben valaki hajításra nem alkalmas fegyvert akar dobni, akkor az adott fegyver harcmodorában kismesteri, azaz `6`.szinten jártasnak kell lennie. Ez alatt képzetlen fegyverhasználat büntetéseivel történhet a dobás.

- [Hajítófegyverek táblázata](067_fegyverek.md#hajítófegyverek-harcértékei)
- [Lőfegyverek táblázata](067_fegyverek.md#lőfegyverek-harcértékei)

---
### Támadások száma (Íjászat, Hajítás)
```
Sebesség = aktuális harcmodor + Gyorsaság Tulajdonság
```

Az íjász/hajigász támadásainak száma attól függ, hogy milyen képzett az adott fegyver használatában, vagy annak Harcmodorában, illetve fürge. Ezt a kapcsolódó harci képzettség foka és a Gyorsaság tulajdonság határozzák meg a fentiek szerint.

Kézifegyvereknél az alábbi módon kategorizálunk:

```
(5) rövid fegyverek            → 5 Sebesség pontonként nő 1-el a támadások száma
(6) egykezes és szálfegyverek  → 6 Sebesség pontonként nő 1-el a támadások száma
(7) kétkezes fegyverek         → 7 Sebesség pontonként nő 1-el a támadások száma
```

Távolsági fegyverek esetén viszont nem mindegyiknek van **Sebesség** kategóriája, mivel újratöltésük annyi időt vesz igénybe, hogy nem lehetséges velük egy körben többször támadni (pl. nyílpuskák).

Ebben az esetben lehet hasznos a [Gyors újratöltés](fortelyok.harci/gyors_ujratoltes.md) harci fortély.

Az egyes fegyverek Sebesség kategóriáját lásd a **Harcrendszer** [Fegyverek](067_fegyverek.md) alfejezetében (táblázat)!

---
### Erőből / Ügyességből forgatott fegyverek

Távolba ható fegyverek esetén különbséget teszünk **Erőből** és **Ügyességből** használtak között. A fenti tulajdonság szerepe a sebzésbónusz és a végső Célzó Érték kiszámításánál mutatkozik meg. Hogy egy fegyvert Erőből, vagy Ügyességből forgathatunk, azt a [Távolsági fegyverek fejezet](067_fegyverek.md#hajítófegyverek-harcértékei) alatt található táblázatból olvashatjuk ki.

---
### Hatótáv

Minden távolba ható fegyvernek van **Hatótávja**, amely értelemszerűen az adott fegyverrel elérhető legnagyobb lőtávolságot jelenti. Ezt minden fegyvernél számon tarjuk, értékét méterben jelezzük. A játékos nem lőhet/dobhat a fegyver hatótávján túl (illetve hajítás esetén még szerepet játszhat a támadó Ereje, de erről később).

⚡Példa: a Könnyű nyílpuska **Hatótávja** `50`, tehát maximálisan `50` méterre lehet vele ellőni.

---
### Távolsági fegyverek minősége

Nem minden fegyver egyformán jó minőségű, valamelyik igazi mestermunka, pontos, megbízható, mások pedig olyan hitványul vannak összeeszkábálva, hogy még egy öt méterre álló gólemet se talál el vele az ember.

A távolsági fegyverek minősége azok **CÉ**-jét javítja, vagy éppen rontja. Például egy átlagos könnyű nyílpuska `16`-es **CÉ**-vel bír. Egy kiváló nyílpuska, amely mestermunka, akár `20-25`-öt is elérhet, ugyanakkor egy ócskavasnál nem lehet meglepő az `8`-as érték. Szélsőséges esetben a fegyver **Osztó** értéke is módosulhat, de ökölszabályként kimondható, hogy az **Osztó** – minőségtől függően - **legfeljebb** `±1`-el változhat az alapértékhez képest, továbbá csak lőfegyverekre vonatkozik, hajítófegyverekre nem. Egy hajítófegyvernél legfeljebb akkor elképzelhető a **Osztó** változása, ha annyira rossz minőségű, hogy átkerül az `2`-esből a `1`-es kategóriába. Pozitív irányba nem módosulhat.

<br />

---
## Fortélyok - Távolsági harc

A tapasztalt lövész (hajigász) nem csupán harcértékeivel tűnik ki társai közül, hanem egyedi trükkökkel, ismeretekkel, amik egy bizonyos területen a többi fölé emelik. Lásd bővebben a [Távolsági Harccal kapcsolatos fortélyokat](042_harci_fortelyok.md#távolsági-harci-fortélyok)!

<br />

---
## Példalövészet

Tetves, a tolvaj-bérgyilkos egy raktár ablakából, nyílpuskával les a sikátorban közelgő áldozatára, egy tehetős kalmárra, aki éppen hazafelé battyog. A könnyű nyílpuska **Osztója:** `4`

**Tetves Célzó Értéke**

```
CÉ = -30 (Konstans) + 6 (Önuralom 2x) + 16 (nyílpuska) +15 (CM) + 4 (lövészet) = 11
```

**A célpont Védő Értéke**

$$ VÉ = {5(lassan\ mozgó)+0(normál\ méret)+0(jól\ látható)}\ x\ {15(távolság)\over 4(nyílpuska\ osztója)}$$


Az osztásnál felfelé kell kerekíteni, `15/4` → Cellaszám `4`.

```
VÉ = 5x4 = 20
```

**Tehát a próba**

```
11 + k100  vs  20
```

azaz ha Tetves legalább `9`-et dob `k100`-on, akkor találatot ér el. Könnyű cél...

Dob `k100`-zal, az eredmény `31`, végső `CÉ = 11+31 = 42`, tehát eltalálta a célt, dobhatja a sebzést.

De lássunk egy bonyolultabb esetet.

⭕TODO: 2. példa⭕

<br />

---
## Ritka, speciális esetek

Az alábbi szabályokat csak nagyon kiélezett, fontos pillanatokban használjuk, mikor jut rá idő, tömegjelenetben semmiképp, mert borzasztóan lassítaná a harcot.

### Távolsági harc vaksötétben, zajos célpontra

Ha a karakternek nincs **Vakharc** fortélya, de alkalmazza a „Hatodik érzék” diszciplínát, akkor dobjunk `K10`-el, a dobáshoz ne adjunk hozzá semmit. A Célszám a célpont távolsága méterben. Ha sikeres a próba, akkor elkezdhetjük kiszámolni a CÉ és VÉ értékeket a táblázatban megadott 15x-ös **Látási Szorzóval**. Ha a karakter nem alkalmazza a diszciplínát, akkor a célszám 3-al nő.

Ha a próba sikertelen, akkor a lövés/dobás is automatikusan sikertelennek minősül. A rontás mértékétől függően közelben lévő barátot, szövetségest találhat el az eltévedt lövedék. Erről a KM dönt. Az `1`-es dobás itt is mindig kudarc, a `10`-es mindig siker.

Ha a támadó rendelkezik **Vakharc** fortéllyal (1, vagy 2. fok), akkor nem kell a fenti dobást elvégeznie, hanem rögtön lőhet a táblázatban megadott Láthatóság módosítókkal.

Érthető, hogy közvetlen közelről egy képzetlen is valószínűleg betalál, viszont ahogy nő a távolság, úgy csökkenek (drasztikusan) találati esélyei.

#### Példalövészet vaksötétben

`4.`szintű harcos, Vakharcban képzetlen, **CÉ Alap**: `30`, **Önuralom**:`+3`, **Lövészet** – `9.szint`\
**Fegyver**: nyílpuska

```
CÉ = 30 + 6(Önuralom) – 30(konstans) = 6
```


**Célpont jellemzői**

- Táv: 10m → Cellaszám: `4` (`10/3 → 4`)
- Láthatóság: sötét, zajos célpont (`+12x`)

A játékos először is dob `k10`-el. Ha az eredmény egyenlő `10`-el (`10m`) (`10%` esély), akkor lőhet a Vakharc–`1.`foknak megfelelő szorzóval (`+12x`). Ha ez sikerül, akkor, jön a **VÉ** számítás és a lövés, egyébként automatikusan célt téveszt.

**Célpont sétál**

- Mozgás: lassan mozgó (`+5x`)
- `VÉ = 4 x(12+5) = 68`
- Találati esély: `33%`

**Célpont áll**

- Mozgás: álló (`3x`)
- `VÉ = 4 x(12+3) = 60`
- Találati esély: `41%`

#### Távolsági harc vaksötétben - Csendes célpont

Mielőtt bármit kiszámolnánk, nézzük meg, van-e a karakternek **Vakharc** fortélya. Ha nincs, és a célpont nem ad ki semmilyen zajt (ne feledjük, vaksötétben vagyunk!), akkor a távolsági támadás automatikusan cél téveszt.

Ha van, akkor dobjunk K10-al, a dobáshoz ne adjunk hozzá semmit. A Célszám alapfokú Vakharc esetében a célpont távolsága méterben, mesterfokú esetén pedig e szám fele. Ha sikeres a próba, akkor elkezdhetjük kiszámolni a CÉ és VÉ értékeket a fenti táblázatban foglalt **Látási Szorzóval.** **Amennyiben a karakter „Hatodik érzék” diszciplínát alkalmaz, a próba célszáma 3-al lecsökken.**

Ha a próba sikertelen, akkor a lövés/dobás is automatikusan sikertelennek minősül. A rontás mértékétől függően közelben lévő barátot, szövetségest találhat el az eltévedt lövedék. Erről a KM dönt. Az 1-es dobás itt is mindig kudarc, a 10-es mindig siker.
