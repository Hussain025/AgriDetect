"""
Home Page - AgroDetect AI
Landing page with features and CTA
"""

import streamlit as st
from components.translation_service import t, init_translation_state
from components.navbar import render_navbar
from components.cards import feature_card
from components.auth import init_auth_state, require_auth
from components.chatbot_popup import render_floating_chatbot_button

# Page configuration
st.set_page_config(
    page_title="Home - AgroDetect AI",
    page_icon="🌱",
    layout="wide"
)

# Initialize
init_translation_state()
init_auth_state()

# Require authentication
require_auth()

# Load custom CSS
try:
    with open("assets/styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

render_navbar()

# ==================== HOME PAGE CONTENT ====================

# Header
st.markdown(f"""
<h1 style='text-align: center; color: #2e7d32; font-size: 48px; margin-bottom: 10px;'>
    🌱 {t('APP_TITLE')}
</h1>
""", unsafe_allow_html=True)

st.markdown(f"""
<h3 style='text-align: center; color: #558b2f; font-size: 24px; margin-bottom: 30px;'>
    {t('APP_SUBTITLE')}
</h3>
""", unsafe_allow_html=True)

st.markdown("---")

# Welcome message
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown(f"""
    <div class='feature-card' style='text-align: center; font-size: 18px; padding: 35px;'>
        <h2 style='color: #1b5e20; margin-bottom: 20px; font-weight: 600;'>{t('HOME_WELCOME')}</h2>
        <p style='color: #2e7d32; line-height: 1.8; font-size: 17px;'>{t('HOME_DESC')}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Features section
st.markdown(f"""
<h2 style='text-align: center; color: #2e7d32; margin-bottom: 30px;'>
    ✨ {t('FEATURES_TITLE')}
</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    feature_card(
        "🌱",
        t('FEATURE1_TITLE'),
        t('FEATURE1_DESC')
    )

with col2:
    feature_card(
        "🎯",
        t('FEATURE2_TITLE'),
        t('FEATURE2_DESC')
    )

with col3:
    feature_card(
        "📊",
        t('FEATURE3_TITLE'),
        t('FEATURE3_DESC')
    )

st.markdown("<br><br>", unsafe_allow_html=True)

# CTA Button
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button(t('GET_STARTED'), use_container_width=True, key="get_started_btn"):
        st.switch_page("pages/3_Upload.py")

# Render floating chatbot button
render_floating_chatbot_button()
