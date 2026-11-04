# `dynamic_markowitz_page.py` – Dinamikus XGBoost + Markowitz Streamlit Nézet

Ez a felületi modul jeleníti meg az XGBoost predikciókra és korlátozott Markowitz-optimalizálásra épülő dinamikus portfólió eredményeit.

---

### 1. Módszertani Összefoglaló és KPI-k (`render_dynamic_markowitz_page`)
* Röviden ismerteti az intézményi szintű megközelítést (Walk-Forward ML, PIT tagság, 2%–25% súlykorlátok).
* Megjeleníti a kezdőtőkét, végső egyenleget és a teljes kumulált hozamot.

### 2. Teljes Portfóliógörbe és Újrasúlyozási Jelölők
* Interaktív Plotly grafikonon ábrázolja a portfólió percalapú értékváltozását.
* Függőleges szaggatott vonalakkal jelöli a havi újrasúlyozási (rebalance) időpontokat.

### 3. Markowitz Súlyozás Vizualizációja
* Oszlopdiagramon mutatja be az adott hónapban allokált részvények súlyait a 2%-os minimum és 25%-os maximum korlátok mentén.
* Színátmenetes (background gradient) táblázatban jeleníti meg az XGBoost jóslatokat és a tényleges hozamokat.
