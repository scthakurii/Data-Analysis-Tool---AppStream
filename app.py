import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Analysis Tool")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    # Example plot
    st.subheader("Data Visualization")
    if st.checkbox("Show plot"):
        plt.figure(figsize=(10, 5))
        plt.plot(df['Column1'], df['Column2'])
        st.pyplot(plt)
