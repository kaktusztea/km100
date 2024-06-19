## Támadások száma varázsláskor

### Varázskeret

```
 Varázskeret =
      Tapasztalati Szint
    + Mágia Tradíció szint
    + Összpontosítás szint

    + Gyors varázsló fortély bónusza
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
