### Manőver végbevitelének lépései

A játékosnak a kör elején be kell jelentenie, hogy Manővert akar alkalmazni és azt is, hogy melyiket. Ezután a karakterek kezdeményezést dobnak (kivéve pl. a **Meglepetés** szituációt), majd mikor az alkalmazóra kerül a sor, jön a Manőver. Ha a KM úgy látja jónak, megtilthatja adott szituációban a Manőver alkalmazását. Amennyiben a játékos ezt a döntést nem képes kulturáltan kezelni, a KM növelje intenzíven a Manőver nehézségét...

Minden **Manővernek** lehetnek egyéni, speciális követelményei, ezek a saját leírásuknál találhatóak meg.

Egy Manőver alkalmazása – jellegétől függően – legfeljebb az alábbi három (de nem kötelezően az összes!) alapfázisból állhat. Mindegyik opcionális - hogy melyikre van szükség, azt az adott Manőver leírásánál találjuk. Végrehajtásuk sorrendjében:

<br />

⚜️ `1.` **Megakasztás**\
Az **Ellenfél** teszi. Sima (extra) támadás, ha sikeres, a Manőver rögtön sikertelen.

⚜️`2.` **Végrehajtás**\
Manővert végző teszi. Sikeréhez sebzést érő támadás szükséges `TÉ+20` módosítóval, de nem okoz sebet. Aktuális, fegyveres `TÉ` számít. Ha sikertelen, a Manőver rögtön sikertelen.
Azért dobjuk ezt előbb, mert ez ad gyorsabban eredményt 🔆

⚜️`3.` **Ellenpróba**\
Manővert végző teszi. `Próbadobás vs Célszám`

---
### Megakasztás (M)

A Megakasztás az első fázis a Manőver végrehajtása során.\
Megelőző támadási forma, melyre **az Ellenfél** jogosult teljes, fegyveres `TÉ` harcértékével. Ez egy soron kívüli extra támadás. Csak akkor szükséges, ha az adott típusú manőver fázisai között ez szerepel.

Ha az így érkező támadás sebző, akkor a Manőver nem sikerült. Tipikus példája a [Belharcba kerülés](065_05_altalanos_manoverek.md#belharcba-kerülés).

<br />

---
### Végrehajtás (V)

Nem más, mint egy támadás az aktuális, **fegyveres TÉ** értékkel, melyhez `+20 TÉ` módosító járul. Ha ez a támadás sikeres, akkor a Végrehajtás is sikeres (sebzés nincs). Ne feledjük, hogy a `TÉ` értékébe beleszámít az esetleges több támadás levonása is (`-10` támadásonként)!

Ha a **Végrehajtás** sikertelen, akkor a helyzet megvolt, de nem sikerült kihasználni. 

<br />

---
### Ellenpróba (E)

```
Manőver Alap + k10
       vs
Manőver Alap (Ellenfél)
 + Manőver Nehézség       
```

#### ⚜️ Dobás módosítói

| Módosítók             | Érték, Leírás                                                      |
| --------------------- | ------------------------------------------------------------------ |
| Manőver Pont          | Opcionális. Pontonként `+2` bónuszt ad. Maximum `2 pont` költhető. |
| Követelmények nélkül  | `-3`, ha nem teljesülnek a Manőver Követelményei                   |
| Belharc fortély fokai | `+2/fok` az alkalmazó oldalán (Belharci Manőver esetén)            |

#### ⚜️ Célszám módosítói

| Módosítók             | Érték, Leírás                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Manőver Pont          | Ellenfél alkalmazhatja opcionálisan. Pontonként `+2` bónuszt ad. Maximum `2 pont` költhető. A dobások előtt kell bejelenteni. |
| Újrapróbálkozás       | `+2` → az Ellenfél már számít rá                                                                                              |
| Módosító körülmények  | `[-5;+5]` KM által megadott +/- érték. Körülmény függő nehezítés / könnyítés. Például "bódulat" esetén.                       |

| Belharci Manőver módosítók | Érték, Leírás                                          |
| -------------------------- | ------------------------------------------------------ |
| Belharc fortély fokai      | `+2/fok` az Ellenfél oldalán (Belharci Manőver esetén) |
| Testméret különbség        | `[-2; +2]`                                             |
| Páncél különbség           | `[-2; +2]`                                             |

Az Ellenpróba dobása nem mást fed, mint hogy a karakter képes -e megteremteni maga számára a lehetőséget, úgymond „megágyazni magának”, hogy egyáltalán megkísérelhesse a **Manővert**. A harcban ez helyezkedést, „pozícióba kerülést” jelent, amelynek sikere függ a karakter és Ellenfelének **Manőver Alapjától**, a Manőver **Nehézségétől** és egyéb módosító körülményektől. A játékban logikailag az **Ellenpróbának** kéne előbb jönnie, de mivel a a **Végrehajtás** gyorsabban számolható, azt dobjuk előbb (ha van olyan fázis).

Az **Ellenpróba** dobása során a KM meghatározza a próba **Célszámát**, a játékos, pedig veszi [Manőver Alapját](065_01_manover_alap.md), esetlegesen felhasznál [Manőver Pontokat](065_02_manover_pontok.md), majd dob hozzá `k10`-el. Ha a végső érték eléri a célszámot, akkor az **Ellenpróba** **sikeres volt.**

Ha csak az **Ellenpróba** az adott Manőver követelménye, akkor annak sikere esetén az egész **Manőver** automatikusan sikeresnek tekinthető.

A KM a körülményektől és szituációtól függően adhat pozitív/negatív célszám módosítót `[+5;-5]` értékhatáron belül. Sőt, a KM dönthet úgy, hogy a feltételei adottak, nincs szükség Ellenpróbára.

<br />

---
### Követelmények nélkül

```
Követelmények nélkül:
  Ellenpróba célszám: +3
```

A Manőverek végrehajtásával bárki próbálkozhat, aki az adott Manővernél leírt **Végbevitel-követelményeket** teljesíti.

Amennyiben nem teljesíti, akkor is nekifuthat, de az **Ellenpróba** dobásánál a célszám számára `3`-al megemelkedik.

---
### Újrapróbálkozás

```
+2 Nehézség
 újrapróbálkozásnál
```

A Manőver ha sikeres volt, ha nem – az Ellenfél legközelebb már számít az ilyen jellegű támadásra, ezért amennyiben ismét ezt a Manővert kísérli meg az alkalmazó, akkor az **Ellenpróba** során a célszám már `+2`-vel nőni fog. Ez a büntetés **nem** halmozódik.

A fenti módosító akkor is megjelenhet, ha az Ellenfél az alkalmazót már látta korábban küzdeni és egy konkrét Manővert gyakran alkalmazni. KM dönt.

---
### Fegyverméret-kategóriák

A Fegyverméret-kategóriák adta különbségek az **Ellenpróbánál** (`E`) módosítóként **nem** szükségesek amennyiben a Manőverben van kötelező (**M**)egakasztás, vagy (**V**)égrehajtás fázis, mert ez a hatás résztvevők harcértékeiben már benne foglaltatnak.

---
🔗 [Általános Manőverek listája](065_05_altalanos_manoverek.md) →
