## Támadások száma fegyverrel

```
Alapeset:  minden fegyver támadásainak száma: 1 / kör.
```
(néhány kivételnél ez kevesebb. Lásd a fegyver táblázatot)

---
### „Harcmodor-Sebesség”

Egy karakter plusz támadásainak száma attól függ, hogy milyen fegyvert forgat, mennyire képzett annak Harcmodorában, és hogy mennyire fürge (`Gyorsaság` tulajdonság).

Számszerűen: az aktuális fegyverhez tartozó harcmodor-képzettség szintje és a Gyorsaság tulajdonság összege határozzák meg az ún. **Harcmodor-Sebesség**”értéket. Ez – mint – sejthető harcmodoronként egyedi érték.

```
„Harcmodor-Sebesség” = aktuális Harcmodor szint + Gyorsaság tulajdonság
```

---
### „Fegyver-Sebesség”

Szintén minden fegyvernek van egy egyedi Sebesség értéke, az ún. `„Fegyver-Sebesség”`. Minél kisebb ez a szám, annál fürgébb, minél nagyobb, annál lomhább az adott fegyver.

---
### Plusz támadások száma (fegyverrel)

A plusz támadások számát úgy kapjuk meg, hogy megvizsgáljuk, a `„Fegyver-Sebesség”` hányszor van meg a karakter aktuális „Harcmodor-Sebesség” értékében (lefelé kerekítve).

```
Plusz támadások (db) = (Harcmodor Sebesség) / (Fegyver Sebesség)
```

---
### ⚡Példa több fegyveres támadásra

- Fegyver: Hosszú kard: `Fegyver-Sebesség: 6`
- Harcmodor: `Kardvívás – 4.szint`
- Gyorsaság tulajdonság: `+3`

Ekkor az aktuális Harcmodor-Sebesség érték:  `4+3 = 7`

Mivel ez elérte a`6`-os értéket, ezért `+1` támadás – összesen tehát már `2db` jár körönként. A 3 támadást `12`-es, a 4 támadást pedig `18`-as `„Harcmodor-Sebesség”` értéknél kapja meg.

```
Minden újabb támadás során az aktuális Támadó Értékre -10 levonás jár!
```

- Második támadás: `-10TÉ`
- Harmadik támadás: `-20TÉ`, stb

További támadásokat `Kétkezes Harc` során szerezhet a karakter. Lásd a [Kétkezes Harc](065_04_ketkezes_harc.md) fejezetet!

---
---
## Támadások száma varázsláskor

### "Varázskeret"
```
 "Varázskeret" = Mágia Tradíció szint + ⭕Gyorsaság⭕ tulajdonság 
```

Varázslásnál nagyjából ez felel meg a "Harcmodor-Sebességnek", annyi különbséggel, hogy a "Harcmodort" itt a "Mágia Tradíció" helyettesíti, annak szintje számít.


### „Formula-Sebesség”
```
„Formula-Sebesség” = 4 + Varázslat Erőssége   (Magasmágiánál a legerősebb mozaik)
```

Varázslásnál ez felel meg a "Fegyver-Sebességnek", értéke minél magasabb, annál lassabban jön létre a varázslat.

Látható, hogy az apró, kis változtató erejű mágiákból többet jóval könnyebben el lehet varázsolni, mint a nagyobb hatalmú varázslatokból.


### Varázskeret csökkentése varázsláskor
```
Varázskeret = Varázskeret - "Formula Sebesség"
```

Azt kell megvizsgálni, hogy a `"Formula-Sebesség"` eléri -e a **Varázskeretet**.
- Ha egyenlő, vagy felette van, akkor az aktuális  `„Formula-Sebesség”` értékét levonjuk a **Varázskeretből**. A karakter a maradék keretből gazdálkodhat még a kör hátralevő részében.
- Ha alatta van, akkor a varázslat "átcsúszik" a következő körre és rögtön annyival csökkenti a következő kör **Varázskeretét**, amennyivel alatta volt.

A **Varázskeret** minden kör elején eredeti értékére "töltődik vissza".

