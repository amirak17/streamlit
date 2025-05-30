import streamlit as st

st.title('Dropdown App')

option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

# notice sidebar