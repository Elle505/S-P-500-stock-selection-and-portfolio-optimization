# CAPM-Markowitz Adat-architektúra (`capm_markowitz/data/`)

Ez a mappa tárolja a CAPM + Markowitz modell futtatása során generált kimeneti adatokat és kísérleti eredményeket.

---

### 1. `monthly/`
* `sector_winners.parquet`: Havi bontásban tartalmazza a CAPM Jensen Alpha által kiválasztott 11 szektorgyőztes részvényt, azok Béta, Alpha, várt és tényleges hozamát, valamint a Markowitz által meghatározott portfóliósúlyokat.

### 2. `results/`
* `monthly_summary.parquet`: Összefoglaló a 12 teszthónap (2025-09 – 2026-08) mindegyikéről: havi portfólióhozam, kezdő és záró tőkeértékek.
* `portfolio_curve.parquet`: A portfólió tőkeértékének percalapú idősora a teljes tesztidőszak alatt (100 000 Ft kezdőtőkéről indítva).
