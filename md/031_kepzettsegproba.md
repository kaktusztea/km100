## Képzettségpróba

⭕TODO: belső tartalomjegyzék frissítése
  - [Vállalás](#vállalás)
  - [Próba biztos tudásból](#próba-biztos-tudásból)
  - [Próba képzetlenül](#próba-képzetlenül)
  - [Összetett képzettségpróba, Másodlagos próbadobások](#összetett-képzettségpróba-másodlagos-próbadobások)
  - [Összhangok](#összhangok)
  - [Sérülés hatása képzettségpróbára](#sérülés-hatása-képzettségpróbára)


Vesszük az adott szituációban épp szükséges Tulajdonság értékét (KM mondja meg, hogy melyiket), hozzáadjuk a **Képzettség** értékét, majd dobunk `k10`-es kockával és a fentieket összeadjuk. Ha a kapott szám nagyobb, vagy egyenlő a Célszámmal, akkor a próba sikerült.

```
Tulajdonság + Képzettség + k10   vs.  Célszám
```

| Képzettségpróba<br /><sub>(dobás k10-el)</sub> | Célszám  |
| ------ | :-----: |
| Könnyű          | 6  |
| Átlagos         | 9  |
| Nehéz           | 12 |
| Nagyon nehéz    | 15 |
| Rendkívül nehéz | 18 |
| Emberfeletti    | 21 |

Ha a KM úgy látja, hogy az adott próbánál több Tulajdonság is szerepet játszik, akkor a szükséges Tulajdonságok átlagával kell számolni.

---
### Vállalás

A Vállalás azt jelenti, hogy (ha a KM is beleegyezik) képzettségpróba esetén kaphatsz legfeljebb `+3` bónuszt a próbára - Te döntöd el mennyit. Minél többet vállalsz, annál nagyobb veszélynek teszed ki magad. Ugyanis a próba előtt „Vállalás próbát" kell dobni:

```
k6 vs. (a vállalás értéke)
```

> **Fontos**: a Vállalás értéke nem haladhatja meg képzettséged aktuális értékét!

Ha `k6`-on a Vállalás értékével megegyezőt, vagy kisebbet dobsz, akkor kritikus, halálos hibát vétesz és természetesen nem dobhatsz képzettségpróbát se. Ebből látszik, hogy vállalni csak nagyon fontos, ritka esetben van értelme. Úgy foglalhatjuk össze, hogy mikor vállalsz, olyankor megpróbálkozol valami olyan dologgal, ami hatékonyabb, mint jelenlegi tudásod, de még nem gyakoroltad be rendesen (pl. csak ellested a mesteredtől), így a rontásra is nagyobb az esélyed.

A fenti példánál maradva egy 2-es Vállalás esetén már a következőképpen fest a próba:

```
2 (Ügyesség) + 5 (Mászás) + 2 (Vállalás)+ k10   vs.  15 (Nagyon nehéz)

Azaz: (9+k10)  vs  15
```

Ez sokat dob az esélyeken, de megvan a rizikója is: ha a fenti karakter a dobás előtt a Vállalás-próbánál k6-on 1-et, vagy 2-t dob, akkor Halálos hibát vét!

> **Fontos**: összetett, több dobást igénylő képzettségpróbánál nem alkalmazható Vállalás! (pl. megmászni a nagy hegyet).

---
### Próba biztos tudásból

Bizonyos képzettségeket csak biztos tudásból lehet megpróbálni, nincs lehetőség képzettségpróba dobására. Tipikusan a „Tudok-e valamit róla?"-jellegű határozottan eldönthető esetekben. Ilyenkor a KM dönti el, hogy az adott képzettségszinttel az adott feladat megoldható, avagy sem.

---
### Próba képzetlenül

```
→ +3 a próba nehézségére
→ Fizikai képzettségeknél nincs büntetés
```
Ha a karakter egyáltalán nem jártas az adott képzettségben (vonatkozó értéke nulla), akkor - ha a képzettség leírásánál engedélyezett a képzetlen dobás - ugyanúgy próbát dob, mint bárki, de a **célszám `3`-al emelkedik**. Fizikai képzettségeknél **nem jár** a `3`-as, célszám emelő büntetés.

Ha az adott képzettséget nem lehet képzetlenül megpróbálni, akkor a KM egyszerűen megtagadja a próbát, automatikusan sikertelennek véve azt.

---
### Összetett képzettségpróba, Másodlagos próbadobások

Ha a karakternek egy olyan összetett feladatot kell elvégeznie, ami nem intézhető el 1db dobással (pl. megmászni egy hegyet, vagy rettentő magas várfalat, esetleg órákon keresztül verset szavalni), akkor igazságtalan lenne a maximális nehézséget többször megdobatni vele, hiszen így drasztikusan lecsökken az esélye a sikerre. Ilyenkor a következő módszert használjuk:

- A játékos dob egy próbát az indokolt maximális nehézségre (pl. „Nagyon nehéz" (`Célszám:12`))
- Ezután dob több (a KM dönti el, hány) próbát **1 fokozattal (-3 célszám) alacsonyabb nehézség ellen**. Pl. (`2db Nehéz próbát`). Így a siker eloszlása sokkal fokozatosabb és a biztos tudást is jobban jutalmazzuk, valamint elkerüljük, hogy egy kezdő - csak azért, mert szerencséset dobott - egy hosszú, részletes, tudását jóval meghaladó feladatot „véletlenül" megcsinálhasson.
- Hogy a másodlagos dobásból hány kell, az főleg attól függ, hogy a feladat „milyen hosszú", mennyire „többlépcsős".
- Ha nagyon finom bontást akarunk, akkor `akár 2 fokozattal` (-6  célszám) alacsonyabb nehézségre is dobathatunk akár így is: Nagyon nehéz (1db), Nehéz(1db), Átlagos (1db).

> Példa ⚡ Megmászni egy 200 ynevi láb magas, omladékos hegyet

- Tetves, a tolvaj `Mászás képzettsége: 7`, `Ügyessége: +2` , így `8+2=9`-re dob majd rá `k10`-el.
- A próba „Nagyon nehéz" (`Célszám: 15`)
- Mivel az út hosszú, nem intézhető el a dolog 1db dobással, a KM `2db Másodlagos próbát` ír elő.
- Ekkor a próbák célszámai: `15`, `12`, `12` (azaz `50%`, `80%` és `80%` esély a sikerre). Ezzel kb. `30%`-a van a teljes feladat sikerére (`0.5 x 0.8 x 0.8`). Látható, hogy az összetettebb feladatok nagyobb fokú biztos tudást igényelnek.
- Tehát a próbák:

```
- 1x Nagyon nehéz (15)
- 2x Nehéz        (12)
```

⭕ **TODO**: Kidolgozni további példákat⭕

---
### Összhangok

Vannak olyan esetek, amikor egyes képzettségek ismerete helyettesítő segítséget nyújthat más képzettségek használatakor. Az ilyet nevezzük Összhangnak.

Ekkor a helyettesítő képzettség `1/3`-a helyettesíthető be az elsődleges képzettséghez.

❗**Fontos**: a helyettesítő értékek NEM adódnak hozzá a helyettesített képzettséghez, hanem kiváltják azt.

Tehát:

```
- (Szint/3) működik behelyettesítő értékként
- Maximum elérhető szint Összhangokkal: 5
- lefelé kerekítünk
```

A fentieknek csak kismesteri (`6`.) szint **alatt** van csak értelme, azaz a helyettesítő képzettség(ek) legfeljebb `5.szintig` adhatnak helyettesítő értéket.

#### ⚡Példa: Nyomozás összhangokkal

A karakter egy bűntény helyszínén gyanús személyekkel találkozik. Kikérezné őket, **Nyomozás** képzettségpróbát kéne dobnia. Mivel **Nyomozás** képzettsége csak `2.szintű`, ezért egy kapcsolódó képzettsége segítségére támaszkodik, amiben sokkal járatosabb és le is fedi az aktuális szituációban szükséges ismeretet. A KM az adott helyzetben ezt jól megindokoltnak látja, így engedélyezi.

- Nyomozás `2.szint`
- Emberismeret: `9.szint`  (Összhang Nyomozás képzettséggel)

Ebben az esetben az **Emberismeret** képzettség az, amely helyettesítő képzettségként működik. Mivel a jelen próbához az **Emberismeret** Összhangként kapcsolódik, ezért annak `1/3`-a működhet **Nyomozás** képzettségként (a próba idejére): `9/3 = 3`

Tehát a próbát `3 + Érzékenység  vs  Próba célszám` értékekkel dobja.


---
### Sérülés hatása képzettségpróbára

Ha megsérül a karakter, képzettségpróbáira levonások járnak. Hogy mennyi, az attól függ, hogy melyik [sebesülés kategóriában](060_01_eletero.md#sebes%C3%BCl%C3%A9s) van, illetve hogy fizikai mozgást igénylő, vagy nem igénylő képzettségét teszi próbára:

|      | S1  | S2 | S3 | S4 |
| ---- | :----: | :----: | :----: | :----: |
| **fizikai** | -  | -2 | -4 | -6 |
| **egyéb**   | -  | -  | -1 | -3 |
