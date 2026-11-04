# Adat-architektúra és Mappaszerkezet (`data/`)

Ez a mappa tartalmazza a kísérletek során felhasznált összes historikus árfolyamot, S&P 500 tagsági információt, vállalati eseményt és a kimeneti modelleket. 

*Megjegyzés: A bináris adatfájlok (.parquet) és a cache mappák automatikusan generálódnak a kódok lefuttatásakor.*

---

## Mappák és Fájlok Leírása

### 1. `corporate_actions/`
A tőzsdei vállalati események (fúziók, felvásárlások, névváltozások, kivezetések) adatait tárolja a hozamok torzításmentes korrekciójához.
* `api_cache/`: Az Alpaca Corporate Actions API nyers JSON válaszainak gyorsítótára.
* `price_cache/`: A kivezetett vagy átnevezett részvények perces árfolyam-cache-e.
* `resolved_missing_targets.parquet` / `.csv`: A sikeresen helyreállított hiányzó célhozamok és az eseményláncok audit naplója.

### 2. `membership/`
Az S&P 500 index tagságának historikus és dinamikus nyilvántartása.
* `dynamic/`: Havi bontású Point-in-Time tagsági CSV fájlok (`sp500_members_YYYY-MM.csv`).
* `sp500_training_membership_intervals.parquet`: Historikus tagsági intervallumok a kezdeti 24 hónapos tanítóablakhoz.
* `sp500_training_universe.csv`: Az alaptanításban részt vevő részvények teljes listája.

### 3. `models/dynamic/`
A betanított gépi tanulási modellek (XGBoost) és a hibrid finomhangolási kísérletek mentett modellfájljai és paraméterei.
* `xgboost/`: A havi gördülő ablakon betanított végleges XGBoost modellek.
* `xgboost_baseline/` & `xgboost_tuning/`: Az alapértelmezett és a finomhangolt paraméterű modellek változatai.

### 4. `processed/`
Az előfeldolgozott napi árak, kiszámított technikai mutatók (feature-ök) és a szimulációs snapshotok gyűjtőhelye (Parquet formátumban).

### 5. `raw/`
A nyers perces részvényadatok (`minute/`) és az S&P 500 indexet követő SPY ETF napi záróárainak (`market/`) tárolója.

### 6. `results/`
A kísérleti futások eredményei, a backtest hozamok, a portfólió-súlyok és az audit riportok.

### 7. `sectors/`
Az S&P 500 tagok 11 hivatalos GICS szektorbesorolása, beleértve a Wikipédia PIT revíziókból és az S&P Global sajtóközleményekből származó adatokat.

### 8. `run_config.json`
A modellfutások aktuális beállításait és paramétereit tartalmazó konfigurációs fájl.
