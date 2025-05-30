import streamlit as st

st.title('Radio Button App')

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

st.write(f'You selected: {genre}')
