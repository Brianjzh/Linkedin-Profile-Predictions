# LinkedIn User Predictor App

## About
This is a Streamlit-based web application that predicts whether a person is a LinkedIn user based on their demographic and socioeconomic attributes. The app uses a pre-trained logistic regression model to make predictions and provides the probability of being a LinkedIn user.

---

## Features
- **Input Parameters**:
  - Age
  - Parental Status (`0` = No, `1` = Yes)
  - Income (Scale `1-10`)
  - Education Level (Scale `1-10`)
  - Marital Status (`0` = No, `1` = Yes)
  - Gender (`0` = Female, `1` = Male)
- **Prediction**:
  - Determines whether the user is a LinkedIn user or not.
  - Outputs the probability of being a LinkedIn user.

---

## Requirements
- **Programming Language**: Python
- **Dependencies**:
  - `streamlit`
  - `pandas`
  - `pickle`
  - `scikit-learn` (for model training, if needed)

