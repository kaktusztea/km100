### Kábulat Életerő Pont (KT)

A rendszer különbséget tesz a fizikai sérülés és a karakter azon állapota között, amely a pillanatnyi állapotát, ájulástól való „távolságát” meghatározza. Ez utóbbit szimulálja a **Kábulat Életerő Pont** (`KT`). A `KT` nem azonos a **Fájdalomtűrés** képzettséggel, tőle független fogalom. A `KT` jelenthet kábultságot, rosszullétet, mérgezés okozta gyengeséget, sőt másnaposságot is!

A KT-nek nincs kezdeti értéke, csak a fenti hatások valamelyike következtében jöhet létre. Tehát ebből a szempontból jegyzése az `ÉP`-vel ellentétes. Mikor valaki olyan „sebesülést” szenved el, hogy `KT`-t „szerez”, a hatás megegyezik azzal, mint amit valós sebesülés esetén tapasztal, de nem jár strukturális károsodással (valódi ÉP sebbel), vagy halállal, legfeljebb ájulással. Tipikus esete a `KT` sebesülésnek, mikor valakit alaposan fejbe kólintanak. Ez – szándéktól függően – okozhat valós sebesülést is, de ezen kívül `Kábulat Életerő Pontokat` is szül. Másik példa lehet, mikor a karakter rosszullétet okozó mérget iszik.

A sima `ÉP` és a `KT` értékek kezelése ugyanabban az ÉP táblázatban történik, hatásaik is megegyeznek, csak a `KT` esetén nincs valós fizikai sérülés. Így tehát a „sebesülés” okozta harcérték levonások úgy számítandóak, mintha valós sebzés történt volna! A gyakorlatban ez úgy néz ki, hogy ha a karakter Kábulat ÉP-t szerez, azt bejelöli a rendes `ÉP` táblázatban.

---
#### Sebzések jelölése az ÉP táblázatban

Először jelöljük be a valós sebesülés okozta ÉP-ket, majd utána a Kábulat ÉP-ket (ajánlott egy „**K**” betű írása a rubrikákba).

---
#### Valós ÉP seb elszenvedése Kábulat ÉP után

Amennyiben a karakter életerő táblázatában van bármennyi KT, akkor egy újabb, - immár valós - ÉP seb elszenvedésekor először ezeket a KT jelölőket "alakítsuk" át valós sebbé és csak utána jelöljünk be újabb seb rubrikákat. Egyszerűen fogalmazva: egy valós sebzés először a KT-kat írja át ("felülről") és csak a "maradék" sebez újonnan.

---
#### Túlcsordult Kábulat ÉP

Amennyiben az életerő táblázat "betelt" és vannak benne Kábulat ÉP pontok, akkor a "túlcsorduló" bármilyen sebzés (ÉP, KT) felülről átírja a KT pontokat ÉP pontokra.

---
#### Kábulat ÉP gyógyulása

```
Óránként 1 KT gyógyul
Alvásban óránként 2 KT
```

A Kábulat ÉP, mivel nem valós sebesülés okozta, gyorsabban „gyógyul”, mint a valós ÉP seb. Fizikai behatás esetén kb. **óránként 1 pont „tűnik el”**, és így szép lassan „visszaolvad” a valós sebzésbe. Mérgezés, betegség esetén a hatás tartósabb is lehet, itt a KM dönt. **Alvás közben** a gyógyulási sebesség duplázódik, tehát **2KT/óra**. Ha a KM úgy látja indokoltnak eltérhet a fenti számoktól.

---
#### Tartós rosszullét

Ha a karakter például méregnek „köszönhetően” tartósan gyengélkedik, akkor tartósan alkalmazhatjuk a `KT`-ket, azaz a rosszullét idejére ezek megmaradnak, vagy lassabban tűnnek el.

---
#### Verekedés, Kocsmai bunyó és Kábulat ÉP

```
Minden 5. KT
1 ÉP sebet okoz. 
```
A `KT` kiválóan alkalmas kocsmai verekedések, kisebb – nem „vérre menő” – összetűzések szimulálására is. Mint ahogy azt a „Fegyverek” fejezetben láthatjuk, a Puszta kéz sebzése mindig `KT` (kivéve egyes harcművész stílusokat).

**Minden 5. KT okoz csak 1 ÉP valós sebesülést: 4 KT, 1 ÉP**

---
#### Fejbe vágás

Gyakori eset, hogy valakinek ráhúznak egy nagyot a fejére. Például sisakos ellenfelet fejen találnak egy buzogánnyal. A sisak ugyan megvédi, de a feje mégis igen nagy traumát szenved el, pár körig meglehetősen kellemetlenül érzi magát. Ez természetesen helyzet specifikus, a – KM dönt –, de irányadónak elmondhatjuk, hogy ilyenkor például plusz 2-3 KT büntetést kap az áldozat, amelyek azonban pár kör alatt elmúlnak. Ne keverjük a **Fejbe vágást** a 🗡️[Leütés hátulról](066_05_altalanos_manoverek.md#leütés-hátulról) harci taktikával!

---
#### ⚡ Példa Kábulat ÉP alkalmazására

⭕TODO: Aktualizálni a kész Orvtámadáshoz (amikor kész lesz). Nem lesz Orvtámadás fortély. Csak észrevétlen támadás van.⭕

Cravignon-t leütik hátulról. ÉP-inek száma 14. Támadója mesterfokú **Orvtámadással** rendelkezik. Sebzést dob `k6`-al, az eredmény `4`. Ekkor a mesterfokú Orvtámadás miatt a valós sebzés csak `2 ÉP`. Lássuk a kábulat sebzést:
`4 KT + k10SP` amely bónusz szintén a `Mf` miatt csak `KT` sebzést okoz. `k10` dobás eredménye: `7`.

Az összesített `KT` sebzés tehát: `4+7=11`. A hatás így `11 ÉP`-nyi sebre vonatkozik, ebből `2 ÉP` valós sérülés. Cravignon tehát bejelöl `2 ÉP` valós és `11-2=9 KT` sérülést.

Látható, hogy a karaktert irdatlanul fejbe kólintották, ha elrontja **Fájdalomtűrés próbáját** `18-as célszám` ellen, akkor elájul. Maradt `2` „érintetlen” `ÉP`-je.

Ha további seb nem éri, akkor – a magához térés után – a `9 KT` 9 óra alatt tűnik el, Cravignon pedig `12 ÉP`-vel és egy púppal a fején éli tovább életét.

---

🔗 [Sebesülés](061_03_sebesules.md) →

⚜️ [Nyitóoldal](start.md)