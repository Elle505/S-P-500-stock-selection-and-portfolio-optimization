# `diagnostic_metrics.py` – Portfólió Diagnosztika és Bias Detektor


Ez a diagnosztikai szkript ellenőrzi a dinamikus XGBoost + Markowitz modell működését. 
Számolja a kockázati mutatókat és automatikusan kiszűri a túlillesztésre vagy jövőbelátásra utaló jeleket.

---

### 1. Adatok Betöltése és Összehasonlítása (`run_diagnostic()`)
* Betölti a dinamikus Markowitz portfóliógörbét és összekapcsolja a az egyenlő súlyozású XGBoost-al.
* Napi hozamokat számol a perces adatok záróértékeiből.

### 2. Hozam- és Kockázati Statisztikák Számítása
* Kiszámítja a kumulált hozamot, az évesített volatilitást, a Sharpe-rátát és a maximális visszaesést.
* Kovariancia alapján meghatározza a piaci kitettséget (Béta / $\beta$) és a többlethozamot (Alpha / $\alpha$).

### 3. Automatizált Overfitting & Look-Ahead Bias Ellenőrzés
* **Béta ellenőrzés:** Jelez, ha a piaci kitettség extrém magas.
* **Alpha ellenőrzés:** Jelez, ha a többlethozam gyanúsan magas, ami adatszivárgásra utalhat.
* **Drawdown ellenőrzés:** Figyelmeztet, ha a visszaesés $0\%$ körüli, mert az a jövőbelátás biztos jele.
