## Támadások száma fegyverrel, mágiával, Akció, Mozgás

```
Alapeset:
 fegyverek támadás száma: 1 / kör
```
(néhány kivételnél ez kevesebb. Lásd a fegyver táblázatot)

---
### Akció fogalma

Az Akció a harcban megtett elemi cselekedet. 1 Akció az alábbiak cselekedetekkel egyenértékű:
- 1 harci támadás
- 1 Manőver
- 1 Varázslás

A körön belüli Akciók számát lent írjuk le.

---
### Harckeret

Egy karakter plusz támadásainak száma attól függ, hogy milyen fegyvert forgat, mennyire képzett annak Harcmodorában, és hogy mennyire fürge (`Gyorsaság` tulajdonság).

Számszerűen: az aktuális fegyverhez tartozó harcmodor-képzettség szintje és a Gyorsaság tulajdonság összege határozzák meg az ún. **Harckeret** értéket. Ez – mint – sejthető harcmodoronként egyedi érték.

```
Harckeret = 
    aktuális Harcmodor szint
  + Gyorsaság tulajdonság
```

---
### Fegyver Sebesség

Szintén minden fegyvernek van egy egyedi **Sebesség** értéke. Minél kisebb ez a szám, annál fürgébb, minél nagyobb, annál lomhább az adott fegyver.

---
### Plusz támadások száma (fegyverrel)

Az alap 1 támadáson felül kapott **plusz** támadások számát úgy kapjuk meg, hogy megvizsgáljuk, a `„Fegyver-Sebesség”` hányszor van meg a karakter aktuális „Harckeret” értékében (lefelé kerekítve).

```
Plusz támadások (db) =
   Harckeret / (Fegyver Sebesség)
```

---
### ⚡Példa több fegyveres támadásra

- Fegyver: Hosszú kard: `Fegyver-Sebesség: 6`
- Harcmodor: `Kardvívás – 4.szint`
- Gyorsaság tulajdonság: `+3`

Ekkor az aktuális Harckeret érték:  `4+3 = 7`

Mivel ez elérte a`6`-os értéket, ezért `+1` támadás – összesen tehát már `2db` jár körönként. A 3 támadást `12`-es, a 4 támadást pedig `18`-as **Harckeret** értéknél kapja meg.

```
Minden újabb támadás során az aktuális Támadó Értékre -10 levonás jár!
```

- Második támadás: `-10TÉ`
- Harmadik támadás: `-20TÉ`, stb

További támadásokat `Kétkezes Harc` során szerezhet a karakter. Lásd a [Kétkezes Harc](060_13_ketkezes_harc.md) fejezetet!

---
---
## Támadások száma varázsláskor

### Varázskeret

```
 Varázskeret =
     Mágia Tradíció szint
    + Összpontosítás szint
```

Varázslásnál nagyjából ez felel meg a **Harckeretnek**.


### Formula Sebesség

```
Formula-Sebesség =
   Max Erősség + Max Komplexitás
```

A varázslatban használt összes formula közül a legmagasabb Komplexitás értéket és a legmagasabb Erősség értéket kell összeadnunk.

Varázslásnál ez felel meg a **Fegyver Sebességnek**, értéke minél magasabb, annál lassabban jön létre a varázslat.

Látható, hogy az apró, egyszerű, kis változtató erejű mágiákból többet jóval könnyebben el lehet varázsolni, mint a nagyobb hatalmú varázslatokból.

### Varázskeret csökkentése varázsláskor
```
Varázskeret =
   Varázskeret - "Formula Sebesség"

Következő körbe átcsúszó varázslatot
csak a kör elején lehet megkezdeni!
```

A **Varázskeret** minden kör elején eredeti értékére "töltődik vissza".

Kör elején azt kell megvizsgálni, hogy a **"Formula-Sebesség"** eléri -e a **Varázskeretet**.

`1.` Ha egyenlő, vagy alatta van, akkor az aktuális **"Formula-Sebesség"** értékét levonjuk a **Varázskeretből**. A karakter a maradék keretből gazdálkodhat még a kör hátralevő részében.

`2.` Ha felette van, akkor a kört teljes egészében varázslással tölti a mágiatudó, a varázslat "átcsúszik" a következő körre és rögtön annyival csökkenti a következő kör **Varázskeretét**, amennyivel alatta volt.

Egy nagy, hosszú varázslat akár sok körön át is "csúszhat", ez idő alatt a varázstudó mozdulatlanul állhat, vagy legfeljebb lassú, egyenletes sétát végezhet.

---
### Mozgás harcban, mozgás hatása támadások számára

Harc közben nem ugyanazon a pár négyzetméteres területen mozog a karakter, sokszor át kell rohannia segíteni másnak, vagy épp visszavonulnia (már ha sikerült kibontakoznia). A harci körben való mozgás

#### Maximum mozgás, maximum támadással

```
Max Mozgás egy körben =
   (5 + Gyorsaság) méter
```

Egy karakter egy harci körön belül szabadon mozoghat maximum (`5 + Gyorsaság Tulajdonság`) mennyiségű métert anélkül, hogy elveszítene egyet is támadásaiból.
#### Maximum mozgás egy körben

Ha a karakter a `Max mozgás` távolságnál mindenképpen nagyobb távot akar megtenni egy körben és még 1 db támadást le is akar adni, akkor azt megteheti az alábbi megkötésekkel:

- Maximum táv: `Max mozgás x 2 (méterben)`
- A körben nem lehet/lehetett ezen kívül más támadása
- Csak [Roham](060_11_harci_taktikak.md#roham) Harci taktikával végezhető a támadás
