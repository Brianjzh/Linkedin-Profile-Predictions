import streamlit as st
import pandas as pd
import pickle

# Load the saved logistic regression model
with open('log_regression.pkl', 'rb') as file:
    lr = pickle.load(file)

# Define the prediction function
def predict_linkedin_with_prob(age, parent, income, education, married, gender):
    input_data = pd.DataFrame({
        'income': [income],
        'education': [education],
        'parent': [parent],
        'married': [married],
        'gender': [gender],
        'age': [age]
    })
    prediction = lr.predict(input_data)
    probs = lr.predict_proba(input_data)[0][1]
    if prediction[0] == 1:
        return "linkedin user", probs
    else:
        return "not a linkedin user", probs

# Streamlit UI
st.title('LinkedIn User Predictor')
st.markdown("This app predicts whether a person is a LinkedIn user based on their attributes.")

with st.form('user_input'):
    age = st.number_input('Age', min_value=0, max_value=100, value=25, step=1)
    parent = st.number_input('Parent (0 or 1)', min_value=0, max_value=1, value=0, step=1)
    income = st.number_input('Income (scale 1-10)', min_value=1, max_value=10, value=5, step=1)
    education = st.number_input('Education (scale 1-10)', min_value=1, max_value=10, value=7, step=1)
    married = st.number_input('Married (0 or 1)', min_value=0, max_value=1, value=0, step=1)
    gender = st.number_input('Gender (0 = Female, 1 = Male)', min_value=0, max_value=1, value=1, step=1)
    submit_button = st.form_submit_button('Predict')

if submit_button:
    prediction, probability = predict_linkedin_with_prob(age, parent, income, education, married, gender)
    st.write(f"Prediction: {prediction}")
    st.write(f"Probability of being a LinkedIn user: {probability:.2f}")
