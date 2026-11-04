# `build_walkforward_training.py` – Gördülőablakos Tanító Adatszettek Építése

Ez a modul felel a walk-forward tesztelés során használt tanító adathalmazok összeállításáért.
Biztosítja, hogy a modell minden teszthónap előtt pontosan az abban a pillanatban elérhető legfrissebb tanítóadatokból tanuljon.

---

### 1. Éves Újraindítási Logika (`get_training_window()`)
* Meghatározza az aktív tanítóablak méretét.
* Minden év szeptemberében alaphelyzetbe állítja az ablakot 24 hónapra (`BASE_TRAINING_MONTHS = 24`), majd hónapról hónapra bővíti azt egészen 35 hónapig (`MAX_TRAINING_MONTHS = 35`).

### 2. Havi Célértékek Lezárása (`finalize_month_target()`)
* Amint lezárult egy teszthónap, kiszámolja a benne szereplő részvények megvalósult hozamát (`target_next_month`).
* Az így lezárt adatokat elmenti a `completed_YYYY-MM.parquet` fájlba, hogy a későbbi hónapok tanításánál már fel lehessen őket használni.

### 3. Tanítókészlet Összeállítása a Modellnek (`build_training_for_run()`)
* Összegyűjti az alaptetétből és a korábbi teszthónapokból származó adatokat.
* Szigorúan kiszűri azokat a hozamokat, amelyek a modell futtatási időpontja után zártak le (adatszivárgás elleni védelem).
* Elmenti a modell számára kész tanítóállományt a `training_for_YYYY-MM.parquet` fájlba.
