# `config.py` – Konfiguráció és Paraméterek

## Áttekintés
Ez a fájl tartalmazza a teljes rendszer globális beállításait és alapvető paramétereit. 
Központi vezérlőként szolgál az adatfeldolgozás, a tanítási-tesztelési időszakok beállí tása, valamint a gépi tanulási modell bemeneti változóinak megadása során.

---

### 1. Tanítási és Tesztelési Időintervallumok
* **`TRAIN_START_MONTH` & `TRAIN_END_MONTH`**: A kezdeti tanító adathalmaz időtartama (2023. szeptembertől 2025. augusztusig, összesen 24 hónap).
* **`TEST_START_MONTH` & `TEST_END_MONTH`**: Az out-of-sample tesztelési időszak (2025. szeptembertől 2026. augusztusig, összesen 12 hónap).

### 2. Gördülőablak és Éves Újraindítás (Training Reset)
* **`ANNUAL_RESET_MONTH = 9`**: Minden év szeptemberében újraindul a tanítóablak.
* **`BASE_TRAINING_MONTHS = 24`**: A tanítás alapértelmezett, minimális hossza 24 hónap.
* **`MAX_TRAINING_MONTHS = 35`**: A tanító adathalmaz maximális mérete (hónapról hónapra bővül 24 és 35 hónap között), ami megelőzi az elavult adatok túlsúlyát.

### 3. Historikus Adatbeolvasás és Puffer (Warmup)
* **`WARMUP_START` & `INITIAL_DATA_CUTOFF`**: A nyers historikus árfolyamadatok kezdő és záró időpontja a technikai indikátorok kiszámításához.
* **`NEW_TICKER_WARMUP_SESSIONS = 252`**: Az újonnan S&P 500-ba kerülő részvényeknél 252 kereskedési nap historikus adatot tölt be a rendszer, amely biztosítja a leghosszabb mutató (200 napos mozgóátlag) torzításmentes számítását.

### 4. Modell Bemeneti Változók (`MODEL_FEATURES`)
A gépi tanulási modell által használt 12 bemeneti jellemző listája:
* **Hozamok:** `return_5d`, `return_20d`, `return_60d` (rövid és középtávú hozamok).
* **Trendek:** `ma50_distance`, `ma200_distance` (relatív eltérés az 50 és 200 napos mozgóátlagtól).
* **Technikai indikátorok:** `rsi_14` (Relatív Erősségi Index), `macd_normalized` (normalizált MACD), `macd_signal_diff` (szignálvonal eltérése).
* **Kockázat és forgalom:** `volatility_20d`, `volatility_60d` (évesített volatilitás), `volume_ratio_20d` (forgalomarány).
* **Relatív teljesítmény:** `relative_return_20d` (az S&P 500 indexhez képest mért hozam).
