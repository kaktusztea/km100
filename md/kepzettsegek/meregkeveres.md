#### 🔴 Méregmester, 🔵 Méregkeverés

````diff
⭕TODO⭕
- Alvás: melyik "Hatás" kategóriába tartozzon?
- Most a legenyhébben van (1), de lehet, hogy nehezebb alvást előidézni, mint pl. bódulatot...?
````

**Próba**: van, a rontás rejtett, a játékos csak a méreg alkalmazásakor szembesül a balsikerrel (nem hat). 

**Domináns Tulajdonságok**: Emlékezet, Önuralom

**Kapcsolódó fortélyok**: -

**Leírás**: A méregkeverés képzettség tanulható **Átfogó** képzettségként (ekkor minden típusú méregre vonatkozik és **Méregmester** néven illetjük), illetve **Átlagos** képzettségként - ekkor választani kell, hogy mely típusú mérgeket tanulja a karakter a lenti három csoportból:

- Étel és italmérgek
- Légi- és kontaktmérgek
- Fegyvermérgek

A mérgek összetevő szerint csoportosítva három kategóriába sorolhatók:

- állati
- növényi
- ásványi (szervetlen)

Egy jó „szakembernek" tudnia kell, hogy a fenti anyagokból (állat, növény, ásvány) hogyan vonja ki a méreganyagot, ezért a lenti képzettség limit vonatkozik rá:

<br />

---

**Limitek**

🔻 A Méregkeverés képzettség szintje nem lehet magasabb, mint az `Élettan`, `Herbalizmus` és `Alkímia` képzettségek szintjeinek összege. ⭕PROBLÉMA: Élettan is „halmazos" képzettség (Átfogó-Átlagos)⭕

🔻 Hogy egy nyersanyagból a karakter ki tud-e vonni méreganyagot, az a fenti képzettségek szintjétől (is) függ. A konkrét esetet és körülményeket figyelembe véve a KM dönt.

🔻 A méregkeverő legfeljebb olyan Szintű mérget képes kikeverni, ami **nem nagyobb a Méregkeverés képzettség szintjének kétszeresénél**. Valamint szükséges a megfelelő összetevők megléte!

<br />

---

**A méreg szintje**

A Méregkeverés képzettség megadja, hogy az alkalmazó milyen típusú, hatékonyságú mérget képes megalkotni. A mérgeket elkészítésük bonyolultsága szerint egy ún. Szinttel jellemzünk.

```
Méreg szintje = Erősség + Súlyosság + Elállás + Hatóidő + Speciális
```

- **Méreg erőssége** `(1-10)`: Ez adja meg, hogy mennyire nehezen áll ellen a szervezet a méregnek, mennyire hatékony. Gyakorlatilag az összetevők „erejétől" függ. A hatékonyabb (esetleg titkos) összetevők ismerete a magas szintű méregkeverés ismérve.
  - Az 1-es a leggyengébb, a 10-es a legerősebb mérgek jellemzője (Figyelem! Az erősség nem egyenlő a romboló hatással! Léteznek
    például nagyon hatékony, 10-es erősségű altatók is)
  - Plusz adag: ha a normális adagnál nagyobb mennyiséget használunk fel, megnőhet a méreg erőssége (KM dönt). Szabály: **a méreg erősségét az adag növelésével legfeljebb duplájára növelhetjük!!** Vegyük figyelembe viszont, hogy a hordozó közeg (levegő, fegyver pengéje, stb) legfeljebb mekkora adagot képes tárolni, valamint egyéb nehezítő körülményeket is: pl az italméregben nagyobb mennyiségnél nagyon feltűnő lehet a megváltozott íz, stb. ⭕TODO: adag növelés és Erősség növekedés matematikai kapcsolata⭕

<br />

- **Hatása súlyossága**

| Hatás max súlyossága | Érték  | Követelmény |
| :----------- | :----------- | :----------- |
| Enyhe rosszullét, hányás, alvás | ⭕1  | ⭕- |
| Kábulat, Görcs | ⭕2  | ⭕- |
| Bódulat, Részleges bénulás | ⭕3  | ⭕- |
| Életveszély, Teljes bénulás | ⭕4  | ⭕- |
| Halál | ⭕5  | ⭕- |

<br />

- **Elállás**: meddig áll el szabad levegőn/folyadékban?

| Meddig áll el? | Érték  | Méregkeverés követelmény |
| :----------- | :----------- | :----------- |
| Pár másodperc | 0  | - |
| 1 perc  | 1  | - |
| 10 perc | 2  | - |
| 1 óra   | 3  | 3.szint |
| 1 nap   | 4  | 6.szint |
| 1 hónap | 5  | 9.szint |
| Örökké  | 6  | 12.szint |

<br />

- **Hatóidő**

| Milyen gyorsan hat? | Érték  | Követelmény |
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

- **Speciális**
  - Több komponensű: minden újabb komponensre bontás: `+2`
  - Több hordozó közeg (étel/ital, légnemű, véráramban ható): plusz hordozónként `+3`
  - Kis mennyiség: ha egészen kis mennyiség is elég 1 adaghoz: `+2`
  - Szintelen: `+3`
  - Szagtalan/ízetlen: `+3` (egyben értendő)

<br />

---

> Példa 1 ⚡ **Lórúgás (brutálisan erős altató - italméreg)**

```
- Erősség: 10 (a legerősebb)
- Hatás max súlyossága: 1 (alvás)
- Meddig áll el: +4 (1 nap folyadékban)
- Hatóidő: +5 (azonnal)
- 1 komponensű, 1 hordozó közeg, normál adag: +0
```

```
Így a méreg szintje: 20
 → Minimum 10. szintű méregkeverés szükséges
```

