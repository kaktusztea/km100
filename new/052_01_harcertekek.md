
```diff
⭕Kiemelni ide a harc (1.2) részt a Harcrendszer doksiból (11-22. oldal)
1.2 Harc
✅1.2.1 Harcértékek felépítése
✅1.2.2 KÉ, TÉ, VÉ, CÉ
🟡1.2.3 Mozgásgátló tényező
🟡1.2.4 Előnyös és hátrányos helyzet
🟡1.2.5 Támadások száma
```

Mikor két teremtmény fegyvert ragad és ütésekkel, szúrásokkal, vágásokkal, karmolással, harapással próbálják legyőzni egymást, akkor bizony **Fegyveres harcról** beszélünk.

---

### 1.2.1 Harcértékek felépítése

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

#### Harcérték Alapok

Első szinten minden karakter egységes konstans értékeket kap KÉ, TÉ, VÉ és CÉ értékére.

Értékeik :

```
- KÉ konstans: 10
- TÉ konstans: 20
- VÉ konstans: 120
- CÉ konstans: -30
```  

Ehhez az alapértékhez adódnak majd hozzá az egyéb módosítók.

#### Harci Tulajdonságok

Egyes Tulajdonságok értékei beleszámítanak a harcértékekbe. Hogy melyek azt az adott harcérték leírásánál találhatjuk a KÉ, TÉ, VÉ, CÉ fejezetben. ⭕(link)⭕

---

#### Harcérték Módosító (HM)

Ahogy fejlődik, megjár sok harci helyzetet, a karakter általános harcértékei fejlődnek. Ezt szimbolizálja a Harcérték módosító, melyet a játékos vehet fel karaktere szintlépésének alkalmával.

Minden karakter szintenként **maximum** **(6+Ügyesség)** pontnyi úgynevezett HM-et és **maximum 4** ún. Célzóérték Módosítót (**CM)** vehet fel (nem kötelező!) Karakter Pontjaiból. Egy HM-re, illetve CM-re **4** Karakter Pontot kell költenie.

```
Maximum: 8 HM / Szint
Maximum: 4 CM / Szint
1 HM = 5 KP
1 CM = 5 KP
```

A sima `HM` a `KÉ`, `TÉ`, és `VÉ` harcértékek növelésére szolgál, a `CM` (Célzó Érték Módosító) pedig a távolsági fegyverek használatára vonatkozik. Nem keverhetők, tehát a CM-re költhető max `4 HM` nem „pakolható át” a sima `HM`-re és viszont!

##### HM korlát

Szintenként `TÉ`-re vagy `VÉ`-re **legfeljebb** `3`-al több `HM`-et lehet költeni, mint a másikra!

---

#### Harcmodor képzettségek

A km100 rendszere az alábbi (átfogó) harci képzettségeket ismeri:

**Közelharc, Kardvívás, Lándzsavívás, Pusztítás, Hajítás, Íjászat, Lövészet, Ostromlövészet**

- **Közelharc: közelharci** **(legfeljebb 0,5 penge hosszú)** **fegyverek**
    
- **Kardvívás: minden „pengés” fegyver (kétkezes kard is)**
    
- **Pusztítás: zúzófegyverek, csatabárdok, csákány**
    
- **Lándzsavívás: Szálfegyverek**
    

A harci képzettségek aktuális szintjétől függ, hogy az alá tartozó fegyvereket milyen általános harcérték pluszokkal forgathatja a karakter.  
Megjegyzés: Az egyes fegyverek további erősítése a Mesterfegyver fortéllyal lehetséges.

 
|Harcmodor Szint|Hatás*|
| :---: | :---: |
|Képzetlen|KÉ: -20, TÉ: -30, VÉ:-30, CÉ: -30|
|1|csak -10KÉ, -20 TÉ,VÉ,CÉ|
|2|csak -5KÉ, -10 TÉ,VÉ,CÉ|
|3|0|
|4|+1 KÉ ; +3 TÉ,VÉ,CÉ|
|5|+2 KÉ ; +6TÉ,VÉ,CÉ|
|6|+3 KÉ ; +9 TÉ,VÉ,CÉ|
|7|+4 KÉ ; +12 TÉ,VÉ,CÉ|
|8|+5 KÉ ; +15 TÉ,VÉ,CÉ|
|9|+6 KÉ ; +18 TÉ,VÉ,CÉ|
|10|+7 KÉ ; +21 TÉ,VÉ,CÉ|
|11|+8 KÉ ; +24 TÉ,VÉ,CÉ|
|12|+9 KÉ ; +27 TÉ,VÉ,CÉ|
|13|+10 KÉ ; +30 TÉ,VÉ,CÉ|
|14|+11 KÉ ; +33 TÉ,VÉ,CÉ|
|15|+12 KÉ ; +36 TÉ,VÉ,CÉ|

