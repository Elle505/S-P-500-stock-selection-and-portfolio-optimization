# Dinamikus Markowitz Adat-architektúra (`dynamic_markowitz/data/`)

Ez a mappa tárolja az XGBoost predikciókra épülő, Markowitz-optimalizált portfólió futtatási kimeneteit.

---

### 1. `monthly/`
* `sector_winners.parquet`: Havi bontásban tárolja a 11 szektorgyőztes XGBoost által becsült hozamát, a ténylegesen megvalósult hozamot, a belépési nyitó- és kilépési záróárakat, valamint a Markowitz által meghatározott optimális portfóliósúlyokat (`markowitz_weight`).

### 2. `results/`
* `monthly_summary.parquet`: A 12 teszthónap (2025-09 – 2026-08) összefoglalója: havi portfólióhozam, kezdő és záró tőkeértékek.
* `portfolio_curve.parquet`: A portfólió tőkeértékének percalapú idősora a teljes tesztidőszak alatt (100 000 Ft kezdőtőkéről indítva).
