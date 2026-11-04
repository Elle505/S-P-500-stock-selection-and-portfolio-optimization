# `dynamic_markowitz_data_source.py` – Dinamikus Markowitz Adatbetöltő Modulja


Segédmodul, amely a Streamlit felület számára biztosít biztonságos adatbetöltő függvényeket a `dynamic_markowitz/data/` mappából.

---


* **Fájlellenőrzés (`require_file`):** Ellenőrzi a Parquet fájlok létezését, és egyértelmű hibaüzenetet ad, ha a kód még nem futott le.
* **Adatbetöltők (`load_dynamic_winners()`, `load_dynamic_summary()`, `load_dynamic_curve()`):** Beolvassa a szektorgyőzteseket, a havi összefoglalókat és a perces portfóliógörbét.
* **Elérhető Hónapok Listázása (`dynamic_available_months()`):** Visszaadja a tesztelt hónapok listáját a felületi választógombokhoz.
