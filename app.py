import pandas as pd
import plotly.express as px
import streamlit as st


@st.cache_data
def kaggle_stem_data():
    df = pd.read_csv("data/kaggle_women_in_stem.csv")
    # Take the mean for duplicate rows
    df_cleaned = df.groupby(["Country", "Year", "STEM Fields"], as_index=False).mean()
    return df_cleaned


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


st.subheader("Female enrollment & graduation in maths in Canada")
df = kaggle_stem_data()

chosen_countries = st.multiselect(label="Country", options=df["Country"].unique())
chosen_subject = st.selectbox(label="Subject", options=df["STEM Fields"].unique())
timeframe = st.slider(
    label="Time period",
    min_value=min(df["Year"]),
    max_value=max(df["Year"]),
    value=(2010, 2020),
)

df = df[
    (df["Country"].isin(chosen_countries))
    & (df["STEM Fields"] == chosen_subject)
    & (df["Year"] >= timeframe[0])
    & (df["Year"] <= timeframe[1])
]

fig = px.bar(df, x="Year", y="Female Enrollment (%)", color="Country", barmode="group")
st.plotly_chart(fig)
fig = px.bar(
    df, x="Year", y="Female Graduation Rate (%)", color="Country", barmode="group"
)
st.plotly_chart(fig)

# TODO - clean data
