## Életerő

### Életerő Pont
A Karakteralkotás fejezetben már ismertetett Életerő pontokat használjuk a harcban elszenvedett sérülések jegyzésére. Emlékeztetőül:

```
ÉP = 12 + (Edzettség x 2)
```

Ha sebet kapunk, ezekből a pontokból kell levonnunk az okozott sérülést (lásd [Sebesülés fejezet](#sebes%C3%BCl%C3%A9s)).

**Életerő Pontok elosztása**

|S1  <br>(ÉP/4)|S2  <br>(ÉP/4)|S3  <br>(ÉP/4)|S4  <br>(ÉP/4)|
|---|---|---|---|
|.|.|.|.|
|.|.|.|.|
|.|.|.|.|
|.|.|.|.|
|.|.|xx|xx|

Az **Életerő Pontok** (ÉP) 4 egészség kategória közt egyenlő arányban oszlanak el. A maradékot balról jobbra osztjuk el. Az ún. sebesülés kategóriák szimulálják, hogy milyen állapotban van a karakter. Az `S1` az enyhén, `S2` a közepesen, `S3` a súlyosan, az `S4` pedig a halálosan sérült állapotot jelöli.

Az egyes kategóriák jelölésében az "`S`" a „Sebesülés” -re utal, a szám utána pedig könnyen azonosítja állapotunkat.

A bal oldali ábra `18 ÉP` elosztását mutatja be. Az állapot romlásának hatásait a „Sebesülés” fejezetben ismertetjük.

---
### Kábulat Életerő Pont (KT)

A rendszer különbséget tesz a fizikai sérülés és a karakter azon állapota között, amely a pillanatnyi állapotát, ájulástól való „távolságát” meghatározza. Ez utóbbit szimulálja a **Kábulat Életerő Pont** (`KT`). A `KT` nem azonos a **Fájdalomtűrés** képzettséggel, tőle független fogalom. A `KT` jelenthet kábultságot, rosszullétet, mérgezés okozta gyengeséget, sőt másnaposságot is!

A KT-nek nincs kezdeti értéke, csak a fenti hatások valamelyike következtében jöhet létre. Tehát ebből a szempontból jegyzése az `ÉP`-vel ellentétes. Mikor valaki olyan „sebesülést” szenved el, hogy `KT`-t „szerez”, a hatás megegyezik azzal, mint amit valós sebesülés esetén tapasztal, de nem jár strukturális károsodással (valódi ÉP sebbel), vagy halállal, legfeljebb ájulással. Tipikus esete a `KT` sebesülésnek, mikor valakit alaposan fejbe kólintanak. Ez – szándéktól függően – okozhat valós sebesülést is, de ezen kívül `Kábulat Életerő Pontokat` is szül. Másik példa lehet, mikor a karakter rosszullétet okozó mérget iszik.

A sima `ÉP` és a `KT` értékek kezelése ugyanabban az ÉP táblázatban történik, hatásaik is megegyeznek, csak a `KT` esetén nincs valós fizikai sérülés. Így tehát a „sebesülés” okozta harcérték levonások úgy számítandóak, mintha valós sebzés történt volna! A gyakorlatban ez úgy néz ki, hogy ha a karakter Kábulat ÉP-t szerez, azt bejelöli a rendes `ÉP` táblázatban.

---
#### Sebzések jelölése az ÉP táblázatban
Először jelöljük be a valós sebesülés okozta ÉP-ket, majd utána a Kábulat ÉP-ket (ajánlott egy „**K**” betű írása a rubrikákba).

Ha egy karakternek egy korábbi fejbekólintás okán vannak már `KT`-i és egy újabb – valós – sebet szerez, akkor az újabb sebet a legutolsó valós seb után írjuk be, a meglevő `KT`-ket pedig „toljuk lejjebb”. Ha `KT`-k hatására betelik az életerő táblázat, a karakter akkor is életben marad. Halált csak a valós `ÉP`-k 0-ra csökkenése okozhat.

---
#### Kábulat ÉP gyógyulása

A Kábulat ÉP, mivel nem valós sebesülés okozta, gyorsabban „gyógyul”, mint a valós ÉP seb. Fizikai behatás esetén kb. **óránként 1 pont „tűnik el”**, és így szép lassan „visszaolvad” a valós sebzésbe. Mérgezés, betegség esetén a hatás tartósabb is lehet, itt a KM dönt. **Alvás közben** a gyógyulási sebesség duplázódik, tehát **2KT/óra**. Ha a KM úgy látja indokoltnak eltérhet a fenti számoktól.

---
#### Tartós rosszullét

Ha a karakter például méregnek „köszönhetően” tartósan gyengélkedik, akkor tartósan alkalmazhatjuk a `KT`-ket, azaz a rosszullét idejére ezek megmaradnak, vagy lassabban tűnnek el.

---
#### Verekedés, Kocsmai bunyó és Kábulat ÉP

A `KT` kiválóan alkalmas kocsmai verekedések, kisebb – nem „vérre menő” – összetűzések szimulálására is. Mint ahogy azt a „Fegyverek” fejezetben láthatjuk, a Puszta kéz sebzése mindig `KT` (kivéve egyes harcművész stílusokat).

**Minden 5. KT okoz csak 1 ÉP valós sebesülést.**

---
#### Fejbe vágás

Gyakori eset, hogy valakinek ráhúznak egy nagyot a fejére. Például sisakos ellenfelet fejen találnak egy buzogánnyal. A sisak ugyan megvédi, de a feje mégis igen nagy traumát szenved el, pár körig meglehetősen kellemetlenül érzi magát. Ez természetesen helyzet specifikus, a – KM dönt –, de irányadónak elmondhatjuk, hogy ilyenkor például plusz 2-3 KT büntetést kap az áldozat, amelyek azonban pár kör alatt elmúlnak. Ne keverjük a [Fejbe vágást](#fejbe-v%C3%A1g%C3%A1s) a 🗡️[Leütés hátulról](055_02_harci_taktikak.md#le%C3%BCt%C3%A9s-h%C3%A1tulr%C3%B3l-fejretark%C3%B3ra) harci taktikával!

---
#### ⚡ Példa Kábulat ÉP alkalmazására

```diff
⭕TODO: Aktualizálni a kész Orvtámadáshoz (amikor kész lesz). Nem lesz Orvtámadás fortély. Csak észrevétlen támadás van.
```

Cravignon-t leütik hátulról. ÉP-inek száma 14. Támadója mesterfokú **Orvtámadással** rendelkezik. Sebzést dob `k6`-al, az eredmény `4`. Ekkor a mesterfokú Orvtámadás miatt a valós sebzés csak `2 ÉP`. Lássuk a kábulat sebzést:
`4 KT + k10SP` amely bónusz szintén a `Mf` miatt csak `KT` sebzést okoz. `k10` dobás eredménye: `7`.

Az összesített `KT` sebzés tehát: `4+7=11`. A hatás így `11 ÉP`-nyi sebre vonatkozik, ebből `2 ÉP` valós sérülés. Cravignon tehát bejelöl `2 ÉP` valós és `11-2=9 KT` sérülést.

Látható, hogy a karaktert irdatlanul fejbe kólintották, ha elrontja **Fájdalomtűrés próbáját** `18-as célszám` ellen, akkor elájul. Maradt `2` „érintetlen” `ÉP`-je.

Ha további seb nem éri, akkor – a magához térés után – a `9 KT` 9 óra alatt tűnik el, Cravignon pedig `12 ÉP`-vel és egy púppal a fején éli tovább életét.

---
### Sebesülés

Ha a karakter találatot kap, harcértékeit - fizikumától függően - levonások sújtják. Persze ami például egy nyeszlett alakot az összeesés szélére sodor, az nem okoz akkora hátrányt egy edzett korgnak.

Ezért kerültek bevezetésre a sebesülés kategóriák. A karakter Életerejét 4 kategória szimbolizálja, melyek között karakteralkotáskor kell elosztani az **Életerő Pontokat.** (Lásd [Karakteralkotás – Életerő Pontok](010_karakteralkotas.md#%C3%A9leter%C5%91-pontok))

Mikor a karaktert sebesülés éri, elkezdi bejelölni az Életerő táblázatban a legmagasabb (`S1`) kategóriában lévő mezőket fentről lefelé. Mikor az első oszlop „betelt”, folytatja az `S2`, majd az `S3` kategóriában levőkkel és így tovább.

Hasznos segítség lehet, ha sérüléskor nem beikszeljük az egyes négyzeteket, hanem a sebesülés „sorszámát” (hányadik seb a harc során) és annak jellegét (S,V,Z) írjuk beléjük (Szúró,Vágó,Zúzó), megkönnyítve a dolgunkat: rögtön látjuk, hány és mekkora sebünk van. (A Kábulat ÉP (KT) sérülések mezőbe pedig „`K`” betűt írjunk). Példa: „`Z2`” jelölés 4db rubrikában: ez a karakter második sebe és egy 4 ÉP-s zúzott sebet jelöl.

![](images/02_eletero_tablazat_harcertek_levonassal_small.png)

Az első (`S1`) kategóriában lévő karaktert még nem sújtják negatív módosítók, sérülése – számára – olyan könnyű, ami nem akadályozza a harcban.

Az `S2`, `S3` és `S4` kategóriákba kerülve viszont már rendre `-10`; `-20` és `-30` `TÉ` a harcérték büntetés. Ezeket az értékeket viszont mérsékli az `Önuralom` tulajdonság és a Fájdalomtűrés képzettség összege. Így tehát a levonások értéke karakterenként változik.

`0 ÉP`-re érve a karakter elájul, és haldokolni kezd (Lásd [Haldoklás](#haldokl%C3%A1s)). Ha további sebet kap, meghal.


---
#### Fájdalomtűrés

A Fájdalomtűrés képzettség fontos szerepet játszik a harcban elszenvedett sebek fájdalmának elnyomásában, illetve egyéb helyzetekben a kín elviselésében. Részben játéktechnikai gyorsítás miatt, részben azért teszünk különbséget a harc közben és azon kívüli fájdalomtűrés miatt, mert harc közben az adrenalin hatására jobban bírja a karakter a fájdalmat, valamint próbáltuk a harc heroizmusát megőrizni.

---
#### Fájdalomtűrés harc közben

Ha harc közben más sebesülés kategóriába lép a karakter, `TÉ` levonást kap büntetésül. Ezt az értéket csökkenti a **Fájdalomtűrés** képzettség és az **Önuralom** tulajdonság összege.

⭕**Bónusz**: a **Harcos elme** fortély minden foka további `1 pontot` csökkent.⭕

| - | S1 | S2 | S3 | S4 |
| :-----: | :----: | :----: | :----: | :----: |
| TÉ levonás | - | -10 | -20 | -30 |

```
A levonást csökkenti: `Önuralom` + `Fájdalomtűrés`
```

#### S4 kategóriás fájdalomtűrés
⭕[Harci láz ad bónuszt?](https://github.com/kaktusztea/km100/wiki/ISSUE.TODO.fortelyok#harci-l%C3%A1z)

```
Fájdalomtűrés (K) + Edzettség (T)  vs.  12
```

Ha a karakter az S4-es (Súlyosan sebesült) kategóriába ér egyszeri Fájdalomtűrés próbát kell dobnia Nehéz (`12`) célszám ellen. Siker esetén ezt a próbát a következő sebesüléskor kell csak újradobnia.

---
#### ⚡ Példa Fájdalomtűrésre

Tetves Fájdalomtűrése `7.szintű`, `Önuralma:+1` (`összesen:8`)
Ekkor az ő sebesülés táblázata így néz ki:

| - | S1 | S2 | S3 | S4 |
| :-----: | :----: | :----: | :----: | :----: |
| TÉ levonás | - | -2 | -12 | -22 |


---
#### Fájdalomtűrés harcon kívül

Mérgezés, kínzás, egyéb fájdalom esetén a karakterek Fájdalomtűrés-próbát kell dobnia a KM által meghatározott célszámra.


---
#### Sérülés hatása képzettségpróbára

Ha megsérül a karakter, képzettségpróbáira levonások járnak. Hogy mennyi, az attól függ, hogy melyik sebesülés kategóriában van, illetve hogy fizikai mozgást igénylő, vagy nem igénylő képzettségét teszi próbára:

| - | S1 | S2 | S3 | S4 |
| :-----: | :----: | :----: | :----: | :----: |
| Fizikai képzettség | - | -2 | -4 | -6 |
| Egyéb képzettség | - | - | -1 | -3 |


---
#### Vértek, SFÉ

→ [STUDY: Vértek, Páncélok](https://github.com/kaktusztea/km100/wiki/STUDY.vertek.pancelok)

```diff
- Itt inkább az általános szabályokat írjuk be, a konkrét vérteket a doksi végén ismertessük táblázatos formában.
```


---
#### ⚡ Példa a sebesülésre

Az alábbi példa Lord Gustav – Domvik lovagjának – egészség kategóriáit mutatja. `17 ÉP`-je van, `Önuralom` tulajdonságának és `Fájdalomtűrés` képzettségének összege pedig `11`.
`(Önuralom + Fájdalomtűrés) = 11`

Ebben az esetben az ő Életerő táblázata a következőképpen néz ki: minden oszlopba `4` - `4` `ÉP` kerül (`17 / 4` kerekítve). A maradék `1 ÉP`-t pedig balról jobbra „osztjuk el”, tehát az `S1` oszlopba kerül.

Sebek jellegének jelölései:
- **S: Szúrt seb**
- **V: Vágott seb**
- **Z: Zúzott seb**
- **K: Kábulat ÉP**

![](images/03_eletero_lord_gustav_small.png)

Találat esetén a sebesülést először az `S1` rubrikában kezdjük jelölni, oszlopon belül pedig fentről lefelé. Ha Lord Gustav egy `2 ÉP`-s sebet kap, az az `S1` oszlopban kerül bejelölésre fentről lefele. Ilyenkor még nem sújtja levonás.

Gustav ismét megsebesül. Ezúttal `5 ÉP`, ezzel az `S2` kategóriába kerül. Mivel a `(Fájdalomtűrés+Önuralom=11)` mérsékli a standard `S2`-nél használt (`-10TÉ`) büntetést, ezért még itt sincs `TÉ` levonás.

A harmadik seb `4 ÉP`, Gustav a harmadik (közepesen sérült) kategóriába kerül. Alapból (`-20TÉ`) lenne a büntetés, de ez (`-9TÉ`)-re mérséklődik (`-11`).

Gustav hátrálás közben belefejel a kovácsoltvas kapuba. `4KT` a büntetése. Ezzel az `S4` (utolsó) kategóriába került. Büntetése `-19TÉ` (a `-30` helyett).

Mivel S4-es kategóriába került, jön az [automatikus Fájdalomtűrás próba](#s4-kateg%C3%B3ri%C3%A1s-f%C3%A1jdalomt%C5%B1r%C3%A9s) `12` (Nehéz) ellen Edzettséggel. Ha elrontja, akkor el is ájul.

Ha túléli a kalandot, akkor a „szerzett” `4 Kábulat ÉP` gyógyulása `4 óra` alatt, a sebek okozta ÉP csökkenés pedig a [Gyógyulás](051_eletero.md#gy%C3%B3gyul%C3%A1s) fejezetben meghatározott ütemben történik.


---
### Haldoklás

Ha a karakter ÉP-inek száma `0`-ra zuhan, akkor haldokolni kezd.

Ilyenkor dobnia kell egy `Edzettség` tulajdonságpróbát `Átlagos (5-ös)` nehézség ellen. Ha megdobja, életben marad, de `2 perc` múlva újra dobnia kell, míg nem stabilizálják. Ha elrontja, meghal.

**Stabilizálás**: `Sebgyógyítás`, vagy `Gyógyítás` képzettségpróba Átlagos (`9`) nehézség ellen. Ha egy karaktert stabilizáltak, akkor nem kell `Edzettség` próbát dobnia, de továbbra is igaz rá, hogy minden további sebzés azonnal végez vele.


---
### Gyógyulás
```
1 ÉP / nap
1 KT / óra
```

⭕Jelenleg a saját [STUDY oldalán](https://github.com/kaktusztea/km100/wiki/STUDY.gyogyulas.gyogyitas) fejlesztjük. Amint ott elkészül, bemásolni ide.

Jelenleg az `1 ÉP` / nap és `1 KT` / óra gyógyulás szabály az irányadó.
