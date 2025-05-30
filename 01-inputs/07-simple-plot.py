import streamlit as st
import pandas as pd
import numpy as np

st.title('Simple Plot App')

number = st.slider('Pick a number', 0, 100, 10)

data = pd.DataFrame({
  'first column': list(range(1, 11)),
  'second column': np.arange(number, number + 10)
})
st.line_chart(data)
