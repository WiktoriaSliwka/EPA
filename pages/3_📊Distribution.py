import streamlit as st
import pandas as pd
import plotly.express as px
import os
import matplotlib.pyplot as plt
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
df['Resolve Date'] = pd.to_datetime(df['Resolve Date'])

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



tab1, tab2, tab3 = st.tabs(["Regional", "Inquiries", "Reps"])

with tab1:
   st.write("blah")
with tab2:
  st.write("Blah")

with tab3:
   st.header("Representatives")
   st.pyplot(fig)
  