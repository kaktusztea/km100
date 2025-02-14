## Harci taktikák

| **Taktika név**                                                       | **Hatás**                                                                                                                                                                                                                              |
| :-------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Támadó taktika](#t%C3%A1mad%C3%B3-taktika)                           | `TÉ:+1 = VÉ:-2`, max `TÉ:+15`                                                                                                                                                                                                          |
| [Védő taktika](#v%C3%A9d%C5%91-taktika)                               | `VÉ:+1 = TÉ:-2`, max `VÉ:+20`                                                                                                                                                                                                          |
| [Teljes Védekezés taktika](#teljes-v%C3%A9dekez%C3%A9s-taktika)       | `VÉ:+30`, ellenfeled csak `kiskockával` csökkenthet rajtad `VÉ`-t. Folyamatos hátrálás, nincs támadás, nem kombinálható más taktikával.                                                                                                |
| [Kezdeményező taktika](#kezdem%C3%A9nyez%C5%91-taktika)               | `KÉ:+1 → VÉ:-2`, max `KÉ:+10`                                                                                                                                                                                                          |
| [Kiváró taktika](#kiv%C3%A1r%C3%B3-taktika)                           | • Átengedett `KÉ`, cserébe első visszatámadásra `TÉ:+5`<br/>• **Támadó taktikával** együtt mehet, Védővel nem, több ellenfeles harcban sem.                                                                                            |
| [Fárasztó taktika](#f%C3%A1raszt%C3%B3-taktika-) ⇄                    | • `+2 VÉ` csökkentés <br />• Sebzés helyett: nagykockás VÉ csökkentés + további `+10 VÉ` csökkentés<br />• `00` dobásnál: további `+5 VÉ` csökkentés<br />• Csak Előnyös helyzetből lehet alkalmazni                                   |
| [Visszafogott taktika](#visszafogott-taktika-) ⇄                      | Kisebb értékű kockával dobhatsz sebzéskor. Lásd a taktika részletes leírását!                                                                                                                                                          |
| [Roham taktika](#roham-taktika)                                       | • `TÉ:+20`, `VÉ:-40` (első oda-visszacsapáskor)<br/>• `VÉ` csökkentés duplázódik első oda-visszacsapásnál , Sebzéshez: `+5 SP` (oda-vissza)                                                                                            |
| [Öngyilkos roham taktika](#%C3%B6ngyilkos-roham-taktika)              | • `TÉ:+25`,`VÉ:-50` (első oda-visszacsapáskor)<br/>• `VÉ` csökkentés duplázódik első oda-visszacsapásnál, Sebzéshez: `+7 SP` (oda-vissza)<br/>• `TÉ` büntetések (sérülésből) nem érvényesek<br/>• Max `1x` használható egy küzdelemben |
| [Támadás erőből taktika](#t%C3%A1mad%C3%A1s-er%C5%91b%C5%91l-taktika) | Erre a [Támadás erőből](fortelyok.harci/tamadas_erobol.md) fortélyt használhatod (lásd a leírását).                                                                                                                                    |
| [Érintő taktika](#%C3%A9rint%C5%91-taktika-) ⇄                        | `KÉ:0`, `TÉ:0`, `VÉ:-10`                                                                                                                                                                                                               |

🔆 A taktikák használatát kör elején, kezdeményezés előtt kell bejelenteni, kivéve az ⇄ jellel megjelölteket, azokat kör és támadások közben is lehet variálni.

### Ökölszabály Védő Érték eltolásra 🔆

Egyes taktikák kombinálhatóak egymással, mások nem (lásd leírásukat), de fontos szabály, hogy **Védő Értékedet** legfeljebb `-30/+30`-al tolhatod el.

---
### Támadó taktika

```
TÉ:+1, VÉ:-2
...
TÉ:+15, VÉ:-30
```

✅ [Meglepetés](065_01_harci_helyzetek.md#meglepetés) szituációban

❌ [Észrevétlen támadás](065_01_harci_helyzetek.md#észrevétlen-támadás) szituációban

✅ **Kezdeményező taktikával** együtt

✅ **Kiváró taktikával** együtt

❌ Más taktikával együtt

Dönthetsz úgy, hogy a következő körben a támadásra helyezed a hangsúlyt és nyomulsz előre. Ekkor védekezésedre kevésbé ügyelsz, sebezhetőbb vagy. Te határozod meg, hogy mennyire tolod el a harcmodorodat a támadás irányába. `TÉ`-det `+1-15`-ig növelheted meg ideiglenesen. Minden pont növelés után `-2` **Védő Érték** módosítót kapsz.

A szándékot, hogy Támadó taktikát akarsz alkalmazni, előre be kell jelentened, mielőtt az adott kör elkezdődött volna. Kör közben nem változtathatsz a taktikán. Ha ebben a taktikában küzdesz, akkor lehetőségeidhez mérten folyamatosan nyomulsz előre.

---
### Védő taktika

```
VÉ:+1, TÉ:-2
...
VÉ:+20, TÉ:-40
```

❌ [Meglepetés](065_01_harci_helyzetek.md#meglepetés) szituációban

❌ [Észrevétlen támadás](065_01_harci_helyzetek.md#észrevétlen-támadás) szituációban

❌ Más taktikával együtt

Dönthetsz úgy, hogy a következő körben a védekezésedre helyezed a hangsúlyt. Ekkor kisebb vehemenciával támadsz, ez megmutatkozik Támadó Értékedben is.

Te határozod meg, hogy mennyire tolod el a harcmodorodat a védekezés irányába. **Védő Értékedet** `+1-20`-ig növelheted meg ideiglenesen. Minden pont növelés után `-2` **Támadó Érték** módosítót kapsz.

Tehát vállalásodtól függően így módosíthatod harcértékeidet. Pl:

---
### Teljes Védekezés Taktika

```
- VÉ:+30
- Ellenfeled csak "kiskockával"
  csökkenthet rajtad VÉ-t.
```

❌ Más taktikával együtt

Ha úgy döntesz, hogy a következő körben csak a védekezéssel törődsz (előre be kell jelenteni!), kizárólag a feléd irányuló támadásokat próbálod elkerülni, nem támadsz (!), valamint folyamatosan hátrálsz, akkor `+30 VÉ` módosítót kapsz arra a körre. A kör közben nem változtathatsz a taktikádon, ha ismét támadni akarsz, azt csak a következő körben teheted meg.

Fontos, hogy másra nem pazarolhatod figyelmedet, kizárólag a védekezésre. Ha nem így teszel, vagy nem vagy képes a folyamatos hátrálásra (például egy fal miatt, ami elzárja mögötted az utat), akkor a KM – tetszése szerint – csökkentheti a fenti `VÉ` módosítódat, akár `0`-ig is.

---
### Kezdeményező taktika

```
KÉ:+1, VÉ:-2
...
KÉ:+10, VÉ:-20
```

✅ **Támadó taktikával** együtt, de ügyelj a [Védő Érték eltolás ökölszabályra](#%C3%B6k%C3%B6lszab%C3%A1ly-v%C3%A9d%C5%91-%C3%A9rt%C3%A9k-eltol%C3%A1sra-)!

✅ **Visszafogott taktikával** együtt

✅ **Érintő taktikával** együtt

❌ Más taktikával együtt

Ha mindenáron magadhoz akarod ragadni a kezdeményezést megteheted, de ennek ára van. A kapkodás sebezhetővé tesz. Kezdeményező taktika alkalmazása esetén megnövelheted **Kezdeményező Értékedet** maximum `10`-el de cserébe kétszer akkora **Védő Érték** csökkenést szenvedsz el **az ellenfél első támadásával szemben** (akár megnyerted így a kezdeményezést, akár nem)

---
### Kiváró Taktika

```
Átengedett KÉ
 → TÉ:+5 első
   visszatámadásra
```

✅ **Támadó taktikával** együtt

✅ **Visszafogott taktikával** együtt

✅ **Támadás Erőből taktikával** együtt

✅ **Érintő taktikával** együtt

✅ **Roham ellen** is bevethető
 
❌ Más taktikával együtt

❌ Több ellenféllel való harc esetén

Ha inkább bevárod ellenfeled támadását, kifejezetten az ellencsapásra készülve, az apró előnyhöz juttathat. Ha megnyered a `KÉ`-t akkor szándékosan átengedheted ellenfelednek a támadás elsőbbségét, majd amennyiben nem kapsz sebet, előnyt kovácsolhatsz a jó időzítésből. Hatása:

Ha úgy döntesz, hogy a fenti feltételekkel lemondasz a kezdeményezésről, cserébe az adott körben **első visszatámadásodra** `TÉ:+5` módosítót kapsz.

---
### Fárasztó taktika ⇄

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

❌ Más taktikával együtt

Csak **Előnyös helyzetből** lehet alkalmazni. Tehát azonos, vagy nagyobb fegyverméretnél.

Ha fárasztani kívánod ellenfeledet, ellenállását megtörni anélkül, hogy sebet ejtenél rajta, akkor a harc ugyanúgy folyik, mint más esetben, csak `+2`-vel nő **VÉ csökkentésed** ha nem érsz el találatot támadó dobásod során.

Sebző támadás esetén pedig elmarad maga a sebzés – helyette **nagykockával** és további `+10`-el csökkentheted ellenfeled **Védő Értékét**. A Többszörös találat nem növeli tovább a `VÉ` csökkentést.

Ha pedig a támadás során `00`-át (természetes 100) dobsz, akkor a fenti bónuszokon kívül még `+5`-tel csökkentheted ellenfeled **Védő Értékét**. 

A Fárasztó taktikának leginkább körbevett ellenfél esetén van értelme: a pribékek kifáraszthatják a „vadat”, míg vezetőjük felkészül.

Kapcsolódó fortély: [Fárasztás](fortelyok.harci/farasztas.md) harci fortély

---
### Visszafogott taktika ⇄

```
Sebzéskocka változik:
TÉ:-10  →  k20 helyett k10
TÉ:-20  →  k20 helyett k6
TÉ:-30  →  nincs kockadobás
           csak a fegyver alap sebzése
```

A [Harci anatómia](fortelyok.harci/harci_anatomia.md) fortély minden foka `10`-zel csökkenti a `TÉ` büntetést.

✅ **Kezdeményező taktikával** együtt

✅ **Kiváró taktikával** együtt

❌ Más taktikával együtt


Szándékosan kisebb sebzést próbálsz okozni találatkor - általában olyankor fordul elő, mikor nem cél az ellenfél megölése.

Némi ritmus megtörés bevállalásával csökkentheted az okozott sebzést: kisebb értékű kockával dobhatsz sebzéskor.

---
### Roham taktika

```
Első oda-vissza csapásnál:
- TÉ:+20, VÉ:-40
- VÉ csökkentés duplázódik (oda-vissza)
- Sebzés: +5 SP (oda-vissza)
```

❌ Más taktikával együtt

Roham esetén **az első oda- és visszacsapás során** a támadó `TÉ:+20` és `VÉ:-40` módosítót kap, és `+5 SP` bónuszt sebzésdobására (`+1` sebzés kategória). Az okozott **VÉ csökkentés** duplázódik az első oda- és visszacsapásnál is.

Ha roham során a karakter sebző támadást ér el, akkor az őt sújtó **VÉ büntetés** azonnal megszűnik, a rá leadott visszacsapást már normál VÉ-vel várhatja és a `+5 SP` bónusz sem jár a visszatámadó félnek.

A **körön belüli** további támadások már normál harcértékekkel történnek és innen már választható harci taktika is!

Rohamhoz legalább `5-10` méter nekifutás szükséges. Hogy pontosan mennyi, az szituáció-függő, a KM szava dönt a terepviszonyok és a felszerelés súlyának ismeretében.

Fontos, hogy Rohamnál is számítanak a fegyverméret kategóriák, tehát egy pikás védekezőt megrohamozni nem mindig bölcs dolog...

---
### Öngyilkos roham taktika

```
Első oda-vissza csapásnál:
- TÉ:+25, VÉ:-50
- VÉ csökkentés duplázódik (oda-vissza)
- Támadó TÉ büntetése sebesülésből
  nem érvényesül
- Sebzés: +7 SP (oda-vissza)
```
❌ Más taktikával együtt

A roham vehemensebb (és őrültebb) verziója. A harcos ekkor szinte semmit nem törődik védekezésével, mindent megtesz, hogy (dupla) sebzést érjen el. Különlegessége, hogy erre az egy támadásra nem érvényesülnek a sérülésből adódó **TÉ levonások**, az adrenalin elsöpör minden gátat. Súlyosan sérült harcosok utolsó mentsvára lehet ez a taktika. Küzdelmenként **legfeljebb 1x** alkalmazható. A fentieken és a harcérték módosítókon kívül az **Öngyilkos roham** minden másban megegyezik a sima **Rohammal**.

---
### Támadás erőből taktika

Erre a [Támadás erőből](fortelyok.harci/tamadas_erobol.md) fortélyt használhatod (lásd a leírását).

✅ **Kiváró taktikával** együtt

❌ Más taktikával együtt

---
### Érintő taktika ⇄

```
KÉ:0, TÉ:0, VÉ:-10
```

✅ **Kezdeményező taktikával** együtt

✅ **Kiváró taktikával** együtt

❌ Más taktikával együtt

Ha csak meg akarunk érinteni valakit harc közben, az könnyebb, mint puszta kézzel sérülést okozó támadást végbevinni. Az Érintő támadásnál a Puszta kéz harcértékei ezért a fentiek. Tehát a támadásra kisebb a büntetés, a védekezés viszont nem változik.

---

🔗 [Harci alakzatok](065_03_harci_alakzatok.md) →

⚜️ [Nyitóoldal](start.md#6-harcrendszer-%EF%B8%8F)
