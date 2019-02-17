# AirbnBoost
[AirbnBoost](http://www.airbnboost.xyz) is an online platform powered by machine learning that enables users to make faster and better informed Airbnb decisions.

## Features
- See how each listing is priced compared to similar listings based on AirbnBoost's price prediction algorithm. __Find great deals__ based on the deviation between the pricing algorithm prediction and the actual listing price.
- Select listings that __match your preferences__ without the need to read through full descriptions. 
- __Understand the urban environment__ surrounding a listing, such as proximity to subway or neighborhood noise levels.


## Tutorial

Here is a step-by-step navigation at AirbnBoost's UI.

![](app/templates/airbnBoost_gif.gif)


## Implementation

The implementation has three main components:

- `01 - data_preprocessing.ipynb`, a notebook that geolocates and spatially joins Airbnb listing data with urban data sets and processes them before they are used as inputs in the modeling part.
- `02 - data_modeling.ipynb`, a notebook that trains the two models behind AirbnBoost. An LDA model extracts the topics from the listing descriptions. XGBoost is the algorithm behind the pricing model.
- `app.py`, is a Flask web app deployed on Heroku cloud.


_Copyright &copy; 2019 Sokratis Papadopoulos. All rights reserved._

