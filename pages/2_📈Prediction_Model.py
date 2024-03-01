import streamlit as st
import pandas as pd
import plotly.express as px
import os
import numpy as np
css_file = os.path.abspath("style.css")

def local_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css()


st.markdown('<div class="banner">BeepBoop</div>', unsafe_allow_html=True)

df = pd.read_csv('/Users/wsliwka/Desktop/Python csv/pandas epa/tickets1.csv')
df['Create Date'] = pd.to_datetime(df['Create Date'])
df.set_index('Create Date', inplace=True)
daily_ticket_volume = df.resample('D').size()
weekly_ticket_volume = daily_ticket_volume.resample('W').sum()
reps_needed = weekly_ticket_volume / 5  
reps_needed['Tickets Generated'] = weekly_ticket_volume





tab1, tab2 = st.tabs ({"Graph", "Table"})
with tab1:
    st.header("Rep Table")
    st.write("Prediction Model")
    st.write("The prediction model calculates how many reps are needed per day/per week based on previous volumes.")
    st.write(reps_needed)
with tab2:
     st.header("Products")
     st.image("graphs/barhorizontal.png")
     st.write("This shows what products each rep specialises in")





