# Project Analisis Data Python
Proyek ini bertujuan untuk melakukan analisis data penyewaan sepeda (Bike Sharing Dataset) berdasarkan kondisi cuaca menggunakan Streamlit untuk membangun dashboard interaktif.

## 1. Setup environment:
####  a. Buat virtual environment
       python -m venv venv
####  b. Aktifkan virtual environment:
       .\venv\Scripts\activate
####  c. Menginstal Library Dependensi
#####  -- 1. Pastikan `pip` telah diupgrade
        pip install --upgrade pip
##### -- 2. Install semua library
        pip install pandas seaborn matplotlib streamlit
        
## 2. Menjalankan Dashboard
####  a. Jalankan aplikasi Streamlit
        streamlit run dashboard/app.py
Ini akan menjalankan aplikasi di localhost dan memberikan URL seperti `http://localhost:8501/`. Buka browser dan masukkan URL tersebut untuk melihat dashboard.

## 3. Struktur Proyek
    Projek-Analisis-Data-Python-master/
    ├── dashboard
        ├── dashboard.py
        └── all_data (1).csv
    ├── data
        ├── Readme.txt
        ├── day.csv
        └── hour.csv
    ├── README.md
    ├── notebook.ipynb
    ├── requirements.txt
    ├── url.txt

        
