import streamlit as st

def apply_custom_styles():
    st.markdown(
        """
        <style>
        /* Define your custom CSS styles here */
        .main-content {
            background-color: #697da4; /* You can change the color code here */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
