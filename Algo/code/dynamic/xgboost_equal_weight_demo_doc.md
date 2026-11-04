# `xgboost_equal_weight_demo.py` – Egyenlő Súlyozású Portfólió Szimuláció

Ez a demó szkript egy konkrét kereskedési stratégiát szimulál. 
Az XGBoost modell által becsült havi hozamok alapján mind a 11 GICS szektorból kiválasztja a legjobb részvényt, majd ezeket egyenlő súlyozással (1/11-ed arányban) beleteszi egy portfólióba.

---

### 1. Havi Predikciók és Szektorgyőztesek Beolvasása (`run_month()`)
* Betölti az adott hónapra tanított XGBoost modellt és lefuttatja a becsléseket.
* Szektoronként rangsorolja a részvényeket, és kiválasztja az 1. helyezetteket (összesen 11 részvényt).

### 2. Tényleges Hozamok Számítása (`calculate_realized_returns()`)
* Összeköti a kiválasztott részvényeket a tényleges piaci árfolyamokkal (hónap első kereskedési napjának nyitóára vs. hónap utolsó napjának záróára).
* Kiszámolja a részvények megvalósult hozamát és az egyenlő súlyozású havi portfólióhozamot.

### 3. Eredmények és Portfólió-mutatók (`main`)
* A teljes tesztidőszakra (2025-09 – 2026-08) összefűzi a havi hozamokat.
* Kiszámítja a portfólió kumulált hozamát, az évesített hozamot és a maximális visszaesést (Max Drawdown).
* Elmenti a részletes havi és összesített CSV/JSON riportokat a `results/dynamic/xgboost_equal_weight_demo/` mappába.
