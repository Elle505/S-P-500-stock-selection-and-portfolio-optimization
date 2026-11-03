# `audit_dynamic_data.py` – Adatszivárgás és Integritás Ellenőrzése
A modul az adatszivárgás (data leakage) és az időbeli hibák kiszűrésére szolgál. 
Végigellenőrzi az összes feldolgozott adathalmazt, snapshotot és tanító fájlt, hogy biztosan ne kerülhessen jövőbeli információ a modellbe a tanítás során.

---

### 1. S&P 500 Tagsági Intervallumok Ellenőrzése (`audit_intervals()`)
* Ellenőrzi, hogy az S&P 500 tagsági adatcsomagban nincsenek-e hiányzó kezdő- vagy hibás záródátumok.
* Kiszűri az egymással fedésben lévő, hibás tagsági időszakokat.

### 2. Tanító Adatszettek Átvizsgálása (`audit_training()`)
* Ellenőrzi a walk-forward ablakokat: a tanító adatokban csak a modell futtatása előtti lezárt hónapok szerepelhetnek.
* Megnézi, hogy a 12 megadott mutató (feature) és a célváltozó (`target_next_month`) hiánytalanul számolható-e.
* Leellenőrzi, hogy a hozam képlete pontosan `exit_close / entry_open - 1`-e.

### 3. Snapshotok Ellenőrzése (`audit_snapshot()`)
* Garantálja, hogy a predikciós pillanatképek szigorúan izolálva vannak, azaz semmilyen célváltozó vagy jövőbeli árfolyam nem szerepel bennük.
* Összeveti a pillanatképben lévő részvényeket az adott havi hivatalos tagsági listával.

### 4. Változatlanság Tesztelése (`audit_training_freeze()` & `audit_snapshot_freeze()`)
* Biztosítja, hogy a korábban lementett historikus adatok a későbbi tanítások során se módosuljanak vagy íródjanak felül.

### 5. Riport Készítése (`save`)
* Az ellenőrzés végén készít egy összefoglaló CSV és JSON jelentést a `results/dynamic/audit/` mappába.
