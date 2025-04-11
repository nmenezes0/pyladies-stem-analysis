import pandas as pd
import streamlit as st


st.title("Welcome to my Streamlit app!")

df = pd.read_csv("data/kaggle_women_in_stem.csv")

st.dataframe(df)






