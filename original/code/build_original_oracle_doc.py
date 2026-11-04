# `build_original_oracle.py` – Idealizált Oracle Portfólió Benchmark

# Az oracle modell csak kiindulási idealizált modellként készült, pusztán a kíváncsiság vezérelte, hogy mi is lenne ha a modellek 100%-os előrejelzésekre lennének képesek. 

Ez a kód valósítja meg a teoretikus felső korlátot (Oracle benchmark). 
Nem végez előrejelzést, hanem a hónap végén ténylegesen megvalósult hozamok (perfect foresight) alapján választja ki a szektorgyőzteseket és optimalizálja a portfóliót.

---


### 1. Tényleges Havi Hozamok Számítása (`build_all_monthly_returns()`)
* Beolvassa a perces adatokat, és kiszámítja a részvények valós havi hozamát (`exit_close / entry_open - 1`).

### 2. Tökéletes Szektorgyőztesek Kiválasztása (`select_sector_winners()`)
* Szektoronként kiválasztja azt a részvényt, amely a legmagasabb tényleges hozamot érte el az adott hónapban (összesen 11 részvény).

### 3. Oracle Markowitz Optimalizálás (`optimize_oracle_weights()`)
* A megvalósult napi hozamokból számított kovarianciamátrix és a tényleges havi hozamok alapján maximalizálja a Sharpe-rátát (SLSQP algoritmussal).

### 4. Percalapú Portfóliógörbe Generálása
* Lemodellezi a 100 000 Ft-os kezdőtőke elméleti maximális növekedését, és elmenti a riportokat az `original/data/results/` mappába.
