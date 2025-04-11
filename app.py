import streamlit as st
import joblib
import pandas as pd

# Load the trained model pipeline
model = joblib.load('cardio_model.pkl')

st.set_page_config(page_title="Cardio Risk Predictor", page_icon="🫀")

st.title("🫀 Cardiovascular Disease Risk Predictor")
st.markdown("This app predicts the risk of cardiovascular disease using a logistic regression model based on clinical data.")

with st.form("prediction_form"):
    age = st.number_input("Age", min_value=1.0, max_value=120.0, value=59.0)
    sex = st.selectbox("Sex", options=["Male", "Female"])
    cp = st.selectbox("Chest Pain Type (1–4)", options=[1, 2, 3, 4])
    trestbps = st.number_input("Resting Blood Pressure", min_value=80.0, max_value=200.0, value=138.0)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100.0, max_value=600.0, value=271.0)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=["Yes", "No"])
    restecg = st.selectbox("Resting ECG Results", options=[0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved", min_value=60.0, max_value=250.0, value=182.0)
    exang = st.selectbox("Exercise-Induced Angina", options=["Yes", "No"])
    oldpeak = st.number_input("ST Depression", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
    slope = st.selectbox("Slope of ST Segment", options=[0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (0–3)", options=[0, 1, 2, 3])
    thal = st.selectbox("Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect)", options=[1, 2, 3])

    submitted = st.form_submit_button("Predict Risk")

if submitted:
    # Encode categorical values
    sex_val = 1.0 if sex == "Male" else 0.0
    fbs_val = 1.0 if fbs == "Yes" else 0.0
    exang_val = 1.0 if exang == "Yes" else 0.0

    input_data = pd.DataFrame([{
        'age': age,
        'sex': sex_val,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs_val,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang_val,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    risk_level = 'High Risk' if probability > 0.7 else 'Medium Risk' if probability > 0.3 else 'Low Risk'

    st.markdown(f"### 🧪 Prediction: {'Positive' if prediction == 1 else 'Negative'}")
    st.markdown(f"### 🔢 Probability: `{probability:.2f}`")
    st.markdown(f"### 🚦 Risk Level: **{risk_level}**")
