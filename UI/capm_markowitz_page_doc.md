# `capm_markowitz_page.py` – CAPM + Markowitz Streamlit Nézet

Ez a fájl felelős a klasszikus CAPM + Markowitz modell eredményeinek megjelenítéséért a Streamlit webes felületen.

---

### 1. Adatbetöltés és KPI Mutatók (`render_capm_markowitz_page()`)
* Beolvassa a `capm_markowitz/data/` mappából a generált Parquet fájlokat.
* Megjeleníti a fő teljesítménymutatókat: Kezdőtőke, Végső Portfólió Érték és Kumulált Hozam.

### 2. Interaktív Portfóliógörbe (Plotly)
* A perces adatokat napi záróértékekre aggregálja a zaj csökkentése érdekében.
* Plotly grafikonon ábrázolja a tőkeérték alakulását a 100 000 Ft-os referenciavonalhoz képest.

### 3. Havi Szektorgyőztesek és Mutatók Táblázata
* Hónapválasztó drop-down menüt biztosít a felhasználónak.
* Táblázatban mutatja be a kiválasztott 11 részvény Béta ($\beta$), Alpha ($\alpha$), Várható Hozam, Tényleges Hozam és Markowitz súly értékeit.
