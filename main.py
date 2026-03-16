import streamlit as st

st.title("Climate Change Comparative Analysis Dashboard")
st.markdown("<h1 style='color:purple;font-size:20px;'>Welcome to My App</h1>", unsafe_allow_html=True)

st.write("This dashboard shows climate change data using pie charts and bar graphs.")
user=st.text_input('ENTER USER NAME')
if st.button('CLICK'):
  st.write(user,'WELCOME TO CLIMATE CHANGE APP')
