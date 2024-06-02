# Méregrendszer, mérgek

A mérgeket jelleg szerint négy csoportra bontjuk:
- Étel és italmérgek
- Légimérgek
- Kontaktmérgek
- Fegyvermérgek

A mérgeket összetevő szerint csoportosítva pedig szintén három kategóriába sorolhatjuk:
- állati
- növényi
- ásványi (szervetlen)

A **Méregkeverés** külön képzettség, működését lásd [annak leírásában](kepzettsegek/meregkeveres.md).

---
## A méreg szintje

A mérgeket elkészítésük bonyolultsága szerint egy ún. Szinttel jellemzünk.

A méreg kikeverése **Méregkeverés** képzettpróbához kötött, amelynek célszáma a **Méreg szintjével** azonos.

```
Méreg szintje = Erősség + Súlyosság + Elállás + Hatóidő + Speciális
```

---
## Méregellenállás próba

```
(Edzettség + k6)  vs  Méreg Erőssége
```

A Méregellenállás próba egyszerű Tulajdonság próba, melynél a célpont `Edzettség` Tulajdonsága számít.

**FONTOS**: A méregellenállást a méreg **Erőssége** (és NEM szintje) ellen kell dobni!!!

<br />

---
### (1) Méreg Erőssége
```
 Méreg erőssége: 1-10
```

A **Méreg erőssége** `(1-10)` intervallumban mozog.\
Ez adja meg, hogy mennyire nehezen áll ellen a szervezet a méregnek, mennyire hatékony. Gyakorlatilag az összetevők „erejétől" függ. A hatékonyabb (esetleg titkos) összetevők ismerete a magas szintű méregkeverés ismérve.

Az `1`-es a leggyengébb, a `10`-es a legerősebb mérgek jellemzője, de tartsuk észben, hogy **az Erősség nem egyenlő a romboló hatással!** Léteznek például nagyon hatékony, `10`-es erősségű altatók is.

#### Plusz adag

Ha a normális adagnál kisebb, vagy nagyobb mennyiséget használunk fel, csökkenhet/megnőhet a méreg erőssége (KM dönt).

**Erősség változása**:
- Kis adag: Erősség `50%`-al csökken (lefele kerekítünk)
- Nagy adag: Erősség: `50%`-al nő (lefele kerekítünk)

Vegyük figyelembe viszont, hogy a hordozó közeg (levegő, fegyver pengéje, stb) legfeljebb mekkora adagot képes tárolni, valamint egyéb nehezítő körülményeket is: például az italméregben nagyobb mennyiségnél nagyon feltűnő lehet a megváltozott íz, stb.



<br />

---
### (2) Hatása súlyossága

````diff
⭕TODO⭕
- Alvás: melyik "Hatás" kategóriába tartozzon?
- Most a legenyhébben van (1), de lehet, hogy nehezebb alvást előidézni, mint pl. bódulatot...?
````

| Hatás max súlyossága            | Érték |
|:------------------------------- |:----- |
| Enyhe rosszullét, hányás, alvás | ⭕1   |
| Kábulat, Görcs                  | ⭕2   |
| Bódulat, Részleges bénulás      | ⭕3   |
| Életveszély, Teljes bénulás     | ⭕4   |
| Halál                           | ⭕5   |

#### Másodlagos hatás

A mérgeknek lehet ún. **Másodlagos hatása**, amely a sikeres próba esetén következik be. Ennek hatása legfeljebb a rendes hatásnál 1-el ⭕(2-vel???)⭕ alacsonyabb kategóriájú lehet. (Pl. Halál→Életveszély(⭕vagy Bódulat⭕))

<br />

---
### (3) Elállás / Kiürülés

Ez a tétel attól függ, hogy milyen típusú mérget szándékozik készíteni a méregkeverő:

- **Elállás**: kizárólag fegyvermérgek esetén: meddig áll el szabad levegőn/folyadékban?
- **Kiürülés**: minden más méreg típus esetén - mennyi idő alatt ürül ki az áldozat szervezetéből

#### (3a) Elállás

| Meddig áll el? | Érték | Méregkeverés követelmény |
|:-------------- |:-----:|:------------------------:|
| Pár másodperc  |   0   |            -             |
| 1 perc         |   1   |            -             |
| 10 perc        |   2   |            -             |
| 1 óra          |   3   |         3.szint          |
| 1 nap          |   4   |         6.szint          |
| 1 hónap        |   5   |         9.szint          |
| Örökké         |   6   |         12.szint         |

