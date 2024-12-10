## 🔵 Mászás

⭕**TODO**⭕

````diff
Menet felfelé:
- Edzettségpróba kell, de ha sokat dobatunk, az exponenciálisan csökkenti az esélyt!
- Ezért legyen szerintem Összetett Edzettségpróba (lásd Összetett tulajdonságpróba) a mászás elején.
- Menet közben Edzettségpróbák
  - Milyen gyakran és milyen nehézség ellen?
- Rontott Edzettségpróba esetén: Újra Mászás képzettségpróba. Az eredeti nehézség + Edzettségpróba rontás különbség ellen.
- Mekkora nehézségű legyen az Edzettségpróba?
- Rontott mászás képzettségpróba:
  - Soron kívüli azonnali Edzettségpróba. Nehézsége: ⭕????⭕
````

**Próba**: dobható

**Domináns Tulajdonságok**: Ügyesség (a mászáshoz), Önuralom (rontott próbánál), Erő (erőtartalék kritikus helyzetben), Edzettség (rontáskor kitartani), Intelligencia (felmérni a mászandó terepet, helyeket)

### Kapcsolódik

- [Biztos kezű mászó](../fortelyok.altalanos/biztos_kezu_maszo.md) fortély
- [Pók](../fortelyok.altalanos/pok.md) fortély

### Leírás

Sokszor fordul elő, hogy fel kell jutni olyan helyekre, ahova egy átlagember nem képes. Ebben segít a Mászás képzettség. Magas szintű alkalmazói jellemzően egyes tolvaj- és fejvadászklánok elit tagjai.

### Szituációk

- [Mászás képzettségpróbára összetett példa](../szituaciok/maszas_osszetett_pelda.md)

<br />

### Biztos tudás, követelmények

Ha a terep (próba) nehézsége nem nagyobb a a Mászás képzettségnél, akkor azon a terepen a mászó bárhol képes megállva kipihenni magát.

