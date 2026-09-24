
import streamlit as st
import pandas as pd
import joblib
import sklearn
import sys

from pathlib import Path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# =========================================================
# MODEL CONFIGURATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "best_model.joblib"

FEATURE_COLUMNS = [
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


# =========================================================
# ENVIRONMENT INFORMATION
# =========================================================

with st.sidebar.expander("Environment Information"):

    st.write("Python Version:")
    st.code(sys.version)

    st.write("Scikit-learn Version:")
    st.code(sklearn.__version__)

    st.write("Joblib Version:")
    st.code(joblib.__version__)

    st.write("Model Path:")
    st.code(str(MODEL_PATH))

    st.write("Model Exists:")
    st.write(MODEL_PATH.exists())


# =========================================================
# MODEL LOADING
# =========================================================

@st.cache_resource
def load_model():

    if not MODEL_PATH.exists():

        raise FileNotFoundError(
            f"Model file not found:\n{MODEL_PATH}\n\n"
            "Please ensure that best_model.joblib exists "
            "inside the models folder."
        )

    try:

        trained_model = joblib.load(MODEL_PATH)

        return trained_model

    except Exception as error:

        raise RuntimeError(
            "The model file exists, but it could not be loaded.\n\n"
            f"Original error: {error}\n\n"
            "This may be caused by a scikit-learn version "
            "compatibility issue. Retrain and export the model "
            "using the same compatible scikit-learn version "
            "used in deployment."
        ) from error


# =========================================================
# APPLICATION HEADER
# =========================================================

st.title("🏠 House Price Prediction")

st.write(
    "Enter the property details below to predict "
    "the estimated house price."
)


# =========================================================
# LOAD TRAINED MODEL
# =========================================================

try:

    model = load_model()

    st.success("Trained model loaded successfully!")

except Exception as error:

    st.error("Unable to load the trained model.")

    st.code(str(error))

    st.warning(
        "Check the Environment Information in the sidebar "
        "and compare the scikit-learn version with your "
        "Jupyter Notebook environment."
    )

    st.stop()


# =========================================================
# INPUT FIELDS
# =========================================================

st.subheader("Property Details")

col1, col2 = st.columns(2)


with col1:

    area_sqft = st.number_input(
        "Area (sqft)",
        min_value=1.0,
        value=1500.0,
        step=50.0
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        value=3,
        step=1
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0,
        value=2,
        step=1
    )

    property_age = st.number_input(
        "Property Age (years)",
        min_value=0,
        value=10,
        step=1
    )

    distance_city_km = st.number_input(
        "Distance from City (km)",
        min_value=0.0,
        value=10.0,
        step=0.5
    )


with col2:

    location_score = st.number_input(
        "Location Score",
        min_value=0.0,
        value=7.0,
        step=0.1
    )

    crime_rate_index = st.number_input(
        "Crime Rate Index",
        min_value=0.0,
        value=5.0,
        step=0.1
    )

    near_school = st.selectbox(
        "Near School",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    near_metro = st.selectbox(
        "Near Metro",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


# =========================================================
# PREDICTION
# =========================================================

st.divider()

if st.button(
    "Predict House Price",
    type="primary",
    use_container_width=True
):

    input_data = pd.DataFrame(
        [[
            area_sqft,
            bedrooms,
            bathrooms,
            location_score,
            property_age,
            distance_city_km,
            near_school,
            near_metro,
            crime_rate_index
        ]],
        columns=FEATURE_COLUMNS
    )

    try:

        # Check whether the model supports predict()
        if not hasattr(model, "predict"):

            raise AttributeError(
                "The loaded object does not have a predict() method."
            )

        # Make prediction
        prediction = model.predict(input_data)[0]

        st.success("Prediction completed successfully!")

        st.metric(
            label="Estimated House Price",
            value=f"₹{prediction:,.2f}"
        )

        with st.expander("View Input Data"):

            st.dataframe(
                input_data,
                use_container_width=True
            )

    except Exception as error:

        st.error("Prediction failed.")

        st.code(str(error))

        st.write("Input columns:")
        st.write(input_data.columns.tolist())

        st.write("Expected feature columns:")
        st.write(FEATURE_COLUMNS)
