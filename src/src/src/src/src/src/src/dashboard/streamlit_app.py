import streamlit as st
import pandas as pd

st.title(
    "Battery Health Monitoring Dashboard"
)

st.write(
    "NASA Battery Health Anomaly Detection System"
)

uploaded_file = st.file_uploader(
    "Upload Battery Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write(df.head())

    st.line_chart(df["Capacity"])
