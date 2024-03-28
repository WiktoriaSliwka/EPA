import streamlit as st
import pandas as pd
import plotly.express as px
import os
import matplotlib.pyplot as plt
import numpy as np

css_file = os.path.abspath("style.css")

st.set_page_config(page_title="Ticket Dahsboard",
                   page_icon=":bar_chart:",
                   layout="wide")

def local_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css()
st.markdown('<div class="banner">BeepBoop</div>', unsafe_allow_html=True)
df = pd.read_csv('/Users/wsliwka/Desktop/Python csv/pandas epa/tickets1.csv')

df['Resolve Date'] = pd.to_datetime(df['Resolve Date'], errors='coerce')
#df['Resolve Date'] = pd.to_datetime(df['Resolve Date'])
df['Create Date'] = pd.to_datetime(df['Create Date'], errors='coerce')


# Group by representative and count the number of tickets closed by each representative
tickets_closed_by_rep = df.groupby('Inquiry Rep Desc')['Resolve Date'].count()
# Create a bar chart
fig, ax = plt.subplots(figsize=(12, 8))
tickets_closed_by_rep.plot(kind='bar', ax=ax)
ax.set_xlabel('Representative')
ax.set_ylabel('Number of Tickets Closed')
ax.set_title('Tickets Closed by Representatives')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()



# Group by day
resolved_tickets_per_day = df.groupby(df['Resolve Date'].dt.date).size().reset_index(name='Resolved Tickets')
# Calc
resolved_tickets_per_day['Representatives Needed'] = np.ceil(resolved_tickets_per_day['Resolved Tickets'] / 5)

# Define function to highlight rows
def highlight_rep(val):
    color = 'lightyellow' if val > 37 else ''
    return f'background-color: {color}'
# Apply the style function to 'Representatives Needed' column
styled_df = resolved_tickets_per_day.style.applymap(highlight_rep, subset=['Representatives Needed'])
# Check for missing or improperly formatted dates
invalid_dates = df[df['Resolve Date'].isnull()]['Resolve Date']
# Drop rows with invalid dates
df = df.dropna(subset=['Create Date', 'Resolve Date'])
# Extract 'Day' from 'Resolve Date'
df['Day'] = df['Resolve Date'].dt.date
# Group by 'Day' and count tickets
resolved_per_day = df.groupby('Day').size().reset_index(name='Ticket Volume')
# Create a line plot
fig_day = px.line(resolved_per_day, x='Day', y='Ticket Volume', title='Tickets Resolved Daily',
                  labels={'Day': 'Day', 'Ticket Volume': 'Ticket Volume'})






# Calculate the duration of each ticket
df['Duration'] = (df['Resolve Date'] - df['Create Date']).dt.days + 1  # Add 1 to include both the start and end dates
# Group by week and count the number of tickets
df['Week'] = df['Create Date'].dt.strftime('%Y-%U')
tickets_per_week = df.groupby('Week').size()
avg_tickets_per_day_per_week = tickets_per_week / 7
reps_needed_per_week = avg_tickets_per_day_per_week / 5
#reps_needed_per_week = reps_needed_per_week.round()
reps_needed_per_week = np.ceil(reps_needed_per_week)  
# Create the DataFrame
data = {'Week': tickets_per_week.index,
        'Tickets Resolved': tickets_per_week.values,
        'Avg Tickets Per Day': avg_tickets_per_day_per_week.values,
        'Reps Needed': reps_needed_per_week}
df_summary = pd.DataFrame(data)
highlighted_weeks = df_summary['Reps Needed'] > 36
def highlight_weeks(row):
    color = 'background-color: lightyellow' if row['Reps Needed'] > 36 else ''
    return [color] * len(row)

# Apply custom styling
styled_summary = df_summary.style.apply(highlight_weeks, axis=1)






tab1, tab2, tab3, tab4= st.tabs(["Resolved Tickets", "Rep calculator Day","Rep calculator Week","Representatives"])

with tab1:
   st.write("How Many Tickets Were Resolved Daily throughtout 2023")
   st.plotly_chart(fig_day)
with tab2:
   st.write("Number of Representatives Needed Each Day:")
   st.write("I analysed 2023 ticket volumes to calculate how many reps would be needed every day and for the service team to organise shift appropriately. ")
   st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)
with tab3:
    st.write("Number of Representatives Needed every week")
    st.write("I analysed 2023 ticket volumes to calculate how many reps would be needed every week and for the service team to organise shift appropriately. ")
    st.write(styled_summary)
with tab4:
    st.write("Tickets resolved annually by each representative")
    st.pyplot(fig)
  