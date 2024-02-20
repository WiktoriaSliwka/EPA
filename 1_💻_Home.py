import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# data = pd.read_csv("C:/Users/wsliwka/Documents/EPA/employees hc.csv")

st.title("BLOOMBERG")
st.header("Rep Schedule")
st.write("This shows Bloomberg ticket volumes over time.")

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
