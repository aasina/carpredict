import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.express as px

# set wide page layout
st.set_page_config(layout="wide")

# Import dataset
datacovid = pd.read_excel('datasetcovidjktid.xlsx')

# add title
with st.container():
    st.title("Dashboard Rekapitulasi Data Covid 19")

with st.container():
    col1, col2 = st.columns([2, 1])
    # define value of X and Y
    x = datacovid.Tanggal
    value1 = datacovid.JKT_DAILY_POSITIVE
    value2 = datacovid.JKT_DAILY_DEATH
    value3 = datacovid.JKT_DAILY_HOSPITALIZED

    with col1:
        # define value of X and Y
        x = datacovid.Tanggal
        value1 = datacovid.JKT_DAILY_POSITIVE
        value2 = datacovid.JKT_DAILY_DEATH

        sizefont = 5

        fig1 = plt.figure(figsize=(4, 3))
        color = 'tab:red'
        plt.title('Data Positif Harian', fontsize=6)
        plt.xlabel('Tanggal', fontsize=sizefont)
        plt.ylabel('Positif Harian', color=color, fontsize=sizefont)
        plt.fill_between(x, value1, color=color)
        plt.tick_params(axis='y', labelcolor=color)
        plt.xticks(fontsize=sizefont)
        plt.yticks(fontsize=sizefont)
        plt.grid(True)
        st.pyplot(fig1)

    with col2:
        # kosong
        st.write("""

        """)

        # Grafik Meninggal
        fig1 = plt.figure(figsize=(4, 2))
        color = 'tab:blue'
        plt.title('Meninggal Harian', fontsize=10)
        plt.plot(x, value2, color=color)
        plt.tick_params(axis='y', labelcolor=color)
        plt.xticks(fontsize=sizefont)
        plt.yticks(fontsize=sizefont)
        # plt.grid(True)
        st.pyplot(fig1)

        st.write("""

        """)

        # grafik Perawatan
        fig2 = plt.figure(figsize=(4, 2))
        color = 'tab:green'
        plt.title('Pasien Rawat Harian', fontsize=10)
        plt.plot(x, value3, color=color)
        plt.tick_params(axis='y', labelcolor=color)
        plt.xticks(fontsize=sizefont)
        plt.yticks(fontsize=sizefont)
        # plt.grid(True)
        st.pyplot(fig2)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        fig3 = px.area(datacovid, x="Day", y="JKT_DAILY_POSITIVE", color="Variant_Suspect")

        fig3.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.65
        ))

        # Plot!
        st.plotly_chart(fig3, use_container_width=True)

from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig4 = make_subplots(rows=1, cols=2)

fig4.add_trace(
    go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
    row=1, col=1
)

fig4.addtrace(
    go.Scatter(x=[20, 30, 40], y=[50, 60, 70]),
    row=1, col=2
)

fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")