| Képzettség szint | Biztos tudás, Speciális <br /><sub>(tanulható fortély, különleges  képesség)</sub>                                                                                                                                                                                                                                                            |                                       Követelmény                                        |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------: |
| Novícius (3)     | Tudja melyik fa bírja el a súlyát és melyik nem.<br />**Példa**: Erdőszerető gyerek, aki felmászik minden fára.                                                                                                                                                                                                                               |                                Erő:`-1`<br />Ügyesség:`0`                                |
| Kismester (6)    | • Ismeri az alapvető mászási technikákat, pár hasznos csomót.<br />• **Példa**: Gyakorlott mászó, rendszeres kiránduló<br />Tanulható:  [Pók](../fortelyok.altalanos/pok.md) fortély                                                                                                                                                          |                               Erő:`-1`<br />Ügyesség:`+1`                                |
| Mester (9)       | • Ismeri az összes mászási technikát és faltípust, mászáshoz szükséges csomókat. Jó látási viszonyok közt ránézésre nagyjából meg tudja mondani, mennyire omladékos a terep. Tudja milyen testhelyzetben pihenjen kapaszkodás közben.<br />• **Példa**: Képzett hegymászó, profi besurranó tolvaj                                             |                      Erő:`-2`<br />Ügyesség:`+2`<br />Önuralom:`+1`                      |
| Nagymester (12)  | • A fentieken kívül képes úgy tartalékolni az erejét, hogy hosszabb távon se fárad ki. Akár ⭕fél óráig⭕ is tartja magát puszta kézzel.<br />• **Példa**: Neves mestergyilkos, behatoló egység vezető fejvadásza                                                                                                                               | Erő:`-2`<br />Ügyesség:`+3`<br />Önuralom:&nbsp;`+2`<br />Összpontosítás:&nbsp;`3.szint` |
| Élő legenda (15) | • Ilyen nincs!! A puszta, csúszós sziklafalon is felkúszik. Kézfeje, lába deformálódott – alkalmazkodva a mászás követelményeihez. Félmágikus hatású ismeretekhez jut.<br />• Függeszkedve ⭕1 órát⭕ is kibír!<br />• **Példa**: mágiával kondicionált elit birodalmi fejvadász<br />• Képzettség bónusz: [Tapadás](#b%C3%B3nusz-tapad%C3%A1s) |      Erő:`-2`<br />Ügyesség:`+4`<br />Önuralom:`+3`<br />Összpontosítás: `6.szint`       |

<br />

---
### Bónusz: Tapadás

Titkos, félmágikus ismeret.

**Követelmény**: Életed a mászás; Mászás - `15.szint`

`15.szint`: Képes vagy pókként megtapadni a falon – akár a mennyezeten is. A kapaszkodáshoz nincs szükséged kiszögelésre.

---
### Próbák

| Célszám | Példa  |
| :----------- | :----------- |
| Könnyű       (6)  | Felmászni a magas tölgyfára,<br />Kötélen mászni (plusz súllyal, illetve lengő kötélen nehezebb! Lásd a módosítóknál) |
| Átlagos      (9)  | Felmászni a fogadó tetejére. ⭕Félig kikötve, félseggel ülve pihenni.⭕ |
| Nehéz        (12) | Repedéses kőfalon felmászni, omladékos, nagyon meredek leejtőn feljutni. |
| Nagyon nehéz (15) | Függőleges – nem repedéses – téglafalon felmászni, visszahajlásokkal tagolt meredek sziklafalon felmászni. |
| Rendkívül nehéz (18) | Gleccserszakadékból puszta kézzel kimászni. |
| Emberfeletti (21) | ⭕Olajjal leöntött visszahajló acélfalon felmászni.⭕ |

<br />

---
### Célszámot módosító körülmények

- Gyorsan mászni: `+3`
- Sötétben mászni: `+[3;6]`
- Plusz súllyal mászni: Erőtől függ, a KM dönt. Keretek: `+[1;6]` ; Erőpróba kellhet
- Lengő kötélen mászni: `+[1;6]`
- Sérülten mászni: Lásd a [Sérülés hatása képzettségpróbára](../036_kepzettsegproba.md#sérülés-hatása-képzettségpróbára) c. fejezetet!
- Mászókampók: ⭕?????  ez adjon pluszt, vagy legyen követelmény a durvább próbákhoz? Ha pluszt ad, az borítja a próbák „behangolt” értékeit.⭕

<br />

### Edzettség és Erő

Rontott Mászás próba esetén dobható – a rontás mértékétől függő – Edzettségpróba (`1 pont rontás: Könnyű próba`, `2 pont rontás: Átlagos próba`, stb), hogy a kritikus (rontott) szituációban képes -e megtartani magát a mászó. Ha nem, lehullik, mint a falevél, ha igen, sikerül megkapaszkodnia egy stabil pozícióban. Az Edzettségpróbára „rátehet” a karakter az `Erő` tulajdonságából, kvázi erőtartalékait felemésztve. Ennek viszont ára van: az így átcsoportosított Erő pontok elvesznek, és óránként csak `1` tér vissza (⭕vagy esetleg inkább 10 percenként 1⭕).

⭕Kérdés: ha csak meg akarja így tartani magát, azt mennyi ideig tudja megtenni?⭕

<br />

### Önuralom

Ha a próbát nagyon kiélezett, életveszélyes helyzetben rontja el a karakter, a KM dönthet úgy, hogy `Önuralom` próbát dobat. Ha ez nincs meg, akkor a KM-nek jogában áll, hogy tetszőlegesen nagy `Erő` tulajdonság tartalékot felhasználtasson a karakterrel (adrenalin hatása). Így jó eséllyel meg tud kapaszkodni, de minden erőtartalékát feléli, gyakorlatilag remegve a falhoz tapadva marad, további mászása erősen kérdéses, segítségre szorul.

Hogy egy karakter hányas `Erő` tulajdonsággal képes még továbbmászni, az főleg a testsúlyától, kisebb részben pedig pszichikai állapotától függ. A fenti probléma eldöntése a KM feladata.

<br />

---
