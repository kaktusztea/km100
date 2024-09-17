## Példalövészet

Tetves, a tolvaj-bérgyilkos egy raktár ablakából, nyílpuskával les a sikátorban közelgő áldozatára, egy tehetős kalmárra, aki éppen hazafelé battyog.

A könnyű nyílpuska **Osztója:** `4`

### Tetves Célzó Értéke

```
CÉ = -30 (Konstans) + 6 (Önuralom 2x) + 16 (nyílpuska) +15 (CM) + 4 (lövészet) = 11
```

<br />

### A célpont Védő Értéke

$$ VÉ = {5(lassan\ mozgó)+0(normál\ méret)+0(jól\ látható)}\ x\ {15(távolság)\over 4(nyílpuska\ osztója)}$$


Az osztásnál felfelé kell kerekíteni, `15/4` → `4`.

```
VÉ = 5x4 = 20
```

<br />

### Tehát a próba

```
11 + k100  vs  20
```

azaz ha Tetves legalább `9`-et dob `k100`-on, akkor találatot ér el. Könnyű cél...

Dob `k100`-zal, az eredmény `31`, végső `CÉ = 11+31 = 42`, tehát eltalálta a célt, dobhatja a sebzést.

De lássunk egy bonyolultabb esetet.

⭕TODO: 2. példa⭕
