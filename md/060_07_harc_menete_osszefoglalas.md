
## A harc menete – összefoglalás

### Harcértékek
```
KÉ = 10
   + (Gyorsaság + Intelligencia)
   + Tapasztalati szint
   + Harcmodor/Mágia-Tradíció bónusz
   + Mf bónusz
   + Fegyver KÉ

TÉ = 20
   + 2 x (Erő + Ügyesség + Gyorsaság)
   + TÉ HM
   + Harcmodor/Mágia-Tradíció bónusz
   + Mf bónusz
   + Fegyver TÉ

VÉ = 120
   + 2 x (Ügyesség + Gyorsaság)
   + VÉ HM
   + Harcmodor/Mágia-Tradíció bónusz
   + Mf bónusz
   + Fegyver VÉ
   + Pajzs VÉ

VÉ Bónusz:
  → Vértviselet 3.szint:
    - félvért +5VÉ
    - teljes vért +10VÉ

CÉ = -30
   + (2 x Önuralom)
   – 30 (Konstans)
   + CM
   + Harcmodor/Mágia-Tradíció bónusz
   + Fegyver CÉ
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
```

```
Minden újabb támadás a körben:
   TÉ:-10; -20, ...

Támadás jellege: elsődleges támadási
        típusa az alapértelmezett
        (például: Szúró).
        Másodlagos támadási formával
        TÉ:-10 módosítóval támadhatsz

Előnyös/hátrányos helyzetű harcos:
   1 penge méretkülönbségtől

01 támadó dobás: kudarc, KM dönt.
   Pl. az ellenfél kap +1 támadást
```

<br />

---
### 😵TÉ < VÉ  → VÉ csökkentés

Alaphelyzetben: nincs előnyös-hátrányos helyzet
```
Mindkét fél nagykockával csökkent (k100),

Példa: 58  → 8
```

`1` penge, vagy nagyobb fegyverméret különbségnél:

```
Előnyös helyzetű támadó:
  nagykocka értékével csökkent (k100)
  Példa: 58  → 8

Hátrányos helyzetű támadó:
  kiskocka` értékével csökkent (k100)
  Példa: 58  → 5
```

`2` penge, vagy nagyobb fegyverméret különbségnél:

```
Előnyös helyzetű támadó:
  nagykocka+1 értékével csökkent (k100)
  Példa: 58  → 9

Hátrányos helyzetű támadó:
  kiskocka értékével csökkent (k100)
  Példa: 58  → 5
```

<br />

---
### 🗡️Fegyver

```
Fegyver SP: k20 + X

X: fegyver alap sebzése
```

```
- Erő Tulajdonság 1:1-ben hozzáadódik
  (vagy levonódik, ha negatív).
- Mesterfegyver fortély: +1 SP / fok
- Fegyver mágia bónusz hozzáadódik
```

```
- Többszörös találat (TÉ > VÉ+20):
      20-anként SP:+3   (max +9 SP)
- 00 támadó dobás: SP:+5
      Ellenfél SFÉ nem számít
      (de Aranyharang, Elemi Erő igen)
- Roham: SP:+5
- Támadás erőből fortély bónusza
```

<br />

---
### 💥TÉ >= VÉ  → Találat, Sebzés

```
Páncéldobás: áldozat dob k10    
   → nincs SFÉ
   → van SFÉ (szúró, vágó, zúzó)
     Fegyver Átütés csökkenti!
```

```
SP = Fegyver SP
   + módosítók
   + bónuszok
   – aktuális SFÉ
```

```
ÉP seb:
  - SP ↔ ÉP átváltás Sebzés táblázatban

VÉ csökkentés:
  - SP ↔ VÉ átváltás Sebzés táblázatban
  - Fárasztás alkalmazásakor:
    nincs Sebzés, VÉ:+5 csökkentés
```

Lásd: [Sebzés táblázat](060_08_harc_menete_reszletes.md#sebz%C3%A9s)

**Megjegyzés**: a "Harci anatómia" ÉP bónusza csak akkor adható hozzá, ha az alap sebzés átment a páncélon! ⭕TODO⭕

<br />

---
### 🍎VÉ regenerálódás
```
1 kör pihenéssel töltött idő:
    visszatér a harcban
    (nem sebtől) elvesztett VÉ
```

Teljes, fenyegetetlen nyugalom szükséges!

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
1 + Plusz támadások

Plusz támadások (db) =
  Harckeret / (Fegyver-Sebesség)
```

```
Harckeret =
  aktuális harcmodor + Gyorsaság

Fegyver-Sebesség:
  fegyverenként eltérő egyéni érték 
```

Lásd: [Fegyverek táblázat](060_16_fegyverek.md)

<br />

---
### 🛡️Mozgásgátló Tényező (MGT)

Lásd a [Vértek, Páncélok - MGT fejezetét](060_17_vertek_pancelok.md#mozg%C3%A1sg%C3%A1tl%C3%B3-t%C3%A9nyez%C5%91-mgt).

<br />

---
### 📖Csataszabályok

Nagy tömegjelenetben a sok statisztika kezelése drasztikusan lelassíthatja a játékot. Ilyenkor a következő – opcionális – szabályt javasoljuk:

```
- TÉ:+20 mindenkinek
- Nincs VÉ csökkentés
- Nincs páncéldobás
- TÉ/VÉ: kerekítjük 10-el oszthatóan
  (1-5: lefelé, 6-9: felfelé)
- Támadó dobást is kerekítjük
- Erősített sebzés:
  1-10: 6ÉP
  11-20: 12ÉP
  21-30: 20ÉP
  31-től halál
```