A méregellenállást `10` ellen (**méreg erőssége**) kell dobni, még egy kicsattanó egészségű, 120 kilós barbár is szinte biztos, hogy kidől tőle egy kis délutáni durmolásra.

🔆 Látható, hogy egy fél óra alatt ható, ugyanilyen méreghez elég lenne a `8.szintű` Méregkeverés képzettség is.

<br />

---

> Példa 2 ⚡ **Könycsepp a pengén (halálos fegyverméreg)**

```
- Erősség: 6
- Hatás max súlyossága: 5 (halál)
- Meddig áll el: +2 (10 percig a pengére locsolva)
- Hatóidő: +4 (gyors (10 szegmens)
- 1 komponensű, 1 hordozó közeg, normál adag: +0
```

```
Így a méreg szintje: 17
 → Minimum 9. szintű Méregkeverés képzettség szükséges
```

🔆 A fenti fegyverméreg erőssége az átlagosnál kicsit erősebbnek mondható, de egy magas Edzettséggel bíró áldozat jó eséllyel megússza az elsődleges hatását (halál) és "csak" lebénul, vagy erős bódulatba kerül.

Fontos, hogy amennyiben 10 percen belül nem kerül a pengéről véráramba, akkor nagyon gyorsan elveszíti hatóerejét.

<br />

---

> Példa 3 ⚡ **Múló évszakok (többkomponensű mesteri ital/légiméreg)**

```
- Erősség: 5
- Hatás max súlyossága: 5 (halál)
- Meddig áll el: +6 (Örökké)
- Hatóidő: +1 (fél nap múlva)
- 4 komponensű, 2 hordozó közeg, normál adag: +6 +3 +0
- Szagtalan/ízetlen: +3
```

```
Így a méreg szintje: 29
 → Minimum 15. szintű Méregkeverés képzettség szükséges!
```

Ez már tényleg művészet. Ha a méregkeverő irodalommal foglalkozna ilyen szinten, ünnepelt poéta vagy dalnok lehetne. Ez meg is látszik a rendkívül magas szinten és a képzettség követelményen.

⚜️ "Az öreg király rajongott az orchideákért. Tavaszra, nyárra és őszre is volt egy-egy különleges, ritka fajtája végtelen udvarának kertjében. Tavasszal leszakajtotta a legszebbet a narancsszínből, nyáron a bíborszínből, ősszel a kékből. Mindhárom hálószobáját díszítette.

Az őszi virág leszakajtása után az uralkodó este elfogyasztotta bőséges vacsoráját és borral öblítette le, mint mindig. Álma békés volt, olyannyira, hogy reggel már fel sem ébredt... "Öreg volt, szépen ment el" - mondták a szolgálók. Ételét átvizsgálva az udvari vajákosok és a varázsló semmit nem találtak. "Eljött az ideje." - mondták ők is.

Fia nem lévén, unokaöccse lépett helyébe, ki - úgy mondják - már nagyon türelmetlen volt. Asszott, vén tudósa Taba el Ibarából mindig mellette ólálkodott - azt mondják életelixírt készít a hercegnek..."

<br />

🔆 A fenti méreget `4` darab komponensre bontotta a déli vajákos: a király borába (ital hordozó) adagolta hetente egyszer az elmúlt 9 hónapban a szagtalan/ízetlen alapmérget, amely önmagában ártalmatlan, így nem is kimutatható, viszont stabilan felgyűlt a szervezetben. A maradék 3 komponens a 3 orchidea (légi hordozó) virágpora volt, melyet a király belélegzett - hisz mindet a hálószobájába tette. Az első kettő leszakajtása után még nem történt semmi, a hatáshoz mind a háromra (plusz a borban levő alapméregre) szükség volt.

A hatást a vajákos eltolta fél nappal, hogy éjszaka jöjjön a vég, így a gyanú sem ébredt fel senkiben. Az Erősséget (`5`) bőven elégnek vélte - a király Egészsége (`-1`) már amúgy is igen gyenge lábakon állt.

---

**Méregellenállás**

A Méregellenállás próba egyszerű Tulajdonság próba, melynél a karakter `Edzettség` Tulajdonsága számít.

```
Méregellenállás próba:
(Edzettség + k6)  vs  Méreg Erőssége
```

> A méregellenállást a méreg Erőssége (és NEM szintje) ellen kell
dobni!!!

<br />

---

***Másodlagos hatás***

A mérgeknek lehet ún. **Másodlagos hatása**, amely a sikeres próba esetén következik be. Ennek hatása legfeljebb a rendes hatásnál 1-el ⭕(2-vel???)⭕ alacsonyabb kategóriájú lehet. (Pl. Halál→Életveszély(⭕vagy Bódulat⭕))

<br />

---

> Biztos tudás, követelmények

| Képzettség szint | Biztos tudás  | Speciális <br /> <sub>(tanulható fortély, különleges  képesség)</sub> | Követelmény |
| :----- | :----- | :-----: | :-----: |
| Novícius (3)     | ⭕xyz <br /> **Példa**: x | ⭕ | Lásd: "Limitek" bekezdés |
| Kismester (6)    | ⭕xyz <br /> **Példa**: x | ⭕ | Lásd: "Limitek" bekezdés |
| Mester (9)       | ⭕xyz <br /> **Példa**: x | ⭕ | Lásd: "Limitek" bekezdés |
| Nagymester (12)  | ⭕xyz <br /> **Példa**: x | ⭕ | Lásd: "Limitek" bekezdés |
| Élő legenda (15) | ⭕xyz <br /> **Példa**: x | ⭕ | Lásd: "Limitek" bekezdés |