#### (3b) Kiürülés

| Mennyi idő alatt ürül ki | Érték | Méregkeverés követelmény |
|:------------------------ |:-----:|:------------------------:|
| 1 kör                    |   0   |         3.szint          |
| 1 óra                    |   1   |         6.szint          |
| 1 nap                    |   2   |         9.szint          |
| 1 hét                    |   3   |         12.szint         |

<br />


---
### (4) Hatóidő

| Milyen gyorsan hat? | Érték  | Méregkeverés követelmény |
| :----------- | :-----------: | :-----------: |
| 30 perc - 3 óra múlva | 0  | - |
| 4 - 23 óra múlva      | +1  | 3.szint |
| 2-20 perc múlva       | +1  | 3.szint |
| 1-10 nap múlva        | +2  | 5.szint |
| 2-6 kör múlva         | +2  | 5.szint |
| 2-4 hét múlva         | +3  | 7.szint |
| Gyorsan (10 szegmens) | +4  | 7.szint |
| Hónapok múlva         | +4  | 9.szint |
| Azonnal (1szegmens)   | +5  | 9.szint |
| Évek múlva            | +5  | 12.szint |

<br />


---
### (5) Speciális

- Több komponensű: minden újabb komponensre bontás: `+2`
- Több hordozó közeg (étel/ital, légnemű, véráramban ható): plusz hordozónként `+3`
- Több hordozó közegből csak `1` amiben hatóanyag van, a többi természetes alapanyag: `+3`
- Sűrű: ha egészen kis mennyiség is elég 1 adaghoz: `+2`
- Színtelen: `+3`
- Szagtalan/ízetlen: `+3` (egyben értendő)
- Félrevezető tünetek: `+3/+6` (két lépcső lehetséges, ennyivel nő a méreg azonosítás nehézsége)
- Szabadban sem eloszló légméreg: itt nincs nehézség módosító, hanem olyan fizikai közvetítő kell, ami ezt megoldja: egy labdacs, ami látványosan okádja a füstöt - folyamatos utánpótlást adva.

<br />


---
## Példamérgek

### ⚡ **Lórúgás (brutálisan erős altató - italméreg)**

```
- Erősség: 10 (a legerősebb)
- Hatás max súlyossága: 1 (alvás)
- Meddig áll el: +4 (1 nap folyadékban)
- Hatóidő: +5 (azonnal)
- 1 komponensű, 1 hordozó közeg, nem-sűrű: +0
```

```
Így a méreg szintje: 20
 → Minimum 10. szintű méregkeverés szükséges
```

A méregellenállást `10` ellen (**méreg erőssége**) kell dobni, még egy kicsattanó egészségű, 120 kilós barbár is szinte biztos, hogy kidől tőle egy kis délutáni durmolásra.

🔆 Látható, hogy egy fél óra alatt ható, ugyanilyen méreghez elég lenne a `8.szintű` Méregkeverés képzettség is.

<br />

---
### ⚡ **Könycsepp a pengén (halálos fegyverméreg)**

```
- Erősség: 6
- Hatás max súlyossága: 5 (halál)
- Meddig áll el: +2 (10 percig a pengére locsolva)
- Hatóidő: +4 (gyors (10 szegmens)
- 1 komponensű, 1 hordozó közeg, nem-sűrű: +0
```

```
Így a méreg szintje: 17
 → Minimum 9. szintű Méregkeverés képzettség szükséges
```

🔆 A fenti fegyverméreg erőssége az átlagosnál kicsit erősebbnek mondható, de egy magas Edzettséggel bíró áldozat jó eséllyel megússza az elsődleges hatását (halál) és "csak" lebénul, vagy erős bódulatba kerül.

Fontos, hogy amennyiben 10 percen belül nem kerül a pengéről véráramba, akkor nagyon gyorsan elveszíti hatóerejét.

<br />

---
### ⚡ **Múló évszakok (többkomponensű mesteri ital/légiméreg)**

