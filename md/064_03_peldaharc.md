## Példaharc

⚡Lássunk egy konkrét összecsapást, hiszen egy példa többet ér több oldal szabályleírásnál is!

### Lord Gustav, Domvik lovagja

```
KÉ: 20 TÉ: 85 VÉ: 165
Fegyver: Hosszú kard  (1 penge)
Sebzés: k20+5 (V/S)  (Erőbónuszzal együtt)
ÉP: 18
Erő: +3
Fájdalomtűrés (8) + Önuralom (1) = 9
  - ennyivel csökkennek a TÉ levonások

Vért:
- Láncing (torzó, felkarok, combok, lábszár befedve: 80%)
- Átlagos minőség, Acél

SFÉ: 8 / 13 / 5
MGT: 5 (13 - (2 x 3) + (3 x 2) = 13
+ Vértviselet – 2.fok
```

 #### Életerő Pontok

|                |                |                |                |
| :------------: | :------------: | :------------: | :------------: |
| **\_\_S1\_\_** | **\_\_S2\_\_** | **\_\_S3\_\_** | **\_\_S4\_\_** |
|      `1V`      |      `2V`      |      `3V`      |      `3V`      |
|      `1V`      |      `2V`      |      `3V`      |                |
|      `1V`      |      `2V`      |      `3V`      |                |
|      `2V`      |      `2V`      |      `3V`      |                |
|      `2V`      |      `3V`      |      ✖️✖️      |      ✖️✖️      |

 #### Harcérték levonások

|**\_\_S1\_\_**|**\_\_S2\_\_**|**\_\_S3\_\_**|**\_\_S4\_\_**|
|:---:|:---:|:---:|:---:|
| `-` |`-1TÉ`|`-11TÉ`|`-21TÉ`|


### Tetves, a bérgyilkos
```
KÉ: 15 TÉ: 80 VÉ: 160
Fegyver: Rövidkard (0,5 penge)
Sebzés: k20+2 (V/S)
ÉP: 14
Fájdalomtűrés (6) + Önuralom (0) = 6
  - ennyivel csökkennek a TÉ levonások

Vért: -
SFÉ: -
```


 ####  Életerő Pontok

|     |     |     |     |
|:---:|:---:|:---:|:---:|
|**\_\_S1\_\_**|**\_\_S2\_\_**|**\_\_S3\_\_**|**\_\_S4\_\_**|
|`1V`|`1V`|`1V`|`1V`|
|`1V`|`1V`|`1V`|`1V`|
|`1V`|`1V`|`1V`|    |
|`1V`|`1V`|✖️✖️|✖️✖️|
|✖️✖️|✖️✖️|✖️✖️|✖️✖️|

 #### Harcérték levonások

|**\_\_S1\_\_**|**\_\_S2\_\_**|**\_\_S3\_\_**|**\_\_S4\_\_**|
|:---:|:---:|:---:|:---:|
| `-` |`-4TÉ`|`-14TÉ`|`-24TÉ`|


### Lord Gustav és Tetves részletes összecsapása

Lord Gustav elmélázva sétál ki a könyvtárból, mikor Tetves, a bérgyilkos veti rá magát. Jó pénzt ígértek neki a lovag haláláért. Gustav szerencsére időben észbe kap (**Lopakodás/rejtőzés** vs. **Észlelés** próbát a lovag nyeri) így Tetves csak a meglepetés `TÉ:+20` bónuszát kapja meg.

> **Megjegyzés**: mivel kettőjük fegyverének mérete közt nincs meg az `1 penge` méretkülönbség, ezért mindketten Előnyös helyzetben vannak, tehát sikertelen (nem sebző) támadások esetén a **k100** támadás `Nagykockájával` csökkentik egymás **Védő Értékét**.

<br />

---
#### Gustav első sebe

Tetves dob: `73`. Összesen `80+20+73= 173`, ami meghaladja a lovag VÉ-jét: **talált**!

```
Tetves Sebzés dobás: k20+2  → 20 SP (Vágó)
```

Gustav Páncéldobást végez. Teste `80%`-ban van befedve a láncing anyagával, így ha `k10`-en `1-8`-ig dob, akkor a csapás védett területet ért.\
Gustav dob: `6`, így a páncél **SFÉ**-je beszámít.

A lovag SFÉ-je vágófegyverek ellen `13`, a végső **SP** így:
```
20-13 = 7SP

7SP → -3 ÉP seb és -10 VÉ
```

A `7 SP` a második Sebzés-kategóriába tartozik, ami `3 ÉP`-s (❗) sebet és (`-10 VÉ`) büntetést jelent.

A lovag ezzel a sebesüléssel még az `S1` egészség-kategóriában marad, így `TÉ` büntetést egyelőre nem kap. Ugyanennek a sebnek a hatására egy gyengébb fizikumú (`ÉP: 8`) ember már átcsúszna az `S2` kategóriába.

