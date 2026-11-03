# `build_daily_features.py` – Napi Árak és Mutatók Számítása

Felépiti a perces adatokból a napi záróárakat és kiszámolja a gépi tanulási modell által használt 12 technikai és piaci mutatót.

---

### 1. Perces Adatok Egységesítése (`build_daily_prices()`)
* Beolvassa a részvények perces adatait, és elkészíti belőlük a napi `open`, `high`, `low`, `close` és `volume` értékeket.
* Lementi az eredményt a `daily_prices_all.parquet` fájlba.

### 2. Technikai Indikátorok Kiszámítása (`calculate_ticker_features()`)
* **Hozamok:** Kiszámolja az 5, 20 és 60 napos hozamokat (`return_5d`, `return_20d`, `return_60d`).
* **Mozgóátlagok:** Kiszámolja az 50 és 200 napos mozgóátlagtól való eltérést (`ma50_distance`, `ma200_distance`).
* **RSI és MACD:** Kiszámolja a 14 napos RSI-t, valamint a normalizált MACD-t és a szignálvonal eltérését.
* **Volatilitás és Forgalom:** Kiszámolja a 20 és 60 napos évesített volatilitást, és a napi forgalom arányát a 20 napos átlaghoz képest.

### 3. Piaci Relatív Hozam (`build_daily_features()`)
* Letölti az S&P 500 indexet követő SPY ETF napi adatait.
* Levonja a részvény 20 napos hozamából az SPY hozamát, így megkapjuk a piacgazdasági relatív teljesítményt (`relative_return_20d`).
* Az elkészült adathalmazt elmenti a `daily_features_all.parquet` fájlba.
