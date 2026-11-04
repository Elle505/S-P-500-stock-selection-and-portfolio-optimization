# S&P 500 Stock Selection and Portfolio Optimization

> 🚧 This repository is currently under development.

## About

This repository contains the documentation and implementation of my BSc tdk project, focusing on machine learning-based stock selection and portfolio optimization using S&P 500 stocks.


## Benchmark Modellek (Reference Models)

A projekt tartalmaz egy idealizált, "Oracle" (perfect foresight) modellt is (`build_original_oracle.py`). 

* **Szerepe:** Elméleti felső korlátot (theoretical upper bound) biztosít a tesztidőszakra. Nem végez valódi előrejelzést, hanem a már megvalósult jövőbeli hozamok alapján állítja össze az optimális portfóliót.
* **Használat:** Kizárólag a gépi tanulási (XGBoost) és a klasszikus pénzügyi (CAPM/Markowitz) modellek elméleti maximális teljesítményviszonyítására szolgál.
