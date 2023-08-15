import pickle
import streamlit as st

#read model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#title web
st.title('Data Mining Prediksi Diabetes')
#input
col1,col2= st.columns(2)
with col1:Pregnancies = st.text_input('input nilai Pregnancies')
with col2:Glucose = st.text_input('input nilai Glucose')
with col1:BloodPressure = st.text_input('input nilai BloodPressure')
with col2:SkinThickness = st.text_input('input nilai SkinThickness')
with col1:Insulin = st.text_input('input nilai Insulin')
with col2:BMI = st.text_input('input nilai BMI')
with col1:DiabetesPedigreeFunction = st.text_input('input nilai DiabetesPedigreeFunction')
with col2:Age = st.text_input('input nilai Age')
#prediksi
diabetes_predict = ''
if st.button('test prediksi diabetes'):
    diabetes_predict = diabetes_model.predict([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    if diabetes_predict[0] == 1:
        diabetes_predict = 'diabetes'
    else:
        diabetes_predict = 'no diabetes'

    st.success(diabetes_predict)

