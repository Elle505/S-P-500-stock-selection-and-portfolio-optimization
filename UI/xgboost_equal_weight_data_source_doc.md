# `xgboost_equal_weight_data_source.py` – XGBoost Equal Weight Adatbetöltő

Segédmodul, amely a felület számára biztosít adatbeolvasási funkciókat az `xgboost_equal_weights/data/` mappából.

---

* **Fájlellenőrzés (`require_file`):** Hibát dob, ha az egyenlő súlyozású modell futtatási fájljai még nem jöttek létre.
* **Adatbeolvasás (`load_sector_winners`, `load_monthly_summary`, `load_portfolio_curve`):** Tölti a szektorgyőzteseket, havi összefoglalókat és a perces portfóliógörbét.
* **Hónapok Listázása (`available_months`):** Lekéri a tesztelt hónapok listáját a felületi valasztódobozhoz.
