# `summary_page.py` – Portfólió Stratégiák Összesítő és Összehasonlító Nézete

Ez a felületi modul végzi a projektben kifejlesztett mind a 4 portfólió-építési stratégia közvetlen, egymás melletti teljesítmény-összehasonlítását.

---

### 1. Adatbányászat és KPI Kártyák (`get_summary_stats()`)
* Automatikusan beolvassa mind a 4 modell kimeneti adatait (CAPM, XGBoost EW, XGBoost Markowitz, Oracle).
* Négy egymás melletti kártyán mutatja be a végső portfólióértékeket és a elért kumulált hozamokat.

### 2. Reális Stratégiák Grafikonja (1. Diagram)
* Diagramon hasonlítja össze a 3 valóban kereskedhető modell teljesítményét:
  * **XGBoost Egyenlő Súlyozás (+32.05%)**
  * **Dynamic XGBoost + Markowitz (+21.24%)**
  * **CAPM + Markowitz Baseline (+1.08%)**

### 3. Teljes Összehasonlítás az Oracle Referenciával (2. Diagram)
* Egy második diagramon a reális modellek görbéi mellett feltünteti az idealizált Oracle modellt is (+1250.99%), szemléltetve az elméleti maximális hozampotenciált.
