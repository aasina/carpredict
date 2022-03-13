import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def app():
    st.title("Regresi Linier")

    st.write(
        "Halaman ini digunakan untuk memperlihatkan model yang dibangun menggunakan regresi linier"
    )

    # load dataset
    datacovid = pd.read_csv("datasetcovidsamplejkt.csv")

    covid_JKT = datacovid.loc[
        :,
        [
            "Variant_Suspect",
            "Day",
            "JKT_DAILY_POSITIVE",
            "JKT_DAILY_DEATH",
            "JKT_DAILY_HOSPITALIZED",
            "JKT_DAILY_POSTRATE",
            "Risk",
        ],
    ]

    covid_Delta = datacovid.loc[
        datacovid.Variant_Suspect == "Delta",
        [
            "Day",
            "JKT_DAILY_POSITIVE",
            "JKT_DAILY_DEATH",
            "JKT_DAILY_HOSPITALIZED",
            "JKT_DAILY_POSTRATE",
            "Risk",
            "Risk_Criteria",
        ],
    ]

    covid_Omicron = datacovid.loc[
        datacovid.Variant_Suspect == "Omicron",
        [
            "Day",
            "JKT_DAILY_POSITIVE",
            "JKT_DAILY_DEATH",
            "JKT_DAILY_HOSPITALIZED",
            "JKT_DAILY_POSTRATE",
            "Risk",
            "Risk_Criteria",
        ],
    ]

    # Perform Test Train Split
    X_train, X_test, y_train, y_test = train_test_split(
        covid_Delta.JKT_DAILY_POSTRATE, covid_Delta.JKT_DAILY_POSITIVE
    )

    # visualisasi Dataset
    fig1 = plt.figure(figsize=(12, 8))
    plt.scatter(X_train, y_train, label="Training Data", color="r", alpha=0.7)
    plt.scatter(X_test, y_test, label="Testing Data", color="g", alpha=0.7)
    plt.legend()
    plt.title("Test Train Split")
    st.pyplot(fig1)

    # Model fitting using Linear Regression Module
    LR = LinearRegression()
    LR.fit(X_train.values.reshape(-1, 1), y_train.values)

    # Use model to predict on test data
    prediction = LR.predict(X_test.values.reshape(-1, 1))

    # Plot prediction line against actual test data
    fig2 = plt.figure(figsize=(12, 8))
    plt.plot(X_test, prediction, label="Linear Regression", color="b")
    plt.scatter(X_test, y_test, label="Actual Test Data", color="g", alpha=0.7)
    plt.legend()
    st.pyplot(fig2)

    #find parameter for Linear Regression
    lrcoef = LR.coef_
    lrint = LR.intercept_

    #daily_positive_predict = LR.intercept_ + LR.coef_*(daily_postrate)
    daily_postrate = 0.4
    daily_positive_predict = lrint + lrcoef*daily_postrate

    # direct predict estimated daily_positive_predict using predict
    LR.predict(np.array([[0.4]]))[0]

    # Model scoring
    print('Mean squared error (MSE): %.2f'
        % mean_squared_error(y_test, prediction))
    print('Coefficient of determination (R^2): %.2f'
        % r2_score(y_test, prediction))