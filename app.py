"""
AgroDetect AI - Main Application Entry Point
Redirects to Landing page (public access)
"""

import streamlit as st
from components.language import init_session_state, load_custom_css
from components.auth import init_auth_state

# Page configuration
st.set_page_config(
    page_title="AgroDetect AI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session states
init_session_state()
init_auth_state()

# Load custom CSS
load_custom_css()

# Always redirect to Landing page (public access)
st.switch_page("pages/0_Landing.py")
