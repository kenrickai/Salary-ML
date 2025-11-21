import streamlit as st 
import joblib
import numpy as np

st.title("Salary Prediction Model")

st.divider()


st.write("With this app, you can get an estimations for the salaries of the company employees based on their experience.")

years = st.number_input("Years of Experience", value=1.0, step=1.0, min_value = 0.0)
jobrate = st.number_input("Job Rate",value=3.5, step = 0.5, min_value = 0.0)

X = [years, jobrate]

model = joblib.load("linearmodel.pkl")

st.divider()

predict = st.button("Predict Salary")

st.divider()

if predict:

    st.balloons()

    X1 = np.array([X])

    prediction = model.predict(X1)[0]

    st.success(f"The estimated salary is **${prediction:,.2f}**")




else:
    "Please press the button to make prediction"