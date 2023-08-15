import pickle
import streamlit as st

#read model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#title web
st.title('Data Mining Prediksi Diabetes')

#input
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('input nilai Pregnancies')
    Glucose = st.text_input('input nilai Glucose')
    BloodPressure = st.text_input('input nilai BloodPressure')
    SkinThickness = st.text_input('input nilai SkinThickness')

with col2:
    Insulin = st.text_input('input nilai Insulin')
    BMI = st.text_input('input nilai BMI')
    DiabetesPedigreeFunction = st.text_input('input nilai DiabetesPedigreeFunction')
    Age = st.text_input('input nilai Age')

#prediksi
diabetes_predict = ''
if st.button('test prediksi diabetes'):
    # Memeriksa apakah semua input telah diisi
    if (Pregnancies and Glucose and BloodPressure and SkinThickness and
        Insulin and BMI and DiabetesPedigreeFunction and Age):
        
        diabetes_predict = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,
                                                     SkinThickness, Insulin, BMI,
                                                     DiabetesPedigreeFunction, Age]])

        if diabetes_predict[0] == 1:
            diabetes_predict = 'diabetes'
        else:
            diabetes_predict = 'no diabetes'

        st.success(diabetes_predict)
    else:
        st.warning('Silahkan lengkapi semua data sebelum melakukan prediksi.')
