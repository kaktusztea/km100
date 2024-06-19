## Mozgás harcban, mozgás hatása támadások számára

Harc közben nem ugyanazon a pár négyzetméteres területen mozog a karakter, sokszor át kell rohannia segíteni másnak, vagy épp visszavonulnia (már ha sikerült kibontakoznia). A harci körben való mozgás az alábbiak szerint lehetséges.

---
### Maximum mozgás, maximum támadással

```
Max Mozgás egy körben =
   (5 + Gyorsaság) méter
```

Egy karakter egy harci körön belül szabadon mozoghat maximum (`5 + Gyorsaság Tulajdonság`) mennyiségű métert anélkül, hogy elveszítene egyet is támadásaiból.

---
### Maximum mozgás egy körben

Ha a karakter a `Max mozgás` távolságnál mindenképpen nagyobb távot akar megtenni egy körben és még 1 db támadást le is akar adni, akkor azt megteheti az alábbi megkötésekkel:

- Maximum táv: `Max mozgás x 2 (méterben)`
- A körben nem lehet/lehetett ezen kívül más támadása
- Csak [Roham](064_02_harci_taktikak.md#roham) Harci taktikával végezhető a támadás
