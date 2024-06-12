## KÉ, TÉ, VÉ, CÉ

## Harcértékek felépítése

A karaktert a harcban harcértékei jellemzik. Ezek mutatják meg, hogy mennyire képzett a küzdelem egyes területein. Alapvetően négy érték határozza meg az aktuális harcértékeket, melyek szituációtól, forgatott fegyvertől, illetve harcmodortól függően változhatnak. Ezek az alábbiak:

- Kezdeményező Érték (KÉ)
- Támadó Érték (TÉ)
- Védő Érték (VÉ)
- Célzó Érték (CÉ)

Ezen értékek öt jellemzőből épülnek fel:

```
- Harcérték Alap
- Tulajdonságok
- Harcérték Módosító
- Harcmodor képzettség
- Mesterfegyver fortély
- Fegyver harcértékei
```

Az alábbiakban részletesen kifejtjük a fenti értékek kiszámítási módját, valamint hogy mi és hogyan képes módosítani őket.

---
### Harcérték Alapok

Első szinten minden karakter egységes konstans értékeket kap `KÉ`, `TÉ`, `VÉ` és `CÉ` értékére.

Értékeik :

```
KÉ konstans: 10
TÉ konstans: 20
VÉ konstans: 120
CÉ konstans: -30
```

Ehhez az alapértékhez adódnak majd hozzá az egyéb módosítók.

### Harci Tulajdonságok

Egyes Tulajdonságok értékei beleszámítanak a harcértékekbe. Hogy melyek azt az adott harcérték leírásánál találhatjuk a következőkben.

<br />

És most lássuk a bevezetőben már említett négy konkrét harcértéket.

---


### Kezdeményező érték

A Kezdeményező Érték (**KÉ**) szerepe a harcban, hogy meghatározza, ki „mozdul először” a harcban. Nem jelent harci dominanciát, csak azt, hogy ki a gyorsabb, ki cselekedhet előbb.

