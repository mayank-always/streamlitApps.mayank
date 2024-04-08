import streamlit as st
import pandas as pd

# Page Title
st.title("CSV Data Analysis Website 1.0")
st.caption("created by Mayank B.")

# File Upload
uploaded_file = st.file_uploader("Upload a datafile", type=["csv"])

# Data Analysis
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.write(df)

    # Basic Data Analysis
    st.subheader("Basic Analysis:")
    st.write("Shape of the data:", df.shape)
    st.write("Summary Statistics:", df.describe())

    # Visualization (Example: Histogram)
    st.subheader("Data Visualization:")
    column = st.selectbox("Select a column for visualization", df.columns)
    st.write("Histogram of", column)
    st.bar_chart(df[column].value_counts())
