import streamlit as st

st.title("Climate Change Comparative Analysis Dashboard")

st.write("This dashboard shows climate change data using pie charts and bar graphs.")
user=st.text_input('ENTER USER NAME')
if st.button('CLICK'):
  st.write('WELCOME TO CLIMATE CHANGE APP')
