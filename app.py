import streamlit as st
import pickle
import numpy as np

# Load model
data = pickle.load(open("heart_disease.pkl", "rb"))
model = data["model"]
scaler = data.get("scaler", None)  # scaler iruntha use aagum
st.write("Scaler expects:", scaler.n_features_in_)


st.title("❤️ Heart Disease Prediction App")

# Inputs
male = st.selectbox("Gender", ["Female", "Male"])
age = st.number_input("Age", min_value=1, max_value=120, value=30)
educatinal_level = st.selectbox("Educational Level", ["High School", "Bachelor's", "Master's", "PhD"])
currentSmoker = st.selectbox("Current Smoker", ["No", "Yes"])
cigsPerDay = st.number_input("Cigarettes Per Day", min_value=0, value=0)
BPMeds = st.selectbox("BP Medicines", ["No", "Yes"])
prevalentStroke = st.selectbox("Prevalent Stroke", ["No", "Yes"])
prevalentHyp = st.selectbox("Hypertension", ["No", "Yes"])
diabetes = st.selectbox("Diabetes", ["No", "Yes"])
totChol = st.number_input("Total Cholesterol", value=200)
sysBP = st.number_input("Systolic BP", value=120)
diaBP = st.number_input("Diastolic BP", value=80)
BMI = st.number_input("BMI", value=25.0)
heartRate = st.number_input("Heart Rate", value=70)
glucose = st.number_input("Glucose", value=80)

# Prediction
# Prediction
if st.button("Predict"):

    male = 1 if male == "Male" else 0
    currentSmoker = 1 if currentSmoker == "Yes" else 0
    BPMeds = 1 if BPMeds == "Yes" else 0
    prevalentStroke = 1 if prevalentStroke == "Yes" else 0
    prevalentHyp = 1 if prevalentHyp == "Yes" else 0
    diabetes = 1 if diabetes == "Yes" else 0
    education = 0
 
    input_data = np.array([[age, male,
    education,          # 👈 NEW (15th feature)
    currentSmoker,
    cigsPerDay,
    BPMeds,
    prevalentStroke,
    prevalentHyp,
    diabetes,
    totChol,
    sysBP,
    diaBP,
    BMI,
    heartRate,
    glucose
]])

    # model expects 15 features
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)

    st.success(f"Prediction: {prediction[0]}")
