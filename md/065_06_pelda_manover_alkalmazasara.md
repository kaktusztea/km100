### Példák Manőverek alkalmazására

Lássunk náhány gyakorlati alkalmazást!
#### ⚡Egyszerű példa egy Manőver alkalmazására

**Rühes** külön ismeret nélkül megpróbálja lefegyverezni ellenfelét. Mindkettőjüknél hosszú kard van, Rühes kicsivel jobb vívó.

Rühes értékei:
- `KÉ: 15`
- `TÉ: 55 / 45`
- `VÉ: 125`
- `Manőver Alap = 41 HM / 10 = 4`

Ellenfelének értékei:
- `VÉ: 115`
- `Manőver Alap = 32 HM / 10 = 3`

A Lefegyverzés manőver nehézsége: `10`\
A Lefegyverezés fázisai: sikeres Végrehajtás (`V`) és Ellenpróba (`E`) szükséges.

**1. Végrehajtás**  (`V`)
- Rühes `+20`-al leadja támadását
- `TÉ = 55+20+k100 = 132`, ez nagyobb mint ellenfele `VÉ`-je
- Sikeres Végrehajtás

**2. Ellenpróba**  (`E`)
- Tetves dobása:  `4` (Manőver Alap) + `k10`
- Célszám: `3 + 10 = 13` (ellenfél `HM/10 + Lefegyverzés nehézsége`)

```
A próbadobás így:   (4 + k10)  vs.  13
```

Tehát ha Rühes legalább  `9`-et dob  `k10`-en, akkor az **Ellenpróba** is sikeres és így az egész manőver is, ellenfele kardja kihullik annak kezéből. Látható, hogy a **Lefegyverzés** a [Manőver Keret](017_03_manover_keret.md) használata nélkül nagyjából azonos tudású ellenfelek között nem könnyű művelet.

Ha Rühes `2` pontot költött volna el Manőver Keretéből, akkor már `+4` járna a próbadobására ( `8+k10`) és így már `5`-ös dobással is sikert érhetne el. Ha viszont ellenfele is elköltött volna `1` pontot, akkor az ő `+2` bónusza mérsékelné Rühes `+4`-es bónuszát és ismét csak a `7`-es dobással(vagy felette) lenne eredményes.

<br/>

---
#### ⚡Összetettebb példa egy Manőver alkalmazására

Tetves **Gáncsolást** akar alkalmazni. Ellenfelénél kard van, nála tőr és elkölt `1` pontot Manőver Keretéből. Bejelenti, hogy ezen kívül `2 pontot` vállal is (lásd [Vállalás](065_02_manover_vegbevitele.md#v%C3%A1llal%C3%A1s)) a cél érdekében → `VÉ:-20`

Tetves értékei:
- KÉ: `15`
- TÉ: `55`
- VÉ: `125` ; A Vállalás miatt csak: `105`
- `HM/10`: `41/10 = 4`

Ellenfelének értékei:
- `VÉ: 140`
- `HM/10`: `32/10 = 3`

A Gáncsolás manőver nehézsége: `8` (belharcban `5` lenne, de ez most nem áll fenn)\
Gáncsolás fázisai: sikeres Végrehajtás (`V`) és Ellenpróba (`E`) szükséges.

**1. Végrehajtás**
- Tetves leadja támadását.
- `TÉ = 55+20+k100 = 142`, ez nagyobb mint ellenfele `VÉ`-je
- Sikeres Végrehajtás

**2. Ellenpróba**
- Tetves manőver próbája: `4 + 2 + 2 = 8`
- `1` pont bónusza (`+2`) + vállalás (`+2`)


```
Célszám = 8 + 3 + 2 = 11
```

(HM/10 + Gáncsolás nehézsége + a fegyverméretek különbözősége miatt a KM megnöveli `2`-vel a célszámot)

```
Próbadobás:  (8 + k10)  vs.  11
```

Tehát ha Tetves legalább `3`-at dob `k10`-en, akkor az **Ellenpróba** (`E`) is sikeres és így az egész manőver is az, kikaszálta ellenfele lábát. Ha nem sikerült volna a manőver, akkor ellenfele következő rendes visszatámadása ellen Tetves `-20 VÉ` büntetés szenvedett volna el (a Vállalás miatt).
