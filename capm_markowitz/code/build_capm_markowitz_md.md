# `build_capm_markowitz.py` – CAPM és Markowitz Portfólió Építője

Ez a kód valósítja meg a gépi tanulásos XGBoost modell benchmarkjaként használt klasszikus pénzügyi modellt (CAPM + Markowitz). 
Havi szinten választja ki a szektorok legjobb részvényeit Jensen Alpha alapján, majd Markowitz-optimalizálással határozza meg azok ideális portfóliósúlyait.

---

### 1. Historikus Adatok Beolvasása (`load_unified_daily_prices()`)
* Összegyűjti és napi szintre csoportositja az elmúlt időszak és a teszthónapok nyitó- és záróárait az adatszivárgásmentes feldolgozáshoz.

### 2. CAPM Jensen Alpha Számítás (`calculate_capm_expected_returns()`)
* Walk-forward megközelítéssel az adott teszthónap előtti 60 kereskedési nap adataiból kiszámítja a részvények Béta és Alpha mutatóit.
* Kiszámolja a kockázattal korrigált Alpha-szignált (`alpha_signal`).

### 3. Szektoronkénti Kiválasztás
* A 11 GICS szektor mindegyikéből kiválasztja a legmagasabb `alpha_signal`-lal rendelkező részvényt (összesen 11 részvényt).

### 4. Markowitz Sharpe-ráta Optimalizálás (`optimize_dynamic_weights()`)
* Felépíti a 11 részvény zsugorított kovarianciamátrixát.
* SLSQP algoritmussal maximálja a várt Sharpe-rátát a megadott korlátok mellett (min. 2%, max. 25% részvényenkénti súly).

### 5. Portfóliógörbe Szimulációja (`main`)
* Perces adatok alapján lemodellezi a 100 000 Ft-os kezdőtőke havi egyenlegváltozását és elmenti az eredményeket.
