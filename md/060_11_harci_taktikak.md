## Harci taktikák

A taktikák használatát kör elején, kezdeményezés előtt kell bejelenteni, kivéve az **(X)**-el jelölteket, azokat kör közben is lehet variálni.

### Összefoglaló

| **Taktika**                                                | **Hatás**                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :--------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Támadó taktika                                             | `TÉ:+1 = VÉ:-2`, max `TÉ:+15`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Védő taktika                                               | `VÉ:+1 = TÉ:-2`, max `VÉ:+20`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Kezdeményező taktika                                       | `KÉ:+1 → VÉ:-2`, max `KÉ:+10`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Kiváró taktika                                             | • Átengedett KÉ, cserébe első visszatámadásra `TÉ:+5`<br/>• Támadó taktikával együtt mehet, Védővel nem, több ellenfeles harcban sem.                                                                                                                                                                                                                                                                                                                                       |
| Védekező harc                                              | `VÉ:+30`, folyamatos hátrálás, nincs támadás, nem kombinálható más taktikával                                                                                                                                                                                                                                                                                                                                                                                               |
| Fárasztás                                                  | Nyert a Kezdeményezés szükséges<br/>• ⭕VÉ csökkentésre: `+2`<br/>• Sebzés helyett: további `+10VÉ` csökkentés, saját VÉ is csökken `3`-mal.⭕                                                                                                                                                                                                                                                                                                                                |
| Roham                                                      | • `TÉ:+20`, `VÉ:-40` (első oda-visszacsapáskor)<br/>• VÉ csökkentés duplázódik, Sebzéshez: `+5 SP`                                                                                                                                                                                                                                                                                                                                                                          |
| Öngyilkos roham                                            | • `TÉ:+25`,`VÉ:-50` (első oda-visszacsapáskor)<br/>• VÉ csökkentés duplázódik, Sebzéshez: `+7 SP`<br/>• TÉ büntetések (sérülésből) nem érvényesek, max `2x` használható egy küzdelemben                                                                                                                                                                                                                                                                                     |
| Belharci szituáció                                         | • Bekerülni: „Belharcba kerülés” manőverrel<br/>• Kijönni: „Kibontakozás” manőverrel<br/>• Mindenki a saját Harcmodorának módosítóival küzd<br/>• Belharc fortély bónuszai: `KÉ:+2`, `TÉ/VÉ:+3` fokonként. Csak **Közelharc** harcmodorban jár.<br/>• A `rövid (0)` pengénél nagyobb fegyverek értékei: `0`-ra esnek, sebzésük max: `+1 SP`,  „**Harckeret**” csökken `5`-el. **Erőbónusz** és **MF** fortély bónuszai maradnak.<br/>• Puszta kéz értékei `0`-ra emelkednek |
| Támadás erőből                                             | A [Támadás erőből](fortelyok.harci/tamadas_erobol.md) fortélyt használod (lásd a leírását).                                                                                                                                                                                                                                                                                                                                                                                 |
| Leütés hátulról                                            | • Követelmény: „Észrevétlen támadás” harci helyzet, Sebző Találat<br/>• Ha Súlyos a seb (`12 ÉP`) → Fájdalomtűrés (+Edzettség) próba (`12`). Ha nincs meg, elájul.<br/>• [Harci anatómiával](fortelyok.harci/harci_anatomia.md) könnyebb (lásd a leírást)                                                                                                                                                                                                                   |
| Orvtámadás                                                 | • Követelmény: „Észrevétlen támadás” harci helyzet<br/>• Bónuszt ad: **Harci anatómia** fortély                                                                                                                                                                                                                                                                                                                                                                             |
| Érintő támadás **(X)**                                     | `KÉ:0`, `TÉ:0`, `VÉ:-10`                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Csonkolás **(X)**                                          | • Kéz csonkolása: (áldozat `max ÉP / 3`) (felfele kerekítve) sebzés szükséges<br/>• Láb csonkolása: (áldozat `max ÉP / 2`) (felfele kerekítve) sebzés szükséges                                                                                                                                                                                                                                                                                                             |
| Kijelölt testrészre támadás **(X)**                        | Sebző támadás `TÉ:-20`-al                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Pontok támadása harc közben **(X)**                        | • Követelmény: **Harci anatómia** fortély – `2.fok`<br/>• Követelmény: **Pontra támadás** manőver                                                                                                                                                                                                                                                                                                                                                                           |
| Visszafogott csapás / Harc az ellenfél elfogásáért **(X)** | ⭕TODO⭕ Bónuszt ad: **Harci anatómia** fortély                                                                                                                                                                                                                                                                                                                                                                                                                               |

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
### Védekező harc

```
VÉ:+25
```

