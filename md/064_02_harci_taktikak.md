## Harci taktikák

A taktikák használatát kör elején, kezdeményezés előtt kell bejelenteni, kivéve az **(X)**-el jelölteket, azokat kör közben is lehet variálni.

### Összefoglaló

| **Taktika**              | **Hatás**                                                                                                                                                                                                                                                                     |
| :----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Támadó taktika           | `TÉ:+1 = VÉ:-2`, max `TÉ:+15`                                                                                                                                                                                                                                                 |
| Védő taktika             | `VÉ:+1 = TÉ:-2`, max `VÉ:+20`                                                                                                                                                                                                                                                 |
| Teljes Védekezés taktika | `VÉ:+30`, ellenfeled csak `kiskockával` csökkenthet rajtad `VÉ`-t. Folyamatos hátrálás, nincs támadás, nem kombinálható más taktikával.                                                                                                                                       |
| Kezdeményező taktika     | `KÉ:+1 → VÉ:-2`, max `KÉ:+10`                                                                                                                                                                                                                                                 |
| Kiváró taktika           | • Átengedett KÉ, cserébe első visszatámadásra `TÉ:+5`<br/>• Támadó taktikával együtt mehet, Védővel nem, több ellenfeles harcban sem.                                                                                                                                         |
| Fárasztás taktika        | • VÉ csökkentésre: `+2`<br/>• Sebzés helyett: nagykockás VÉ csökk + további `+10VÉ` csökkentés                                                                                                                                                                                |
| Roham taktika            | • `TÉ:+20`, `VÉ:-40` (első oda-visszacsapáskor)<br/>• VÉ csökkentés duplázódik első oda-visszacsapásnál , Sebzéshez: `+5 SP` (oda-vissza)                                                                                                                                     |
| Öngyilkos roham taktika  | • `TÉ:+25`,`VÉ:-50` (első oda-visszacsapáskor)<br/>• VÉ csökkentés duplázódik első oda-visszacsapásnál, Sebzéshez: `+7 SP` (oda-vissza)<br/>• TÉ büntetések (sérülésből) nem érvényesek, max `2x` használható egy küzdelemben<br/>• Küzdelmenként legfeljebb 1x alkalmazható. |
| Támadás erőből           | Erre a [Támadás erőből](fortelyok.harci/tamadas_erobol.md) fortélyt használhatod (lásd a leírását).                                                                                                                                                                           |


| **Taktika**                                                | **Hatás**                                                                                                                                                                                                                                                 |
| :--------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Leütés hátulról                                            | • Követelmény: „Észrevétlen támadás” harci helyzet, Sebző Találat<br/>• Ha Súlyos a seb (`12 ÉP`) → Fájdalomtűrés (+Edzettség) próba (`12`). Ha nincs meg, elájul.<br/>• [Harci anatómiával](fortelyok.harci/harci_anatomia.md) könnyebb (lásd a leírást) |
| Orvtámadás                                                 | • Követelmény: „Észrevétlen támadás” harci helyzet<br/>• Bónuszt ad: [Harci anatómia](fortelyok.harci/harci_anatomia.md) fortély - vértmentes terület találata esetén                                                                                     |
| Érintő támadás **(X)**                                     | `KÉ:0`, `TÉ:0`, `VÉ:-10`                                                                                                                                                                                                                                  |
| Csonkolás és törés **(X)**                                 | • Kéz csonkolása: (áldozat `max ÉP / 3`) (felfele kerekítve) sebzés szükséges<br/>• Láb csonkolása: (áldozat `max ÉP / 2`) (felfele kerekítve) sebzés szükséges                                                                                           |
| Kijelölt testrészre támadás **(X)**                        | Sebző támadás `TÉ:-20`-al                                                                                                                                                                                                                                 |
| Pontok támadása harc közben **(X)**                        | • Követelmény: **Harci anatómia** fortély – `2.fok`<br/>• Követelmény: **Pontra támadás** manőver                                                                                                                                                         |
| Mögékerülés                                                | ⭕TODO⭕                                                                                                                                                                                                                                                    |
| Rávetődés hátulról                                         | ⭕TODO⭕                                                                                                                                                                                                                                                    |
| Visszafogott csapás / Harc az ellenfél elfogásáért **(X)** | ⭕TODO⭕ Bónuszt ad: **Harci anatómia** fortély                                                                                                                                                                                                             |

### Ökölszabály Védő Érték eltolásra

Egyes taktikák kombinálhatóak egymással, mások nem (lásd leírásukat), de fontos szabály, hogy **Védő Értékedet** legfeljebb `-30`-al tolhatod el.

