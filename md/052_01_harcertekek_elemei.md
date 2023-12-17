
Mikor két teremtmény fegyvert ragad és ütésekkel, szúrásokkal, vágásokkal, karmolással, harapással próbálják legyőzni egymást, akkor bizony **Fegyveres harcról** beszélünk.

---
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

Első szinten minden karakter egységes konstans értékeket kap KÉ, TÉ, VÉ és CÉ értékére.

Értékeik :

```
KÉ konstans: 10
TÉ konstans: 20
VÉ konstans: 120
CÉ konstans: -30
```  

Ehhez az alapértékhez adódnak majd hozzá az egyéb módosítók.

### Harci Tulajdonságok

Egyes Tulajdonságok értékei beleszámítanak a harcértékekbe. Hogy melyek azt az adott harcérték leírásánál találhatjuk a KÉ, TÉ, VÉ, CÉ fejezetben. ⭕(link)⭕


---
### Harcérték Módosító (HM)

Ahogy fejlődik, megjár sok harci helyzetet, a karakter általános harcértékei fejlődnek. Ezt szimbolizálja a Harcérték módosító, melyet a játékos vehet fel karaktere szintlépésének alkalmával.

Minden karakter szintenként **maximum** **(6+Ügyesség)** pontnyi úgynevezett HM-et és **maximum 4** ún. Célzóérték Módosítót (**CM)** vehet fel (nem kötelező!) Karakter Pontjaiból. Egy HM-re, illetve CM-re **4** Karakter Pontot kell költenie.

```
Maximum: 8 HM / Szint
Maximum: 4 CM / Szint
1 HM = 5 KP
1 CM = 5 KP
```

A sima `HM` a `KÉ`, `TÉ`, és `VÉ` harcértékek növelésére szolgál, a `CM` (Célzó Érték Módosító) pedig a távolsági fegyverek használatára vonatkozik. Nem keverhetők, tehát a CM-re költhető max `4 HM` nem „pakolható át” a sima `HM`-re és viszont!

#### HM korlát

Szintenként `TÉ`-re vagy `VÉ`-re **legfeljebb** `3`-al több `HM`-et lehet költeni, mint a másikra!


---
### Harcmodor képzettségek

A km100 rendszere az alábbi (átfogó) harci képzettségeket ismeri:

**Közelharc, Kardvívás, Lándzsavívás, Pusztítás, Hajítás, Íjászat, Lövészet, Ostromlövészet**

- **Közelharc: közelharci** **(legfeljebb 0,5 penge hosszú)** **fegyverek**
- **Kardvívás: minden „pengés” fegyver (kétkezes kard is)**
- **Pusztítás: zúzófegyverek, csatabárdok, csákány**
- **Lándzsavívás: Szálfegyverek**
    

A harci képzettségek aktuális szintjétől függ, hogy az alá tartozó fegyvereket milyen általános harcérték pluszokkal forgathatja a karakter.  
**Megjegyzés**: Az egyes fegyverek további erősítése a Mesterfegyver fortéllyal lehetséges.

</br>

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
#### Harcmodorok és Manőverek

A Manőverek alkalmazását, leírását részletesen lásd a „[Manőverek](./055_05_manoverek.md)” fejezetben.

Harc közben gyakran előfordul, hogy egy karakter speciális húzásokkal próbálkozik, egyedi cseleket vet be, hogy megkönnyítse győzelmét, például kirúgja ellenfele lábát, vagy homokot szór annak szemébe. Sokszor van olyan is, hogy egy karakter különösen jó egy adott csel alkalmazásában és azt előszeretettel veti be. Ezek a manőverek.

Vannak olyan manőverek is, melyek csak adott fegyverre, vagy harcmodorra jellemzőek, de a legtöbb szabadon, bárki által alkalmazható, amennyiben teljesíti a végrehajtás követelményeit. Vannak olyan manőverek, amelyek külön fejleszthetőek is. Ez az adott manőver leírásánál szerepel. Az ilyen ismeretet Manőver-ismeretnek nevezzük és pontokba kerülnek. Lásd alább.

#### Manőverek tanulása

A Manőver-ismeretek tanulása szorosan összekapcsolódik a Harcmodor-képzettségekkel.

Minden nem-távolsági Harcmodor harmadik (**3.**) képzettség szintje 1 db ún. Manőverfejlesztő Pontot (**MFP**) ad. Az egyes manőver ismeretek tanulása ezekből a pontokból történik. Fontos, hogy a manővereknek csak egy része fejleszthető – kizárólag ezekre lehetséges MFP-t költeni. Az tanulható manőverek különböző mértékben fejleszthetők. Különböző fokon lehet felvenni őket – melyeknek természetesen követelményük is van.

Ha ezeken felül is manővert akar tanulni, akkor fokonként +10KP-t kell költenie.

---
### Mesterfegyver fortély

A legtöbb esetben egy karakternek van egy (vagy több) fegyver típusa, amelyet előnyben részesít, gyakran forgat egy harcmodoron belül. A Mesterfegyver fortély segítségével egyes fegyverek harcértékeit tovább növelheti, így elszakadva kicsit tudásban a harcmodor többi fegyverétől. A Mesterfegyver fortélyt legfeljebb 3. fokon lehet felvenni az alábbi követelményekkel és jutalmakkal:

     
|Fok|Követelmény|KÉ|TÉ|VÉ|Sebzés|
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1.fok    | 4.szint a harcmodorban  | `KÉ:+2`, `TÉ:+3`, `VÉ:+3`, `SP:+1`     |
| 2.fok    | 8.szint a harcmodorban  | `KÉ:+4`, `TÉ:+6`, `VÉ:+6`, `SP:+2`     |
| 3.fok    | 12.szint a harcmodorban | `KÉ:+6`, `TÉ:+9`, `VÉ:+9`, `SP:+3`     |

Bizonyos manővereknek követelménye lehet ennek a fortélynak valamely foka, melyet csak az adott fegyverrel képes végrehajtani a forgatója. Például: „Első vágás”, „Mesterjel”
