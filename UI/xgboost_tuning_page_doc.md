# `xgboost_tuning_page.py` – XGBoost Hiperparaméter Finomhangolási és Validációs Nézete

Ez az oldal mutatja be a 12 hónapos gördülőablakos hiperparaméter-tuning és a robusztus modellkiválasztás részletes eredményeit.

---

### 1. Modellösszehasonlító Mutatók (`Baseline` vs. `Raw Best` vs. `Robust Selected`)
* Összehasonlítja az alapértelmezett beállításokat, a legmagasabb Rank IC-jű nyers modellt és a véglegesen kiválasztott robusztus modellt.

### 2. Konfigurációk Szórásdiagramja (Scatter Plot)
* Diagramon ábrázolja az összes kipróbált paraméter-kombinációt a Mean RMSE és a Mean monthly Rank IC dimenziójában.

### 3. Validációs Hónapok és Hiperparaméterek Táblázatai
* Oszlopdiagramon mutatja meg a Spearman Rank IC értékét a 12 validációs hónap mindegyikében.
* Részletes táblázatban hasonlítja össze az egyes hiperparaméterek (`learning_rate`, `max_depth`, `subsample` stb.) konkrét értékeit és magyarázatát.
