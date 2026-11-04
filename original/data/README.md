# `original/data/` – Alapvető Adatarchitektúra és Benchmark Adatok

Ez a mappa tartalmazza a teljes projekt alapjául szolgáló nyers és feldolgozott adatokat. 
Innen indul a 12 hónapos tesztidőszak (2025-09 – 2026-08) S&P 500 tagsági listája, az 1 perces árfolyamadatok, valamint az idealizált Oracle benchmark kimeneti fájljai.

# Az oracle modell csak kiindulási idealizált modellként készült, pusztán a kiváncsiság vezérelte, hogy mi is lenne ha a modellek 100%-os előrejelzésekre lennének képesek 

--- 

### 1. `membership/`
A teszthónapok időponthű S&P 500 tagsági listái és a szektorbesorolás audit fájljai.

* `sp500_members_YYYY-MM.csv`: Az adott hónap első kereskedési napján érvényes S&P 500 tagság és a hozzájuk tartozó GICS szektorok.
* `sector_enrichment_status.csv`: A Wikipedia revíziók alapján végzett historikus szektorbesorolás állapotát és érvényességét tartalmazza.
* `official_sector_fallback_audit.csv`: Napló azokról a részvényekről, ahol a szektort az S&P Global hivatalos sajtóközleményeiből kellett feloldani.

### 2. `minute/`
* Havi bontású mappákban tárolja a 490-510 S&P 500 részvény 1 perces árfolyamadatait (`.parquet` formátumban), szigorúan a NYSE hivatalos nyitvatartási idejére szűrve.
* Minden hónap mappájában megtalálható a `_COMPLETE` marker fájl, ha a letöltés hiánytalanul lefutott.

### 3. `monthly/`
A teljes univerzumra vonatkozó havi megvalósult hozamok és szektorgyőztesek gyűjtőhelye.

* `monthly_returns.csv` / `.parquet`: Az S&P 500 összes tagjának ténylegesen megvalósult havi hozama (`exit_close / entry_open - 1`).
* `sector_winners.csv` / `.parquet`: A 11 GICS szektor legmagasabb valós hozamot elérő részvényei hónapról hónapra.

### 4. `results/`
Az idealizált Oracle (perfect foresight) benchmark modell futtatási kimenetei.

* `oracle_monthly_summary.csv` / `.parquet`: Havi
