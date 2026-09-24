# House Price Prediction --- Robust Regression Engine

A machine learning project for predicting house prices using multiple
regression models and a Streamlit web application.

## Project Overview

This project trains and compares several regression algorithms for
predicting:

-   **Target variable:** `house_price_inr`
-   **Dataset:** `Data/HousePrice_Dataset.csv`
-   **Application:** Streamlit
-   **Saved model format:** Joblib

The training notebook includes preprocessing, model training,
hyperparameter tuning, cross-validation, model comparison, and
prediction analysis.

## Features Used

The trained model uses the following input features:

1.  `area_sqft`
2.  `bedrooms`
3.  `bathrooms`
4.  `location_score`
5.  `property_age`
6.  `distance_city_km`
7.  `near_school`
8.  `near_metro`
9.  `crime_rate_index`

The columns `property_id` and `sale_date` are excluded from the model,
and `house_price_inr` is used as the target variable.

## Models Compared

The notebook compares the following regression models:

-   Ridge Regression
-   Lasso Regression
-   Decision Tree Regressor
-   Random Forest Regressor
-   Linear SVR
-   RBF SVR

The best-performing model is selected based on test RMSE.

## Project Structure

``` text
robust_regression_engine/
│
├── app.py
├── requirements.txt
├── README.md
│
├── Data/
│   └── HousePrice_Dataset.csv
│
├── models/
│   └── best_model.joblib
│
├── outputs/
│   ├── model_comparison.csv
│   └── actual_vs_predicted.png
│
└── robust_regression_engine (1).ipynb
```

## Installation

### 1. Create or activate a Python environment

Using Anaconda:

``` bash
conda activate base
```

Or activate your own project environment.

### 2. Install dependencies

Run the following command inside the project folder:

``` bash
pip install -r requirements.txt
```

## Train and Export the Model

Open the Jupyter Notebook:

``` bash
jupyter notebook
```

Run the notebook cells to:

1.  Load the dataset.
2.  Prepare features and target.
3.  Split the data into training and testing sets.
4.  Apply preprocessing.
5.  Train and tune the regression models.
6.  Compare model performance.
7.  Select the best model.
8.  Export the selected model.

The exported model should be saved at:

``` text
models/best_model.joblib
```

Example export code:

``` python
import joblib
from pathlib import Path

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)

best_model_name = all_results.iloc[0]["model"]
best_estimator = dict(all_estimators)[best_model_name]

joblib.dump(
    best_estimator,
    MODEL_DIR / "best_model.joblib"
)

print("Best model:", best_model_name)
print("Model saved successfully!")
```

## Run the Streamlit Application

Open a terminal in the project directory and run:

``` bash
streamlit run app.py
```

The application will normally open at:

``` text
http://localhost:8501
```

The Streamlit app accepts property details and displays the predicted
house price.

## Input Fields in the App

The application accepts:

-   Area in square feet
-   Number of bedrooms
-   Number of bathrooms
-   Location score
-   Property age
-   Distance from the city in kilometers
-   Whether a school is nearby
-   Whether a metro station is nearby
-   Crime rate index

The input column names must match the feature names used during model
training.

## Important Notes

-   Run the model export code before launching the Streamlit app.
-   Keep `best_model.joblib` inside the `models` folder.
-   Do not change the feature names in `app.py` unless the training
    pipeline is also updated.
-   The app loads the trained model and does not retrain the model each
    time it starts.
-   If the model file is missing, check the `models` folder and the file
    path.
-   If a column mismatch error appears, compare the input columns in
    `app.py` with the training features in the notebook.

## Troubleshooting

### Streamlit command not found

Install Streamlit:

``` bash
pip install streamlit
```

### Model file not found

Confirm that this file exists:

``` text
models/best_model.joblib
```

### Missing package error

Install all dependencies:

``` bash
pip install -r requirements.txt
```

### Missing columns error

Ensure that the input DataFrame contains all nine model features:

``` python
[
    "area_sqft",
    "bedrooms",
    "bathrooms",
    "location_score",
    "property_age",
    "distance_city_km",
    "near_school",
    "near_metro",
    "crime_rate_index"
]
```

## Technologies Used

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Joblib
-   Matplotlib
-   Seaborn
-   Streamlit
-   Jupyter Notebook

## Author

House Price Prediction / Robust Regression Engine Project
