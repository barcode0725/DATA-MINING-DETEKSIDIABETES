import pickle
import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        return None
    height_meters = height / 100
    bmi = weight / (height_meters ** 2)
    return bmi

#read model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#title web
st.title('Data Mining Prediksi Diabetes')

# Input for BMI calculation
st.header('Kalkulator BMI')
weight = st.number_input('Berat (kg)', min_value=0, step=1)
height = st.number_input('Tinggi (cm)', min_value=0, step=1)
calculate_bmi_button = st.button('Hitung BMI')

calculated_bmi = None
if calculate_bmi_button:
    calculated_bmi = calculate_bmi(weight, height)
    if calculated_bmi is not None:
        st.success(f'BMI Anda adalah: {calculated_bmi:.2f}')
    else:
        st.warning('Mohon masukkan berat dan tinggi yang valid.')

#title web
st.title('Data Mining Prediksi Diabetes')

#input
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('input nilai Pregnancies',)
    Glucose = st.text_input('input nilai Glucose')
    BloodPressure = st.text_input('input nilai BloodPressure')
    SkinThickness = st.text_input('input nilai SkinThickness')

with col2:
    Insulin = st.text_input('input nilai Insulin')
    BMI = st.text_input('input nilai BMI')
    DiabetesPedigreeFunction = st.text_input('input nilai DiabetesPedigreeFunction')
    Age = st.selectbox('Pilih umur', list(range(1, 101)))

#prediksi
diabetes_predict = ''
if st.button('test prediksi diabetes'):
    # Memeriksa apakah semua input telah diisi
    if (Pregnancies and Glucose and BloodPressure and SkinThickness and
        Insulin and BMI and DiabetesPedigreeFunction and Age):
        
        diabetes_predict = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,SkinThickness, Insulin, BMI,DiabetesPedigreeFunction, Age]])

        if diabetes_predict[0] == 1:
            diabetes_predict = 'diabetes'
        else:
            diabetes_predict = 'no diabetes'

        st.success(diabetes_predict)
    else:
        st.warning('Silahkan lengkapi semua data sebelum melakukan prediksi.')
