# `algo.py` – A Projekt Fő Vezérlőszkriptje

A rendszer központi vezérlője (CLI parancssori felület). 
A nyers adatgyűjtéstől és a havi tanítóállományok építésétől kezdve a szektorbesoroláson át egészen az XGBoost modell lefuttatásáig.

---

### 1. Napi Adatok és Alaptanítás Előkészítése (`prepare-initial`)
* Generálja a napi mutatókat és összeállítja a kezdeti 24 hónapos tanítóhalmazt.

### 2. Havi Adatelőkészítési Lépések (`prepare-month`)
* Letölti az adott hónap elején érvényes S&P 500 tagságot.
* Frissíti és szinkronizálja a részvények és az SPY ETF perces/napi árfolyamait a vágási időpontig (cutoff).
* Lezárja az előző hónap tényleges hozamait és létrehozza az aktuális havi predikciós pillanatképet (snapshot).

### 3. Dinamikus Szektor-helyreállítás (`sector-month`)
* Ellenőrzi és hozzárendeli a 11 hivatalos GICS szektorbesorolást a hónap részvényeihez az időponthű elv (PIT) historikus adatok alapján.

### 4. Modell Futtatása és Tesztelés (`predict-month`, `predict-test`, `run-month`)
* Elindítja az XGBoost tanítását és predikcióját egy adott hónapra vagy a teljes tesztidőszakra (2025-09 – 2026-08).
* Élő (`live`) módban automatikusan futtatja a vállalati eseményeket rendező szkriptet is.

### 5. Állapotlekérdezés és Audit (`status`, `audit`)
* Kirajzolja a tanítóablakok méretét és felméri a meglévő adatok állapotát.
* Futtatja az adatszivárgás elleni teljes audithoz tartozó ellenőrzéseket.
