# `build_dynamic_snapshot.py` – Havi Predikciós Pillanatképek Építése

Létrehozza az adott hónap predikciójához szükséges bemeneti pillanatképet (snapshotot). 
Pontosan a hónap eleji belépési időpontban érvényes mutatószámokat gyűjti össze az S&P 500 tagjaira.

---

### 1. Historikus Előzmények Beolvasása (`load_ticker_history()`)
* Beolvassa a részvények elmúlt 500 napos előzményét, hogy a mozgóátlagok és indikátorok pontosan kiszámíthatók legyenek.

### 2. Havi Snapshot Összeállítása (`build_current_snapshot()`)
* Az adott hónapra érvényes S&P 500 tagsági lista alapján egyenként lekéri a részvények adatait.
* Kiszámolja a cutoff napra érvényes 12 modell mutatót.
* Jelöli, ha egy részvénynek hiányzik a története vagy nem számolható ki valamelyik mutatója (`exclusion_reason`).

### 3. Metaadatok és Izoláció
* Hozzáadja a futtatás pontos UTC időpontjait (belépés, kilépés, adatzárás).
* Kiszűri a célváltozót: szigorúan csak a bemeneti jellemzőket tartalmazhatja, jövőbeli árfolyamot nem
* Az elkészült fájlt lementi a `snapshot_YYYY-MM.parquet` néven.
