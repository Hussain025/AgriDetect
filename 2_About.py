"""
About Page - AgroDetect AI
Project overview, technologies, and how it works
"""

import streamlit as st
from components.language import init_session_state, get_text, load_custom_css
from components.navbar import render_navbar
from components.cards import step_card, tech_card
from components.auth import init_auth_state, require_auth

# Page configuration
st.set_page_config(
    page_title="About - AgroDetect AI",
    page_icon="📖",
    layout="wide"
)

# Initialize
init_session_state()
init_auth_state()

# Require authentication
require_auth()

load_custom_css()
render_navbar()

# ==================== ABOUT PAGE CONTENT ====================

# Header
st.markdown(f"""
<h1 style='text-align: center; color: #2e7d32; font-size: 42px;'>
    📖 {get_text('about_title')}
</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# What is AgroDetect AI
st.markdown(f"<h2 style='color: #2e7d32;'>🌿 {get_text('what_is')}</h2>", unsafe_allow_html=True)

st.markdown(f"""
<div style='font-size: 16px; line-height: 1.8; padding: 20px; 
            background-color: white; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
    <p style='color: #1b5e20; margin-bottom: 15px;'>{get_text('what_is_desc')}</p>
    <ul style='color: #1b5e20;'>
        <li style='margin: 10px 0;'>{get_text('helps_farmers')}</li>
        <li style='margin: 10px 0;'>{get_text('helps_gardeners')}</li>
        <li style='margin: 10px 0;'>{get_text('helps_experts')}</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Transfer Learning Section
st.markdown(f"<h2 style='color: #2e7d32;'>🧠 {get_text('transfer_learning')}</h2>", unsafe_allow_html=True)

st.markdown(f"""
<div style='padding: 20px; background-color: #e8f5e9; border-radius: 15px; 
            border-left: 5px solid #4CAF50;'>
    <p style='color: #1b5e20; font-size: 16px; line-height: 1.8;'>
        {get_text('transfer_desc')}
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# How it works
st.markdown(f"<h2 style='text-align: center; color: #2e7d32;'>⚙️ {get_text('how_works')}</h2>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    step_card(1, "📸", "Upload", get_text('step1'))

with col2:
    step_card(2, "🤖", "Analyze", get_text('step2'))

with col3:
    step_card(3, "✅", "Results", get_text('step3'))

st.markdown("<br>", unsafe_allow_html=True)

# Technologies
st.markdown(f"<h2 style='text-align: center; color: #2e7d32;'>🛠️ {get_text('tech_title')}</h2>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    tech_card(
        get_text('tech_prog'),
        [
            "🐍 <strong>Python</strong> - Core programming language",
            "🎨 <strong>Streamlit</strong> - Web application framework",
            "🖼️ <strong>OpenCV</strong> - Image processing library"
        ]
    )

with col2:
    tech_card(
        get_text('tech_ai'),
        [
            "🧠 <strong>TensorFlow</strong> - Deep learning framework",
            "🔥 <strong>Keras</strong> - Neural network API",
            "🎯 <strong>CNN</strong> - Convolutional Neural Networks",
            "📱 <strong>MobileNetV2</strong> - Transfer learning model"
        ]
    )
