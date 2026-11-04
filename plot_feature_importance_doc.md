# `plot_feature_importance.py` – XGBoost Indikátor-fontosság Vizualizáló

Ez a szkript végzi a 12 teszthónap Walk-Forward XGBoost modelljeinek kiértékelését az indikátorok fontossága alapján, és kirajzolja a Streamlit felületen megjelenő diagramot (`feature_importance.png`).

---

### 1. Átlagos Fontosságok Számítása (`main`)
* Végigmegy a 12 teszthónapon, betölti a tanítóadatokat és lefuttatja az XGBoost modellt.
* Kinyeri az egyes modellek `feature_importances_` értékeit, majd veszi a 12 hónap átlagát a 12 indikátorra.

### 2. Sötét Témájú Grafikon Generálása (Matplotlib)
* Vízszintes oszlopdiagramot (`barh`) rajzol a rendezett fontosságokból, illeszkedve a Streamlit sötét témájához.
* Ráteszi a pontos numerikus értékeket az oszlopok végére.

### 3. Kép Mentése (`feature_importance.png`)
* A képet nagy felbontásban (300 DPI) elmenti a projekt gyökérmappájába, amit a dashboard `app.py` fájlja jelenít meg.
