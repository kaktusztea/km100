#### Méregkeverés, Méregmester

**Próba:** nincs, csak biztos tudásból ⭕Így egyszerűbb, de ne lehessen elrontani egy méreg kikeverését...?⭕

**Domináns Tulajdonságok**: Emlékezet, Önuralom

**Kapcsolódó fortélyok**: ⭕xyz

**Leírás**: A méregkeverés képzettség tanulható `Átfogó` képzettségként (ekkor minden típusú méregre vonatkozik), illetve `Átlagos` képzettségként - ekkor választani kell, hogy mely típusú mérgeket tanulja a karakter a lenti három csoportból:

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
| Enyhe rosszullét, hányás | ⭕1  | ⭕- |
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
| :----------- | :----------- | :----------- |
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

<br />

---

> Példa
⚡ **Brutális altató (italméreg)**

```
- Erősség: 10 (a legerősebb)
- Hatás max súlyossága: 1 (alvás)
- Meddig áll el: +4 (1 nap folyadékban)
- Hatóidő: +5 (azonnal)
- 1 komponensű, 1 hordozó közeg, normál adag: +0
```

```
Így a méreg szintje: `20` → Minimum `10. szintű` méregkeverés szükséges
```

A méregellenállást `10` ellen (**méreg erőssége**) kell dobni.

Látható, hogy egy fél óra alatt ható ugyanilyen méreghez elég lenne a `8.szintű` méregkeverés is.

<br />

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
