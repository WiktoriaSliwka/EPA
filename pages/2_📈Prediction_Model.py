import streamlit as st
import pandas as pd
import plotly.express as px


# Display the prediction model section
st.header("Prediction Model")
st.write("The prediction model calculates how many reps are needed per day/per week based on previous volumes.")