## Távolsági fegyverek

### Távolsági fegyver kategóriák, Fegyverek Célzó Értéke

A távolsági fegyverek több kategóriába sorolhatóak attól függően, hogy általánosságban mennyire könnyű kezelni őket, mennyire alkalmasak messzi célok leküzdésére. Ezek szerint az alábbi módosítók járulnak ****minden**** karakter Célzó Értékéhez, aki a felsorolt fegyverek valamelyikét kezébe veszi. A lentiek csak irányadó számok a konkrét fegyverek Célzó Értéke és egyedi jellemzőik eltérhetnek ezen értékektől, de nagyjából ebben a skálán mozognak.

|            Fegyverkategória            |  CÉ   | Fegyverek                                              | Speciális                                                                                                                             |
|:--------------------------------------:|:-----:| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Hajító szálfegyverek,<br>Egyéb tárgyak | `+0`  | Kard, zsámoly, korsó, hajításra nem alkalmas fegyverek | Maximális Hatótávjukhoz hozzáadható:  <br>(ERŐ x Osztó)                                                                               |
|          Apró hajítófegyverek          | `+4`  | Tőr, dobótőr, hajítóbárd, dárda, lándzsa, kő           | -                                                                                                                                     |
|                  Íjak                  | `+10` | Íjak                                                   | Sebzés bónusz: ERŐ Tulajdonság 1:1<br>(**ha** erre az Erőre lett tervezve)                                                            |
|               Nyílpuskák               | `+16` | Nyílpuskák                                             | A kézi nyílpuskától felfelé **Páncéltörőnek** számítanak:<br>SFÉ = a vért rétegeinek száma<br>(mágikus vértek esetén a KM szava dönt) |

🔆 **Megjegyzés**: Amennyiben valaki hajításra nem alkalmas fegyvert akar dobni, akkor az adott fegyver harcmodorában kismesteri, azaz `6`.szinten jártasnak kell lennie. Ez alatt képzetlen fegyverhasználat büntetéseivel történhet a dobás.

- [Hajítófegyverek táblázata](067_fegyverek.md#hajítófegyverek-harcértékei)
- [Lőfegyverek táblázata](067_fegyverek.md#lőfegyverek-harcértékei)

<br />

---
### Sebzés bónusz hiánya

Távolsági fegyverek esetén NINCS **Többszörös találatból** adódó plusz sebzés.

<br />

---
### Támadások száma (Íjászat, Hajítás)
```
Sebesség = aktuális harcmodor + Gyorsaság Tulajdonság
```

Az íjász/hajigász támadásainak száma attól függ, hogy milyen képzett az adott fegyver használatában, vagy annak Harcmodorában, illetve fürge. Ezt a kapcsolódó harci képzettség foka és a Gyorsaság tulajdonság határozzák meg a fentiek szerint.

Kézifegyvereknél az alábbi módon kategorizálunk:

```
(5) rövid fegyverek            → 5 Sebesség pontonként nő 1-el a támadások száma
(6) egykezes és szálfegyverek  → 6 Sebesség pontonként nő 1-el a támadások száma
(7) kétkezes fegyverek         → 7 Sebesség pontonként nő 1-el a támadások száma
```

Távolsági fegyverek esetén viszont nem mindegyiknek van **Sebesség** kategóriája, mivel újratöltésük annyi időt vesz igénybe, hogy nem lehetséges velük egy körben többször támadni (pl. nyílpuskák).

Ebben az esetben lehet hasznos a [Gyors újratöltés](fortelyok.harci/gyors_ujratoltes.md) harci fortély.

Az egyes fegyverek Sebesség kategóriáját lásd a **Harcrendszer** [Fegyverek](067_fegyverek.md) alfejezetében (táblázat)!

<br />

---
### Erőből / Ügyességből forgatott fegyverek

Távolba ható fegyverek esetén különbséget teszünk **Erőből** és **Ügyességből** használtak között. A fenti tulajdonság szerepe a sebzésbónusz és a végső Célzó Érték kiszámításánál mutatkozik meg. Hogy egy fegyvert Erőből, vagy Ügyességből forgathatunk, azt a [Távolsági fegyverek fejezet](067_fegyverek.md#hajítófegyverek-harcértékei) alatt található táblázatból olvashatjuk ki.

<br />

---
### Hatótáv

Minden távolba ható fegyvernek van **Hatótávja**, amely értelemszerűen az adott fegyverrel elérhető legnagyobb lőtávolságot jelenti. Ezt minden fegyvernél számon tarjuk, értékét méterben jelezzük. A játékos nem lőhet/dobhat a fegyver hatótávján túl (illetve hajítás esetén még szerepet játszhat a támadó Ereje, de erről később).

⚡Példa: a Könnyű nyílpuska **Hatótávja** `50`, tehát maximálisan `50` méterre lehet vele ellőni.

<br />

---
### Távolsági fegyverek minősége

Nem minden fegyver egyformán jó minőségű, valamelyik igazi mestermunka, pontos, megbízható, mások pedig olyan hitványul vannak összeeszkábálva, hogy még egy öt méterre álló gólemet se talál el vele az ember.

A távolsági fegyverek minősége azok **CÉ**-jét javítja, vagy éppen rontja. Például egy átlagos könnyű nyílpuska `16`-es **CÉ**-vel bír. Egy kiváló nyílpuska, amely mestermunka, akár `20-25`-öt is elérhet, ugyanakkor egy ócskavasnál nem lehet meglepő az `8`-as érték. Szélsőséges esetben a fegyver **Osztó** értéke is módosulhat, de ökölszabályként kimondható, hogy az **Osztó** – minőségtől függően - **legfeljebb** `±1`-el változhat az alapértékhez képest, továbbá csak lőfegyverekre vonatkozik, hajítófegyverekre nem. Egy hajítófegyvernél legfeljebb akkor elképzelhető a **Osztó** változása, ha annyira rossz minőségű, hogy átkerül az `2`-esből a `1`-es kategóriába. Pozitív irányba nem módosulhat.