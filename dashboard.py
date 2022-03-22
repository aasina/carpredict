import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set wide page layout
st.set_page_config(layout="wide")

# Import Dataset
dataset = pd.read_csv("datasetcovidsamplejkt.csv")

ydayposid = dataset.ID_DAILY_POSITIVE
ydayposjkt = dataset.JKT_DAILY_POSITIVE
ydaydeathid = dataset.ID_DAILY_DEATH
ydaydeathjkt = dataset.JKT_DAILY_DEATH
xdaily = dataset.Tanggal

# sidebar
st.sidebar.text("Testing")

# create first line
with st.container():
    st.title("Dashboard Rekapitulasi Data Covid")

with st.container():
    col1, col2 = st.columns([2, 1])

    with col1:
        fig1 = plt.figure()
        plt.plot(xdaily, ydayposid, "r", label="Positive Harian Indonesia")
        plt.plot(xdaily, ydayposjkt, "b", label="Positif Harian DKI Jakarta")
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
