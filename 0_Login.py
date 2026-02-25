"""
Login Page - AgroDetect AI
User authentication with Firebase
"""

import streamlit as st
from components.auth import init_auth_state, sign_in, is_authenticated, validate_email
from components.language import init_session_state, get_text, load_custom_css
from components.navbar import render_navbar

# Page configuration
st.set_page_config(
    page_title="Login - AgroDetect AI",
    page_icon="🔐",
    layout="centered"
)

# Initialize
init_session_state()
init_auth_state()
load_custom_css()

# Render navbar with language selector
render_navbar()

# Redirect if already logged in
if is_authenticated():
    st.success("✅ You are already logged in!")
    st.info("Redirecting to Home page...")
    if st.button("Go to Home", use_container_width=True):
        st.switch_page("pages/1_Home.py")
    st.stop()

# ==================== LOGIN PAGE CONTENT ====================

# Back to Landing button
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button(f"← {get_text('back_to_landing')}", key="back_to_landing"):
        st.switch_page("pages/0_Landing.py")

st.markdown("<br>", unsafe_allow_html=True)

# Header
st.markdown(f"""
<h1 style='text-align: center; color: #2e7d32; font-size: 42px;'>
    🌱 {get_text('app_title')}
</h1>
""", unsafe_allow_html=True)

st.markdown(f"""
<h3 style='text-align: center; color: #558b2f; margin-bottom: 30px;'>
    🔐 {get_text('login_title')}
</h3>
""", unsafe_allow_html=True)

st.markdown("---")

# Login form
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div class='feature-card' style='padding: 40px;'>
    """, unsafe_allow_html=True)
    
    # Email input
    email = st.text_input(
        f"📧 {get_text('email')}",
        placeholder="Enter your email",
        key="login_email"
    )
    
    # Password input
    password = st.text_input(
        f"🔒 {get_text('password')}",
        type="password",
        placeholder="Enter your password",
        key="login_password"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Login button
    if st.button(f"🚀 {get_text('login_btn')}", use_container_width=True, key="login_btn"):
        # Validation
        if not email or not password:
            st.error("❌ Please fill in all fields")
        elif not validate_email(email):
            st.error("❌ Please enter a valid email address")
        else:
            # Attempt login
            with st.spinner("🔄 Logging in..."):
                success, message, user_data = sign_in(email, password)
                
                if success:
                    st.success(f"✅ {message}")
                    st.balloons()
                    st.info("Redirecting to Home page...")
                    st.rerun()
                else:
                    st.error(f"❌ {message}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Signup link
    st.markdown(f"""
    <div class='info-box' style='text-align: center; padding: 20px; margin-top: 20px;'>
        <p style='color: #1b5e20; font-size: 16px; margin: 0;'>
            {get_text('no_account')}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(f"📝 {get_text('create_account')}", use_container_width=True, key="goto_signup"):
        st.switch_page("pages/0_Signup.py")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #666; font-size: 14px;'>
    <p>🌱 AgroDetect AI - Plant Disease Classification Engine</p>
    <p>Secure authentication powered by Firebase</p>
</div>
""", unsafe_allow_html=True)
