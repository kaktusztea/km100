## Példalövészet

Tetves, a tolvaj-bérgyilkos egy raktár ablakából, nyílpuskával les a sikátorban közelgő áldozatára, egy tehetős kalmárra, aki éppen hazafelé battyog.

A könnyű nyílpuska **Osztója:** `4`

### Tetves Célzó Értéke

Ezt már karakteralkotáskor kiszámoltuk, így játék közben már nincs szükség semmilyen számításra. Az érthetőség kedvéért azért listázzuk a `CÉ` komponenseit.

```
CÉ = -30 (Konstans)
     + 6 (Önuralom 2x)
     + 16 (nyílpuska CÉ)
     + +15 (CM)
     + 4 (lövészet)
     = 11
```

<br />

---
### A célpont Védő Értéke

- Mozgás szorzó: `5x` (lassan mozgó)
- Távolság: `15 méter`
- Cella:  (`15m/4 ↑`) → `4` (az osztásnál felfelé kell kerekíteni)

$$VÉ = {5(lassan\ mozgó)+0(normál\ méret)+0(jól\ látható)}\ x\ {15(távolság)\over 4(nyílpuska\ Osztója)}$$

```
VÉ = 5x4 = 20
```

<br />

---
### Tehát a próba

```
11 + k100  vs  20
```

azaz ha Tetves legalább `9`-et dob `k100`-on, akkor találatot ér el. Könnyű cél...

Dob `k100`-zal, az eredmény `31`, végső `CÉ = 11+31 = 42`, tehát eltalálta a célt, dobhatja a sebzést.

---
De lássunk egy bonyolultabb esetet.

⭕TODO: 2. példa⭕
