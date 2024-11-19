## Képzettségek és fortélyok kapcsolata

Két módszer létezik: **Kiterjesztés** (Normál, Erős) és **Bónusz adása**.

### `1.` Képzettségek kiterjesztése Fortélyokkal

Egyes képzettségek az alap tudást lefedő ismeretek keretein túl is "kiterjeszthetőek", egyesek pedig "felszeletelhetőek" tudásterületekre. A [Szabad Fortélyok](042_szabad_fortelyok.md) jellemzője, hogy mind ilyen képzettség-kiterjesztést végeznek, de egyes egyéb fortélyok is képesek erre. Hogy melyek, azok mindig az adott képzettség adatlapján olvashatóak.

A képzettségkiterjesztésnek két módja van: **Normál** és **Erős**. Ez azt fejezi ki, hogy mennyire szigorú a kapcsolat a képzettség és a fortély között. Ha van egy képzettségpróba, amelynek ismeret területe a KM szerint ezen képzettség alá tartozik ÉS lefed egy kapcsolódó Fortélyt, akkor használjuk ezeket a kiterjesztéseket.

### ⚜️ Normál kiterjesztés

Ebben a kapcsolatban a Fortély megléte nem követelmény, de hiánya esetén levonással dobhat a játékos, mivel a törzstudás (a képzettség maga) nem nyújt az adott területen teljeskörű ismeretet.

```
0.fok: -3
1.fok: +0
2.fok: +2
3.fok: +4
...
```

`0.fok:` ha nincs meg a Fortély, akkor `-3` módosítóval dobjuk a képzettségpróbát

`1.fok:` ekkor simán, alapértékkel dobjuk a képzettségpróbát

`2+.fok`: ha több fokú a fortély, akkor minden további foka `+2` bónuszt ad a próbára

### ⚜️ Erős kiterjesztés

Ekkor a kapcsolat olyan erős a két ismeret között, hogy a fortély követelménnyé válik, amennyiben nincs meg lagalább `1.fokon`, akkor a képzettségpróba nem is dobható.

```
0.fok: letilt
1.fok: +0
2.fok: +2
3.fok: +4
...
```

`0.fok:` ha nincs meg a Fortély, akkor az adott próba nem is dobható, automatikusan sikertelen

`1.fok`: ekkor simán, alapértékkel dobjuk a képzettségpróbát

`2+.fok`: ha több fokú a fortély, akkor minden további foka `+2` bónuszt ad a próbára

<br />

---
### `2.` Fortély mint bónusz

```
Valamilyen bónuszt ad

1.fok: Jellemzően +2
2.fok: Jellemzően +4
3.fok: Jellemzően +6
...
```

Ebben az esetben az adott fortély megléte nem követelmény, viszont ha megvan, akkor valamilyen - jellemzően statikus -, vagy egyedi bónuszt ad az kapcsolódó képzettségre.

---

🔗 [Képzettségpróba, Összhangok](037_kepzettsegproba.md) →

⚜️ [Nyitóoldal](start.md)
