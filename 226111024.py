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
        elif prediction[0] == 6:import pickle
import streamlit as st
import numpy as np

# Memuat model (menggunakan with untuk pengelolaan file yang lebih baik)
with open('baju_model.sav', 'rb') as model_file:
    weather_model = pickle.load(model_file)

# --- Tampilan ---

# Judul dengan Markdown untuk sedikit styling
st.markdown("<h1 style='text-align: center;'>Prediksi Ukuran Baju</h1>", unsafe_allow_html=True)

# Input data dengan placeholder yang lebih informatif
weight = st.number_input('Berat Badan (kg)', min_value=0.0, value=70.0, step=0.1)  
age = st.number_input('Usia (tahun)', min_value=0, value=30, step=1)  
height = st.number_input('Tinggi Badan (cm)', min_value=0.0, value=170.0, step=0.1)  

# Tombol Prediksi dengan styling
predict_button = st.button("Prediksi Ukuran", key="predict")

# --- Logika Prediksi ---

if predict_button:
    try:
        # Konversi input menjadi numerik (tidak perlu jika sudah number_input)
        inputs = np.array([[weight, age, height]])  

        # Prediksi
        prediction = weather_model.predict(inputs)

        # Mapping hasil prediksi ke ukuran baju
        size_mapping = {
            1: 'XXS', 2: 'XS', 3: 'S', 4: 'M', 5: 'L', 6: 'XL', 7: 'XXL', 8: 'XXXL'
        }
        predicted_size = size_mapping.get(prediction[0], "Ukuran tidak valid")

        # Menampilkan hasil dengan Markdown untuk styling yang lebih baik
        st.markdown(f"<h2 style='text-align: center;'>Ukuran Baju Anda: {predicted_size}</h2>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")

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
        st.error(f"Terjadi kesalahan: {e}")
