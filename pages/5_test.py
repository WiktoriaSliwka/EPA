import pandas as pd
import streamlit as st

df = pd.read_csv('/Users/wsliwka/Desktop/Python csv/pandas epa/tickets1.csv')

tab1, tab2 = st.tabs(["test1", "test2"])
df['Resolve Date'] = pd.to_datetime(df['Resolve Date'], errors='coerce')

#drop -
df = df.dropna(subset=['Resolve Date'])

# Group by day
resolved_tickets_per_day = df.groupby(df['Resolve Date'].dt.date).size().reset_index(name='Resolved Tickets')

# Calc
resolved_tickets_per_day['Representatives Needed'] = resolved_tickets_per_day['Resolved Tickets'] / 5

# Define function to highlight rows
def highlight_rep(val):
    color = 'lightyellow' if val > 35 else ''
    return f'background-color: {color}'

# Apply the style function to 'Representatives Needed' column
styled_df = resolved_tickets_per_day.style.applymap(highlight_rep, subset=['Representatives Needed'])
 
with tab1:
    st.write("Number of Representatives Needed Each Day:")
    st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

with tab2:
    st.write("Test")




