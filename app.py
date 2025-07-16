import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("salary_model.pkl")

st.title("💼 Employee Salary Prediction")
st.write("Enter employee details to predict if salary is >50K or <=50K.")

# Form fields
age = st.number_input("Age", 18, 100, step=1)
workclass = st.selectbox("Workclass", ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov',
                                       'Local-gov', 'State-gov', 'Without-pay'])
education = st.selectbox("Education", ['10th', '11th', 'HS-grad', 'Some-college', 'Bachelors', 'Masters'])
marital = st.selectbox("Marital Status", ['Never-married', 'Married-civ-spouse', 'Divorced', 'Separated'])
occupation = st.selectbox("Occupation", ['Tech-support', 'Craft-repair', 'Sales', 'Exec-managerial',
                                         'Handlers-cleaners', 'Machine-op-inspct', 'Other-service', 'Prof-specialty'])
relationship = st.selectbox("Relationship", ['Husband', 'Not-in-family', 'Own-child', 'Unmarried'])
race = st.selectbox("Race", ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'])
gender = st.selectbox("Gender", ['Male', 'Female'])
hours = st.slider("Hours per week", 1, 100, 40)

# Encoding manually (match your label encodings)
gender = 1 if gender == 'Male' else 0
race_map = {'White': 4, 'Black': 2, 'Asian-Pac-Islander': 1, 'Amer-Indian-Eskimo': 0, 'Other': 3}
race = race_map[race]

# Fake encoded values (You’ll replace these with real ones from your training)
workclass = 3
education = 5
marital = 1
occupation = 2
relationship = 1

# Prediction button
if st.button("Predict Salary Range"):
    input_data = np.array([[age, workclass, 0, education, 0, marital, occupation, relationship,
                            race, gender, 0, 0, hours, 0]])  # All encoded values
    result = model.predict(input_data)

    if result[0] == 1:
        st.success("✅ The employee is likely to earn *more than 50K* 💰")
    else:
        st.warning("⚠ The employee is likely to earn **less than or equal to 50K**")