# `build_dynamic_markowitz.py` – Dinamikus XGBoost + Markowitz Portfólió Építője

Összeköti a gépi tanulásos XGBoost modellt a klasszikus Markowitz-féle portfólió-optimalizálással. 
Az XGBoost által becsült havi hozamok alapján szektoronként kiválasztott 11 részvényt súlyozza át a Sharpe-ráta maximálásával, figyelembe véve a kockázati korlátokat.

---

### 1. XGBoost Tanítás és Szektoronkénti Kiválasztás (`main`)
* Havi gördülőablakos tanítással illeszti az XGBoost modellt az elérhető adatokra.
* Kiszámítja a várható havi hozamokat az S&P 500 aktuális tagjaira, majd mind a 11 GICS szektorból kiválasztja az 1-1 legjobb részvényt.

### 2. Historikus Adatok és Kovariancia Kezelése (`get_historical_returns_for_month()`, `build_covariance_matrix()`)
* Összegyűjti a kiválasztott 11 részvény utolsó 90 kereskedési napjának adatait a korábbi perces és napi állományokból.
* Kezeli az új belépő részvényeket (amik teljesen újak, tehát nincs hozzájuk még adat), zsugorítással (shrinkage) numerikusan stabil kovarianciamátrixot épít.

### 3. Sharpe-ráta Optimalizálás Súlykorlátokkal (`optimize_dynamic_weights()`)
* Maximálja a portfólió várt Sharpe-rátáját SLSQP algoritmussal.
* Betartja a szigorú korlátokat: a súlyok összege 100%, és egyetlen részvény súlya sem lehet kisebb 2%-nál vagy nagyobb 25%-nál.

### 4. Percalapú Portfóliógörbe Szimuláció
* A megadott 100 000 Ft-os kezdőtőkéből kiindulva szimulálja a portfólió perces értékváltozását a teszthónapok során, majd elmenti az eredményeket.