*A távolsági fegyvereknél értelemszerűen csak +1 KÉ és +3 CÉ jár szintenként, hiszen nincs TÉ és VÉ értékük.

---

##### Harcmodorok és Manőverek

A Manőverek alkalmazását, leírását részletesen lásd a „Manőverek” fejezetben.

Harc közben gyakran előfordul, hogy egy karakter speciális húzásokkal próbálkozik, egyedi cseleket vet be, hogy megkönnyítse győzelmét, például kirúgja ellenfele lábát, vagy homokot szór annak szemébe. Sokszor van olyan is, hogy egy karakter különösen jó egy adott csel alkalmazásában és azt előszeretettel veti be. Ezek a manőverek.

Vannak olyan manőverek is, melyek csak adott fegyverre, vagy harcmodorra jellemzőek, de a legtöbb szabadon, bárki által alkalmazható, amennyiben teljesíti a végrehajtás követelményeit. Vannak olyan manőverek, amelyek külön fejleszthetőek is. Ez az adott manőver leírásánál szerepel. Az ilyen ismeretet Manőver-ismeretnek nevezzük és pontokba kerülnek. Lásd alább.

##### Manőverek tanulása

A Manőver-ismeretek tanulása szorosan összekapcsolódik a Harcmodor-képzettségekkel.

Minden nem-távolsági Harcmodor harmadik (**3.**) képzettség szintje 1 db ún. Manőverfejlesztő Pontot (**MFP**) ad. Az egyes manőver ismeretek tanulása ezekből a pontokból történik. Fontos, hogy a manővereknek csak egy része fejleszthető – kizárólag ezekre lehetséges MFP-t költeni. Az tanulható manőverek különböző mértékben fejleszthetők. Különböző fokon lehet felvenni őket – melyeknek természetesen követelményük is van.

Ha ezeken felül is manővert akar tanulni, akkor fokonként +10KP-t kell költenie.

  ---

#### Mesterfegyver fortély

A legtöbb esetben egy karakternek van egy (vagy több) fegyver típusa, amelyet előnyben részesít, gyakran forgat egy harcmodoron belül. A Mesterfegyver fortély segítségével egyes fegyverek harcértékeit tovább növelheti, így elszakadva kicsit tudásban a harcmodor többi fegyverétől. A Mesterfegyver fortélyt legfeljebb 3. fokon lehet felvenni az alábbi követelményekkel és jutalmakkal:

     
|Fok|Követelmény|KÉ|TÉ|VÉ|Sebzés|
|:---:|:---:|:---:|:---:|:---:|:---:|
|1|4. szint a harcmodorban|+2|+3|+3|+1|
|2|8. szint a harcmodorban|+4|+6|+6|+2|
|3|12. szint a harcmodorban|+6|+9|+9|+3|

Bizonyos manővereknek követelménye lehet ennek a fortélynak valamely foka, melyet csak az adott fegyverrel képes végrehajtani a forgatója. Például: „Első vágás”, „Mesterjel”

---

### 1.2.2 KÉ, TÉ, VÉ, CÉ

És most lássuk a bevezetőben már említett négy konkrét harcértéket.

#### Kezdeményező érték

A Kezdeményező Érték szerepe a harcban, hogy meghatározza, ki „mozdul először” a harcban. Nem jelent harci dominanciát, csak azt, hogy ki a gyorsabb, ki cselekedhet a előbb.

