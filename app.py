import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Immune Cell Score Analysis")

# File Uploader
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())

    # Summary Statistics
    st.write("### Summary Statistics")
    st.write(df.describe())
    
    # Column Selection
    column = st.selectbox("Select a column for visualization", df.columns[1:])
    
    # Histogram
    st.write("### Histogram")
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=True, ax=ax)
    st.pyplot(fig)
    
    # Box Plot
    st.write("### Box Plot")
    fig, ax = plt.subplots()
    sns.boxplot(y=df[column], ax=ax)
    st.pyplot(fig)
    
    # Correlation Heatmap
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

# Run with: streamlit run script.py