A kezdeményezésről bővebben lásd a [Harc menete - Kezdeményezés](063_04_harc_menete_reszletes.md#kezdeményezés) fejezetet!

Két típusú KÉ létezik:
- Fegyveres KÉ
- Varázslás KÉ

A fenti két KÉ számítása azonos, egyedül a "Harcmodor"/"Mágia Tradíció" által adott bónuszban térnek el (lásd lenn). Külön számolandóak és külön is kezelendőek. Bővebben lásd a [Harc menete](063_04_harc_menete_reszletes.md#kezdeményezés) - "Kezdeményezés" és "Varázslás kezdeményezése" bekezdéseket.

A karakter Kezdeményező Értékét a következőképpen kell kiszámítani:

|               🗡️                | Kezdeményező Érték meghatározása                                                                                                                                                                                                                                                              |
| :------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|             Konstans             | `10` (minden karakternek)                                                                                                                                                                                                                                                                     |
|            Gyorsaság             | A karakter Gyorsaság Tulajdonsága                                                                                                                                                                                                                                                             |
|          Intelligencia           | A karakter Intelligencia Tulajdonsága                                                                                                                                                                                                                                                         |
|              Szint               | A karakter szintje                                                                                                                                                                                                                                                                            |
| Harcmodor KÉ /<br />Varázslás KÉ | [Harcmodor képzettség](062_02_harcmodor_kepzettsegek.md#harcmodor-képzettségek) szintje által kapott bónusz /<br />[Mágia Tradíció](051_00_magia_tradiciok.md) által kapott bónusz (mintha [Harcmodor képzettség](062_02_harcmodor_kepzettsegek.md#harcmodor-képzettségek) lenne) |
|      Mesterfegyver fortély       | `+2` fokonként (csak harcos KÉ esetén)                                                                                                                                                                                                                                                        |
|            Speciális             | - Gyors Kezdeményezés fortély: `KÉ:+4`<br>  - Szituációkból adódó módosítók<br>  - Mágia hatására kapott módosító                                                                                                                                                                             |

<br />

---
### Védő Érték

A Védő Érték szimbolizálja a karakter közelharcban nyújtott azon képességét, hogy mennyire hatásosan képes elhárítani, elkerülni az ellene intézett csapásokat. Értéke nem mondható konstansnak, hisz a harci helyzettől függően változik, ráadásul kihat rá a testi-lelki, szellemi fáradság és persze a sebesülés is (lásd később).

|          🗡️          | Védő Érték meghatározása                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :-------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       Konstans        | `120` (minden karakternek)                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|     `2x` Ügyesség     | A karakter Ügyesség Tulajdonságának kétszerese                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|    `2x` Gyorsaság     | A karakter Gyorsaság Tulajdonságának kétszerese                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|     Harcmodor VÉ      | Harcmodor képzettség szintje által kapott bónusz (lásd a [Harcmodor képzettségeket](062_02_harcmodor_kepzettsegek.md#harcmodor-képzettségek)!)                                                                                                                                                                                                                                                                                                                                         |
|      Fegyver VÉ       | A forgatott fegyver Védő Értéke                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Mesterfegyver fortély | `+3` fokonként                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|          HM           | A VÉ-re költött (KP-ból felvett) Harcérték módosító                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Vértviselet – `3.fok` | A nehézvért viselés mesterei (Vértviselet 3.fok) képesek a csapásokat páncélzatukról szándékoltan lecsúsztatni, sokszor hárítás helyett használva azt.  <br>Ezért félvért esetén `+5 VÉ`, teljes vért esetén `+10 VÉ` adódik Védő Értékükhöz                                                                                                                                                                                                                                                 |
|       Pajzs VÉ        | Értéke a pajzs jellegétől függ.<br />Ha a karakter készületlen, vagy meglepetésből támadnak rá, a pajzs VÉ nem adódik hozzá a aktuális Védő Értékhez.<br />Képzetlen Pajzshasználat esetén csak értékének fele számít be.                                                                                                                                                                                                                                                                    |
|       Speciális       | Harc során bekövetkező csökkenés (sima találat esetén)<br>  - Sebesülésből adódó csökkenés<br>  - Fortélyokból adódó módosítók<br>  - Harci helyzetből adódó módosítók (pl. harc alulról, harc megrendülten, stb)<br>  - Fegyver minőségéből adódó módosító<br>&nbsp;&nbsp;&nbsp;&nbsp; - Mestermunka: max `CÉ:+5`<br>&nbsp;&nbsp;&nbsp;&nbsp; - Gyatra fegyver: max `VÉ:-10`<br>&nbsp;&nbsp;&nbsp;&nbsp; - Mágikus fegyver módosítói<br>&nbsp;&nbsp;&nbsp;&nbsp; - Mágiából adódó módosítók |

<br />

---
### Támadó Érték

A Támadó Érték szimbolizálja a harcos azon tulajdonságát, hogy az adott fegyverrel milyen hatékonyan képes ellenfele ellen támadást, támadásokat intézni.

Az alábbi táblázat megadja, a Támadó Érték kiszámolásának módját.

|          🗡️           | Támadó Érték meghatározása                                                                                                                                                                                                                                                                                             |
| :--------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        Konstans        | `20` (minden karakternek)                                                                                                                                                                                                                                                                                              |
|        2 x Erő         | A karakter Erő Tulajdonságának kétszerese                                                                                                                                                                                                                                                                              |
|      2 x Ügyesség      | A karakter Ügyesség Tulajdonságának kétszerese                                                                                                                                                                                                                                                                         |
|     2 x Gyorsaság      | A karakter Gyorsaság Tulajdonságának kétszerese                                                                                                                                                                                                                                                                        |
|      Harcmodor TÉ      | Harcmodor képzettség szintje által kapott bónusz (lásd a [Harcmodor képzettségeket](062_02_harcmodor_kepzettsegek.md#harcmodor-képzettségek)!)                                                                                                                                                                   |
|       Fegyver TÉ       | A forgatott fegyver Támadó Értéke                                                                                                                                                                                                                                                                                      |
| Mesterfegyver fortély  | `+3` fokonként                                                                                                                                                                                                                                                                                                         |
|           HM           | A VÉ-re költött (KP-ból felvett) Harcérték módosító                                                                                                                                                                                                                                                                    |
| Plusz támadás levonása | Minden plusz támadás esetén `-10` levonás jár a **TÉ**-re.  <br>(a 2. támadásra: `TÉ:-10`, a 3.támadásra: `TÉ:-20`, stb)                                                                                                                                                                                               |
|       Speciális        | - Fortélyokból adódó módosítók<br> - Harci helyzetből adódó módosítók<br> - Fegyver minőségéből adódó módosító<br>&nbsp;&nbsp;&nbsp;&nbsp; - Mestermunka: max `TÉ:+5`<br>&nbsp;&nbsp;&nbsp;&nbsp; - Gyatra fegyver: max `TÉ:+5`<br>&nbsp;&nbsp;&nbsp;&nbsp; - Mágikus fegyver módosítói<br> - Mágiából adódó módosítók |

Bővebben lásd a [Harc menete - Támadás, Védő Érték csökkentése](063_04_harc_menete_reszletes.md#támadás-védő-érték-csökkentése) fejezetben!

<br />

---
### Célzó Érték

|                 🗡️                 | Célzó Érték kiszámítása                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :---------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                `-30`                | Konstans. Ez az érték gyakorlatilag a célpont Védő Érték alapját adná, de mivel itt csak 1x (karakteralkotáskor) kell vele számolni, ezért a számolás meggyorsítása miatt átkerült ide.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|            `2x` Önuralom            | Az Önuralom kétszerese                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|            Harcmodor CÉ             | Harcmodor képzettség szintje által kapott bónusz (lásd a [Harcmodor képzettségeket](062_02_harcmodor_kepzettsegek.md#harcmodor-képzettségek)!)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Fegyver CÉ<br><br>(kategória függő) | Különbséget teszünk a fegyverkategóriák közt attól függően, hogy alapesetben milyen könnyű velük célba találni. Az alábbi értékek csak irányszámok, a konkrét fegyver értékek ettől eltérhetnek.<br><br>- Hajító szálfegyverek: `CÉ:+0`<br>    <br>- Apró hajítófegyverek: `CÉ:+4`<br>    <br>- Íjak: `CÉ:+10`<br>    <br>- Nyílpuskák: `CÉ:+16`<br>    (A fentiek irányadó számok, egyes speciális fegyverek ezen értéke eltérhet ettől. Lásd a [Távolsági fegyverek harcértékei](067_fegyverek.md#hajítófegyverek-harcértékei) fejezetet!)                                                                                                                                                                                |
|        Mesterfegyver fortély        | `+3` fokonként                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                 CM                  | Célzóérték Módosító. Szintnként legfeljebb 4 vehető fel. `1 CM = 2 KP`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|          Célzás körönként           | +10CÉ / kör amit célzással tölt el a támadó. Maximum 2 körig.  <br>+15CÉ / kör: Képzett Célzás fortély megléte esetén.<br><br>(Figyelem: íjnál csak 1 körig, alkalmazható mert nehéz kitartani!! 1 kör után körönként ugyanennyi levonás!)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                Egyéb                | - Képzetlenségből adódó levonás: `CÉ:-40`<br>    <br>- Hirtelen lövés: `CÉ:-30`<br>    (Pl. a célpont hirtelen átfut az úton be egy másik takarás védelmébe és ez a lövészt felkészületlenül éri)<br>    <br>- Az egyes Fortélyokból adódó bónuszok.<br>    <br>- Nem “belőtt” lőfegyver: `CÉ:-30` (íjak) / `CÉ:-15` (nyílpuskák)  <br>  Ha a támadó most lő először a fegyverrel, akkor íjak esetében `CÉ:-30`, nyílpuskák használatánál pedig `CÉ:-15` módosító sújtja. Ha legalább fél órát töltött el a “belövéssel”, ez a módosító megszűnik. Egyébiránt a használat során folyamatosan tűnik el a hátrány (negyed óra után már csak `CÉ:-15` / `CÉ:-8` és így tovább).<br>    <br>- A fegyverek minősége befolyásolhatja azok Célzó értéket. |

→ Bővebben lásd a [Távolsági Harc](070_tavolsagi_harc.md) fejezetet!
