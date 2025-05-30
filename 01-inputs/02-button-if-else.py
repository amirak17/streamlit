import streamlit as st

st.title('Button App')

if st.button('Greeting'):
    st.write('Hi, hello there')
else:
    st.write('Goodbye')
