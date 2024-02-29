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

tab1, tab2 = st.tabs ({"Graph", "Table"})
with tab1:
    st.header("Rep Table")
    st.write("Prediction Model")
    st.write("The prediction model calculates how many reps are needed per day/per week based on previous volumes.")
    # Load the data into a DataFrame
df_absolute = pd.read_csv('/Users/wsliwka/Desktop/EPA code/EPA/csv/employees.csv')

# Convert 'Create Date' column to datetime
df_absolute['Create Date'] = pd.to_datetime(df_absolute['Create Date'])

# Set 'Create Date' column as index
df_absolute.set_index('Create Date', inplace=True)

# Resample by day to get daily ticket volume
daily_ticket_volume = df_absolute.resample('D').size()

# Calculate average daily ticket volume for each product specialization
average_daily_volume = daily_ticket_volume.mean()

# Calculate number of reps needed per day for each product specialization
reps_needed_per_day = np.ceil(average_daily_volume / 5)

# Resample by week to get weekly ticket volume
weekly_ticket_volume = df_absolute.resample('W').size()

# Calculate number of reps needed per week for each product specialization
reps_needed_per_week = np.ceil(weekly_ticket_volume / 5)

# Create a DataFrame with the results
df_results = pd.DataFrame({
    #'Week': weekly_ticket_volume.index,
    'Number of Tickets': weekly_ticket_volume.values,
    'Reps Needed': reps_needed_per_week
})


st.write(df_results)

with tab2:
     st.header("Products")
     st.image("graphs/barhorizontal.png")
     st.write("This shows what products each rep specialises in")
    # Load the data into a DataFrame




# # Load the data into a DataFrame
# df_absolute = pd.read_csv('/Users/wsliwka/Desktop/EPA code/EPA/csv/tickets.csv')

# # Convert 'Create Date' column to datetime
# df_absolute['Create Date'] = pd.to_datetime(df_absolute['Create Date'])

# # Set 'Create Date' column as index
# df_absolute.set_index('Create Date', inplace=True)

# # Resample by day to get daily ticket volume
# daily_ticket_volume = df_absolute.resample('D').size()

# # Calculate average daily ticket volume for each product specialization
# average_daily_volume = daily_ticket_volume.mean()

# # Calculate number of reps needed per day for each product specialization
# reps_needed_per_day = np.ceil(average_daily_volume / 5)


# # Create a DataFrame with the results
# df_results = pd.DataFrame({
#     'Week': weekly_ticket_volume.index,
#     'Number of Tickets': daily_ticket_volume.values,
#     'Reps Needed': reps_needed_per_day 
# })


# # Calculate the number of reps needed per day based on the ticket volume
# reps_needed_per_day = np.ceil(daily_ticket_volume / 5)

# # Create a DataFrame with the results
# df_results_per_day = pd.DataFrame({
#     'Date': daily_ticket_volume.index,
#     'Number of Tickets': daily_ticket_volume.values,
#     'Reps Needed': reps_needed_per_day
# })

# # Display the DataFrame as a table
# st.write(df_results_per_day)
