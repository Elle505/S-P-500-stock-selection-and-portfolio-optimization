# `paths.py` – Projekt Elérési Útvonalak és Könyvtárak

## Áttekintés
Ez a modul határozza meg a teljes projekt könyvtárszerkezetét és a legfontosabb adatfájlok pontos elérési útját. 
Biztosítja, hogy az adatelőkészítési, tanítási és tesztelési lépések egységesen kezeljék a fájlokat, valamint a futás során automatikusan létrehozza a hiányzó könyvtárakat.

---

### 1. Gyökérkönyvtárak (Root Paths)
* **`PROJECT_ROOT`**: A projekt fő gyökérkönyvtára.
* **`ALGO_ROOT`**: Az algoritmusokat és adatkezelést tartalmazó `Algo/` könyvtár.
* **`DATA_ROOT`**: Az adatok tárolására szolgáló `Algo/data/` főmappa.

### 2. Nyers Adatok (`raw/`)
* **`MINUTE_DIR`**: A részvények perces felbontású árfolyamadatainak helye.
* **`MARKET_DIR`**: Piaci szintű adatok (pl. `SPY_daily.parquet` az S&P 500 ETF napi záróáraihoz).

### 3. Tagsági Adatok (`membership/`)
* **`MEMBERSHIP_DIR`**: A statikus S&P 500 tagsági fájlok és intervallumok tárolója.
* **`RUNTIME_MEMBERSHIP_DIR`**: A havi gördülő (dynamic) S&P 500 tagsági CSV fájlok mappája (`Algo/data/membership/dynamic/`).

### 4. Feldolgozott Adatok és Snapshotok (`processed/`)
* **`DAILY_DIR`**: Összegzett napi árak és kiszámított feature-ök.
* **`SNAPSHOT_DIR`**: A havi pillanatképek (snapshotok), célváltozók és tanító mátrixok könyvtára.
* **`DYNAMIC_DIR`**: A walk-forward tesztelés havi bővülő snapshotjai, célváltozói és tanító adathalmazai.

### 5. Eredmények (`results/`)
* **`RESULTS_DIR`**: A kísérleti kimenetek, hozamgörbék és elemzési fájlok gyűjtőhelye.

### 6. Könyvtárak Automatikus Létrehozása
A fájl végén található ciklus automatikusan létrehozza a projekt működéséhez szükséges összes mappa-struktúrát, ha azok még nem léteznének.