Kezdeményező dobás: minden kör elején `KÉ + k10`. A kezdeményezésről bővebben lásd a ⭕(link)„Harc menete” fejezetet⭕! 

A karakter Kezdeményező Értékét a következőképpen kell kiszámítani:

| 🗡️ | Kezdeményező Érték meghatározása  |
|:---:|---|
|Konstans|10 (minden karakternek)|
|2 x Gyorsaság|A karakter Gyorsaság Tulajdonságának kétszerese|
|Szint|A karakter szintje|
|Harcmodor KÉ|Harcmodor képzettség szintje által kapott bónusz (lásd a harcmodor képzettségeket!)|
|Mesterfegyver fortély|+2 fokonként|
|Speciális|- Gyors Kezdeményezés fortély: `+4 KÉ`<br>  - Szituációkból adódó módosítók<br>  - Mágia hatására kapott módosító|

---

#### Védő Érték

A Védő Érték szimbolizálja a karakter közelharcban nyújtott azon képességét, hogy mennyire hatásosan képes elhárítani, elkerülni az ellene intézett csapásokat. Értéke nem mondható konstansnak, hisz a harci helyzettől függően változik, ráadásul kihat rá a testi-lelki, szellemi fáradság és persze a sebesülés is (lásd később).

 
| 🗡️ | Védő Érték meghatározása |
|:---:|---|
|Konstans|120 (minden karakternek)|
|2 x Ügyesség|A karakter Ügyesség Tulajdonságának kétszerese|
|2 x Gyorsaság|A karakter Gyorsaság Tulajdonságának kétszerese|
|Harcmodor VÉ|Harcmodor képzettség szintje által kapott bónusz (lásd a harcmodor képzettségeket!)|
|Fegyver VÉ|A forgatott fegyver Védő Értéke|
|Mesterfegyver fortély|+3 fokonként|
|HM|A VÉ-re költött (KP-ból felvett) Harcérték módosító|
|Vértviselet – 3.fok|A nehézvért viselés mesterei (Vértviselet 3.fok) képesek a csapásokat páncélzatukról szándékoltan lecsúsztatni, sokszor hárítás helyett használva azt.  <br>Ezért félvért esetén +5VÉ, teljes vért esetén +10VÉ adódik Védő Értékükhöz|
|Pajzs VÉ|Értéke a pajzs jellegétől függ. Ha a karakter készületlen, vagy meglepetésből támadnak rá, a pajzs VÉ nem adódik hozzá a aktuális Védő Értékhez. Képzetlen Pajzshasználat esetén csak értékének fele számít be.|
|Speciális|- Harc során bekövetkező csökkenés (sima találat esetén)<br>    - Sebesülésből adódó csökkenés<br>    - Fortélyokból adódó módosítók<br>    - Harci helyzetből adódó módosítók (pl. harc alulról, harc megrendülten, stb)<br>   - Fegyver minőségéből adódó módosító<br>&nbsp;&nbsp;&nbsp;&nbsp; - Mestermunka: max +5 VÉ<br>&nbsp;&nbsp;&nbsp;&nbsp; - Gyatra fegyver: max -10 VÉ<br>&nbsp;&nbsp;&nbsp;&nbsp; - Mágikus fegyver módosítói<br>        - Mágiából adódó módosítók|

---

#### Támadó Érték

A Támadó Érték szimbolizálja a harcos azon tulajdonságát, hogy az adott fegyverrel milyen hatékonyan képes ellenfele ellen támadást, támadásokat intézni.

