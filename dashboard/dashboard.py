import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Memuat data
day_df = pd.read_csv('/content/all_data (1).csv')

# Judul aplikasi
st.title("Analisis Penyewaan Sepeda Berdasarkan Cuaca dan Tahun 2012")

# Menghitung total jumlah penyewa per cuaca
day_df['total_all_sewa'] = day_df['casual'] + day_df['registered']
sewa_by_weathersit = day_df.groupby('weathersit')['total_all_sewa'].sum()

# Menghitung persentase penyewa per cuaca
percent_by_weathersit = (sewa_by_weathersit / day_df['total_all_sewa'].sum()) * 100

# Pertanyaan 1: Seberapa besar persentase pengaruh kondisi cuaca terhadap jumlah customer?
st.header("1. Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda")
st.write("Berikut adalah persentase pengaruh kondisi cuaca terhadap jumlah penyewa sepeda:")

# Membuat pie chart dengan matplotlib
fig1, ax1 = plt.subplots(figsize=(6, 6))
ax1.pie(percent_by_weathersit, labels=sewa_by_weathersit.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
plt.title('Persentase Pengaruh Kondisi Cuaca Terhadap Jumlah Penyewa Sepeda')

# Tampilkan pie chart di Streamlit
st.pyplot(fig1)

# Pertanyaan 2: Pola penyewaan sepeda di tahun 2012
st.header("2. Pola Penyewaan Sepeda di Tahun 2012 (Casual vs Registered)")

# Mengatur kolom month agar terurut
day_df['month'] = pd.Categorical(
    day_df['month'],
    categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    ordered=True
)

# Menghitung total sewa per bulan untuk casual dan registered
monthly_sewa = day_df.groupby('month')[['casual', 'registered']].sum()

# Menampilkan data di streamlit
st.write("Berikut adalah data penyewaan per bulan di tahun 2012:")
st.dataframe(monthly_sewa)

# Membuat line plot untuk customer casual dan registered dalam satu grafik
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(monthly_sewa.index, monthly_sewa['casual'], label='Casual', marker='o')
ax2.plot(monthly_sewa.index, monthly_sewa['registered'], label='Registered', marker='o')
ax2.set_xlabel('Month')
ax2.set_ylabel('Jumlah Penyewaan')
ax2.set_title('Pola Penyewaan Sepeda di Tahun 2012')
ax2.legend()

# Tampilkan line plot di Streamlit
st.pyplot(fig2)
