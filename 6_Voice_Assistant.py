"""
Voice Assistant Page - AgroDetect AI
Voice interaction interface with multi-language support
"""

import streamlit as st
from components.language import init_session_state, get_text, load_custom_css
from components.navbar import render_navbar
from components.voice_ui import render_voice_assistant
from components.auth import init_auth_state, require_auth

# Page configuration
st.set_page_config(
    page_title="Voice Assistant - AgroDetect AI",
    page_icon="🎤",
    layout="wide"
)

# Initialize
init_session_state()
init_auth_state()

# Require authentication
require_auth()

load_custom_css()
render_navbar()

# ==================== VOICE ASSISTANT PAGE CONTENT ====================

# Header
st.markdown(f"""
<h1 style='text-align: center; color: #2e7d32; font-size: 42px;'>
    🎤 {get_text('voice_title')}
</h1>
""", unsafe_allow_html=True)

st.markdown(f"""
<h4 style='text-align: center; color: #558b2f; font-size: 18px; margin-bottom: 20px;'>
    {get_text('voice_subtitle')}
</h4>
""", unsafe_allow_html=True)

st.markdown("---")

# Description with real-time AI info
st.markdown(f"""
<div class='info-box' style='text-align: center; font-size: 16px; padding: 25px; margin-bottom: 30px;'>
    <p style='color: #0d3d0d; margin: 0; font-size: 17px; font-weight: 600;'>🗣️ {get_text('voice_desc')}</p>
    <p style='color: #2e7d32; margin: 15px 0 0 0; font-weight: 700; font-size: 18px;'>
        🌍 Current Language: {st.session_state.language}
    </p>
    <p style='color: #1b5e20; margin: 10px 0 0 0; font-size: 15px;'>
        🤖 Powered by Gemini AI | 🔊 Real-time Voice Output
    </p>
</div>
""", unsafe_allow_html=True)

# Render voice assistant interface
render_voice_assistant()
