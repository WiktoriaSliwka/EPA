import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import os
import holidays
import plotly.graph_objects as go

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
st.header("2023 Ticket history")
st.write("BeepBoop is a global finance software, media, and data company that provides real-time financial market data, news analysis, and insights to financial professionals, investors, and businesses around the world. Within the service team many tickets are generated daily. The service teams require a sophisticated scheduling solution to efficiently manage client coverage, improving response times and overall service quality")


df['Create Date'] = pd.to_datetime(df['Create Date'])
df['Month'] = df['Create Date'].dt.month
df['Week'] = df['Create Date'].dt.isocalendar().week
df['Day'] = df['Create Date'].dt.date

tickets_per_month = df.groupby('Month').size()
tickets_per_week = df.groupby('Week').size()
tickets_per_day = df.groupby('Day').size()

#Uk holiday calender
uk_holidays = holidays.UK(years=df['Create Date'].dt.year.unique())
# didnt mention days with no tickets e.g. christmas
date_range = pd.date_range(start=df['Create Date'].min(), end=df['Create Date'].max(), freq='D')

def highlight_holidays(day):
    is_holiday = day in uk_holidays
    is_weekend = day.weekday() in [5, 6]  
    
    if is_holiday and is_weekend:
        return 'background-color: lightyellow'
    elif is_holiday:
        return 'background-color: lightblue'
    elif is_weekend:
        return 'background-color: lightgreen'
    else:
        return ''

# tickets_per_day with highlight applied
tickets_per_day_highlighted = pd.DataFrame(tickets_per_day)
tickets_per_day_highlighted.reset_index (inplace=True)
tickets_per_day_highlighted.columns = ['Day', 'Ticket Count']
tickets_per_day_highlighted = tickets_per_day_highlighted.style.applymap(
    lambda x: highlight_holidays(x), subset=['Day']).set_caption('Tickets per Day (Highlighted Holidays)')


df['Month'] = df['Create Date'].dt.month
# count the number of tickets 
tickets_by_month = df.groupby('Month').size().reset_index(name='Ticket Volume')
tickets_by_week = df.groupby('Week').size().reset_index(name='Ticket Volume')
tickets_by_day = df.groupby('Day').size().reset_index(name='Ticket Volume')

# Create a line graph
fig_month = px.line(tickets_by_month, x='Month', y='Ticket Volume', title='Ticket Distribution Throughout the Year',
              labels={'Month': 'Month', 'Ticket Volume': 'Ticket Volume'})

# Group by week
tickets_by_week = df.groupby('Week').size().reset_index(name='Ticket Volume')
fig_week = px.line(tickets_by_week, x='Week', y='Ticket Volume', title='Ticket Distribution by Week',
                   labels={'Week': 'Week', 'Ticket Volume': 'Ticket Volume'})
#Group by day
tickets_by_day = df.groupby('Day').size().reset_index(name='Ticket Volume')
fig_day = px.line(tickets_by_day, x='Day', y='Ticket Volume', title='Ticket Distribution by Day',
                  labels={'Day': 'Day', 'Ticket Volume': 'Ticket Volume'})

#tab layout
tab1, tab2, tab3, tab4 = st.tabs(["Month", "Week", "Day", "Tables"])

with tab1:
   st.header("Monthly ticket distribution")
   st.write("BeepBoops tickets analysis throughout 2023 represented ticket volume via a linegraph")
   st.plotly_chart(fig_month)
 
with tab2:
   st.header("Weekly ticket distribution")
   st.write("Weekly ticket creation")
   st.plotly_chart(fig_week)
   
with tab3:
   st.header("Dailey ticket distribution")
   st.write("Dailey ticket creation")
   st.plotly_chart(fig_day)
  
with tab4:
    st.header("Ticket Distribution")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Monthly Ticket Count")
        st.write(tickets_per_month)
    with col2:
        st.write("Weekly Ticket Count")
        st.write(tickets_per_week)
    with col3:
     st.write("Daily Ticket Count")
     st.write(tickets_per_day_highlighted)
     index_string = "Index:, Blue-Holiday, Yellow-Weekend, Green-Both"
     delimiter = ", "
     parts = index_string.split(delimiter)
     for part in parts:
        st.write(part)








