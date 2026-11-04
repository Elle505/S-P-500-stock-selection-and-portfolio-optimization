# `download_original_month.py` – Egy Hónapos Alpaca Adatletöltő

# Az oracle modell csak kiindulási idealizált modellként készült, pusztán a kiváncsiság vezérelte, hogy mi is lenne ha a modellek 100%-os előrejelzésekre lennének képesek 

Ez a szkript egy konkrét megadott hónapra (alapértelmezetten 2025-09) tölti le az S&P 500 aktuális tagságát és a hozzá tartozó 1 perces részvényárfolyam-adatokat az Alpaca API-ról.

---


### 1. Naptár és Tagság Letöltése (`get_month_schedule`, `build_membership_snapshot()`)
* Lekéri a hivatalos NYSE kereskedési naptárat (nyitó és záró időpontok).
* A historikus tagsági adatbázisból kinyeri az adott hónap első napján érvényes S&P 500 részvényeket.

### 2. Perces Adatok Letöltése és Szűrése (`download_symbol_month()`, `normalize_bars()`)
* Letölti a 1 perces árfolyamadatokat (OHLCV) az Alpaca REST API-ról.
* Szigorúan a hivatalos nyitvatartási időre (`market_open` – `market_close`) szűri az adatokat, és átalakítja a megfelelő időzónára.

### 3. Validerálás és Marker Mentés (`validate_month_store()`)
* Ellenőrzi az adatok teljességét és hiánytalanságát (nincsenek duplikációk vagy hibás árak).
* Sikeres letöltés esetén létrehoz egy `_COMPLETE` statust.
