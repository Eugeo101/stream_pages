# plot figures
import streamlit as st
import plotly.express as px
tips_df = px.data.tips()
fig = px.bar(tips_df, x="day", y='tip')
chart = st.plotly_chart(fig)
# update

user_choice = st.multiselect("choose days", options=tips_df['day'].unique())
submit = st.button("Apply Changes")
if submit:
    dff = tips_df[tips_df['day'].isin(user_choice)]
    fig = px.bar(dff, x="day", y='tip')
    chart.plotly_chart(fig)
# dff
