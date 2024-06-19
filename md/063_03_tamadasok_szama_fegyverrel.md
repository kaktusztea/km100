## Támadások száma fegyverrel

```
Alapeset:
 fegyverek támadás száma: 1 / kör
```
(néhány kivételnél ez kevesebb. Lásd a fegyver táblázatot)

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

További támadásokat `Kétkezes Harc` során szerezhet a karakter. Lásd a [Kétkezes Harc](064_04_ketkezes_harc.md) fejezetet!
