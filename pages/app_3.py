## inputs
import streamlit as st
value = st.slider(min_value=0, max_value=100, label='age') # slider
value_4 = st.select_slider(label="weather", options=["Sunny", "Cold", "Windy"]) # select_slider
value_2 = st.checkbox(label="is_male") # checkbox
value_3 = st.radio(label="is an dog animal?", options=['Yes', "No", "I don't know"]) # radio
value_5 = st.selectbox(label="Drop Down Button", options=['A', "B", "C"])
value_6 = st.multiselect(label="which fruit is round?", options=['apple', "orange", "banna"])
submit = st.button(label="Submit") # button
if submit:
    print(value)
    print(value_2)
    print(value_3)
    print(value_4)
    print(value_5)
    print(value_6)
    # model.predict()
