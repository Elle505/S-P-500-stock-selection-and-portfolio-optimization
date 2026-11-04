# `app.py` – A Streamlit Alkalmazás Fő Belépési Pontja és Dashboard Vezérlője

Ez a teljes webes dashboard központi indítófájlja. 
Ez építi fel a bal oldali navigációs menüt (sidebar), kezeli az oldalak közötti váltást (routing), és itt kapott helyet a kutatási eredmények és az XGBoost indikátor-fontosságok (Feature Importance) külön összefoglaló oldala is.

---

### 1. Oldalbeállítás és Navigáció (`st.sidebar.radio`)
* Beállítja az alkalmazás címét, ikonját és a széles elrendezést (wide mode).
* Egy 7 elemű menürendszert biztosít a különböző stratégiák és elemzések eléréséhez:
  1. Összesítés & Összehasonlítás
  2. Dinamikus S&P 500 (Markowitz)
  3. CAPM + Markowitz (Klasszikus)
  4. XGBoost egyenlő súlyozás
  5. Original S&P 500 változás
  6. XGBoost fine tuning
  7. Vizsgálat és eredményei

### 2. Vizsgálat és Eredményei Oldal (`render_evaluation_page`)
* Kirajzolja az XGBoost modell által használt 12 indikátor relatív fontosságát bemutató grafikont (`feature_importance.png`).
* Vázlatos szöveges elemzést ad a 3 legfontosabb tényezőről (`volume_ratio_20d`, `volatility_60d`, `relative_return_20d`).
* Összefoglaló táblázatban hasonlítja össze a 4 vizsgált modell zárótőkéjét és kumulált hozamát.

### 3. Dinamikus Újratöltés (`st.cache_data.clear`)
* A menüsávban található gomb segítségével törli a memóriában tárolt gyorsítótárat (cache-t), így az adatok azonnal frissülnek a Parquet fájlok újraolvasásával.
