## Célzó Érték számítása

Mikor a támadó lövést, vagy hajítást végez, a Célzó Értékét állítja szembe a célpont távolsági Védő Értékével. A Célzó Érték kiszámolása a következőképpen történik - még karakteralkotási időben.

```
Támadó CÉ = -30 + CM + Harcmodor CÉ + (2 x Önuralom/Erő) + Fegyver CÉ + Mf-bónusz
```

|     **Összeadandó értékek**     | **Leírás**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              `-30`              | Konstans. Ez az érték gyakorlatilag a célpont Védő Érték alapját adná, de mivel itt csak 1x (karakteralkotáskor) kell vele számolni, ezért a számolás meggyorsítása miatt átkerült ide.                                                                                                                                                                                                                                                                                                                           |
|               CM                | Célzóérték Módosító. Szintenként legfeljebb `4` vehető fel. `1 CM = 2 KP`                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|          Harcmodor CÉ           | Harcmodor képzettség szintje által kapott bónusz (lásd a [Harcmodor képzettségeket](062_02_harcmodor_kepzettsegek.md#harcmodor-képzettségek)!)                                                                                                                                                                                                                                                                                                                                                                    |
| `2x` Önuralom<br>/<br> `2x` Erő | Az Önuralom vagy Erő kétszerese ([fegyvertől függ](#er%C5%91b%C5%91l--%C3%BCgyess%C3%A9gb%C5%91l-forgatott-fegyverek))                                                                                                                                                                                                                                                                                                                                                                                            |
| Fegyver CÉ<br>(kategória függő) | Különbséget teszünk a fegyverkategóriák közt attól függően, hogy alapesetben milyen könnyű velük célba találni. Az alábbi értékek csak irányszámok, a konkrét fegyver értékek ettől eltérhetnek.<br> • Hajító szálfegyverek: `CÉ:+0`<br> • Apró hajítófegyverek: `CÉ:+4`<br> • Íjak: `CÉ:+10`<br> • Nyílpuskák: `CÉ:+16`<br> (A fentiek irányadó számok, egyes speciális fegyverek ezen értéke eltérhet ettől. Lásd a [Távolsági fegyverek harcértékei](067_fegyverek.md#hajítófegyverek-harcértékei) fejezetet!) |
|               Mf                | Mesterfegyver fortély után járó bónusz, amennyiben a használt fegyverre felvette a karakter. Fokonként `CÉ:+3` bónusz.                                                                                                                                                                                                                                                                                                                                                                                            |

<br />

---
## Módosítók

| Módosító                                                                                                                                    |   **CÉ**    |
|:------------------------------------------------------------------------------------------------------------------------------------------- |:-----------:|
| Célzás - 1 célzással eltöltött kör után (nem additív) 🔆                                                                                    |    `+10`    |
| Célzás - 1 célzással eltöltött kör után (nem additív) - [Képzett célzás](fortelyok.harci/kepzett_celzas.md) fortéllyal 🔆                   |   ⭕`+20`   |
| Képzetlenségből adódó levonás                                                                                                               |    `-40`    |
| Hirtelen lövés                                                                                                                              |    `-30`    |
| Álló cél "belövése" (gyakorlás) min. negyed órán át                                                                                         |  `+10-30`   |
| Fegyver minősége                                                                                                                            | ⭕`-5 - +5` |
| Nem “belőtt” íjak  / most lő először ezzel az íjjal - [Távolsági Harcmodor](kepzettsegek/tavolsagi_harcmodor.md) 9.szintje alatt            |    `-30`    |
| Nem “belőtt” nyílpuskák / most lő először ezzel a nyílpuskával - [Távolsági Harcmodor](kepzettsegek/tavolsagi_harcmodor.md) 9.szintje alatt |    `-15`    |
| Egyes [Fortélyokból](#fort%C3%A9lyok---t%C3%A1vols%C3%A1gi-harc) adódó bónuszok.                                                            |             |

🔆**Célzás**: íjnál csak 1 körig lehet kitartani! 1 kör után nem nincs bónusz, sőt körönként `CÉ:-10` büntetés jár!

### Fegyver belövése

Ha **legalább fél órát** töltött el a karakter a “belövéssel”,  a büntető módosító megszűnik. A használat során folyamatosan tűnik el a hátrány - KM dönt.

---
## Célzott Támadó dobás

```
CÉ + k100
```

