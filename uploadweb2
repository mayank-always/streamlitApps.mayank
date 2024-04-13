import streamlit as st
import pandas as pd

# Page Title
st.title("CSV Data Analysis Website 2.0")
st.caption("created by Mayank B. 4/13/24")

# File Upload
uploaded_file = st.file_uploader("Upload a datafile", type=["csv"])

# Data Analysis
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.write(df)

    # Basic Data Analysis
    st.subheader("Basic Analysis:")

    st.write("Summary Statistics:", df.describe())

    # Visualization (User-Selectable Chart Type)
    st.subheader("Data Visualization:")
    column = st.selectbox("Select a column for visualization", df.columns)

    # Add a dropdown menu for chart selection
    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Histogram"])

    if chart_type == "Line Chart":
        st.line_chart(df[column])
    elif chart_type == "Bar Chart":
        st.bar_chart(df[column])
    else:
        st.bar_chart(df[column].value_counts())  

