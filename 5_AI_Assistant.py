"""
AI Assistant Page - AgroDetect AI
Chatbot interface for plant disease Q&A
"""

import streamlit as st
from components.language import init_session_state, get_text, load_custom_css
from components.navbar import render_navbar
from components.chatbot_ui import render_chatbot
from components.auth import init_auth_state, require_auth

# Page configuration
st.set_page_config(
    page_title="AI Assistant - AgroDetect AI",
    page_icon="🤖",
    layout="wide"
)

# Initialize
init_session_state()
init_auth_state()

# Require authentication
require_auth()

load_custom_css()
render_navbar()

# ==================== AI ASSISTANT PAGE CONTENT ====================

# Header
st.markdown(f"""
<h1 style='text-align: center; color: #2e7d32; font-size: 42px;'>
    🤖 {get_text('chatbot_title')}
</h1>
""", unsafe_allow_html=True)

st.markdown(f"""
<h4 style='text-align: center; color: #558b2f; font-size: 18px; margin-bottom: 20px;'>
    {get_text('chatbot_subtitle')}
</h4>
""", unsafe_allow_html=True)

st.markdown("---")

# Description with glass effect
st.markdown(f"""
<div class='info-box' style='text-align: center; font-size: 16px; padding: 25px; margin-bottom: 30px;'>
    <p style='color: #1b5e20; margin: 0; font-size: 17px;'>💬 {get_text('chatbot_desc')}</p>
</div>
""", unsafe_allow_html=True)

# Render chatbot interface
render_chatbot()
