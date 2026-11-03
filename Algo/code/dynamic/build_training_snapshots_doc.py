# `build_training_snapshots.py` – Kezdeti Tanító Adatszet Összeállítása

Ez a modul felelős a modell legelső tanításához szükséges 24 hónapos historikus adathalmaz összeállításáért (a 2023. szeptember és 2025. augusztus közötti időszakra).

---

### 1. Tagság és Naptár Kezelése (`load_membership()` & `get_month_metadata()`)
* Betölti a historikus S&P 500 tagsági időszakokat.
* Az NYSE naptár alapján meghatározza minden tanító hónaphoz a pontos belépési (hónap eleje) és kilépési (hónap vége) kereskedési napokat.

### 2. Mutatók és Hozamok Párosítása (`build_training_snapshots()`)
* Kiválasztja a hónap elején érvényes 12 technikai mutatót.
* Lekéri a hónap első nyitóárát (`entry_open`) és az utolsó záróárát (`exit_close`).
* Kiszámolja a következő havi célhozamot (`target_next_month = exit_close / entry_open - 1`).

### 3. Fájlok Mentése
* Kiszűri a hiányos sorokat (ahol nem teljes valamelyik mutató vagy hiányzik az ár).
* Lementi a havi naptárt, a snapshotokat, a célértékeket és a végleges összefűzött tanító adatszetet a `training_dataset.parquet` fájlba.
