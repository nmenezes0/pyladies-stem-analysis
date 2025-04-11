import pandas as pd
import streamlit as st


st.title("Welcome to my PyLadies Lithuania app!")

st.subheader("Women in STEM data")
df = pd.read_csv("data/kaggle_women_in_stem.csv")

chosen_countries = st.multiselect(label="Select country", options=df["Country"].unique())
chosen_subjects = st.multiselect(label="Select subject", options=df["STEM Fields"].unique())

df = df[df["Country"].isin(chosen_countries)]
df = df[df["STEM Fields"].isin(chosen_subjects)]

st.dataframe(df)