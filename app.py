import streamlit as st
st.title('Loan Approval Process Automation')
model=joblib.load(C:/54A1/loan_data1.joblib')
gender=st.number_input('enter gender male:0 female:1')
married=st.number_input('enter applicant income in thousands')
la=st.number_input(' enter the loan amount in thousands')
if st.button('predict Approval'):
    prediction=model.predict([[gender,married,income,la]])
    if prediction=='y':
        st.text('Loan Approved')
    else:
        st.text('loan Rejected')
