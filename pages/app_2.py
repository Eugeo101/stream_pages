# display media
import streamlit as st
import plotly.express as px
st.image("download.jpeg") 
# st.image(["download.jpeg", "download - Copy.jpeg"]) # display media
df = px.data.tips()
st.dataframe(df)
