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
    st.title("DASHBOARD COVID 19 - CASE STUDY DKI JAKARTA")

# Opening Summary
with st.container():
    st.header('DATA SUMMARY')
    col1, col2, col3, col4, col5 = st.columns(5)

    # summary
    with col1:
        st.write('#### Type of Variant:')
        st.write("""
        1. Alpha - Beta - Gamma (First Wave)
        2. Delta (Second Wave)
        3. Omicron (Third Wave)
        """)

    with col2:
        st.write('#### Initial Observation Date:')
        # get first row data from Tanggal column
        startdate = datacovid['Tanggal'].iloc[0]
        st.write(startdate.strftime('%d-%m-%Y'))
        st.write('#### Last Observation Date:')
        totalobsday = len(datacovid.Tanggal)  # total observation day
        # get last row data from Tanggal column
        lastdate = datacovid['Tanggal'].iloc[totalobsday-1]
        st.write(lastdate.strftime('%d-%m-%Y'))

    with col3:
        st.write('#### Total Tested:')
        st.write("{:,.0f}".format(datacovid.JKT_DAILY_TESTED.sum()))
        st.write('#### Highest Positivity Rate:')
        st.write("{:.2f}".format(datacovid.JKT_DAILY_POSTRATE.max()))

    with col4:
        st.write('#### Total Positive Case:')
        st.write("{:,}".format(datacovid.JKT_DAILY_POSITIVE.sum()))
        st.write('#### Highest Daily Positive Case:')
        st.write("{:,}".format(datacovid.JKT_DAILY_POSITIVE.max()))

    with col5:
        st.write('#### Total Death Case:')
        st.write("{:,}".format(datacovid.JKT_DAILY_DEATH.sum()))
        st.write('#### Highest Daily Death Case:')
        st.write("{:,}".format(datacovid.JKT_DAILY_DEATH.max()))

with st.container():
    st.header('TIMELINE CURVE')
    st.write('#### Type of Variant:')
    st.write("""
    1. Alpha - Beta - Gamma (First Wave)
    2. Delta (Second Wave)
    3. Omicron (Third Wave)
    """)

    col1, col2 = st.columns(2)
    # define value of X and Y
    x = datacovid.Tanggal
    value1 = datacovid.JKT_DAILY_POSITIVE
    value2 = datacovid.JKT_DAILY_DEATH
    value3 = datacovid.JKT_DAILY_HOSPITALIZED
    sizefont = 5

    with col1:
        # Historical Graphic
        histselect = st.selectbox(
            'Please select data label',
            ('Positive Case', 'Death Case', 'Hospitalized Case')
        )

        if histselect == 'Positive Case':
            colorgraph = 'tab:red'
            yvalue = value1
            labely = 'Daily Positive'
        elif histselect == 'Death Case':
            colorgraph = 'tab:blue'
            yvalue = value2
            labely = 'Daily Death'
        else:
            colorgraph = 'tab:green'
            yvalue = value3
            labely = 'Daily Hospitalized'

        fig1 = plt.figure(figsize=(4, 3))
        color = colorgraph
        plt.title('Historical Timeline', fontsize=6)
        plt.xlabel('Date', fontsize=sizefont)
        plt.ylabel('labely', color=colorgraph, fontsize=sizefont)
        plt.fill_between(x, yvalue, color=color)
        plt.tick_params(axis='y', labelcolor=color)
        plt.xticks(fontsize=sizefont)
        plt.yticks(fontsize=sizefont)
        st.pyplot(fig1)

    with col2:
        fig2 = plt.figure(figsize=(4, 3))
        color = 'tab:red'
        plt.title('Variant Historical Timeline', fontsize=6)
        plt.xlabel('Day', fontsize=sizefont)
        plt.ylabel('Positif Harian', color=color, fontsize=sizefont)
        plt.fill_between(x, value1, color=color)
        plt.tick_params(axis='y', labelcolor=color)
        plt.xticks(fontsize=sizefont)
        plt.yticks(fontsize=sizefont)
        st.pyplot(fig2)
