# `original_data_source.py` – Oracle Benchmark Adatbetöltő Segédmodul

# Az oracle modell csak kiindulási idealizált modellként készült, pusztán a kiváncsiság vezérelte, hogy mi is lenne ha a modellek 100%-os előrejelzésekre lennének képesek 

Ez a modul felelős az idealizált Oracle benchmark adatainak biztonságos beolvasásáért és előkészítéséért a Streamlit felület számára.

---


### 1. Fájllétezés Ellenőrzése (`require_file`)
* Szigorúan ellenőrzi a Parquet fájlok jelenlétét a `original/data/` mappában, és egyértelmű hibaüzenettel adja meg a hiányzó fájlokat.

### 2. Adatállományok Beolvasása (`load_*`)
* **`load_monthly_returns`**: Az S&P 500 tagok tényleges havi hozamait tölti be.
* **`load_sector_winners`**: A 11 GICS szektor valós győzteseit olvassa be.
* **`load_oracle_weights`**: A Markowitz-optimalizációval meghatározott ideális súlyokat tölti be.
* **`load_monthly_summary` & `load_portfolio_curve`**: A havi tőkeváltozásokat és a perces felbontású portfóliógörbét teszi elérhetővé.

### 3. Havi Szűrő Segédfüggvény (`load_month()`)
* Egy adott kiválasztott teszthónapra (pl. `2025-09`) kinyeri az összes kapcsolódó részletadatot egyetlen szótár struktúrába.