---
### Támadó taktika

Dönthetsz úgy, hogy a következő körben a támadásra helyezed a hangsúlyt és nyomulsz előre. Ekkor védekezésedre kevésbé ügyelsz, sebezhetőbb vagy. Te határozod meg, hogy mennyire tolod el a harcmodorodat a támadás irányába. `TÉ`-det `+1-15`-ig növelheted meg ideiglenesen. Minden pont növelés után `-2` **Védő Érték** módosítót kapsz.

Tehát vállalásodtól függően például így módosíthatod harcértékeidet:

- `TÉ:+1`, `VÉ:-2`
- `TÉ:+5`, `VÉ:-10`
- `TÉ:+10`, `VÉ:-20`
- `TÉ:+15`, `VÉ:-30`


A szándékot, hogy Támadó taktikát akarsz alkalmazni, előre be kell jelentened, mielőtt az adott kör elkezdődött volna. Kör közben nem változtathatsz a taktikán. Ha ebben a taktikában küzdesz, akkor lehetőségeidhez mérten folyamatosan nyomulsz előre.

Támadó taktika nem alkalmazható Észrevétlen támadás szituációban.
```diff
- És Meglepetés szituációban?
```

---
### Védő taktika

Dönthetsz úgy, hogy a következő körben a védekezésedre helyezed a hangsúlyt. Ekkor kisebb vehemenciával támadsz, ez megmutatkozik Támadó Értékedben is.

Te határozod meg, hogy mennyire tolod el a harcmodorodat a védekezés irányába. **Védő Értékedet** `+1-20`-ig növelheted meg ideiglenesen. Minden pont növelés után `-2` **Támadó Érték** módosítót kapsz.

Tehát vállalásodtól függően így módosíthatod harcértékeidet. Pl:

- `VÉ:+1`, `TÉ:-2`
- `VÉ:+5`, `TÉ:-10`
- `VÉ:+10`, `TÉ:-20`
- `VÉ:+20`, `TÉ:-40`

---
### Teljes Védekezés Taktika

```
VÉ:+30

Ellenfeled csak "kiskockával"
csökkenthet rajtad VÉ-t.
```

Ha úgy döntesz, hogy a következő körben csak a védekezéssel törődsz (előre be kell jelenteni!), kizárólag a feléd irányuló támadásokat próbálod elkerülni, nem támadsz (!), valamint folyamatosan hátrálsz, akkor `+30 VÉ` módosítót kapsz arra a körre. A kör közben nem változtathatsz a taktikádon, ha ismét támadni akarsz, azt csak a következő körben teheted meg.

Fontos, hogy másra nem pazarolhatod figyelmedet, kizárólag a védekezésre. Ha nem így teszel, vagy nem vagy képes a folyamatos hátrálásra (például egy fal miatt, ami elzárja mögötted az utat), akkor a KM – tetszése szerint – csökkentheti a fenti `VÉ` módosítódat, akár `0`-ig is. A Teljes Védekezés Taktika nem kombinálható más taktikával.

---
### Kezdeményező taktika

Ha mindenáron magadhoz akarod ragadni a kezdeményezést megteheted, de ennek ára van. A kapkodás sebezhetővé tesz. Kezdeményező taktika alkalmazása esetén megnövelheted **Kezdeményező Értékedet** maximum `10`-el de cserébe kétszer akkora **Védő Érték** csökkenést szenvedsz el **az ellenfél első támadásával szemben** (akár megnyerted így a kezdeményezést, akár nem)

Tehát `+1KÉ` → `-2VÉ` (max `10`)

A Kezdeményező taktika alkalmazható Támadó taktikával együtt is, de nem használható Védekező Taktikával kombinálva!

---
### Kiváró Taktika

Ha inkább bevárod ellenfeled támadását, kifejezetten az ellencsapásra készülve, az apró előnyhöz juttathat. Ha megnyered a `KÉ`-t akkor szándékosan átengedheted ellenfelednek a támadás elsőbbségét, majd amennyiben nem kapsz sebet, előnyt kovácsolhatsz a jó időzítésből. Hatása:

Ha úgy döntesz, hogy a fenti feltételekkel lemondasz a kezdeményezésről, cserébe az adott körben **első visszatámadásodra** `+5 TÉ` módosítót kapsz.

A Kiváró taktika alkalmazható **Támadó taktikával** együtt is, továbbá roham ellen is bevethető, de **nem** használható **Védő Taktikával** együtt, sőt több ellenféllel való harc esetén sem!

---
### Fárasztás taktika


