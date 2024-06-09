import warnings
import joblib
import streamlit as st
import pandas as pd

"""
# Diabetes Prediction Model

This model predicts whether or not a female member of the Pima Native American Tribe may have type II diabetes.

### Enter Your Results
"""

def submit_input(X):
  model_filepath = "models/pima_diabetes_model.sav"
  model = joblib.load(open(model_filepath, 'rb'))

  warnings.filterwarnings("ignore", message="X does not have valid feature names.*")
  classification = model.predict(X)[0]

  if classification == 1:
    st.markdown("<h3 style='text-align: center;'>You May Have Diabetes</h3>", unsafe_allow_html=True)
  else:
    st.markdown("<h3 style='text-align: center;'>You May Not Have Diabetes</h3>", unsafe_allow_html=True)

def main():
  name = st.text_input("Name", value=None, placeholder="Enter your name")
  if name is None: return

  st.markdown(f"Hello {name}! Please enter the following information.")
  age = st.number_input(label="Age", value=None, min_value=21, max_value=100, placeholder="Enter your age")
  if age is None: return

  glucose_level = st.number_input("Glucose Level (mmol/L)", value=None, min_value=0, max_value=199, placeholder="Enter your glucose tolerance test result")
  blood_pressure = st.number_input("Blood Pressure (mmHg)", value=None, min_value=0, max_value=150, placeholder="Enter your blood pressure result")
  bmi = st.number_input("BMI", value=None, min_value=0.0, max_value=75.0, placeholder="Enter your BMI")
  diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", value=None, min_value=0.08, max_value=2.4, placeholder="Enter your diabetes pedigree function value")
  num_pregnancies = st.select_slider(label="Number of pregnancies", options=[_ for _ in range(21)])
  # skin_thickness = st.number_input("Triceps Skin Fold Thickness (mm)", value=None, min_value=0.0, placeholder="Enter your triceps skin fold thickness measurement")
  # insulin = st.number_input("Insulin Level", value=None, min_value=0.0, placeholder="Enter your current insulin level")

  input_params = pd.DataFrame({
    "Pregnancies": [num_pregnancies],
    "Glucose": [glucose_level],
    "BloodPressure": [blood_pressure],
    "BMI": [bmi],
    "DiabetesPedigreeFunction": [diabetes_pedigree_function],
    "Age": [age],
    # "SkinThickness": [skin_thickness],
    # "Insulin": [insulin],
  })

  if st.button("Submit"):
    if input_params.isna().any().any():
      st.error("Not all values have been inputted properly.")
    else:
      submit_input(input_params)


if __name__ == "__main__":
  main()
