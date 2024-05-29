## Harcértékek felépítése

A karaktert a harcban harcértékei jellemzik. Ezek mutatják meg, hogy mennyire képzett a küzdelem egyes területein. Alapvetően négy érték határozza meg az aktuális harcértékeket, melyek szituációtól, forgatott fegyvertől, illetve harcmodortól függően változhatnak. Ezek a

- Kezdeményező Érték
- Támadó Érték
- Védő Érték
- Célzó Érték

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

Egyes Tulajdonságok értékei beleszámítanak a harcértékekbe. Hogy melyek azt az adott harcérték leírásánál találhatjuk a [KÉ, TÉ, VÉ, CÉ](060_03_ke_te_ve_ce.md) fejezetben.

---
### Harcérték Módosítók (HM), Célzóérték Módosítók (CM)

Lásd a [Harcérték módosítók (HM) / Célzóérték módosítók (CM)](019_hm_cm.md) fejezetet.

---
### Harcmodor képzettségek

A km100 rendszere az alábbi (Primer) harci képzettségeket ismeri:

**Közelharc, Kardvívás, Lándzsavívás, Zúzás, Hajítás, Íjászat, Lövészet, Ostromlövészet**

- **Közelharc**: Rövid (0) pengehosszú fegyverek, puszta kéz
- **Kardvívás**: minden további „pengés” fegyver (kétkezes kard is)
- **Zúzás**: zúzófegyverek, csatabárdok, csákány
- **Lándzsavívás**: Szálfegyverek

A harci képzettségek aktuális szintjétől függ, hogy az alá tartozó fegyvereket milyen általános harcérték pluszokkal forgathatja a karakter.
**Megjegyzés**: Az egyes fegyverek további erősítése a [Mesterfegyver](fortelyok.harci/mesterfegyver.md) fortéllyal lehetséges.

<br />

| Harcmodor Szint |               Hatás*                |
| :-------------: | :---------------------------------: |
|    Képzetlen    | `KÉ: -20, TÉ: -30, VÉ:-30, CÉ: -30` |
|       `1`       |     csak `-10KÉ, -20 TÉ,VÉ,CÉ`      |
|       `2`       |      csak `-5KÉ, -10 TÉ,VÉ,CÉ`      |
|       `3`       |                 `0`                 |
|       `4`       |        `+1 KÉ ; +3 TÉ,VÉ,CÉ`        |
|       `5`       |        `+2 KÉ ; +6TÉ,VÉ,CÉ`         |
|       `6`       |        `+3 KÉ ; +9 TÉ,VÉ,CÉ`        |
|       `7`       |       `+4 KÉ ; +12 TÉ,VÉ,CÉ`        |
|       `8`       |       `+5 KÉ ; +15 TÉ,VÉ,CÉ`        |
|       `9`       |       `+6 KÉ ; +18 TÉ,VÉ,CÉ`        |
|      `10`       |        `+7 KÉ ; +21 TÉ,VÉ,`         |
|      `11`       |       `+8 KÉ ; +24 TÉ,VÉ,CÉ`        |
|      `12`       |       `+9 KÉ ; +27 TÉ,VÉ,CÉ`        |
|      `13`       |        `+10 KÉ ; +30 TÉ,VÉ,`        |
|      `14`       |       `+11 KÉ ; +33 TÉ,VÉ,CÉ`       |
|      `15`       |       `+12 KÉ ; +36 TÉ,VÉ,CÉ`       |

\* A távolsági fegyvereknél értelemszerűen csak `KÉ: +1` és `CÉ: +3` jár szintenként, hiszen nincs `TÉ` és `VÉ` értékük.

---
### Harcmodorok és Manőverek

A Manőverek alkalmazását, leírását részletesen lásd a „[Manőverek](060_14_00_manoverek.md)” fejezetben.

Harc közben gyakran előfordul, hogy egy karakter speciális húzásokkal próbálkozik, egyedi cseleket vet be, hogy megkönnyítse győzelmét, például kirúgja ellenfele lábát, vagy homokot szór annak szemébe. Sokszor van olyan is, hogy egy karakter különösen jó egy adott csel alkalmazásában és azt előszeretettel veti be. Ezek a manőverek.

Vannak olyan manőverek is, melyek csak adott fegyverre, vagy harcmodorra jellemzőek, de a legtöbb szabadon, bárki által alkalmazható, amennyiben teljesíti a végrehajtás követelményeit. Vannak olyan manőverek, amelyek külön fejleszthetőek is. Ez az adott manőver leírásánál szerepel. Az ilyen ismeretet Manőver-ismeretnek nevezzük és pontokba kerülnek. Lásd alább.

---
### Manőverek tanulása

A Manőver-ismeretek tanulása szorosan összekapcsolódik a Harcmodor-képzettségekkel.

Minden nem-távolsági Harcmodor harmadik (`3.`) képzettség szintje `1` db ún. Manőverfejlesztő Pontot (**MFP**) ad. Az egyes manőver ismeretek tanulása ezekből a pontokból történik. Fontos, hogy a manővereknek csak egy része fejleszthető – kizárólag ezekre lehetséges **MFP**-t költeni. Az tanulható manőverek különböző mértékben fejleszthetők. Különböző fokon lehet felvenni őket – melyeknek természetesen követelményük is van.

---
### Mesterfegyver fortély

A kapott bónuszokat, módosítókat lásd a [Mesterfegyver](fortelyok.harci/mesterfegyver.md) fortély leírásában.
