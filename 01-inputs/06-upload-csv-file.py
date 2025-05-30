import streamlit as st

st.title('Upload File App')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

print(uploaded_file)