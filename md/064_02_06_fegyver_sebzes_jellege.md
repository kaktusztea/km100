## Fegyver sebzés jellege

Számos paraméter befolyásolja az éppen forgatott fegyver aktuális sebzését.

#### Erőbónusz és Erőhiány

```
Az Erő tulajdonság 1:1-ben
hozzáadódik az SP értékhez.

Ha az Erő értéke negatív,
akkor pedig levonódik.
```

Egyes fegyverek forgatása esetén a karakter fizikai ereje megnöveli az okozott sebzés. Tipikusan azok a fegyverek ezek, amelyek használata során a plusz erő használata felgyorsítja azt, jól kivezethető ívű csapások végezhetők vele. Továbbá számos fegyver van, melynek forgatása **Erő** követelményhez kötött, azaz csak megfelelő fizikumú karakter használhatja. Erről az egyes fegyverek egyéni leírásában találhatunk részleteket, de általánosságban a fenti szabályok az irányadóak.

---
#### Sebzés jellege, páncél SFÉ jellege

```
Szúró, Vágó és Zúzó sebzés
```

Támadáskor fontos momentum annak jellegének meghatározása, valamint az ellenfél vértjének aktuális **Sebzés Felfogó Értéke**, az **SFÉ**, amely mérsékelheti a sebesülést. Ez utóbbi (SFÉ) nem egy konkrét érték, pont a támadás jellegétől és a fegyver esetleges átütéséből adódik.

A harcban használt fegyverek igen sokszínűek, a **km100** rendszere különbséget tesz az általuk okozott sebzés jellege szerint: **⚜️Szúró, ⚜️Vágó és ⚜️Zúzó** támadás.

Egyes fegyverek többféle sebzési formát is lehetővé tesznek, gondoljunk csak a jól ismert hosszú kardra, amellyel szúrni is, vágni is lehet.

---
#### Elsődleges sebzési típus

```
TÉ: -10  → másodlagos sebzési típussal
TÉ: -20  → alkalmatlan sebzési típussal

Jelölése "/" jellel: például "V/S"
V: Vágás;  S: Szúrás;  Z: Zúzás
```

Majdnem minden fegyver rendelkezik egy **elsődleges sebzési típussal**, pl. szúrás. Ha emellett más típusú támadásra is alkalmas, az legtöbbször másodlagos lehet (kivételeket lásd lejjebb az "Egyenjogú sebzési típus" bekezdésben). Ha a karakter nem jelenti be, hogy milyen típusú támadást akar leadni, akkor mindig az elsődleges sebzési típust vesszük megtörténtnek.

Például a hosszú kard: vágás/szúrás (`V/S`). Ekkor az alapértelmezett sebzési típus a vágás. Ha a karakter bejelenti, hogy szúrni szeretne, akkor azt `TÉ:-10` módosítóval teheti meg. Ha pedig zúzni szeretne (amire a fegyver alkalmatlan), akkor – ha a KM engedi – azt `TÉ:-20`-szal teheti meg.

A Harcrendszer végén található **Fegyvertáblázatban** minden fegyver sebzési típusa megtalálható.

---
#### Egyenjogú sebzési típus

```
Jelölése "+" jel: például "S+V"

Nincs levonás egyik sebzés típusnál sem
```

Egyes fegyverekkel többféle sebzési típust lehet használni anélkül, hogy a forgató hátrányba kerülne és levonást szenvedne el a TÉ-ből. Ilyen fegyvereknél az egyes sebzési típusokat "+" jellel választjuk el.

---
#### Átütés

```
Aktuális SFÉ = Vért SFÉ - Átütés
```

Fontos szerep jut még azoknak a fegyvereknek, amelyek rendelkeznek Átütés értékkel (a legtöbb fegyver `Átütés értéke: 0`), mivel a támadott vért megfelelő SFÉ-jének kiválasztása után annak értékéből még le kell vonni az **Átütést** is, így kapjuk meg a vért végleges aktuális SFÉ-jét. Átütéssel olyan fegyverek rendelkeznek, amelyek kifejezetten alkalmasak vértek átlyukasztására legtöbbször azon okból, hogy kis területre koncentrálnak nagy erőt.\
Például: csákány...

---

🔗 [Sebzés](064_02_07_sebzes.md) →

⚜️ [Nyitóoldal](start.md#6-harcrendszer-%EF%B8%8F)