Ha úgy döntesz, hogy a következő körben csak a védekezéssel törődsz (előre be kell jelenteni!), kizárólag a feléd irányuló támadásokat próbálod elkerülni, nem támadsz (!), valamint folyamatosan hátrálsz, akkor `+25 VÉ` módosítót kapsz arra a körre. A kör közben nem változtathatsz a taktikádon, ha ismét támadni akarsz, azt csak a következő körben teheted meg.

Fontos, hogy másra nem pazarolhatod figyelmedet, kizárólag a védekezésre. Ha nem így teszel, vagy nem vagy képes a folyamatos hátrálásra (például egy fal miatt, ami elzárja mögötted az utat), akkor a KM – tetszése szerint – csökkentheti a fenti `VÉ` módosítódat, akár `0`-ig is. A Védekező harc nem kombinálható más taktikával.

---
### Fárasztás
```
- Nyert KÉ szükséges
- ⭕Előnyös helyzet szükséges (pengehossz különbség kisebb 0,5 pengénél)
```
```diff
- Aktualizálni
```

- Nyert kezdeményezés szükséges
- VÉ csökkentésre: `+2`
- Sebzés helyett: további `+10 VÉ` csökkentés (a Többszörös találat nem növeli tovább)
	- Hátrány: a "sebzős" esetben az intenzív plusz mozgástól te is elszenvedsz konstans `3 VÉ` csökkenést.

Ha fárasztani kívánod ellenfeledet, ellenállását megtörni anélkül, hogy sebet ejtenél rajta, akkor a harc ugyanúgy folyik, mint más esetben, csak nyert kezdeményezést követően mindig `+2`-vel nő **VÉ csökkentésed**.

Sebző támadás esetén pedig ugyanez, de elmarad maga a sebzés – helyette további `+10`-el csökkentheted ellenfeled **Védő Értékét**. ⭕Ehhez a taktikához „fel kell pörgethed” magad, így minden alkalmazásakor Te is elszenvedsz egy ⭕`+3 VÉ`⭕ csökkenést.

A taktika használatát mindig a Kezdeményező dobás előtt kell bejelentened. Amennyiben elveszted a kezdeményezést, akkor sima harci kör következik számodra, amiben nem használhatsz semmilyen – kör elején bejelentendő – harci taktikát.

A Fárasztás taktikának leginkább körbevett ellenfél esetén van értelme: a pribékek kifáraszthatják a „vadat”, míg vezetőjük felkészül. Fontos: a Fárasztás **nem** használható **Rohammal** együtt.

Kapcsolódó fortély: [Fárasztás](fortelyok.harci/farasztas.md) harci fortély

---
### Roham

Roham esetén az első oda- és visszacsapás során a támadó `TÉ:+20` és `VÉ:-40` módosítót kap, és `+5 SP` bónuszt sebzésdobására (`+1` sebzés kategória). Az okozott **VÉ csökkentés** duplázódik.

Ha roham során a karakter sebző támadást ér el, akkor a rohamozót sújtó **VÉ levonások** azonnal megszűnnek.

Roham alkalmazása során nem használhatóak a **Támadó**, **Védő**, **Kezdeményező** és **Kiváró** taktikák! Fontos viszont, hogy Rohamnál is számítanak a fegyverméret kategóriák, tehát egy pikás védekezőt megrohamozni nem mindig bölcs dolog...

Rohamhoz legalább `5-10` méter nekifutás szükséges. Hogy pontosan mennyi, az szituáció-függő, a KM szava dönt a terepviszonyok és a felszerelés súlyának ismeretében.

Módosítók az első oda-vissza csapásnál:

- `TÉ:+20`, `VÉ:-40`
- VÉ csökkentés duplázódik
- Sebzés: `+5 SP`

---
### Öngyilkos roham

A roham vehemensebb (és őrültebb) verziója. A harcos ekkor szinte semmit nem törődik védekezésével, mindent megtesz, hogy (dupla) sebzést érjen el. Különlegessége, hogy erre az egy támadásra nem érvényesülnek a sérülésből adódó **TÉ levonások**, az adrenalin elsöpör minden gátat. Súlyosan sérült harcosok utolsó mentsvára lehet ez a taktika. Küzdelmenként **legfeljebb 2x** alkalmazható. A fentieken és a harcérték módosítókon kívül az Öngyilkos roham minden másban megegyezik a sima **Rohammal**.

Módosítók az első oda-vissza csapásnál:

- `TÉ:+25` ; `VÉ:-50`
- VÉ csökkentés duplázódik
- Sebzés: `+7 SP`

---
### Belharc, Belharci szituáció

```diff
- PROB_HARC_#46
```

Ha a képzett harcosnak sikerül ellenfele fegyvere „mögé”, testközelébe kerülni, akkor ebből előnyt kovácsolhat.

