# S&P 500 Stock Selection & Portfolio Optimization (TDK)

A projekt célja a gépi tanulásos szektoronkénti részvénykiválasztás és a klasszikus portfólió-optimalizációs technikák alkalmazása az S&P 500 univerzumon, szigorú **Időponthű elemzési elv** és **Walk-Forward** kísérleti elrendezés mellett.

---

## Projekt Áttekintése & Módszertan

A kutatás a **2025-09 – 2026-08** közötti 12 hónapos tesztidőszakot vizsgálja. A modell felépítése a következő elvekre épül:

1. **Időponthű Tagság:** Kizárólag az adott hónap első kereskedési napján érvényes S&P 500 tagok kereskedhetők (túlélési torzítás kiszűrése).
2. **Walk-Forward XGBoost Tanítás:** Az XGBoost modell minden teszthónapban kizárólag a megelőző, lezárt hónapok adataiból tanul (jövőbelátás kiszűrése).
3. **Szektoronkénti Kiválasztás:** Mind a 11 szektorból kiválasztásra kerül a legmagasabb várható hozamú részvény.
4. **Markowitz Optimalizálás:** A kiválasztott 11 részvény súlyozása a Sharpe-ráta maximalizálásával történik, szigorú egyedi súlykorlátok mellett ($2\% \le w_i \le 25\%$).

---

## Összehasonlított Stratégiák & Eredmények

A tesztidőszak alatt (100 000 Ft-os kezdőtőkéből indítva) az alábbi portfólió-stratégiák teljesítménye került összehasonlításra:

| Stratégia | Zárótőke (HUF) | Kumulált Hozam (%) |
| :--- | :--- | :---: | :---: |
| **XGBoost + Equal Weight**  | **132 048 Ft** | **+32.05%** |
| **Dynamic XGBoost + Markowitz**  | **121 236 Ft** | **+21.24%** |
| **CAPM + Markowitz** | **101 085 Ft** | **+1.08%** |
| **Oracle (Perfect Foresight)**  | *1 350 991 Ft* | *+1250.99%* |

> **Megjegyzés az Oracle modellről:** Az *Oracle* (`build_original_oracle.py`) egy idealizált benchmark. Nem kereskedhető stratégia, hanem a már megvalósult jövőbeli hozamok alapján állítja össze az elérhető legmagasabb felső korlátot. Készitését pusztán a kiváncsiság vezérelte, hogy hogyan is alakulna a hozamgörbe, ha a modellek 100%-os előrejelzésekre lennének képesek. Éppen ezért a tdk szempontjából nem hordoz plusz értéket.

---

## Projektszerkezet

```text
.
├── Algo/                     # XGBoost modellkódok, tanítóadatok és snapshotok
│   ├── code/dynamic/         # XGBoost tanítás, hiperparaméter-tuning és modellszabályok
│   └── data/                 # Napi indikátorok és feldolgozott datasetek
├── dynamic_markowitz/        # Dinamikus XGBoost + Markowitz modul és adatai
├── xgboost_equal_weights/    # XGBoost + Equal Weighting modul és adatai
├── capm_markowitz/           # CAPM + Markowitz klasszikus modell és adatai
├── original/                 # Alapvető adatszivárgás-mentes architektúra & Oracle benchmark
├── ui/                       # Streamlit webes dashboard és vizualizáció
├── app.py                    # Fő Streamlit alkalmazás belépési pontja
├── diagnostic_metrics.py     # Portfólió diagnosztika és bias-detektáló szkript
└── plot_feature_importance.py # XGBoost indikátor-fontosságot generáló szkript

---
*Dokumentációs megjegyzés:
Ez a repository a TDK dolgozatom kód dokumentációja, célja a kutatásom során kidolgozott architektúrába tartozó részvénykiválasztási és portfólió-optimalizálási eljárások rendszerezett bemutatása.
A teljes projekt forráskódjai kérésre elérhetőek a szecsi.elizabet@gmail.com e-mail címen.*
