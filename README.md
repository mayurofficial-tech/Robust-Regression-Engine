<p align="center">
  <img src="assets/house_header.svg" alt="House Price Prediction - Robust Regression Engine" width="100%" />
</p>

<p align="center">
  <a href="https://robust-regression-engine-ml-project.streamlit.app/"><b>🏡 &nbsp;VIEW THE LIVE LISTING → Try the App</b></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
</p>

---

## 🏷️ PROPERTY LISTING

```text
╔══════════════════════════════════════════════════════╗
║   🏠  ROBUST REGRESSION ENGINE                       ║
╠══════════════════════════════════════════════════════╣
║   Type        :  Machine Learning · Regression       ║
║   Estimates   :  House price in INR                  ║
║   Target      :  house_price_inr                     ║
║   Inputs      :  9 property features                 ║
║   Models      :  6 algorithms compared               ║
║   Status      :  ✅ Deployed on Streamlit            ║
╚══════════════════════════════════════════════════════╝
```

---

## 📝 DESCRIPTION

The **Robust Regression Engine** predicts house prices in INR from property-related features. It compares multiple regression models, applies hyperparameter tuning and cross-validation, picks the best performer, and serves it through an interactive **Streamlit** web app.

> 🎯 **Goal:** Build and deploy a machine learning model that estimates house prices based on property characteristics.

---

## 🛋️ PROPERTY SPECS (Input Features)

| | Feature | What it describes |
|:-:|---|---|
| 📐 | `area_sqft` | Size of the property |
| 🛏️ | `bedrooms` | Number of bedrooms |
| 🛁 | `bathrooms` | Number of bathrooms |
| 📍 | `location_score` | How good the location is |
| 🕰️ | `property_age` | Age of the property |
| 🏙️ | `distance_city_km` | Distance from the city |
| 🏫 | `near_school` | Is a school nearby? |
| 🚇 | `near_metro` | Is a metro nearby? |
| 🚨 | `crime_rate_index` | Crime level of the area |

**💰 Price tag (target):** `house_price_inr`

---

## 🧑‍⚖️ THE APPRAISERS (Models Compared)

Six different "valuers" were asked to price the same houses:

| Appraiser | Family |
|---|---|
| Ridge Regression | Linear (regularised) |
| Lasso Regression | Linear (regularised) |
| Decision Tree Regressor | Tree-based |
| Random Forest Regressor | Tree-based (ensemble) |
| Linear SVR | Support Vector |
| RBF SVR | Support Vector |

---

## 🧭 HOW THE VALUATION WORKS

```text
   🗂️  Raw housing data
        ↓
   🧹  Preprocessing & feature preparation
        ↓
   🤖  Train 6 regression models
        ↓
   ⚙️  Hyperparameter tuning + cross-validation
        ↓
   📈  Evaluate every model using RMSE
        ↓
   🏆  Select the best-performing model
        ↓
   💾  Export with Joblib
        ↓
   🌐  Serve it in a Streamlit app
```

---

## ✨ HIGHLIGHTS

- 📊 Data preprocessing and feature preparation
- 🤖 Comparison of multiple regression algorithms
- ⚙️ Hyperparameter tuning and cross-validation
- 📈 Model evaluation using RMSE
- 🏆 Best model selection
- 🌐 Interactive Streamlit web application
- 💾 Model export using Joblib

---

## 🧰 TOOLBOX

`Python` · `Pandas` · `NumPy` · `Scikit-learn` · `Matplotlib` · `Seaborn` · `Joblib` · `Streamlit` · `Jupyter Notebook`

---

## 🚪 TAKE A TOUR (Run Locally)

```bash
pip install -r requirements.txt
streamlit run app.py
```

Or skip the setup and **[open the live app](https://robust-regression-engine-ml-project.streamlit.app/)**.

---

## 🗺️ FLOOR PLAN (Project Structure)

```text
🏠 robust_regression_engine/
 ├─ 📄 app.py                          Streamlit web app
 ├─ 📄 requirements.txt                Dependencies
 ├─ 📄 README.md
 ├─ 📁 Data/                           Dataset
 ├─ 📁 models/                         Saved model (Joblib)
 ├─ 📁 outputs/                        Results and charts
 ├─ 📁 assets/                         house_header.svg
 └─ 📓 robust_regression_engine (1).ipynb
```

---

<p align="center">
  <b>🔑 Listed by Mayur Makwana</b><br>
  <sub>Data Analyst · Machine Learning Enthusiast</sub>
</p>
