
## A harc menete – összefoglalás

```
- KÉ = 10 + (Gyorsaság + Intelligencia) + Tapasztalati szint + Harcmodor/Mágia-Tradíció bónusza + Mf bónusz + Fegyver KÉ

- TÉ = 20 + 2 x (Erő + Ügyesség + Gyorsaság) + HM + Harcmodor bónusza + Mf bónusz + Fegyver TÉ

- VÉ = 120 + 2 x (Ügyesség + Gyorsaság) + Pajzs VÉ + HM + Harcmodor bónusza + Mf bónusz + Fegyver VÉ
Bónusz: Vértviselet – 3.szint: félvért +5VÉ, teljes vért +10VÉ

- CÉ = -30 +(2 x Önuralom) – 30 (Konstans) + CM + Harcmodor bónusza + Fegyver CÉ
```

<br />

---
### 🤞Kezdeményezés

```
Kezdeményező dobás: KÉ + k10
```

Minden kör elején van kezdeményezés, ami csak a cselekvési sorrend meghatározására szolgál, nem jelent dominanciát, vagy a harc irányítását.

A magasabb számot kapott kezd, `10`-es (`0`) dobásra rá lehet dobni újra.

Azonos kezdeményezésnél: egyszerre csapnak.

<br />

---
### 🤺Támadás

```
Támadó dobás: TÉ + k100

Minden újabb támadás a körben: TÉ:-10; -20, ...

Támadás jellege: a fegyver elsődleges támadási típusa az alapértelmezett (például: Szúró).
                 Másodlagos támadási formával `TÉ:-10` módosítóval lehet támadni

Előnyös/hátrányos helyzetű harcos: 1 penge méretkülönbségtől

01 támadó dobás: kudarc, KM dönt. Általában az ellenfél kap `1` plusz támadást.
```

<br />

---
### 😵TÉ < VÉ  → VÉ csökkentés

```
Alaphelyzetben:  mindkét fél nagykockával csökkent (k100)           -   58  → 8
(nincs előnyös-hátrányos helyzet)
```

Legalább `1` penge fegyverméret különbségnél:

```
- Előnyös helyzetű támadó:  `nagykocka` értékével csökkent (k100)   -   58  → 8
- Hátrányos helyzetű támadó: `kiskocka` értékével csökkent (k100)   -   58  → 5
```

`2` penge, vagy nagyobb méretkülönbségnél:

```
- Előnyös helyzetű támadó: `nagykocka+1` értékével csökkent (k100)  -   58  → 9
- Hátrányos helyzetű támadó:  `kiskocka` értékével csökkent (k100)  -   58  → 5
```

<br />

---
### 🗡️Fegyver

```
Fegyver SP: k20 + X
  - Erő Tulajdonság 1:1-ben hozzáadódik (vagy levonódik, ha negatív).
  - Mesterfegyver fortély: +1 SP minden fok után
  - Fegyver mágia bónusz hozzáadódik
  + többszörös találat (TÉ > VÉ+20):
         20-anként SP:+3   (max +9 SP)

- 00 támadó dobás: SP:+5;    Ellenfél SFÉ nem számít (de Aranyharang, Elemi Erő igen)
- Roham: SP:+5
```

<br />

---
### 💥TÉ >= VÉ  → Találat, Sebzés

```
Páncéldobás: áldozat dob k10    
   → nincs SFÉ
   → van SFÉ (szúró, vágó, zúzó)  - Fegyver Átütés csökkenti!

SP = Fegyver SP + bónuszok + módosítók  – aktuális SFÉ

ÉP seb:         SP ↔ ÉP megfeleltetés a Sebzés táblázatban
VÉ csökkentés:  SP ↔ VÉ megfeleltetés a Sebzés táblázatban
   - Fárasztás alkalmazásakor: nincs Sebzés, VÉ:+5 csökkentés
```

Lásd: [Sebzés táblázat](064_01_02_harc_menete_reszletes.md#sebz%C3%A9s)

**Megjegyzés**: a "Harci anatómia" ÉP bónusza csak akkor adható hozzá, ha az alap sebzés átment a páncélon! ⭕TODO⭕

<br />

---
### 🍎VÉ regenerálódás
```
1 kör pihenéssel töltött idő:
      visszatérnek a harcban - nem sérüléssel - elvesztett VÉ pontok
```


#### Győzelmi szabály

```
VÉ: +10
```

Ha a karakter végzett egy - hozzá hasonló tudású, vagy erősebb - ellenfelével (úgy hiszi, legyőzte), akkor **Védő Értékéhez** visszatér `+10` pont.\
Ez a siker hatása a szervezetre + heroizmus. Persze itt is lehetnek kivételek (barát megölése, stb).

<br />

---
### 🔢Támadások száma

```
1 + plusz támadások

Plusz támadások (db)  =  Harckeret / (Fegyver-Sebesség)
```

```
Harckeret  =  aktuális harcmodor + Gyorsaság tulajdonság

Fegyver-Sebesség: fegyverenként eltérő egyéni érték 
```

Lásd: [Fegyverek táblázat](067_fegyverek.md)

<br />

---
### 🛡️Mozgásgátló Tényező (MGT)

Lásd a [Vértek, Páncélok - MGT fejezetét](068_vertek_pancelok.md#mozgásgátló-tényező-mgt).

<br />

---
### 📖Csataszabályok

Nagy tömegjelenetben a sok statisztika kezelése drasztikusan lelassíthatja a játékot. Ilyenkor a következő – opcionális – szabályt javasoljuk:

```
- TÉ:+20 mindenkinek
- Nincs VÉ csökkentés
- Nincs páncéldobás
- TÉ/VÉ értékeket kerekítjük 10-el oszthatóan (1-5: lefelé, 6-9: felfelé)
- Támadó dobás eredményét is kerekítjük ugyanígy
- Erősített sebzés: 1-10: 6ÉP; 11-20: 12ÉP; 21-30: 20ÉP; 31-től halál
```
