import streamlit as st

"""
# Diabetes Prediction Model

### Enter Your Results
"""

def main():
  name = st.text_input("Name", value=None, placeholder="Enter your name")
  if name is None: return

  st.markdown(f"Hello {name}! Please enter your the following information.")
  age = st.number_input(label="Age", value=None, min_value=5, max_value=100, placeholder="Enter your age")
  if age is None: return

  glucose_level = st.number_input("Glucose Level (mmol/L)", value=None, placeholder="Enter your glucose tolerance test result")
  blood_pressure = st.number_input("Blood Pressure (mmHg)", value=None, min_value=0.0, placeholder="Enter your blood pressure result")
  skin_thickness = st.number_input("Triceps Skin Fold Thickness (mm)", value=None, min_value=0.0, placeholder="Enter your triceps skin fold thickness measurement")
  insulin = st.number_input("Insulin Level", value=None, min_value=0.0, placeholder="Enter your current insulin level")
  bmi = st.number_input("BMI", value=None, min_value=0.0, placeholder="Enter your BMI")
  diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", value=None, min_value=0.08, max_value=2.4, placeholder="Enter your diabetes pedigree function value")

  num_pregnancies = st.select_slider(label="Number of pregnancies", options=[_ for _ in range(21)])


if __name__ == "__main__":
  main()
