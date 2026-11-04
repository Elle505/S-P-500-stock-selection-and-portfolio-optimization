# `resolve_corporate_actions.py` – Vállalati Események és Hiányzó Célváltozók Kezelése

## Áttekintés
Ez a modul a tőzsdei vállalati események (Corporate Actions) automatikus korrekciójáért felel. 
Ha egy részvény a teszthónap során felvásárlás, összeolvadás, névváltoztatás vagy kivezetés miatt eltűnik a tőzsdéről, a modul az Alpaca API esemény-naplójából rekonstruálja a folyamatot, így a tanító adathalmaz nem veszít értékes információt.
---

### 1. Hiányzó Célváltozók Azonosítása (`find_missing_targets()`)
* Megkeresi azokat a snapshot sorokat, ahol a bemeneti változók (feature-ök) elkészültek, de a hónap végére nem alakult ki tényleges záróár a részvény kivezetése miatt.

### 2. Eseménylánc Rekonstrukciója (`resolve_missing_target()`)
* Az Alpaca Corporate Actions API segítségével lépésről lépésre végigköveti a részvény sorsát a belépési és kilépési dátum között:
  * **Névváltás (`name_change`):** Áttér az új ticker árfolyamának követésére.
  * **Készpénzes felvásárlás (`cash_merger`):** A kapott készpénzösszeget számolja el a hónap végi értéknek.
  * **Részvénycsere (`stock_merger`):** A cserearány alapján az utódrészvény árfolyamával számolja ki a záróértéket.
  * **Részvény- és készpénzcsere (`stock_and_cash_merger`):** Egyesíti a kapott készpénzt és az új részvény pozíciót.
  * **Részvényfelosztás (`forward_split` / `reverse_split`):** Korrigálja a részvények darabszámát.

### 3. Tanító Adathalmazok Javítása (`patch_training_sets()`)
* A kiszámított szintetikus záróérték és a megvalósult hozam alapján pótolja a hiányzó célváltozót (`target_next_month`).
* Frissíti a walk-forward tanítófájlokat (`training_for_YYYY-MM.parquet`), megelőzve az adatok eldobásából adódó torzítást.

### 4. Audit és Biztonság (`save_resolution_log()`)
* Biztonsági mentést készít a módosított tanítófájlokról (`_before_corporate_action_patch/`).
* Részletes naplót ment a feloldott eseményekről (`resolved_missing_targets.parquet`), biztosítva a szimuláció teljes reprodukálhatóságát.
