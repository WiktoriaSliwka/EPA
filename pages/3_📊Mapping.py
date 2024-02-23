import streamlit as st
import pandas as pd
import plotly.express as px
import os
css_file = os.path.abspath("style.css")

def local_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css()


st.markdown('<div class="banner">BeepBoop</div>', unsafe_allow_html=True)