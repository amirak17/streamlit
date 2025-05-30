import streamlit as st

st.title('Slider App')
st.write('Slider Input')
number = st.slider('Pick a number', 0, 100, 10) # start, end, default
st.write(f'You selected: {number}')
