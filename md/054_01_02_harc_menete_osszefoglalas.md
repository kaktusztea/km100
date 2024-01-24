
## A harc menete – összefoglalás

```
- KÉ = 10 + (2 x Gyorsaság) + Tapasztalati szint + Harcmodor/Mágia-Tradíció bónusza + Fegyver KÉ

- TÉ = 20 + 2 x (Erő + Ügyesség + Gyorsaság) + HM + Harcmodor bónusza + Fegyver TÉ

- VÉ = 120 + 2 x (Ügyesség + Gyorsaság) + Pajzs VÉ + HM + Harcmodor bónusza + Fegyver VÉ
Bónusz: Vértviselet – 3.szint : teljes vért SFÉ-je hozzáadható a VÉ-hez

- CÉ = -30 +(2 x Önuralom) – 30 (Konstans) + CM + Harcmodor bónusza + Fegyver CÉ
```

<br />

---
### Kezdeményezés

Minden kör elején van kezdeményezés, ami csak a cselekvési sorrend meghatározására szolgál, nem jelent dominanciát, vagy a harc irányítását.

KÉ dobás: `KÉ+k10` és a magasabb számot kapott kezd, `10`-es (`0`) dobásra rá lehet dobni újra

Azonos kezdeményezésnél: egyszerre csapnak

<br />

---
### Támadás

Támadó dobás: `TÉ + k100`; `1 kör = 5 szegmens`

Minden újabb támadás a körben `TÉ:-10`-vel megy,

Fegyvermérettől függően előnyös/hátrányos helyzetű támadó (`1` penge méretkülönbségtől).

| Támadó dobás eredménye | Hatás                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:----------------------:| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|        TÉ < VÉ         | VÉ csökkentés<br>- Alaphelyzetben (nincs előnyös-hátrányos helyzet):  <br>    mindkét fél kiskockával csökkent (`k100`) <br>- Legalább `1` penge fegyverméret különbségnél:<br>    <br>- Előnyös helyzetű támadó: (`kiskocka+1`)-el csökkent (`k100`)<br>    <br>- Hátrányos helyzetű támadó: (`kiskocka-1`)-el csökkent (`k100`)<br>    <br>- `2` penge, vagy nagyobb méretkülönbségnél:<br>    <br>- Előnyös helyzetű támadó: (`kiskocka+2`)-vel csökkent (`k100`)<br>    <br>- Hátrányos helyzetű támadó: (`kiskocka-1`)-el csökkent (k100)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|        TÉ >= VÉ        | Túlütés → ÉP sebzés* (fegyver); Erőbónusz, fegyver mágia bónusz hozzáadódik<br><br>- Többszörös túlütés: `+20`-anként `SP:+3` (max `+9 SP`)<br>    <br>- VÉ csökkentés: ÉP seb függő (lásd [Sebzés táblázat](054_01_02_harc_menete_reszletes.md#sebz%C3%A9s))<br>    <br>- Támadás jellege: a fegyver elsődleges támadási típusa az alapértelmezett. Másodlagos támadási formával `TÉ:-10` módosítóval lehet támadni<br>    <br>- Páncéldobás: áldozat dobja `k10`-el. Tulajdonképpen százalékdobás, hogy páncéllal fedett területet találtak-e el. Minden páncél X %-ban védi a testet. Pl. torzót védő: `50%` (`1-5`: véd)<br>    <br>- Áldozat SFÉ: támadás jellegétől függő SFÉ. (Támadó fegyver Átütése levonódik belőle!)<br>    <br>- `SP = k20 + fegyver SP – akt.SFÉ`<br>    <br>- ÉP seb: SP↔ÉP megfeleltetés a Sebzés táblázatban<br>    <br>- `00`-ás dobás (100): `+5 SP` ; ellenfél SFÉ nem számít (de az Aranyharang és Elemi Erő igen!)  <br>    Fárasztás alkalmazásakor: `+5` VÉ csökk.<br>    <br>- `01`-es dobás: kudarc (KM dönt, általában az ellenfél kap `1` plusz támadást) |

**Megjegyzés**: a "Harci anatómia" ÉP bónusza csak akkor adható hozzá, ha az alap sebzés átment a páncélon!


- **VÉ regenerálódás:** `1` kör pihenéssel töltött idővel visszatérnek a harcban - **nem sérüléssel** - elvesztett VÉ-k.
- **Támadások száma**: `1` + plusz támadások
- **Plusz támadások (db)** = (Harcmodor-Sebesség) / (Fegyver-Sebesség)
  - **Harcmodor-Sebesség** = aktuális harcmodor + Gyorsaság tulajdonság
  - **Fegyver-Sebesség** : fegyverenként eltérő egyéni érték (lásd a [Fegyverek táblázatot](057_fegyverek.md)!)
- **Győzelmi szabály**: Ha a karakter végzett egy ellenfelével (úgy hiszi, legyőzte), akkor Védő Értékéhez visszatér `+10` pont. (a siker hatása a szervezetre + heroizmus). Persze itt is lehetnek kivételek (barát megölése, stb).

<br />

---
### Statikus SP módosítók
(Karakteralkotáskor, vagy szintlépéskor számolandók)

| Módosító                  | Érték              |
| ------------------------- | ------------------ |
| Mesterfegyver fortély     | +1 minden fok után |
| Jó/rossz minőségű fegyver | ???                |
| Mágikus fegyver           | ???                |


| Erőbónusz és Erőhiány                                                   |
| ----------------------------------------------------------------------- |
| Az Erő tulajdonság +2 feletti része 1:1-ben hozzáadódik az SP értékhez. |

<br />

---
### Dinamikus SP módosítók
(Ezek a módosítók harc közben szituációtól függően adódhatnak hozzá az SP értékhez)

| Módosító                            | Érték                                                           |
| ----------------------------------- | --------------------------------------------------------------- |
| Többszörös túlütés  <br>(20-anként) | `+3 SP`  (max `+9 SP`)                                          |
| Roham                               | `+5 SP`                                                         |
| 00-ás dobás                         | `+5 SP`, SFÉ nem számít  <br>Fárasztáskor: még `+5` VÉ csökk.** |

<br />

---
### Mozgásgátló Tényező (MGT)


```
- 1 MGT  → -0,5 KÉ, -1 TÉ,VÉ
- 1 MGT  → -1/5 mozgást igénylő képzettségpróbákra és tulajdonságpróbákra
  (lefele kerekítve)
```

KM dönt, de például kézügyességet érintő **Ügyességpróbára** nyilván nem jár levonás, ha nincs páncélkesztyűben a játékos.

<br />

---

### Csataszabályok

Nagy tömegjelenetben a sok statisztika kezelése drasztikusan lelassíthatja a játékot. Ilyenkor a következő – opcionális – szabályt javasoljuk:

```
- +20 TÉ mindenkinek
- Nincs VÉ csökkentés
- Nincs páncéldobás
- TÉ/VÉ értékeket kerekítjük 10-el oszthatóan (1-5: lefelé, 6-9: felfelé)
- Támadó dobás eredményét is kerekítjük ugyanígy
- Erősített sebzés: 1-10: 6ÉP; 11-20: 12ÉP; 21-30: 20ÉP; 31-től halál
```
