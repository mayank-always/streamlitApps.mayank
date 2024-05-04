import streamlit as st
import pandas as pd
import numpy as np

# Page Title
st.title("CSV Data Analysis Website 3.0")
st.caption("created by Mayank B.")

# File Upload
uploaded_file = st.file_uploader("Upload a datafile", type=["csv"])

# Data Analysis
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.write(df)

        # Basic Data Analysis
        st.subheader("Basic Analysis:")
        st.write(df.describe())  # Concise summary statistics

        # Text Summarization Function (Simplified)
        def generate_summary(df):
            """
            Generates a user-friendly word-based summary of the data.

            Args:
                df: The Pandas DataFrame containing the data.

            Returns:
                A string summarizing the data in plain language.
            """
            summary = f"The dataset has {len(df)} rows and {len(df.columns)} columns. "

            # Analyze numerical columns (general descriptions)
            numeric_cols = df.select_dtypes(include=[np.number])
            if not numeric_cols.empty:
                summary += "Numerical columns like "
                summary += ', '.join(numeric_cols) + " show interesting patterns. "
                # You can add more specific analysis here (e.g., high/low values, outliers)

            # Analyze categorical columns (number of unique values in simpler terms)
            categorical_cols = df.select_dtypes(include=[object])
            if not categorical_cols.empty:
                summary += "For categorical columns like "
                summary += ', '.join(categorical_cols) + ", there are various categories. "

            return summary

        # Text Summary
        summary = generate_summary(df.copy())
        st.subheader("Word-Based Summary:")
        st.write(summary)

        # Visualization (User-Selectable Chart Type)
        st.subheader("Data Visualization:")
        column = st.selectbox("Select a column for visualization", df.columns)

        # Dropdown menu for chart selection (concise)
        chart_type = st.selectbox("Chart Type", ["Line", "Bar", "Histogram"])

        if chart_type == "Line":
            st.line_chart(df[column])
        elif chart_type == "Bar":
            st.bar_chart(df[column])
        else:
            st.bar_chart(df[column].value_counts())

    except Exception as e:
        st.error(f"Error: {e}")