Az alábbi táblázat megadja, a Támadó Érték kiszámolásának módját.

 
| 🗡️ | Támadó Érték meghatározása |
|:---:|---|
|Konstans|20 (minden karakternek)|
|2 x Erő|A karakter Erő Tulajdonságának kétszerese|
|2 x Ügyesség|A karakter Ügyesség Tulajdonságának kétszerese|
|2 x Gyorsaság|A karakter Gyorsaság Tulajdonságának kétszerese|
|Harcmodor TÉ|Harcmodor képzettség szintje által kapott bónusz (lásd a harcmodor képzettségeket!)|
|Fegyver TÉ|A forgatott fegyver Támadó Értéke|
|Mesterfegyver fortély|+3 fokonként|
|HM|A VÉ-re költött (KP-ból felvett) Harcérték módosító|
|Plusz támadás levonása|Minden plusz támadás esetén -10 levonás jár a TÉ-re.  <br>(a 2.támadásra: -10TÉ, a 3.támadásra: -20TÉ, stb)|
|Speciális|- Fortélyokból adódó módosítók<br> - Harci helyzetből adódó módosítók<br> - Fegyver minőségéből adódó módosító<br>&nbsp;&nbsp;&nbsp;&nbsp; - Mestermunka: max +5 TÉ<br>&nbsp;&nbsp;&nbsp;&nbsp; - Gyatra fegyver: max -5 TÉ<br>&nbsp;&nbsp;&nbsp;&nbsp; - Mágikus fegyver módosítói<br> - Mágiából adódó módosítók|

(A távolsági fegyverekkel végrehajtott támadásokat külön fejezetben tárgyaljuk.)

Harcban, támadáskor a játékos dob `k100`-al, majd a kapott értéket hozzáadja aktuális **Támadó Értékéhez**. Ennek értéke lesz a **Támadó dobás**.
```
Támadó dobás = Támadó Érték + k100
```

Bővebben lásd a „Harc menete” fejezetben!

---

#### Célzó Érték

 
| 🗡️ | Célzó Érték kiszámítása |
|:---:|---|
|K100|Dobás K100-al – támadó dobás esetén.|
|-30|Konstans. Ez az érték gyakorlatilag a célpont Védő Érték alapját adná, de mivel itt csak 1x (karakteralkotáskor) kell vele számolni, ezért a számolás meggyorsítása miatt átkerült ide.|
|2 x Önuralom|Az Önuralom kétszerese|
|Harcmodor CÉ|Harcmodor képzettség szintje által kapott bónusz (lásd a harcmodor képzettségeket!)|
|Fegyver CÉ<br><br>(kategória függő)|Különbséget teszünk a fegyverkategóriák közt attól függően, hogy alapesetben milyen könnyű velük célba találni. Az alábbi értékek csak irányszámok, a konkrét fegyver értékek ettől eltérhetnek.<br><br>- Hajító szálfegyverek: +0 CÉ<br>    <br>- Apró hajítófegyverek: +4 CÉ<br>    <br>- Íjak: +10 CÉ<br>    <br>- Nyílpuskák: +16 CÉ  <br>    (A fentiek irányadó számok, egyes speciális fegyverek ezen értéke eltérhet ettől. Lásd a Távolsági fegyverek harcértékei fejezetet!)|
|Mesterfegyver fortély|+3 fokonként|
|CM|Célzóérték Módosító. Szintnként legfeljebb 4 vehető fel. 1 CM = 5KP|
|Célzás körönként|+10CÉ / kör amit célzással tölt el a támadó. Maximum 2 körig.  <br>+15CÉ / kör: Képzett Célzás fortély megléte esetén.<br><br>(Figyelem: íjnál csak 1 körig, alkalmazható mert nehéz kitartani!! 1 kör után körönként ugyanennyi levonás!)|
|Egyéb|- Képzetlenségből adódó levonás: -40 CÉ<br>    <br>- Hirtelen lövés: -30 CÉ  <br>    (Pl. a célpont hirtelen átfut az úton be egy másik takarás védelmébe és ez a lövészt felkészületlenül éri)<br>    <br>- Az egyes Fortélyokból adódó bónuszok.<br>    <br>- Nem “belőtt” lőfegyver: -30 CÉ (íjak) / -15 CÉ (nyílpuskák)  <br>    Ha a támadó most lő először a fegyverrel, akkor íjak esetében -30CÉ, nyílpuskák használatánál pedig -15 CÉ módosító sújtja. Ha legalább fél órát töltött el a “belövéssel”, ez a módosító megszűnik. Egyébiránt a használat során folyamatosan tűnik el a hátrány (negyed óra után már csak -15 CÉ / -8 CÉ és így tovább).<br>    <br>- A fegyverek minősége befolyásolhatja azok Célzó értéket.|

**Bővebben lásd a Távolsági Harc fejezetet!**

---

