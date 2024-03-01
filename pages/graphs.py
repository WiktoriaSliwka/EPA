import streamlit as st
import pandas as pd

# Read the CSV file into df
df = pd.read_csv('/Users/wsliwka/Desktop/Python csv/pandas epa/tickets1.csv')

# Convert 'Create Date' to datetime
df['Create Date'] = pd.to_datetime(df['Create Date'])

# Extract month and year from 'Create Date' and create a new column 'Month'
df['Month'] = df['Create Date'].dt.to_period('M')

# Group by 'Month' and 'Product' and count the number of tickets
tickets_per_month = df.groupby(['Month', 'Product']).size().reset_index(name='Tickets Generated')

# Display the DataFrame as a table in the Streamlit app
st.write(tickets_per_month)
