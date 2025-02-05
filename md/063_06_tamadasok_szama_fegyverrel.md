## Támadások száma fegyverrel

```
Alapeset:
 fegyverek támadás száma: 1 / kör
```

Néhány kivételnél ez kevesebb. Lásd a [Fegyver](068_00_fegyverek.md) táblázatot!

---
### Harckeret (harcmodoronként)

Egy karakter plusz támadásainak száma attól függ, hogy milyen fegyvert forgat, mennyire képzett annak Harcmodorában, és hogy mennyire fürge (`Gyorsaság` tulajdonság).

Számszerűen: az aktuális fegyverhez tartozó harcmodor-képzettség szintje és a Gyorsaság tulajdonság összege határozzák meg az ún. **Harckeret** értéket. Tehát harcmodoronként egyedi érték.

```
Harckeret = 
    aktuális Harcmodor szint
  + Gyorsaság tulajdonság
```

A **Harckeret** értéke a [Harckeret növelés](fortelyok.harci/harckeret_noveles.md) fortély segítségével emelhető tovább.

<br />

---
### Fegyver Sebesség

Szintén minden fegyvernek van egy egyedi **Sebesség** értéke. Minél kisebb ez a szám, annál fürgébb, minél nagyobb, annál lomhább az adott fegyver.

<br />

---
### Plusz támadások száma (fegyverrel)

Az alap `1` támadáson felül kapott **plusz** támadások számát úgy kapjuk meg, hogy megvizsgáljuk, a `„Fegyver-Sebesség”` hányszor van meg a karakter aktuális „**Harckeret**” értékében (lefelé kerekítve).

```
Plusz támadások (db) =
   Harckeret / (Fegyver Sebesség) ↓
```

<br />

---
### TÉ levonás támadásonként

```
TÉ:-10 minden újabb támadásnál
  aktuális Támadó Értékre.
  Additív.
```

```
Második támadás: `TÉ:-10`
Harmadik támadás: `TÉ:-20`, ...
```

A fenti módosítóknak matematikai oka van: így kerüljük el a plusz kapott támadás okozta radikális ugrást az 1 körön belül leadott támadások sikeressége kapcsán. Ne feledjük: legrosszabb esetben még így is **Védő Érték csökkenést** okoz minden támadás, így a plusz támadások ereje már önmagában is elég hangsúlyos.

<br />

---
### ⚡Példa több támadásra

- Fegyver: Hosszú kard: `Fegyver-Sebesség: 6`
- Harcmodor: `Kardvívás – 4.szint`
- Gyorsaság tulajdonság: `+3`

Ekkor az aktuális Harckeret érték:  `4+3 = 7`

Mivel ez elérte a`6`-os értéket, ezért `+1` támadás – összesen tehát már `2db` jár körönként. A `3.` támadást `12`-es, a `4.` támadást pedig `18`-as **Harckeret** értéknél kapja meg.

További támadásokat `Kétkezes Harc` során szerezhet a karakter. Lásd a [Kétkezes Harc](065_04_ketkezes_harc_szabalyai.md) fejezetet!

---

🔗 [Támadások száma varázsláskor](063_07_tamadasok_szama_varazslaskor.md) →

⚜️ [Nyitóoldal](start.md#6-harcrendszer-%EF%B8%8F)