```
- Erősség: 5
- Hatás max súlyossága: 5 (halál)
- Meddig áll el: +6 (Örökké)
- Hatóidő: +1 (fél nap múlva)
- 3 komponensű, 2 hordozó közeg (levegő, folyadék), nem-sűrű: +4 +3 +0
- Csak 1 komponensben van hatóanyag, a többi természetes: +3
- Szagtalan/ízetlen: +3
```

```
Így a méreg szintje: 30
 → Minimum 15. szintű Méregkeverés képzettség szükséges 5-ös Tulajdonsággal!
```

Ez már tényleg művészet. Ha a méregkeverő irodalommal foglalkozna ilyen szinten, ünnepelt poéta vagy dalnok lehetne. Ez meg is látszik a rendkívül magas szinten és a képzettség követelményen.

⚜️ "Az öreg király rajongott az orchideákért. Tavaszra és nyárra is volt egy-egy különleges, ritka fajtája végtelen udvarának kertjében. Tavasszal leszakajtotta a legszebbet a narancsszínből, nyáron a bíborszínből. Mindkettő hálószobáját díszítette.

A nyári virág leszakajtása után az uralkodó este elfogyasztotta bőséges vacsoráját és borral öblítette le, mint mindig. Álma békés volt, olyannyira, hogy reggel már fel sem ébredt... "Öreg volt, szépen ment el" - mondták a szolgálók. Ételét átvizsgálva az udvari vajákosok és a varázsló semmit nem találtak. "Eljött az ideje." - mondták ők is.

Fia nem lévén, unokaöccse lépett helyébe, ki - úgy mondják - már nagyon türelmetlen volt. Asszott, vén tudósa Taba el Ibarából mindig mellette ólálkodott - azt mondják életelixírt készít a hercegnek..."

<br />

🔆 A fenti méreget `3` darab komponensre bontotta a déli vajákos: a király borába (ital hordozó) adagolta hetente egyszer az elmúlt 9 hónapban a szagtalan/ízetlen alapmérget, amely önmagában ártalmatlan, így nem is kimutatható, viszont stabilan felgyűlt a szervezetben. A maradék 2 komponens a 2 orchidea (légi hordozó) virágpora volt, melyet a király belélegzett - hisz mindet a hálószobájába tette. Az első leszakajtása után még nem történt semmi, a hatáshoz mind a kettőre (plusz a borban levő alapméregre) szükség volt.

A hatást a vajákos eltolta fél nappal, hogy éjszaka jöjjön a vég, így a gyanú sem ébredt fel senkiben. Az Erősséget (`5`) bőven elégnek vélte - a király Egészsége (`-1`) már amúgy is igen gyenge lábakon állt.

---
## Méregérzékelés

Kiszagolod -e a neked felszolgált borban a mérget, feltűnik -e szoba levegőjében terjengő kesernyés szag?

Ha több a méregnek több hordozója van, mindegyikre külön próbá(k) dobható(ak) - kivéve ha az adott komponens természetes alapú (mondjuk sima virágpor, alapból nem is mérhező).

**Méregkeverés próba**
- Ez a próba csak akkor dobható (az Érzékenység tulajdonságpróba mellett), ha a karakter rendelkezik ezzel a képzettségel - legalább `3.szinten`.
- Alap célszám: `xy` ⭕TODO⭕

**Érzékenység tulajdonságpróba**
- Alap célszám: `4` (átlagos)
- Kis (fél) mennyiség: `+1`
- Dupla mennyiség: `-1`
- Sűrű: `+1` (azonos hatás, fele adagnál)
- Színtelen: `+1`
- Szagtalan: `+1`

### Hány adag méreg készíthető?

Ez az alapanyagok beszerezhetőségétől függ. Amennyiben megvan az **Alkímia+Vajákosság** követelmény és az alapanyagok nem rendkívül ritkák, vagy teljesen egyediek, akkor - az ésszerűség határait betartva - bármennyi adag készíthető.

## Fajok különbözősége

Alapesetben nem teszünk különbséget, a Méregkeverők tisztában vannak Ynev leggyakoribb elfszabású teremtményeinek méreggel szembeni tulajdonságaival.

Amennyiben nem hagyományos, rika fajról van szó, ahhoz a [Különleges faj boncolása](hatterek.szabad/kulonleges_faj_boncolasa.md) Szabad Háttér megléte szükséges az adott fajra felvéve.
