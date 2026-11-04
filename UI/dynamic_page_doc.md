# `dynamic_page.py` – Dinamikus Modell Vezérlő és Státusz Streamlit Nézet


Ez a felületi elem teszi lehetővé a dinamikus XGBoost modell futtatási beállításainak (Test / Live) kezelését és a pipeline adat-előkészítési állapotának ellenőrzését.

---


### 1. Futtatási Mód Beállítása és Konfiguráció Mentése (`save_config()`)
* **Test mód:** Engedélyezi a tesztidőszak (2025-09 → 2026-08) kezdő- és záróhónapjának kiválasztását, és generálja a futtatási parancsot.
* **Live mód:** Felületet biztosít a jövőbeli élő futtatási dátum megadásához.

### 2. Adat-előkészítési Státusz (Data Preparation Status)
* Vizuális metrikákkal ellenőrzi a szükséges Parquet fájlok (`daily_features_all`, `monthly_snapshots`, `training_dataset`) létezését.
* Kiírja a tanítóadatbázis mintaszámát, hónapjait és a benne található részvények számát.

### 3. Vizuális Helytartók (Placeholderek)
* Előre kialakított szekciókat biztosít a portfóliógörbe, a kiválasztott részvények és a havi újrasúlyozás későbbi megjelenítéséhez.
