import pandas as pd
import streamlit as st


@st.cache_data
def kaggle_stem_data():
    df = pd.read_csv("data/kaggle_women_in_stem.csv")
    return df


st.title("Welcome to my PyLadies Lithuania app!")

st.subheader("Women in STEM data")
df = kaggle_stem_data()
chosen_countries = st.multiselect(
    label="Select country", options=df["Country"].unique()
)
chosen_subjects = st.multiselect(
    label="Select subject", options=df["STEM Fields"].unique()
)
filtered_data = df[
    (df["Country"].isin(chosen_countries)) & (df["STEM Fields"].isin(chosen_subjects))
]
st.dataframe(filtered_data)


st.subheader("Female graduation in maths in Canada")
df = kaggle_stem_data()
df = df[(df["Country"] == "Canada") & (df["STEM Fields"] == "Mathematics")]
st.bar_chart(df, x="Year", y="Female Graduation Rate (%)", stack=False)
