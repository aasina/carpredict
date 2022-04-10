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
    col2, col3, col4, col5 = st.columns(4)

    # summary
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

    # create column formatting
    col1, col2 = st.columns(2)
    # define value of X and Y
    x = datacovid.Tanggal
    value1 = datacovid.JKT_DAILY_POSITIVE
    value2 = datacovid.JKT_DAILY_DEATH
    value3 = datacovid.JKT_DAILY_HOSPITALIZED
    sizefont = 5

    covid_ABG = datacovid.loc[datacovid.Variant_Suspect == 'Alpha-Beta-Gamma', [
        'Day', 'JKT_DAILY_POSITIVE', 'JKT_DAILY_DEATH', 'JKT_DAILY_HOSPITALIZED']]
    covid_Delta = datacovid.loc[datacovid.Variant_Suspect == 'Delta', [
        'Day', 'JKT_DAILY_POSITIVE', 'JKT_DAILY_DEATH', 'JKT_DAILY_HOSPITALIZED']]
    covid_Omicron = datacovid.loc[datacovid.Variant_Suspect == 'Omicron', [
        'Day', 'JKT_DAILY_POSITIVE', 'JKT_DAILY_DEATH', 'JKT_DAILY_HOSPITALIZED']]

    with col1:
        # This column is for historical Graphic

        # create selectbox
        histselect = st.selectbox(
            'Please select data label',
            ('Positive Case', 'Death Case', 'Hospitalized Case')
        )

        # create parameter from selectbox
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
        varselect = st.selectbox(
            'Please select data label',
            ('Positive', 'Death', 'Hospitalized')
        )

        if varselect == 'Positive':
            y1 = covid_ABG.JKT_DAILY_POSITIVE
            y2 = covid_Delta.JKT_DAILY_POSITIVE
            y3 = covid_Omicron.JKT_DAILY_POSITIVE
            labely = 'Daily Positive'
        elif varselect == 'Death':
            y1 = covid_ABG.JKT_DAILY_DEATH
            y2 = covid_Delta.JKT_DAILY_DEATH
            y3 = covid_Omicron.JKT_DAILY_DEATH
            labely = 'Daily Death'
        else:
            y1 = covid_ABG.JKT_DAILY_HOSPITALIZED
            y2 = covid_Delta.JKT_DAILY_HOSPITALIZED
            y3 = covid_Omicron.JKT_DAILY_HOSPITALIZED
            labely = 'Daily Hospitalized'

        x1 = covid_ABG.Day
        x2 = covid_Delta.Day
        x3 = covid_Omicron.Day

        fig2 = plt.figure(figsize=(4, 3))
        plt.title('Variant Observation', fontsize=6)
        plt.plot(x1, y1, '-r', label="Daily Alpha-Beta-Gamma", alpha=1 ,linewidth=1)
        plt.plot(x2, y2, '-b', label="Daily Delta", alpha=1, linewidth=1)
        plt.plot(x3, y3, '-g', label="Daily Omicron", alpha=1, linewidth=1)
        plt.xlabel('Day', fontsize=sizefont)
        plt.ylabel(labely, fontsize=sizefont)
        plt.legend(fontsize=sizefont)
        plt.xticks(fontsize=sizefont)
        plt.yticks(fontsize=sizefont)
        st.pyplot(fig2)

