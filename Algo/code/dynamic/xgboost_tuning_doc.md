# `xgboost_tuning.py` – XGBoost Hiperparaméter Finomhangolás (Tuning)

Ez a modul végzi az XGBoost modell hiperparamétereinek keresését (Random Search). 
Kizárólag a tesztidőszak előtti 24 hónap adatát (2023-09 – 2025-08) használja a túlillesztés és a tesztadat-szivárgás elkerülése érdekében.


### 1. Tesztadatok Védelmének Ellenőrzése (`load_training_data()`)
* Betölti a teszt előtti 24 hónap tanítóadatait.
* Kemény korlátot tartalmaz: ha a validációs halmazban megjelenik a `2025-09` vagy későbbi dátum, a szkript azonnal leáll!

### 2. Gördülő Validáció (`evaluate_params()`)
* A 24 hónap utolsó 12 hónapján (2024-09 – 2025-08) végez 12 lépcsős bővülő ablakos (expanding window) validációt.
* Számolja a Rank IC-t (sorrendi korreláció), RMSE-t, MAE-t és az iránybéli pontosságot (Directional Accuracy).

### 3. Keresési Tér és Szúrópróba (`SEARCH_SPACE`, `run_tuning()`)
* Véletlenszerűen kipróbálja a megadott számú konfigurációt (alapértelmezés szerint `--trials 50`).
* Teszteli a fák mélységét (`max_depth`), a tanulási rátát (`learning_rate`), a mintavételezést és a L1/L2 regularizációt.

### 4. Konservatív Modellválasztás – Egy Standard Hiba Szabály (`select_robust_candidate`)
* Nem feltétlenül a legmagasabb egyedi pontszámot elért modellt választja, hanem az "One-Standard-Error" szabály alapján a legstabilabb, legegyenletesebben teljesítő modellt.
* Az eredményeket és a kiválasztott legjobb paraméterkészletet elmenti a `best_params.json` és `tuning_trials.csv` fájlokba.
