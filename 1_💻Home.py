import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import os

st.set_page_config(page_title="Ticket Dahsboard",
                   page_icon=":bar_chart:",
                   layout="wide")

df = pd.read_csv('/Users/wsliwka/Desktop/Python csv/pandas epa/tickets1.csv')

#css for banner
css_file = os.path.abspath("style.css")
def local_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css()

#landing page
st.markdown('<div class="banner">BeepBoop</div>', unsafe_allow_html=True)
st.header("Ticket history")
st.write("This shows the companies ticket volumes throughout 2023.")


df['Create Date'] = pd.to_datetime(df['Create Date'])
df['Month'] = df['Create Date'].dt.month
df['Week'] = df['Create Date'].dt.isocalendar().week
df['Day'] = df['Create Date'].dt.date

tickets_per_month = df.groupby('Month').size()
tickets_per_week = df.groupby('Week').size()
tickets_per_day = df.groupby('Day').size()

tab1, tab2, tab3, tab4 = st.tabs(["Month", "Week", "Day", "Tables"])

with tab1:
   st.header("Monthly ticket distribution")
   st.image("graphs/linegraph.png")


with tab2:
   st.header("Weekly ticket distribution")
   st.image("graphs/weekly.png")
 
with tab3:
   st.header("Dailey ticket distribution")
   st.image("graphs/dailey.png")
  
   
with tab4:
    st.header("Ticket Distribution")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Month")
        st.write(tickets_per_month)
    with col2:
        st.write("Week")
        st.write(tickets_per_week)
    with col3:
        st.write("Day")
        st.write(tickets_per_day)











# 📊💻📈🗄️🌍

# # Objective
# st.header("Objective")
# st.write("The objective of the project is to develop a scheduler to help service teams arrange for client coverage.")

# # business reason
# st.header("Business Reason")
# st.write("Service teams will benefit from this information as they can use it to arrange for queue coverage.")
