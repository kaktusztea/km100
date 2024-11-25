## Aura, Mágia Átütése, Mágiaellenállás

<sub>→ [STUDY oldal](https://github.com/kaktusztea/km100/wiki/STUDY.magia.Aura) </sub>

### Aura értéke, jellemzői

Az Aura a karakterek mágikus akaraa és egyben Mágiaellenállása is (Asztrál, Mentál, Fizikai).

Minden lélekkel rendelkező lény rendelkezik Aurával, ez a Tapasztalati Szint (TSz) emelkedésével automatikusan nő (**Aura alap**).

A fentieken túl lehetséges - védelmi, vagy mágikus célokból - konkrét gyakorlati képzéssel fejleszteni az Aurát. Ezt reprezentálja az [Aurafejlesztés](kepzettsegek.primer.misztikus/aurafejlesztes.md) képzettség.

<br />

---
### Aura, mint mágikus akarat: Átütés

Varázsláskor a mágiatudó Aktuális Aura értéke (ez a Mágia **Átütése**) feszül szembe az áldozat **Aktuális Aurájával**. 

<br />

---
### Mágia Átütése vs Mágiaellenállás

```
Mágia Átütése  vs  Mágiaellenállás
```

Varázsláskor a varázsló és a védekező fél is meghatározza **Aktuális Aura** értékékét és ezt vetik össze. A támadónál ezt **Mágia Átütésnek**, a védekezőnél **Mágiaellenállásnak** nevezzük.
Ha az Átütés eléri, vagy meghaladja a Mágiellenállás értékét, akkor a mágia átjutott a védelmen és kifejti hatását.

A Mágiaellenállás egységes, nincs külön asztrál/mentálellenállás, vagy "pajzs". Az Aura mind az Asztrál, Mentál és Fizikai síkon érkező befolyásoló/változtató hatás ellen védelmet nyújt. Egyes hatásokkal szemben alkalmanként gyengébb/erősebb lehet.

#### Aura Alap; AuraErő; Aktuális Aura kiszámolása

```
Aura Alap == Tsz x 2

AuraErő =
   Aurafejlesztés + Önuralom képzettségpróba
   a táblázatos célszámokra
```

```
Aktuális Aura = Aura alap
              + Aura Erő
              - Aura kiterjesztés
```

Az AuraErő egy változó érték, amit úgy kapunk meg, hogy a varázsló és a védekező fél is **Aurafejlesztés** képzettségpróbát dob az **általa önként kiválasztott Nehézségre**. Természetesen választhatják a biztos tudást, amit az `1`-es dobás (k10) által elérhető maximum jelent - ilyenkor nyilván nem kell dobni sem (ez a "Biztos Átütés" a támadó felől, és a "Tudatalatti Mágiaellenállás" a védekező fél felől).

| Aurafejlesztés Próba | AuraErő |
|:--------------------:|:-------:|
|          3   →       |    2    |
|          6   →       |    5    |
|          9   →       |   10    |
|          12  →       |   15    |
|          15  →       |   20    |
|          18  →       |   25    |
|          21  →       |   30    |
|          24  →       |   35    |
|          27  →       |   40    |
|          30  →       |   45    |

```
Ha sikerül a próba:
Aktuális Aura = (2x TSz) + AuraErő

Ha nem sikerül a próba:
Aktuális Aura = (2x TSz)
```

Tehát a **Mágia Átütését** és a **Mágiaellenállást** azonos módon kell meghatározni.

<br />

---
### Tudatalatti mágiaellenállás (TME) / Biztos Átütés

Amennyiben az áldozat nem tud róla, hogy varázsolnak rá, olyankor a Tudatalatti Mágiaellenállása érvényesül, amely a biztos tudásból meglevő AuraErő értékével számol (tehát ha k10-en `1`-es dobott volna, akkor mit ért volna el a próbán). Ugyanígy számoljuk ki a **Biztos Átütés** értékét is - a támadó szempontjából.

```
Önuralom + Aurafejlesztés + 1
  → X AuraErő

TME / Biztos Átütés
  = Aura Alap + (X AuraErő)
```

<br />

---
### Rontott Aurafejlesztés próba

Ha a fent tárgyalt Aurafejlesztés próbát elrontotta a karakter, további negatív hatásokkal kell szembesülnie:

**Védekező**: 1 körig csak az Alap Aurája számít (`2x TSz`), ez idő alatt nem dobhat AuraErőre.

**Mágiatudó**: ugyanaz, mint a Védekezőnél + 1 körig nem képes varázsolni sem

<br />

---
### Mágiaellenállás változása

A Mágiaellenállás nem statikus, körülménytől hangulattól függően, események hatására kis mértékben változhat.
Például Meglepődés / Harc / Érzelmi sokk / másra koncentrálás közben ideiglenesen csökkenhet a Mágiaellenállás, mivel egy időben nehezebb védekezni a fizikai és a felsőbb síkokon. 
Ilyen esetekben a KM kérhet **Összpontosítás** próbát, hogy kap -e büntetést a karakter, vagy nem. Alább egy általános táblázat, hogy nagyjából milyen esetben mivel kell számolnia a védekező félnek.

|                          Hatás, esemény                          |                       Aura Alap diff                        |
| :--------------------------------------------------------------: | :---------------------------------------------------------: |
|                           Érzelmi sokk                           |                       -3  (Asztrális)                       |
|                            Kiégettség                            |                      +1-3 (Asztrális)                       |
|                     Erős koncentrálás másra                      | Összpontosítás próba: [6-9-12-15] Ha nincs meg, -3 Akt.Aura |
|                            Harci láz                             |               +3 Asztrál/Mentál hatások ellen               |
|                         Papi védő áldás                          |                  +⭕X⭕ adott hatások ellen                   |
| Olyan érzelmi befolyás, ami tudat alatt kedvére van a célpontnak |               `-3` ilyen Asztrál hatás ellen                |

<br />

---
### Fizikai ellenállás átalakítással szemben

Ha a mágiatudó közvetlenül a célpont testét szeretné átalakítani, akkor nagyobb fába vágta a fejszéjét, mint akár egy sima asztrális befolyásolással. Az ilyen mágia ellen a (fizikai) Mágiaellenáláshoz bónusz járul:

```
Mágiellenállás fizikai
behatás ellen: +(2x Edzettség)
```

<br />

---
### ⚡Példa

#### Varázsló, mint támadó

```
- TSz: 7 → Aura Alap = 14
- Önuralom: +3
- Aurafejlesztés - 7.szint

- TME / Biztos Átütés
      = Aura Alap (14)
      + (3+7+1)  → 10
      = 24
```

#### Gyanútlan nemesember, mint védekező fél

```
- TSz: 5 → Aura Alap = 10
- Önuralom: `+1`
- Aurafejlesztés - `5.szint`

- TME = Aura Alap (10)
      + (1+5+1)  →  5
      = 15
```

A varázsló megpróbálja asztrális befolyása alá vonni a nemesembert. Úgy dönt, nem dob, neki elég a Biztos Átütés (24), áldozatát jóval gyengébbnek véli.

A nemesember érzékeli az Auraérintést és úgy véli támadója jelentősen erősebb nála - kockázat.
Szeretne `+15`-at elérni az AuraErő dobás hatására, hogy Aura alapjával együtt `25`-as Mágiaellenállást érjen el (`10+15`).

A `15`-ös AuraErőhöz `12`-es célszámot kell megdobnia az `Önuralom + Aurafejlesztés` képzettségpróbán:

```
6 + k10  vs  12
```

Azaz ha legalább `6`-ot dob k10-en, akkor sikerrel jár. Dob: `8`

Ekkor a támadó vs Védő állás így néz ki:

```
24 (Varázsló Mágiájának Akarata)
  vs
25  (Nemesember Mágiaellenálása)
```

A nemesembernek szerencséje volt. Nem tudhatta, mekkora lesz ellenfele Mágiájának Akarata, de jól taktikázott és a kockázatot is megfelelő mederben tartotta. Megpróbálhatott volna `+20` AuraErőre dobni, de mivel annak Nehézség `15`, így annak megdobására csak 20% esélye lett volna (`6 + k10  vs 15`).

A mágiatudó csalódottan horkant fel, mágiája csődöt mondott.

---

🔗 [Varázslás módszerek](095_varazslas_modszerek.md) →

⚜️ [Nyitóoldal](start.md#9-m%C3%A1giarendszer)
