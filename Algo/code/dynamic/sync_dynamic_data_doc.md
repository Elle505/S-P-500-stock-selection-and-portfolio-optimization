# `sync_dynamic_data.py` – Dinamikus Adatszinkronizáció és Letöltés

## Áttekintés
Ez a modul felelős a nyers piaci adatok és az S&P 500 tagsági információk frissítéséért. 
Az Alpaca API-t és a NYSE kereskedési naptárt használva letölti a szükséges perces árfolyamokat, gondoskodik a 252 napos warmup adatok meglétéről, és előkészíti a havi tesztelési időszakokat.

---

### 1. NYSE Naptár és Időpont-meghatározás (`get_run_metadata())
* Meghatározza az adott teszthónap pontos időbélyegeit (előző havi zárás mint feature cutoff, hónap első napjának nyitása mint belépési pont, és hónap utolsó zárása mint kilépési pont).

### 2. Dinamikus Tagság Kezelése (`get_or_create_membership()`)
* Letölti az S&P 500 historikus tagsági változásait.
* Előállítja az adott hónap első kereskedési napjára vonatkozó pontos tagsági listát (`sp500_members_YYYY-MM.csv`), megelőzve a túlélési torzítást (survivorship bias).

### 3. Perces Árfolyamok Letöltése (`sync_tickers_to_cutoff()`)
* **Gördülő letöltés:** Letölti az S&P 500 tagok perces árfolyamait az Alpaca API-ból a megadott időpontig.
* **Új részvények felkészítése (Warmup):** Új részvény bekerülése esetén automatikusan letölti az elmúlt 252 kereskedési nap adatait a 200 napos mozgóátlag (`MA200`) pontos kiszámításához.

### 4. SPY Napi Adatok Letöltése (`sync_spy_daily_to_cutoff()`)
* Frissíti az S&P 500 indexet követő SPY ETF napi záróárait, ami a relatív hozamok (`relative_return_20d`) kiszámításához szükséges.

### 5. Adattárolás és Normalizálás (`save_minute_data()`)
* Évekre bontott Parquet fájlokban tárolja a perces adatokat.
* Egységesíti az időzónákat (UTC / America/New_York) és kiszűri a kereskedési időn kívüli vagy hibás sorokat.
