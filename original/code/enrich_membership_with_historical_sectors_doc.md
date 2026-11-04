# `enrich_membership_with_historical_sectors.py` – Historikus Szektorbesorolás Adatdúsító

# Az oracle modell csak kiindulási idealizált modellként készült, pusztán a kiváncsiság vezérelte, hogy mi is lenne ha a modellek 100%-os előrejelzésekre lennének képesek 


Ez a szkript gondoskodik a időponthű elvről a szektorok tekintetében: a historikus S&P 500 tagsági listák részvényeihez rendel hozzá pontos GICS szektorbesorolást anélkül, hogy jövőbeli adatot használna fel.

---


### 1. Wikipedia Revision Lookup (`get_revision_before()`)
* A Wikipedia API segítségével megkeresi az adott teszthónap nyitása előtti legutolsó szócikk-revíziót a "List of S&P 500 companies" oldalról.
* Kinyeri a 11 hivatalos GICS szektorbesorolást a megadott időpont állapotának megfelelően.

### 2. Automatikus Official S&P Global Fallback (`lookup_official_sp_sector()`)
* Ha a Wikipedia revízióból hiányzik egy újonnan belépett részvény szektora, a kód automatikusan keresést futtat az S&P Global hivatalos sajtóközlemény-archívumában (`press.spglobal.com`).
* Az indexváltozási bejelentések alapján azonosítja a részvény hivatalos szektorát.

### 3. Staging, Biztonsági Mentés és Audit (`main`)
* Ellenőrzi, hogy mind a 11 standard GICS szektor jelen van-e.
* Biztonsági mentést készít az eredeti fájlokról a `_before_sector_enrichment` mappába, és elmenti a részletes audit CSV fájlokat.
