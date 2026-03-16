import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Climate Change Comparative Analysis Dashboard")

st.write("This dashboard shows climate change data using pie charts and bar graphs.")

# -----------------------------
# Data 1 : CO2 Emissions
# -----------------------------

sectors = ['Transportation','Electricity','Industry','Agriculture','Residential']
values = [29,25,23,13,10]

df1 = pd.DataFrame({
    'Sector': sectors,
    'Emission %': values
})

st.subheader("CO2 Emissions by Sector")

fig1, ax1 = plt.subplots()
ax1.pie(values, labels=sectors, autopct='%1.1f%%')
st.pyplot(fig1)

# -----------------------------
# Data 2 : Temperature Rise
# -----------------------------

years = ['2018','2019','2020','2021','2022']
temp = [0.82,0.95,1.02,0.98,1.05]

df2 = pd.DataFrame({
    'Year': years,
    'Temperature Rise': temp
})

st.subheader("Global Temperature Rise")

fig2, ax2 = plt.subplots()
ax2.bar(years,temp)
ax2.set_xlabel("Year")
ax2.set_ylabel("Temperature Rise (°C)")

st.pyplot(fig2)

st.write("Analysis shows increasing global temperature and major emissions from transportation and energy sectors.")
