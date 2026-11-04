# `download_original_test_period.py` – Teljes Tesztidőszak Adatletöltő

# Az oracle modell csak kiindulási idealizált modellként készült, pusztán a kiváncsiság vezérelte, hogy mi is lenne ha a modellek 100%-os előrejelzésekre lennének képesek 

Ez a kód automatizálja a teljes 12 hónapos tesztidőszak (2025-09-től 2026-08-ig) adatainak letöltését. 
Lényegében a `download_original_month.py` kötegelt és szilárdabb, automatikusan folytatható változata.

---

## Mit csinál?

### 1. 12 Hónapos Ciklus Kezelése (`main`)
* Végigmegy a tesztidőszak mind a 12 hónapján.
* Minden hónaphoz lekéri az adott napon érvényes S&P 500 tagságot (Point-in-Time).

### 2. Megszakítás-biztos (Resume) Letöltés (`existing_file_is_usable`)
* Ellenőrzi a már letöltött Parquet fájlokat. Ha egy ticker adatai hiánytalanul megvannak, átugorja, így megszakadás után biztonságosan újraindítható.

### 3. Státuszriport Generálása (`STATUS_FILE`)
* Hónaponként ellenőrzi az állományok érvényességét, és egy összefoglaló `test_period_download_status.csv` fájlban rögzíti a letöltés állapotát.
