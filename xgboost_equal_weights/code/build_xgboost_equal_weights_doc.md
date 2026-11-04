# `build_xgboost_equal_weights.py` – XGBoost Egyenlő Súlyozású Portfólió Építője


Megvalósítja a gépi tanulásos baseline modellt. 
Az XGBoost által becsült havi hozamok alapján szektoronként kiválaszt 1-1 legjobb részvényt (11 részvényt), majd azokat egyenlő arányban súlyozza.

---


### 1. Walk-Forward ML Tanítás és Szektoronkénti Kiválasztás (`main`)
* Havi gördülőablakos tanítással illeszti az XGBoost modellt az elérhető adatokra.
* Kiszámítja a várható havi hozamokat az S&P 500 aktuális időponthű tagjaira.
* Mind a 11 GICS szektorból kiválasztja a legmagasabb predikcióval rendelkező részvényt.

### 2. Egyenlő Súlyozású Portfóliógörbe Építése (`build_month_portfolio_curve()`)
* Nem számol kovarianciamátrixot és Sharpe-maximalizálást: minden kiválasztott részvény fix $1/11$ súlyt kap.
* A perces árfolyamadatok alapján lemodellezi a 100 000 Ft-os kezdőtőke havi egyenlegváltozását.

### 3. Eredmények Mentése
* Elmenti a havi portfólióértékeket, a havi összefoglalókat és a kiválasztott szektorgyőzteseket az `xgboost_equal_weights/data/` mappába.
