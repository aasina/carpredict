import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets


def app():
    #judul
    st.title('Grafik Representasi')

    st.write("Pada halaman ini kita akan menampilkan data terkait dataset yang sudah dipersiapkan.")

    #import dataset
    datacovid = pd.read_csv('datasetcovidsamplejkt.csv')
    
    #show sample dataset
    sample_data = datacovid.sample(5)
    st.write("""
    ### 1. Sample Dataset

    Berikut ini adalah sampel dataset dan nama-nama features nya.""")

    st.dataframe(sample_data)

    #box plot by type of variant
    st.write("""
    ### 2. Boxplot terhadap tipe variant

    """)
    
    fig = sns.boxplot(x="Variant_Suspect", y="JKT_DAILY_DEATH", data=datacovid)
    
    st.pyplot(fig)
