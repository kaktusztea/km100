## Harci taktikák

🔆 A taktikák használatát kör elején, kezdeményezés előtt kell bejelenteni, kivéve az ⇄ jellel megjelölteket, azokat kör közben is lehet variálni.

### Összefoglaló

| **Taktika név**                                                       | **Hatás**                                                                                                                                                                                                                              |
| :-------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Támadó taktika](#t%C3%A1mad%C3%B3-taktika)                           | `TÉ:+1 = VÉ:-2`, max `TÉ:+15`                                                                                                                                                                                                          |
| [Védő taktika](#v%C3%A9d%C5%91-taktika)                               | `VÉ:+1 = TÉ:-2`, max `VÉ:+20`                                                                                                                                                                                                          |
| [Teljes Védekezés taktika](#teljes-v%C3%A9dekez%C3%A9s-taktika)       | `VÉ:+30`, ellenfeled csak `kiskockával` csökkenthet rajtad `VÉ`-t. Folyamatos hátrálás, nincs támadás, nem kombinálható más taktikával.                                                                                                |
| [Kezdeményező taktika](#kezdem%C3%A9nyez%C5%91-taktika)               | `KÉ:+1 → VÉ:-2`, max `KÉ:+10`                                                                                                                                                                                                          |
| [Kiváró taktika](#kiv%C3%A1r%C3%B3-taktika)                           | • Átengedett KÉ, cserébe első visszatámadásra `TÉ:+5`<br/>• Támadó taktikával együtt mehet, Védővel nem, több ellenfeles harcban sem.                                                                                                  |
| [Fárasztó taktika](#f%C3%A1raszt%C3%B3-taktika)                       | • `+2 VÉ` csökkentés <br />• Sebzés helyett: nagykockás VÉ csökkentés + további `+10 VÉ` csökkentés<br />• `00` dobásnál: további `+5 VÉ` csökkentés<br />• Csak Előnyös helyzetből lehet alkalmazni                                   |
| [Visszafogott taktika](#visszafogott-taktika)                         | ⭕TODO⭕                                                                                                                                                                                                                                 |
| [Roham taktika](#roham-taktika)                                       | • `TÉ:+20`, `VÉ:-40` (első oda-visszacsapáskor)<br/>• `VÉ` csökkentés duplázódik első oda-visszacsapásnál , Sebzéshez: `+5 SP` (oda-vissza)                                                                                            |
| [Öngyilkos roham taktika](#%C3%B6ngyilkos-roham-taktika)              | • `TÉ:+25`,`VÉ:-50` (első oda-visszacsapáskor)<br/>• `VÉ` csökkentés duplázódik első oda-visszacsapásnál, Sebzéshez: `+7 SP` (oda-vissza)<br/>• `TÉ` büntetések (sérülésből) nem érvényesek<br/>• Max `1x` használható egy küzdelemben |
| [Támadás erőből taktika](#t%C3%A1mad%C3%A1s-er%C5%91b%C5%91l-taktika) | Erre a [Támadás erőből](fortelyok.harci/tamadas_erobol.md) fortélyt használhatod (lásd a leírását).                                                                                                                                    |
| [Érintő taktika](#%C3%A9rint%C5%91-taktika) ⇄                         | `KÉ:0`, `TÉ:0`, `VÉ:-10`                                                                                                                                                                                                               |

### Ökölszabály Védő Érték eltolásra 🔆

Egyes taktikák kombinálhatóak egymással, mások nem (lásd leírásukat), de fontos szabály, hogy **Védő Értékedet** legfeljebb `-30/+30`-al tolhatod el.

---
### Támadó taktika

Dönthetsz úgy, hogy a következő körben a támadásra helyezed a hangsúlyt és nyomulsz előre. Ekkor védekezésedre kevésbé ügyelsz, sebezhetőbb vagy. Te határozod meg, hogy mennyire tolod el a harcmodorodat a támadás irányába. `TÉ`-det `+1-15`-ig növelheted meg ideiglenesen. Minden pont növelés után `-2` **Védő Érték** módosítót kapsz.

Tehát vállalásodtól függően például így módosíthatod harcértékeidet:

- `TÉ:+1`, `VÉ:-2`
- `TÉ:+5`, `VÉ:-10`
- `TÉ:+10`, `VÉ:-20`
- `TÉ:+15`, `VÉ:-30`

A szándékot, hogy Támadó taktikát akarsz alkalmazni, előre be kell jelentened, mielőtt az adott kör elkezdődött volna. Kör közben nem változtathatsz a taktikán. Ha ebben a taktikában küzdesz, akkor lehetőségeidhez mérten folyamatosan nyomulsz előre.

Támadó taktika nem alkalmazható [Észrevétlen támadás](064_01_harci_helyzetek.md#%C3%A9szrev%C3%A9tlen-t%C3%A1mad%C3%A1s) szituációban.
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

Tehát `+1KÉ` → `-2VÉ` (max `+KÉ:10`)

A Kezdeményező taktika alkalmazható Támadó taktikával együtt is, de nem használható Védekező Taktikával kombinálva!

---
### Kiváró Taktika

Ha inkább bevárod ellenfeled támadását, kifejezetten az ellencsapásra készülve, az apró előnyhöz juttathat. Ha megnyered a `KÉ`-t akkor szándékosan átengedheted ellenfelednek a támadás elsőbbségét, majd amennyiben nem kapsz sebet, előnyt kovácsolhatsz a jó időzítésből. Hatása:

Ha úgy döntesz, hogy a fenti feltételekkel lemondasz a kezdeményezésről, cserébe az adott körben **első visszatámadásodra** `+5 TÉ` módosítót kapsz.

A Kiváró taktika alkalmazható **Támadó taktikával** együtt is, továbbá roham ellen is bevethető, de **nem** használható **Védő Taktikával** együtt, sőt több ellenféllel való harc esetén sem!

---
### Fárasztó taktika

```
VÉ csökkentésre:
 +2 ha nincs találat
```

```
VÉ csökkentésre:
 (nagykocka + 10)
 ha lenne találat
```

```
00 dobás esetén
 további +5 VÉ csökkentés
```

Más taktikával együtt **nem** használható.

Csak azonos, vagy Előnyös helyzetből lehet alkalmazni. Tehát azonos, vagy nagyobb fegyverméretnél.

Ha fárasztani kívánod ellenfeledet, ellenállását megtörni anélkül, hogy sebet ejtenél rajta, akkor a harc ugyanúgy folyik, mint más esetben, csak `+2`-vel nő **VÉ csökkentésed** ha nem érsz el találatot támadó dobásod során.

Sebző támadás esetén pedig elmarad maga a sebzés – helyette **nagykockával** és további `+10`-el csökkentheted ellenfeled **Védő Értékét**. A Többszörös találat nem növeli tovább a `VÉ` csökkentést.

Ha pedig a támadás során `00`-át (természetes 100) dobsz, akkor a fenti bónuszokon kívül még `+5`-tel csökkentheted ellenfeled **Védő Értékét**. 

A Fárasztó taktikának leginkább körbevett ellenfél esetén van értelme: a pribékek kifáraszthatják a „vadat”, míg vezetőjük felkészül.

Kapcsolódó fortély: [Fárasztás](fortelyok.harci/farasztas.md) harci fortély

---
### Visszafogott taktika

⭕kisebb, meghatározható max sebzés. Ez olyankor szokott lenni, amikor elég egy kis seb ejtése, nem cél az ellenfél megölése⭕
 
⭕TODO⭕

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

A roham vehemensebb (és őrültebb) verziója. A harcos ekkor szinte semmit nem törődik védekezésével, mindent megtesz, hogy (dupla) sebzést érjen el. Különlegessége, hogy erre az egy támadásra nem érvényesülnek a sérülésből adódó **TÉ levonások**, az adrenalin elsöpör minden gátat. Súlyosan sérült harcosok utolsó mentsvára lehet ez a taktika. Küzdelmenként **legfeljebb 1x** alkalmazható. A fentieken és a harcérték módosítókon kívül az **Öngyilkos roham** minden másban megegyezik a sima **Rohammal**.

Módosítók az első oda-vissza csapásnál:

- `TÉ:+25` ; `VÉ:-50`
- Támadó `TÉ` büntetése sebesülésből nem érvényesül
- `VÉ` csökkentés duplázódik
- Sebzés: `+7 SP`

---
### Támadás erőből taktika

Erre a [Támadás erőből](fortelyok.harci/tamadas_erobol.md) fortélyt használhatod (lásd a leírását).

E taktika mellett más harci taktikát nem alkalmazhatsz.

---
### Érintő taktika

Ha csak meg akarunk érinteni valakit harc közben, az könnyebb, mint puszta kézzel sérülést okozó támadást végbevinni. Az Érintő támadás harcértékei ezért:

```
KÉ:0, TÉ:0, VÉ:-10
```

Tehát a támadásra kisebb a büntetés, mint puszta kézre, a védekezés viszont nem változik.

---
