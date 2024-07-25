import pickle
import streamlit as st
import numpy as np

# Membaca model
weather_model = pickle.load(open('baju_model.sav','rb'))

# Judul web
st.title('Prediksi Ukuran Baju')

# Input data dengan contoh angka valid untuk pengujian
weight = st.text_input('weight', '2')
age = st.text_input('age', '120')
height = st.text_input('height', '70')


diabetes_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[float(weight), float(age), float(height)]])
        
        # Lakukan prediksi
        prediction = weather_model.predict(inputs)

        # Memeriksa hasil prediksi
        if prediction[0] == 1:
            size_prediksi_str = 'XXS'
            st.success(size_prediksi_str)
        elif prediction[0] == 2:
            size_prediksi_str = 'S'
            st.success(size_prediksi_str)
        elif prediction[0] == 3:
            size_prediksi_str = 'M'
            st.success(size_prediksi_str)
        elif prediction[0] == 4:
            size_prediksi_str = 'L'
            st.success(size_prediksi_str)
        elif prediction[0] == 5:
            size_prediksi_str = 'XL'
            st.success(size_prediksi_str)
        elif prediction[0] == 6:
            size_prediksi_str = 'XXL'
            st.success(size_prediksi_str)
        elif prediction[0] == 7:
            size_prediksi_str = 'XXXL'
            st.success(size_prediksi_str)
        else:
            st.error("Prediksi ukuran tidak valid.")
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
