import streamlit as st
import pandas as pd
import plotly.express as px
import os

css_file = os.path.abspath("style.css")

st.set_page_config(page_title="Ticket Dahsboard",
                   page_icon=":bar_chart:",
                   layout="wide")

def local_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css()

st.markdown('<div class="banner">BeepBoop</div>', unsafe_allow_html=True)

#df = pd.read_csv('/Users/wsliwka/Desktop/Python csv/pandas epa/tickets1.csv')
df = pd.read_csv('/Users/wsliwka/Desktop/EPA code/EPA/csv/tickets.csv')
#tab layout
tab1, tab2, tab3, tab4 = st.tabs(["Product", "Employees", "Inquiries", "Team"])


# Convert 'Create Date' column to datetime format
df['Create Date'] = pd.to_datetime(df['Create Date'])
# Replace "-" with NaN in 'Resolve Date' column
df['Resolve Date'] = pd.to_datetime(df['Resolve Date'], errors='coerce')
# Calculate resolution time for each ticket
df['Resolution Time'] = (df['Resolve Date'] - df['Create Date']).dt.days+ 1
# Group by 'Product' column and calculate average resolution time for each product
average_resolution_time = df.groupby('Product')['Resolution Time'].mean().reset_index()


# Group by 'Inquiry Rep Desc' (employee name) column and calculate average resolution time for each employee
average_resolution_time_per_employee = df.groupby('Inquiry Rep Desc')['Resolution Time'].mean().reset_index()


# Calculate the number of tickets per product
tickets_per_product = df['Product'].value_counts().reset_index()
tickets_per_product.columns = ['Product', 'Number of Tickets']

# Count the number of tickets for each inquiry rep team
tickets_by_team = df['Inquiry Rep Team Desc'].value_counts().reset_index()
tickets_by_team.columns = ['Inquiry Rep Team Desc', 'Number of Tickets']
# Create a pie chart
fig = px.pie(tickets_by_team, values='Number of Tickets', names='Inquiry Rep Team Desc', title='Tickets Distribution by Inquiry Rep Team')

with tab1:
    st.write("Average Resolution Time by Product:")
    st.write(average_resolution_time)
with tab2:
    st.write("Average Resolution Time per Employee:")
    st.write(average_resolution_time_per_employee)
with tab3:
    st.write("Number of Tickets per Product:")
    st.write(tickets_per_product)
with tab4:
    st.header("Team Distriubted Inquiries")
    st.plotly_chart(fig)
   



    
     




