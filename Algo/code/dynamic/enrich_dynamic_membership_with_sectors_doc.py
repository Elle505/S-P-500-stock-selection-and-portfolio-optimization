# `enrich_dynamic_membership_with_sectors.py` – Point-in-Time Szektorbesorolás

## Áttekintés
Ez a modul felelős azért, hogy a havi dinamikus S&P 500 tagsági listák minden egyes részvényéhez hozzárendelje a pontos GICS (Global Industry Classification Standard) szektorbesorolást. 
A felülvizsgálat szigorúan időponthű elemzési elv(PIT) alapon történik, így elkerüli a szektorváltásokból eredő adatszivárgást.

---

### 1. Időponthű Wikipédia Revíziók (`get_wikipedia_revision()`)
* Megkeresi a Wikipédia *List of S&P 500 companies* oldalának pontosan abban az időpontban érvényes korábbi változatát (revízióját), amikor a havi felmérés történt.
* Kinyeri a táblázatból a részvények tickerjét és az 11 hivatalos GICS szektor egyikébe tartozó besorolását.

### 2. Automatikus S&P Global Tartalék-kereső (`official_sector_fallback()`)
* Ha egy újonnan bekerült vagy átnevezett részvény szektora hiányzik a Wikipédiáról, a modul automatikusan lekéri az S&P Global hivatalos sajtóarchívumát.
* Végigszűri a sajtóközlemények táblázatait és szövegét a hivatalos besorolásért.

### 3. Szektor-ellenőrzés és Validáció (`prepare_month()`)
* Ellenőrzi, hogy mind az 500 részvény kapott-e szektort.
* Garantálja, hogy a kimenetben kivétel nélkül mind a 11 standard GICS szektor képviseltetve legyen (ez elengedhetetlen a szektoronkénti 1 győztes kiválasztásához).

### 4. Mentés és Audit (`commit_result()`, `save_status()`)
* A felülvizsgált listát felülírja a dinamikus tagsági CSV fájlokban (`membership_date,ticker,sector`).
* Részletes audit naplót készít a beállításokról és az esetleges S&P Global tartalék-keresésekről (`sector_enrichment_status.csv`).
