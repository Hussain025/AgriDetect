"""
Landing Page - AgroDetect AI
Public page accessible without authentication
"""

import streamlit as st
from components.language import init_session_state, get_text, load_custom_css
from components.auth import init_auth_state, is_authenticated
from components.navbar import render_navbar
from components.chatbot_popup import render_floating_chatbot_button

# Page configuration
st.set_page_config(
    page_title="AgroDetect AI - Plant Disease Detection",
    page_icon="🌱",
    layout="wide"
)

# Initialize
init_session_state()
init_auth_state()
load_custom_css()

# Render navbar with language selector
render_navbar()

# If user is already logged in, redirect to Home
if is_authenticated():
    st.info("✅ You are already logged in! Redirecting to Home...")
    if st.button("Go to Home", use_container_width=True):
        st.switch_page("pages/1_Home.py")
    st.stop()

# ==================== LANDING PAGE CONTENT ====================

# Hero Section
st.markdown(f"""
<div class='feature-card' style='text-align: center; padding: 60px 30px; margin: 20px auto; max-width: 1200px; animation: fadeIn 0.8s ease-out;'>
    <h1 style='color: #1b5e20; font-size: 56px; margin-bottom: 15px; text-shadow: 0 2px 8px rgba(0,0,0,0.1); animation: fadeIn 1s ease-out;'>
        🌱 {get_text('landing_hero_title')}
    </h1>
    <h2 style='color: #2e7d32; font-size: 32px; margin-bottom: 25px; animation: fadeIn 1.2s ease-out;'>
        {get_text('landing_hero_subtitle')}
    </h2>
    <p style='color: #1b5e20; font-size: 20px; line-height: 1.8; max-width: 800px; margin: 0 auto; animation: fadeIn 1.4s ease-out;'>
        {get_text('landing_hero_desc')}
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Call-to-Action Buttons
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col2:
    if st.button(f"🚀 {get_text('get_started_login')}", use_container_width=True, key="cta_login"):
        st.switch_page("pages/0_Login.py")

with col4:
    if st.button(f"📝 {get_text('signup_free')}", use_container_width=True, key="cta_signup"):
        st.switch_page("pages/0_Signup.py")

st.markdown("<br><br>", unsafe_allow_html=True)

# Features Section
st.markdown(f"""
<h2 style='text-align: center; color: #2e7d32; font-size: 36px; margin-bottom: 40px;'>
    ✨ {get_text('powerful_features')}
</h2>
""", unsafe_allow_html=True)

# Feature Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class='feature-card' style='text-align: center; padding: 30px 20px; height: 280px;'>
        <div style='font-size: 64px; margin-bottom: 15px; animation: pulse 2s ease-in-out infinite;'>🌱</div>
        <h3 style='color: #1b5e20; margin-bottom: 15px; font-weight: 600;'>{get_text('disease_detection')}</h3>
        <p style='color: #2e7d32; line-height: 1.6;'>
            {get_text('disease_detection_desc')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='feature-card' style='text-align: center; padding: 30px 20px; height: 280px;'>
        <div style='font-size: 64px; margin-bottom: 15px; animation: pulse 2s ease-in-out infinite 0.2s;'>🤖</div>
        <h3 style='color: #1b5e20; margin-bottom: 15px; font-weight: 600;'>{get_text('ai_assistant')}</h3>
        <p style='color: #2e7d32; line-height: 1.6;'>
            {get_text('ai_assistant_desc')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='feature-card' style='text-align: center; padding: 30px 20px; height: 280px;'>
        <div style='font-size: 64px; margin-bottom: 15px; animation: pulse 2s ease-in-out infinite 0.4s;'>🎤</div>
        <h3 style='color: #1b5e20; margin-bottom: 15px; font-weight: 600;'>{get_text('voice_support')}</h3>
        <p style='color: #2e7d32; line-height: 1.6;'>
            {get_text('voice_support_desc')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class='feature-card' style='text-align: center; padding: 30px 20px; height: 280px;'>
        <div style='font-size: 64px; margin-bottom: 15px; animation: pulse 2s ease-in-out infinite 0.6s;'>🌍</div>
        <h3 style='color: #1b5e20; margin-bottom: 15px; font-weight: 600;'>{get_text('multi_language')}</h3>
        <p style='color: #2e7d32; line-height: 1.6;'>
            {get_text('multi_language_desc')}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# How It Works Section
st.markdown(f"""
<h2 style='text-align: center; color: #2e7d32; font-size: 36px; margin-bottom: 40px;'>
    ⚙️ {get_text('how_it_works')}
</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class='tech-card' style='text-align: center; padding: 30px; height: 250px;'>
        <div style='font-size: 72px; margin-bottom: 15px;'>📸</div>
        <h3 style='color: #1b5e20; margin-bottom: 10px; font-weight: 600;'>{get_text('step_1')}</h3>
        <h4 style='color: #2e7d32; margin-bottom: 10px;'>{get_text('upload_image')}</h4>
        <p style='color: #2e7d32;'>
            {get_text('upload_image_desc')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='tech-card' style='text-align: center; padding: 30px; height: 250px;'>
        <div style='font-size: 72px; margin-bottom: 15px;'>🧠</div>
        <h3 style='color: #1b5e20; margin-bottom: 10px; font-weight: 600;'>{get_text('step_2')}</h3>
        <h4 style='color: #2e7d32; margin-bottom: 10px;'>{get_text('ai_analysis')}</h4>
        <p style='color: #2e7d32;'>
            {get_text('ai_analysis_desc')}
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='tech-card' style='text-align: center; padding: 30px; height: 250px;'>
        <div style='font-size: 72px; margin-bottom: 15px;'>✅</div>
        <h3 style='color: #1b5e20; margin-bottom: 10px; font-weight: 600;'>{get_text('step_3')}</h3>
        <h4 style='color: #2e7d32; margin-bottom: 10px;'>{get_text('get_results')}</h4>
        <p style='color: #2e7d32;'>
            {get_text('get_results_desc')}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Technology Section
st.markdown(f"""
<h2 style='text-align: center; color: #2e7d32; font-size: 36px; margin-bottom: 40px;'>
    🛠️ {get_text('powered_by')}
</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div class='feature-card' style='padding: 40px;'>
        <ul style='font-size: 18px; line-height: 2.2; color: #1b5e20; list-style: none; padding: 0;'>
            <li style='margin: 12px 0; transition: transform 0.3s ease;'>🧠 <strong>Deep Learning</strong> - Neural networks for accurate predictions</li>
            <li style='margin: 12px 0; transition: transform 0.3s ease;'>📱 <strong>MobileNetV2</strong> - Efficient transfer learning architecture</li>
            <li style='margin: 12px 0; transition: transform 0.3s ease;'>🎯 <strong>CNN</strong> - Convolutional Neural Networks for image analysis</li>
            <li style='margin: 12px 0; transition: transform 0.3s ease;'>🔥 <strong>TensorFlow & Keras</strong> - Industry-standard ML frameworks</li>
            <li style='margin: 12px 0; transition: transform 0.3s ease;'>🐍 <strong>Python & Streamlit</strong> - Modern web application stack</li>
            <li style='margin: 12px 0; transition: transform 0.3s ease;'>🔐 <strong>Firebase Auth</strong> - Secure user authentication</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Final CTA Section
st.markdown(f"""
<div class='feature-card glow-effect' style='text-align: center; padding: 60px 30px; margin: 40px auto; max-width: 1000px;'>
    <h2 style='color: #1b5e20; font-size: 36px; margin-bottom: 20px; font-weight: 700;'>
        {get_text('ready_to_protect')}
    </h2>
    <p style='color: #2e7d32; font-size: 20px; margin-bottom: 30px;'>
        {get_text('join_farmers')}
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

with col2:
    if st.button(f"🔐 {get_text('login_now')}", use_container_width=True, key="footer_login"):
        st.switch_page("pages/0_Login.py")

with col4:
    if st.button(f"📝 {get_text('create_account_btn')}", use_container_width=True, key="footer_signup"):
        st.switch_page("pages/0_Signup.py")

st.markdown("<br>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style='text-align: center; padding: 30px; color: #666; font-size: 14px;'>
    <p style='margin: 5px 0;'>🌱 AgroDetect AI - Plant Disease Classification Engine</p>
    <p style='margin: 5px 0;'>Empowering Agriculture with Artificial Intelligence</p>
    <p style='margin: 5px 0;'>© 2024 AgroDetect AI. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)

# Render floating chatbot button (available for all users)
render_floating_chatbot_button()