<br />

---
#### Gustav második sebe

Folytatódik a harc, több sikertelen oda-vissza támadás, Gustav nem támad túl jókat és `VÉ`-je közben lecsökken `144`-re. Rosszul mozdul és bekap egy újabb sebet. **Páncéldobása** (`9`) ezúttal sikertelen, a csapás fedetlen területet ért (pl. alkar), így az SFÉ-je ezúttal nem számít!

```
Tetves Sebzés dobás: k20+2 → 11 SP (Vágó)
  → -6 ÉP seb és -15 VÉ
```

Ezzel Gustav bőven átkerült az `S2` egészség-kategóriába, így már `-1 TÉ` büntetése is van, ami nem számottevő (hála a magas **Fájdalomtűrés+Önuralmának**)

Aktuális harcértékei: `KÉ: 20, TÉ: 84, VÉ: 131, ÉP: 9`

A helyzet kezd veszélyessé válni: a lovag elvesztett több, mint `30`-at **Védő Értékéből** és **Életerő Pontjainak** felét. Egy újabb sebkategóriába átlépéssel tovább csökkennének harcértékei.

<br />

---
#### Gustav harmadik sebe

Bár sikerül sebet ejtenie támadóján (sajnos csak `3 ÉP`-t, ritka szerencsétlen dobás (`3`) volt), a sors nem kedvez a lovagnak, a gyilkos is belevág az oldalába a láncingen keresztül, bordák hasadnak.

```
SP: 19;  SFÉ után: 6 SP  → -3 ÉP, -10 VÉ
```

Gustavnak `6 ÉP`-je marad és `S3`-as kategóriába zuhan (további `-10 TÉ` büntetés), valamint elveszít még `10 VÉ`-t. Eddig összesen `12 ÉP`-t vesztett!

Aktuális harcértékei: `KÉ: 20, TÉ: 74, VÉ: 121, ÉP: 6`

Még csak `S3` kategóriában van, ha `S4`-be kerülne, automatikusan **Fájdalomtűrés** próbát kellene dobnia **Edzettséggel**, hogy ne ájuljon el azonnal. De erre egyelőre még nincs szükség. Gustav helyzete kezd reménytelen lenni, támolyog, még egy közepes seb és vége van.

A játékos bejelenti, hogy a következő körben utolsó esélyként teljes **támadó taktikát** (`+15 TÉ; -30 VÉ`) alkalmaz, ha meg kell halni, tegye azt lovagként!

Nem tudja, de ellenfele – látva elcsigázottságát –, szintén teljes támadó taktikát alkalmaz, hogy következő csapása biztos a túlvilágra küldje prédáját és gyorsan eltűnhessen az éjszakában. Az elgondolás jó... de az istenek ma máshogy akarták.

<br />

---
#### A gyilkos veszte

Tetves nyeri a kezdeményezést, viszont dobása csak `04` (összesen: `114`!), ami még így is talál (!) (tekintve, hogy a lovag `VÉ`-je csak `86` a Támadó taktika miatt), viszont sebzésnek `2`-t dob `k20`-on. Mivel `20`-nál többel ütötte túl ellenfelét, ezért a **Többszörös találatból** további `+3 SP` jár, így a vége: `7 SP`... amit Gustav láncinge pont teljesen felfog (**páncéldobása** sikeres (`3`) volt)!

Tetves kardja lecsusszan az felé dobogó lovag vértjéről, aki visszatámadva... `97`-et dob. Tetves is elveszített már **Védő Értékéből** a harc során, alaphelyzetben aktuális `VÉ`-je `146`, de most ugye neki is `-30` büntetés van (támadó taktika `146-30=116`)

```
Gustav támadása: 64+97 = 151
  → többszörös találat (+1x): +3 SP
```

```
Gustav sebzése: k20 + 5 + 3 = 19 SP
```

Tetvesnek nincs vértje, ezért a `19 SP` 1:1-ben számít → `12 ÉP` és `-25 VÉ`. Tetvesnek `1 ÉP`-je marad, majdnem kettészelték!

Míg Gustav 3 sebet (`12 ÉP`) is elviselt és talpon maradt, addig a gyengébb fizikumú Tetves ennyitől már kidől. `1 ÉP`-je maradt, Fájdalomtűrés próbát dob `12` ellen...

```
Fájdalomtűrés (K) + Edzettség (T)  vs.  12 (Nehéz)
```

... de elvéti és eszméletlenül rogy össze, miután értetlenül bámul a hasából kimeredő kardra. Ha nem látják el, perceken belül meghal.

A lovag kínkeservesen feltápászkodik, hite, bátorsága és a láncing megmentette az életét. A háttérben vasalt csizmák csattogása hallatszik, az őrjárat érkezik futva, de sok dolguk már nem akad...

---

⚜️ [Nyitóoldal](start.md#6-harcrendszer-%EF%B8%8F)
