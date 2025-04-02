import streamlit as st
import joblib
st.title('Loan Approval Process')
model=joblib.load('loan.joblib')
gender=st.number_input('Enter gender Male:0 Female:1')
married=st.number_input('Enter married status Married:1 Unmarried:0')
income=st.number_input('Enter your income in thousands')
la=st.number_input('Enter loan amount')
if st.button('predict approval'):
    prediction=model.predict([[gender,married,income,la]])
    if prediction=='Y':
        st.text('Loan approved')
    else:
        st.text('Loan rejected')
