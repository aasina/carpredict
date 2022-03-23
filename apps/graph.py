import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
from sklearn import datasets

xdate 

def app():
    #judul
    st.title("Dashboard Rekapitulasi Data Covid")

    #import dataset
    datacovid = pd.read_csv('datasetcovidsamplejkt.csv')

    ydayposid = datacovid.ID_DAILY_POSITIVE
    ydayposjkt = datacovid.JKT_DAILY_POSITIVE
    ydaydeathid = datacovid.ID_DAILY_DEATH
    ydaydeathjkt = datacovid.JKT_DAILY_DEATH
    xdaily = datacovid.Tanggal

    with st.container():
        col1, col2 = st.columns([2, 1])

        with col1:
            fig1 = plt.figure()
            plt.scatter(xdaily, ydayposid, "r", label="Positive Harian Indonesia")
            plt.scatter(xdaily, ydayposjkt, "b", label="Positif Harian DKI Jakarta")
            plt.xticks([1, 150, 300, 450, 600, 730], fontsize=6)
            plt.yticks(fontsize=6)
            plt.xlabel("Tanggal")
            plt.ylabel("Jumlah Positif Harian")
            plt.legend(fontsize=8)
            st.pyplot(fig1)

        with col2:
            fig2 = plt.figure()
            plt.plot(xdaily, ydaydeathid, "g", label="Meninggal Harian Indonesia")
            plt.plot(xdaily, ydaydeathjkt, "y", label="Meninggal Harian DKI Jakarta")
            plt.xticks([1, 150, 300, 450, 600, 730], fontsize=6)
            plt.yticks(fontsize=6)
            plt.xlabel("Tanggal")
            plt.ylabel("Jumlah Meninggal Harian")
            plt.legend(fontsize=8)
            st.pyplot(fig2)
    
    #box plot by type of variant
    st.write("""
    ### 2. Boxplot terhadap tipe variant

    """)
    
    fig1 = plt.figure(figsize=(8, 6))
    plt.title("Box Plot Covid Variant di Jakarta")
    sns.boxplot(x="Variant_Suspect", y="JKT_DAILY_DEATH", data=datacovid)
    st.pyplot(fig1)

    #count of calculated risk by type of variant
    st.write("""
    ### 3. Countplot kalkulasi risiko berdasarkan tipe variant

    """)
    fig2 = plt.figure(figsize=(8, 6))
    plt.title("Countplot Kalkukasi Risiko pada tiap Variant")
    sns.countplot(x="Variant_Suspect", hue="Risk_Criteria", data=datacovid)
    st.pyplot(fig2)

    #pair plot of covid JKT

    covid_JKT = datacovid.loc[:,['Variant_Suspect','Day','JKT_DAILY_POSITIVE','JKT_DAILY_DEATH','JKT_DAILY_HOSPITALIZED','JKT_DAILY_POSTRATE','JKT_DAILY_TESTSPECIMENT','Risk','Risk_Criteria']]
    
    st.write("""
    ### 4. Pair Plot terhadap variabel dari data covid 19

    """)
    plt.title("Pairplot C19 di Jakarta")
    fig3 = sns.pairplot(covid_JKT,hue='Variant_Suspect')
    st.pyplot(fig3)

    #prepare data for graph.

    covid_ABG = datacovid.loc[datacovid.Variant_Suspect=='Alpha-Beta-Gamma',['Day','JKT_DAILY_POSITIVE','JKT_DAILY_DEATH','JKT_DAILY_HOSPITALIZED','JKT_DAILY_POSTRATE','JKT_DAILY_TESTSPECIMENT','Risk','Risk_Criteria']]
    covid_Delta = datacovid.loc[datacovid.Variant_Suspect=='Delta',['Day','JKT_DAILY_POSITIVE','JKT_DAILY_DEATH','JKT_DAILY_HOSPITALIZED','JKT_DAILY_POSTRATE','JKT_DAILY_TESTSPECIMENT','Risk','Risk_Criteria']]
    covid_Omicron = datacovid.loc[datacovid.Variant_Suspect=='Omicron',['Day','JKT_DAILY_POSITIVE','JKT_DAILY_DEATH','JKT_DAILY_HOSPITALIZED','JKT_DAILY_POSTRATE','JKT_DAILY_TESTSPECIMENT','Risk','Risk_Criteria']]
    
    #Plot
    y1 = covid_ABG.JKT_DAILY_POSITIVE
    y2 = covid_Delta.JKT_DAILY_POSITIVE
    y3 = covid_Omicron.JKT_DAILY_POSITIVE

    x1 = covid_ABG.Day
    x2 = covid_Delta.Day
    x3 = covid_Omicron.Day

    st.write("""
    ### 5. Histogram kasus infeksi variant covid terhadap waktu

    """)

    fig4 = plt.figure(figsize=(8, 6))
    plt.plot(x1,y1,'--r',label="Daily Alpha-Beta-Gamma")
    plt.plot(x2,y2,'-.b',label="Daily Delta")
    plt.plot(x3,y3,'g', label="Daily Omicron")
    plt.xlabel('Day#')
    plt.ylabel('People Positive Covid')
    plt.legend()
    st.pyplot(fig4)

    #Data correlation.
    corrdata_ABG = covid_ABG.corr()

    st.write("""
    ### 6. Histogram kasus infeksi variant covid terhadap waktu

    6.1 Nilai korelasi parameter pada variant Alpha, Beta & Gamma
    
    """)

    fig5 = plt.figure(figsize=(8, 6))
    sns.heatmap(corrdata_ABG, annot=True)
    st.pyplot(fig5)

    #variant delta
    corrdata_Delta = covid_Delta.corr()

    st.write("""
    6.2 Nilai korelasi parameter pada variant Delta

    """)

    fig6 = plt.figure(figsize=(8, 6))
    sns.heatmap(corrdata_Delta, annot=True)
    st.pyplot(fig6)

    #variant Omicron
    corrdata_Omicron = covid_Omicron.corr()

    st.write("""
    6.2 Nilai korelasi parameter pada variant Omicron

    """)

    fig7 = plt.figure(figsize=(8, 6))
    sns.heatmap(corrdata_Delta, annot=True)
    st.pyplot(fig7)