#### Belharci szituáció

Bejutottál ellenfeled fegyverének fenyegető vége mögé, testközelbe, de nem szükségszerűen érintésbe. Ha az általad épp forgatott fegyverre van tanult [Belharc fortélyod](fortelyok.harci/belharc.md), harcérték bónuszokat kapsz (lásd a fortély leírását). Belharci szituációban eddig tiltott manőverek végrehajtását is megpróbálhatod, melyek végbevitelének követelménye a Belharci szituáció: úgy is mint Átdobás, Feszítés/kijövetel, Kéztörés, Lábtörés, Nyaktörés.

```diff
- Átnézni ezeket a fortélyokat. Belharc fortély is kell hozzájuk?
```

Továbbá pár manőver könnyebbé válik Belharci szituációban: [Gáncsolás/lábsöprés](060_14_manoverek.md#️-g%C3%A1ncsol%C3%A1s--l%C3%A1bs%C3%B6pr%C3%A9s-l%C3%A1bbal) (belharcban `+2` Ellenpróbánál)

#### Belharcba kerülés manőver

A Belharci szituációba kerüléshez ezt a manővert kell sikerrel végrehajtani. Nehézsége alapesetben `9`-es, de fejleszthető (`2 fokkal`). ⭕Csak Közelharc harcmodor alkalmazása közben lehet megpróbálni.⭕ Bővebben lásd a [manőver leírását](060_14_manoverek.md#-belharcba-ker%C3%BCl%C3%A9s).

#### Kibontakozás/Átsiklás manőver

A **Belharci szituációból** kijövetelre ennek sikeres végrehajtására van szükség.
Nehézsége alapesetben `5`-ös. Persze csak akkor kell a próba, ha valamelyik fél benn akarja tartani a másikat.

- Ha az ellenfélnek Belharc fortélya van, akkor fokonként `+2`-vel nő a nehézség Ellenpróbánál
- Ha az alkalmazónak Belharc fortélya van, akkor dobására fokonként `+2` pontot kap Ellenpróbánál
- Ha belharci szituációban a belharcos sebesülést szenved és elrontja fájdalomtűrés próbáját
```diff
- (már nincs **Fájdalomtűrés dobás** sebesüléskor,... de itt esetleg dobhatunk...)
```
... akkor ellenfele – ha akarja – automatikusan megszüntetheti a belharci szituációt, kibontakozhat belőle.

```diff
- Sérülést bevállalva **mindenképpen** kijönni hogy lehessen?
```

#### Belharcos-fegyverek

Minden `rövid (0)` pengehosszú fegyver, kivéve ezek közül azokat a fegyvereket, melyek leírásánál külön meg van említve, hogy nem lehet velük belharcot folytatni (pl. rövidkard, csatabárd, …)

#### Belharc fortély
Legfeljebb `2.fokon` tanulható fortély, amelyet **egy konkrét, választott belharcos-fegyverre** lehet felvenni. Így többször is felvehető más-más fegyverekre. Belharci szituációban az adott fegyvert forgatva fokonként `KÉ:+2`, `TÉ/VÉ:+3` bónuszt ad. A bónuszok csak akkor élnek, ha az alkalmazó Belharci szituációban **Közelharc** harcmodort alkalmaz. Bővebben lásd a [Belharc fortély](fortelyok.harci/belharc.md) leírásánál.

#### Általános szabályok belharci szituációra

- Belharci szituációban a nem-belharcos fegyverek harcértékei `0`-ra zuhannak, sebzésük `+1 SP`, ⭕(ha alacsonyabb volt, akkor `-5 SP`)⭕, a forgató **Harckeret** értéke `5`-el csökken, továbbá **Hátrányos szituációba** kerül, a belharcos pedig **Előnyösbe**. A **Mesterfegyver** és az **Erőbónusz** értékei mindkét félnél megmaradnak.
- A Puszta kéz értékei `0`-ra emelkednek.
- Belharcban az áldozat abban a harcmodorban harcol, amiben előtte is. (De a **Belharc** fortély bónuszaihoz követelmény a **Közelharc** használata). Például egy szablyás harcoshoz bekerül egy belharcos, akkor ő továbbra is kardvívás harcmodorának értékeivel küzd, igaz szablyájának harcértékeit elveszíti annak mérete miatt.
- A Belharc 1:1 elleni szituációban használható leghatékonyabban, külső, harmadik fél ellen viszont kiszolgáltatottabb.

```diff
- TODO: Ez még vitatható, mert Attila szerint olyan, mint harcolók közé lőni.
```

Amennyiben a belharcban levő harcost egy harmadik (vele nem belharcban levő) fél támadja, akkor a belharcos a **Harc helyhez kötve** szituáció VÉ büntetéseit szenvedi el, visszatámadni pedig nem tud, hiszen össze van akaszkodva másik ellenfelével. Kivétel: Sikeres **Leszorítás** (manőver) alkalmazása után, a leszorított áldozatot beforgathatja maga és a támadó közé, kvázi patthelyzetet okozva.


⭕**TODO: Átnézendő:**

```diff
- Manőverek, amik megkövetelik a belharci szitut (és amiket ezzel kapcsolatban át kell nézni): Átdobás, Feszítés/kijövetel, Kéztörés, Lábtörés, Nyaktörés
-	    Ezek natív végrehajtásához követelmény a Belharci szituáció.
```

---
### Érintő támadás

Ha csak meg akarunk érinteni valakit harc közben, az könnyebb, mint puszta kézzel sérülést okozó támadást végbevinni. Az Érintő támadás harcértékei ezért: `KÉ:0`, `TÉ:0`, `VÉ:-10`

Tehát a támadásra kisebb a büntetés, mint puszta kézre, a védekezés viszont nem változik.

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
- Lásd még alább: [Csonkolás](060_11_harci_taktikak.md#csonkol%C3%A1s-%C3%A9s-t%C3%B6r%C3%A9s) harci taktika.

---
### Támadás erőből

A [Támadás erőből](fortelyok.harci/tamadas_erobol.md) fortélyt (lásd a leírását) használod.

E taktika mellett más harci taktikát nem alkalmazhatsz.

---
### Csonkolás és törés

Ha a harcos le kívánja vágni, vagy el akarja törni ellenfele valamely végtagját (kéz,fej), akkor:

Sikeres **Végtagra támadást** kell végrehajtania, valamint megfelelő mennyiségű `ÉP` sebzést okoznia.

- Kéz csonkolása/törése: (áldozat `max ÉP / 3`) (felfele kerekítve) sebzés szükséges
- Láb csonkolása/törése: (áldozat `max ÉP / 2`) (felfele kerekítve) sebzés szükséges

---
### Leütés hátulról (fejre/tarkóra)

- Követelmény: **Észrevétlen támadás**
- Célpont `VÉ = 30 + mozgás jellegétől függő módosító` (lásd [Észrevétlen támadás](060_10_harci_helyzetek.md#%C3%A9szrev%C3%A9tlen-t%C3%A1mad%C3%A1s))

Ha a támadás sebző **Találat**, akkor és a sebzés legalább Súlyos lenne (`12 ÉP`), akkor az áldozat Fájdalomtűrés próbát dob `12`-es célszám (**Nehéz**) ellen, ezúttal **Edzettség** tulajdonsággal. Ha nincs meg, azonnal elájul.

```
Fájdalomtűrés (K) + Edzettség (T)  vs.  12
```

Hogy megkapjuk a valós ÉP seb mennyiségét, amit az áldozat elszenved, dobjunk `k3`-al:

- `1`: nincs `ÉP` seb
- `2`: sebzés fele bement `ÉP`-ben
- `3`: a teljes sebzés bement `ÉP`-ben
Ez azért van, mert egy járatlan támadó nem tudja olyan jól megbecsülni a szükséges erő nagyságát, ha rosszul méri fel az erejét, könnyen komoly sebet okozhat.

**Harci anatómia** fortély minden foka:
- `3`-al emeli a **Fájdalomtűrés** célszámát
- `1` seb kategóriával kevesebb kell (Pl. `2.fokon` már csak `3 ÉP` sebzés elég)
- `K3` hatása `1` kategóriával csökken (Pl. `2.fokon` már sosincs `ÉP` seb)

**Megjegyezés**: a Markolat sebzése: `k20 + 0 SP` (Zúzó)

---
### Orvtámadás

Kapcsoló fortély: [Harci anatómia](fortelyok.harci/harci_anatomia.md)

Ha **Észrevétlen támadást** sikerül leadnod, akkor érvényesülnek a **Harci anatómia** fortélynál leírt bónuszok. `VÉ` értékét lásd az [Észrevétlen támadás](060_10_harci_helyzetek.md#%C3%A9szrev%C3%A9tlen-t%C3%A1mad%C3%A1s) résznél.

---
### Pontok támadása harc közben

Kapcsoló fortély: [Harci anatómia](fortelyok.harci/harci_anatomia.md)

Ha harc közben próbálsz ellenfeleden egy konkrét pont támadásával nagyobb sebzést elérni, vagy a **Harci anatómia** fortélynál leírt hatások valamelyikét elérni, akkor **Pontra támadás** manővert kell végezned (követelménye: **Harci anatómia** – `2.fok`). Amennyiben az sikeres, megkapod a fenti fortélynál megadott bónuszokat.

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