```
VÉ csökkentésre: +2
ha nincs találat.
```

```
Sebzés helyett:
 nagykocka + 10 VÉ csökkentés
```

Ha fárasztani kívánod ellenfeledet, ellenállását megtörni anélkül, hogy sebet ejtenél rajta, akkor a harc ugyanúgy folyik, mint más esetben, csak `+2`-vel nő **VÉ csökkentésed** ha nem érsz el találatot támadó dobásod során.

Sebző támadás esetén pedig elmarad maga a sebzés – helyette **nagykockával** és további `+10`-el csökkentheted ellenfeled **Védő Értékét**. A Többszörös találat nem növeli tovább a VÉ csökkentést.

Más taktikával együtt **nem** használható.

A Fárasztás taktikának leginkább körbevett ellenfél esetén van értelme: a pribékek kifáraszthatják a „vadat”, míg vezetőjük felkészül.

Kapcsolódó fortély: [Fárasztás](fortelyok.harci/farasztas.md) harci fortély

---
### Roham taktika

Roham esetén **az első oda- és visszacsapás során** a támadó `TÉ:+20` és `VÉ:-40` módosítót kap, és `+5 SP` bónuszt sebzésdobására (`+1` sebzés kategória). Az okozott **VÉ csökkentés** duplázódik az első oda- és visszacsapásnál is.

Ha roham során a karakter sebző támadást ér el, akkor az őt sújtó **VÉ büntetés** azonnal megszűnik, a rá leadott visszacsapást már normál VÉ-vel várhatja és a `+5 SP` bónusz sem jár a visszatámadó félnek.

Roham alkalmazása során nem használhatóak a **Támadó**, **Védő**, **Kezdeményező** és **Kiváró** taktikák! Fontos viszont, hogy Rohamnál is számítanak a fegyverméret kategóriák, tehát egy pikás védekezőt megrohamozni nem mindig bölcs dolog...

A **körön belüli** további támadások már normál harcértékekkel történnek és innen már választható harci taktika is!

Rohamhoz legalább `5-10` méter nekifutás szükséges. Hogy pontosan mennyi, az szituáció-függő, a KM szava dönt a terepviszonyok és a felszerelés súlyának ismeretében.

Módosítók az első oda-vissza csapásnál:

- `TÉ:+20`, `VÉ:-40`
- VÉ csökkentés duplázódik (oda-vissza)
- Sebzés: `+5 SP` (oda-vissza)

---
### Öngyilkos roham taktika

A roham vehemensebb (és őrültebb) verziója. A harcos ekkor szinte semmit nem törődik védekezésével, mindent megtesz, hogy (dupla) sebzést érjen el. Különlegessége, hogy erre az egy támadásra nem érvényesülnek a sérülésből adódó **TÉ levonások**, az adrenalin elsöpör minden gátat. Súlyosan sérült harcosok utolsó mentsvára lehet ez a taktika. Küzdelmenként **legfeljebb 1x** alkalmazható. A fentieken és a harcérték módosítókon kívül az Öngyilkos roham minden másban megegyezik a sima **Rohammal**.

Módosítók az első oda-vissza csapásnál:

- `TÉ:+25` ; `VÉ:-50`
- VÉ csökkentés duplázódik
- Sebzés: `+7 SP`

---
### Támadás erőből taktika

Erre a [Támadás erőből](fortelyok.harci/tamadas_erobol.md) fortélyt használhatod (lásd a leírását).

E taktika mellett más harci taktikát nem alkalmazhatsz.

---

---
### Leütés hátulról (fejre/tarkóra)

