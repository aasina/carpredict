import streamlit as st

def app():
    st.title('Home')

    st.write('## Pengolahan Data Covid 19 Data Rekapitulasi and Prediction - Study Case DKI Jakarta')

    st.write('')
    st.write("""
    ### Pertama-tama, disclaimer dulu ya.. :D

    Website ini dibuat untuk keperluan latihan pengolahan data menggunakan bahasa pemrograman Python dan tidak diperuntukan sebagai rujukan dalam studi formal ataupun pembuatan kebijakan.
    
    ### Ada apa di web ini?

    Web ini dibuat dalam bahasa pemrograman Python dengan beberapa library seperti Pandas, Scikit-Learn dan Streamlit.

    Ada dua modul utama pada website ini, modul pertama adalah modul untuk menampilkan data-data yang didapat dalam bentuk grafik menggunakan library matplotlib dan seaborn.
    Modul berikutnya adalah modul prediksi yang dibuat menggunakan scikit-learn berdasarkan Supervised Learning. Ada dua metoda yang digunakan yaitu metoda regresi dan klasifikasi.


    ### Referensi
    1. Streamlit multi-page app menggunakan [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework dikembangkan oleh [Praneel Nihar](https://medium.com/@u.praneel.nihar). Lampiran [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
    """)
