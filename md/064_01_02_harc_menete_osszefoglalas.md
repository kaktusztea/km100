
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
### Kezdeményezés

```
Kezdeményező dobás: KÉ + k10
```

Minden kör elején van kezdeményezés, ami csak a cselekvési sorrend meghatározására szolgál, nem jelent dominanciát, vagy a harc irányítását.

KÉ dobás: `KÉ+k10` és a magasabb számot kapott kezd, `10`-es (`0`) dobásra rá lehet dobni újra.

Azonos kezdeményezésnél: egyszerre csapnak.

<br />

---
### Támadás

```
Támadó dobás: TÉ + k100
```

Minden újabb támadás a körben `TÉ:-10`-vel megy.

Fegyvermérettől függően előnyös/hátrányos helyzetű támadó (`1` penge méretkülönbségtől).

<br />

### 😵TÉ < VÉ  → VÉ csökkentés

Alaphelyzetben (nincs előnyös-hátrányos helyzet):  mindkét fél kiskockával csökkent (`k100`)

Legalább `1` penge fegyverméret különbségnél:
  - Előnyös helyzetű támadó: (`kiskocka+1`)-el csökkent (`k100`)
  - Hátrányos helyzetű támadó: (`kiskocka-1`)-el csökkent (`k100`)

`2` penge, vagy nagyobb méretkülönbségnél:
  - Előnyös helyzetű támadó: (`kiskocka+2`)-vel csökkent (`k100`)
  - Hátrányos helyzetű támadó: (`kiskocka-1`)-el csökkent (`k100`)

<br />

### 💥TÉ >= VÉ  → Találat

Találatkor ÉP sebzés történik.

1. Fegyver SP: Erőbónusz, fegyver mágia bónusz hozzáadódik
2. Többszörös találat: `+20`-anként `SP:+3` (max `+9 SP`)
3. Támadás jellege: a fegyver elsődleges támadási típusa az alapértelmezett. Másodlagos támadási formával `TÉ:-10` módosítóval lehet támadni
4. Páncéldobás: áldozat dobja `k10`-el. Tulajdonképpen százalékdobás, hogy páncéllal fedett területet találtak-e el. Minden páncél X %-ban védi a testet. Pl. torzót védő: `50%` (`1-5`: véd)
5. Áldozat SFÉ: támadás jellegétől függő SFÉ (Támadó fegyver Átütése levonódik belőle!)

```
 SP = k20 + fegyver SP + bónuszok – aktuális SFÉ
```

6. ÉP seb: `SP ↔ ÉP` megfeleltetés a Sebzés táblázatban
  - `00`-ás dobás (100): `+5 SP` ; ellenfél SFÉ nem számít (de az Aranyharang és Elemi Erő igen!)
  - `01`-es dobás: kudarc (KM dönt, általában az ellenfél kap `1` plusz támadást)
7. VÉ csökkentés: ÉP seb függő (lásd [Sebzés táblázat](064_01_02_harc_menete_reszletes.md#sebz%C3%A9s)), Fárasztás alkalmazásakor: `+5` VÉ csökk.

**Megjegyzés**: a "Harci anatómia" ÉP bónusza csak akkor adható hozzá, ha az alap sebzés átment a páncélon!

<br />

### 🍎VÉ regenerálódás

`1` kör pihenéssel töltött idővel visszatérnek a harcban - **nem sérüléssel** - elvesztett VÉ-k.

**Győzelmi szabály**: Ha a karakter végzett egy ellenfelével (úgy hiszi, legyőzte), akkor Védő Értékéhez visszatér `+10` pont. (a siker hatása a szervezetre + heroizmus). Persze itt is lehetnek kivételek (barát megölése, stb).

### Támadások száma

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
### Statikus SP módosítók

Karakteralkotáskor, vagy szintlépéskor számolandók.

```
Mesterfegyver fortély:  +1 SP  minden fok után
```

```
Erőbónusz és Erőhiány:
 Az Erő tulajdonság 1:1-ben hozzáadódik az SP értékhez
 (vagy levonódik, ha negatív).
```

<br />

---
### Dinamikus SP módosítók

(Ezek a módosítók harc közben szituációtól függően adódhatnak hozzá az SP értékhez)

| Módosító                              | Érték                                                             |
| ------------------------------------- | ----------------------------------------------------------------- |
| Többszörös találat  <br>(`20`-anként) | `+3 SP`  (max `+9 SP`)                                            |
| Roham                                 | `+5 SP`                                                           |
| `00`-ás dobás                         | `+5 SP`, SFÉ nem számít  <br>Fárasztáskor: még `+5` VÉ csökkentés |

<br />

---
### Mozgásgátló Tényező (MGT)

Lásd a [Vértek, Páncélok - MGT fejezetét](068_vertek_pancelok.md#mozgásgátló-tényező-mgt).

<br />

---
### Csataszabályok

Nagy tömegjelenetben a sok statisztika kezelése drasztikusan lelassíthatja a játékot. Ilyenkor a következő – opcionális – szabályt javasoljuk:

```
- TÉ:+20 mindenkinek
- Nincs VÉ csökkentés
- Nincs páncéldobás
- TÉ/VÉ értékeket kerekítjük 10-el oszthatóan (1-5: lefelé, 6-9: felfelé)
- Támadó dobás eredményét is kerekítjük ugyanígy
- Erősített sebzés: 1-10: 6ÉP; 11-20: 12ÉP; 21-30: 20ÉP; 31-től halál
```
