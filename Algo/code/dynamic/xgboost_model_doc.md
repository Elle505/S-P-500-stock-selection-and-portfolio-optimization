# `xgboost_model.py` – XGBoost Walk-Forward Modell és Predikció

Ez a modul az XGBoost gépi tanulási modell lelke. 
Ez végzi el a havi megnövelt tanítóállományokon a modell illesztését, és készíti el a predikciókat az aktuális hónap S&P 500 tagjaira.

---

### 1. Tanító és Predikciós Adatok Szigorú Ellenőrzése (`load_training()`, `load_snapshot()`)
* Betölti az adott hónap előtt lezárt tanítóadatokat (`training_for_YYYY-MM.parquet`).
* Ellenőrzi, hogy véletlenül se kerüljön jövőbeli célváltozó (target leakage) a bemeneti adatok közé.
* Beolvassa a hónap eleji érvényes snapshotot és a 11 GICS szektorbesorolást.

### 2. XGBoost Modell Tanítása (`train_and_predict_month()`)
* Egy globális `XGBRegressor` modellt tanít a 12 technikai/piaci mutatón (`return_5d`, `rsi_14`, `volatility_20d`, stb.).
* Kiszámítja a predikciókat az aktuális hónap részvényeire.
*A szektorbesorolást a predikciók utáni szűréshez használja a rendszer.

### 3. Szektoronkénti Rangsorolás és Mentés (`select_sector_winners()`)
* Szektoronként csoportosítja a részvényeket és kiválasztja a legmagasabb várható hozamú papírokat.
* Kiszámolja a mutatók súlyait (Feature Importance / Gain & Weight).
* Elmenti a modellt JSON formátumban (`xgboost_YYYY-MM.json`), a predikciókat és a szektorgyőzteseket CSV/Parquet állományokba.