- Követelmény: **Észrevétlen támadás**
- Célpont `VÉ = 30 + mozgás jellegétől függő módosító` (lásd [Észrevétlen támadás](064_01_harci_helyzetek.md#észrevétlen-támadás))

Ha a támadás sebző **Találat**, akkor és a sebzés legalább Súlyos lenne (`12 ÉP`), akkor az áldozat Fájdalomtűrés próbát dob `12`-es célszám (**Nehéz**) ellen, ezúttal **Edzettség** tulajdonsággal. Ha nincs meg, azonnal elájul.

```
Fájdalomtűrés (K) + Edzettség (T)  vs.  12
```

Hogy megkapjuk a valós ÉP seb mennyiségét, amit az áldozat elszenved, dobjunk `k3`-al:

- `1`: nincs `ÉP` seb
- `2`: sebzés fele bement `ÉP`-ben
- `3`: a teljes sebzés bement `ÉP`-ben
Ez azért van, mert egy járatlan támadó nem tudja olyan jól megbecsülni a szükséges erő nagyságát, ha rosszul méri fel az erejét, könnyen komoly sebet okozhat.

**[Harci anatómia](fortelyok.harci/harci_anatomia.md)** harci fortély módosítja a fenti dobást, bónuszait lásd annak leírásánál.

**Megjegyezés**: a Markolat sebzése: `k20 + 0 SP` (Zúzó)

---
### Orvtámadás

Kapcsoló fortély: [Harci anatómia](fortelyok.harci/harci_anatomia.md)

Ha [Észrevétlen támadást](064_01_harci_helyzetek.md#észrevétlen-támadás) sikerül leadnod (`VÉ` értékét lásd ott), akkor érvényesülnek a [Harci anatómia](fortelyok.harci/harci_anatomia.md) fortélynál leírt bónuszok - vértmentes terület találata esetén.

---
### Érintő támadás

Ha csak meg akarunk érinteni valakit harc közben, az könnyebb, mint puszta kézzel sérülést okozó támadást végbevinni. Az Érintő támadás harcértékei ezért: `KÉ:0`, `TÉ:0`, `VÉ:-10`

Tehát a támadásra kisebb a büntetés, mint puszta kézre, a védekezés viszont nem változik.


---
### Csonkolás és törés

Ha a harcos le kívánja vágni, vagy el akarja törni ellenfele valamely végtagját (kéz,fej), akkor:

Sikeres **Végtagra támadást** kell végrehajtania, valamint megfelelő mennyiségű `ÉP` sebzést okoznia.

- Kéz csonkolása/törése: (áldozat `max ÉP / 3`) (felfele kerekítve) sebzés szükséges
- Láb csonkolása/törése: (áldozat `max ÉP / 2`) (felfele kerekítve) sebzés szükséges

---
### Kijelölt testrészre támadás

```diff
- ⭕TODO: Harci Anatómia adjon bónuszt? (PROB_HARC_#59)
```

Ha küzdelem közben a harcos ellenfele egy konkrét testrészére kíván támadni, akkor ezt előre be kell jelentenie és utána sikeres, túlütő támadást kell dobnia `TÉ:-20` módosítóval.

- Kijelölhető testrészek: fej, törzs, jobb/bal láb, jobb/bal kar.
- Ennél pontosabb találatot harc közben meghatározni csak a **Pontra támadás** manőverrel lehet.
- Találatkor sima sebzést dob a támadó
- Plusz hatás: ha a Sebzés legalább Súlyos (`6 ÉP`), akkor az áldozat valamilyen nem-harcérték korlátozást szenved el. Például ha a cél a fegyverforgató kéz volt, akkor elejti fegyverét és nem képes tovább harcolni vele. Vagy: láb támadása esetén mozgási sebessége felére/harmadára esik vissza (KM dönt). Fejre támadásnál szemébe folyik a vére, esetleg elkábul.
- Lásd még alább: [Csonkolás](064_02_harci_taktikak.md#csonkolás-és-törés) harci taktika.

 
---
### Pontok támadása harc közben

Kapcsoló fortély: [Harci anatómia](fortelyok.harci/harci_anatomia.md)

Ha harc közben próbálsz ellenfeleden egy konkrét pont támadásával nagyobb sebzést elérni, vagy a **Harci anatómia** fortélynál leírt hatások valamelyikét elérni, akkor [Területre/Pontra támadás](065_03_altalanos_manoverek.md#ter%C3%BCletre--pontra-t%C3%A1mad%C3%A1s) manővert kell végezned. Amennyiben az sikeres, megkapod a fenti fortélynál megadott bónuszokat.

---
### Mögékerülés

⭕TODO⭕
→ [Kidolgozás itt](https://github.com/kaktusztea/km100/wiki/TODO.ISSUE.harcrendszer#harci-taktik%C3%A1k-tiszt%C3%A1z%C3%A1sa). Ha kész, bemozgatni ide.

---
### Rávetődés hátulról

⭕TODO⭕
→ [Kidolgozás itt](https://github.com/kaktusztea/km100/wiki/TODO.ISSUE.harcrendszer#harci-taktik%C3%A1k-tiszt%C3%A1z%C3%A1sa). Ha kész, bemozgatni ide.

---
### Visszafogott csapás / Harc az ellenfél elfogásáért

⭕TODO⭕
→ [Kidolgozás itt](https://github.com/kaktusztea/km100/wiki/TODO.ISSUE.harcrendszer#harci-taktik%C3%A1k-tiszt%C3%A1z%C3%A1sa). Ha kész, bemozgatni ide.
