import streamlit as st
from PIL import Image

image = Image.open("riskmodel.png")


def app():
    st.title("Home")

    st.header(
        "Pengolahan Data Covid 19 Data Rekapitulasi and Prediction - Study Case DKI Jakarta"
    )

    st.subheader("Disclaimer")

    st.write(
        """
    1. Website ini dibuat untuk keperluan latihan pengolahan data menggunakan bahasa pemrograman Python dan tidak diperuntukan sebagai rujukan dalam studi formal ataupun pembuatan kebijakan.
    2. Sumber dataset ada https://corona.jakarta.go.id/id dengan sedikit penyesuaian.
    3. Model perhitungan Konsekuensi, Probabilitas Kegagalan adalah asumsi personal untuk tujuan pembelajaran.
    """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Tentang Web")
        with st.expander(""):
            st.write(
                """
            Web ini dibuat dalam bahasa pemrograman Python dengan beberapa library seperti Pandas, Scikit-Learn dan Streamlit.

            Ada dua modul utama pada website ini, modul pertama adalah modul untuk menampilkan data-data yang didapat dalam bentuk grafik menggunakan library matplotlib dan seaborn. Modul berikutnya adalah modul prediksi yang dibuat menggunakan scikit-learn berdasarkan Supervised Learning. Ada dua metoda yang digunakan yaitu metoda regresi dan klasifikasi.
            """
            )

    with col2:
        st.subheader("Konsep Risiko")
        with st.expander(""):
            st.write(
                """
            Konsep penilaian berbasis risiko umum digunakan pada industri untuk menilai kondisi ataupun kelayakan sebuah system ataupun peralatan. Risiko adalah perkalian atara Probabilitas Kegagalan dan Konsekuensi kegagalan.

            Probabilitas kegagalan dinilai berdasarkan nilai positivity rate dan jumlah positive case number. Sedangkan konsekuensi dihitung berdasarkan jumlah kematian, jumlah pasien dirawat dan pasien isolasi mandiri.

            Risk (R) = Probability of Failure (PoF) x Consequence of Failure (CoF)

            """
            )

    st.image(image, caption="3 x 3 Risk Model Assumption")

    st.subheader("Referensi")
    with st.expander("Referensi"):
        st.write(
            """
            1. Streamlit multi-page app menggunakan [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework dikembangkan oleh [Praneel Nihar](https://medium.com/@u.praneel.nihar). Lampiran [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
        """
        )
