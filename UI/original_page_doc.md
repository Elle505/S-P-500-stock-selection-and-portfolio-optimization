# `original_page.py` – Oracle Benchmark Streamlit Megjelenítő Nézete

# Az oracle modell csak kiindulási idealizált modellként készült, pusztán a kiváncsiság vezérelte, hogy mi is lenne ha a modellek 100%-os előrejelzésekre lennének képesek 

Ez a modul vizualizálja az idealizált Oracle referencia-modell teljesítményét a Streamlit felületen.

---

### 1. Kezdő KPI Mutatók és Teljes Portfóliógörbe (`build_full_portfolio_chart()`)
* Megjeleníti a kezdőtőkét (100 000 Ft), az Oracle zárótőkét és az Equal Weight referencia zárótőkét.
* Interaktív Plotly grafikonon ábrázolja a percalapú portfólióértéket a 12 hónapos tesztidőszak alatt.

### 2. Allokációs Hőtérkép (Allocation Heatmap) (`build_allocation_heatmap()`)
* Egy mátrixos térképen mutatja be, hogy a 11 GICS szektor aktuális győzteseire hónapról hónapra mekkora Markowitz-súlyt választott az Oracle modell.

### 3. Havi Részletes Elemző Nézet
* A felhasználó által kiválasztott hónapra bemutatja az összes S&P 500 részvény hozameloszlását és a szektorgyőzteseket.
* Táblázatban és oszlopdiagramon jeleníti meg a szektorgyőztesek pontos súlyait és tényleges havi hozamait.
