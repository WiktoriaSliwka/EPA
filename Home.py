import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import os
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

tab1, tab2, tab3 = st.tabs(["Month", "Week", "Day"])

with tab1:
   st.header("Monthly ticket distribution")
   st.image("graphs/linegraph.png")

with tab2:
   st.header("Weekly ticket distribution")
   st.image("graphs/weekly.png")

with tab3:
   st.header("Dailey ticket distribution")
   st.image("graphs/dailey.png")













# 📊💻📈🗄️🌍
# DEFAULT_PAGE = "main.py"
# with st.sidebar:
#     selected = option_menu(
#         menu_title= "Docs",
#         options=["Home", "Prediction_Model","Mapping"],
#         icons=["house", "chart","graph"]
#     )

# selected = option_menu(
#         menu_title= "Docs",
#         options=["Home", "Prediction Model","Mapping"],
#         icons=["house", "chart","graph"],
#         default_index=0,
#         orientation="horizontal",
#         styles={
#         "container": {"padding": "0!important", "background-color": "defult"},
#         "icon":{"color": "blue", "font-size": "25px"},
#         "nav-link": {
#             "font-size": "25px",
#             "text-align": "left",
#             "margin": "0px",
#             "--hover-color": "#eee",
#          },
#         "nav-link-selected": {"background-color": "green"},
#     }
#     )

# if selected == "Home":
#     st.title(f"Next {selected}")
# if selected == "Prediction Model":
#     st.title(f"Next {selected}")
# if selected == "Mapping":
#     st.title(f"Next {selected}")
# st.page_link("http://www.google.com", label="Google")


# # Objective
# st.header("Objective")
# st.write("The objective of the project is to develop a scheduler to help service teams arrange for client coverage.")

# # business reason
# st.header("Business Reason")
# st.write("Service teams will benefit from this information as they can use it to arrange for queue coverage.")
