# XGBoost Equal Weights Adat-architektúra (`xgboost_equal_weights/data/`)

Ez a mappa tárolja az XGBoost által becsült szektorgyőztesekre épülő, egyenlő súlyozású portfólió kimeneti adatait.

---

### 1. `monthly/`
* `sector_winners.parquet`: Havi bontásban tartalmazza a 11 GICS szektor XGBoost által kiválasztott győztes részvényeit, azok becsült hozamát (`predicted_return`), a ténylegesen megvalósult havi hozamát (`actual_return`), a belépési és kilépési árakat, valamint az egyenlő súlyértéket (`weight` = 1/11).

### 2. `results/`
* `monthly_summary.parquet`: A 12 teszthónap (2025-09 – 2026-08) összefoglalója: az egyenlő súlyozású portfólió havi hozama, valamint a kezdő és záró tőkeértékek.
* `portfolio_curve.parquet`: Az egyenlő súlyozású portfólió tőkeértékének percalapú idősora a 100 000 Ft-os kezdőtőkétől indítva.
