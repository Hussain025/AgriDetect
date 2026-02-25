"""
Signup Page - AgroDetect AI
User registration with Firebase
"""

import streamlit as st
from components.auth import init_auth_state, sign_up, is_authenticated, validate_email, validate_password
from components.language import init_session_state, get_text, load_custom_css
from components.navbar import render_navbar

# Page configuration
st.set_page_config(
    page_title="Signup - AgroDetect AI",
    page_icon="📝",
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

# ==================== SIGNUP PAGE CONTENT ====================

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
    📝 {get_text('signup_title')}
</h3>
""", unsafe_allow_html=True)

st.markdown("---")

# Signup form
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
    <div class='feature-card' style='padding: 40px;'>
    """, unsafe_allow_html=True)
    
    # Email input
    email = st.text_input(
        f"📧 {get_text('email')}",
        placeholder="Enter your email",
        key="signup_email"
    )
    
    # Password input
    password = st.text_input(
        f"🔒 {get_text('password')}",
        type="password",
        placeholder="Enter your password (min 6 characters)",
        key="signup_password",
        help="Password must be at least 6 characters long"
    )
    
    # Confirm password input
    confirm_password = st.text_input(
        f"🔒 {get_text('confirm_password')}",
        type="password",
        placeholder="Re-enter your password",
        key="signup_confirm_password"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Signup button
    if st.button(f"🚀 {get_text('signup_btn')}", use_container_width=True, key="signup_btn"):
        # Validation
        if not email or not password or not confirm_password:
            st.error("❌ Please fill in all fields")
        elif not validate_email(email):
            st.error("❌ Please enter a valid email address")
        elif password != confirm_password:
            st.error("❌ Passwords do not match")
        else:
            # Validate password strength
            is_valid, pwd_message = validate_password(password)
            if not is_valid:
                st.error(f"❌ {pwd_message}")
            else:
                # Attempt signup
                with st.spinner("🔄 Creating your account..."):
                    success, message, user_data = sign_up(email, password)
                    
                    if success:
                        st.success(f"✅ {message}")
                        st.balloons()
                        st.info("Please login with your new account")
                        
                        # Redirect to login after 2 seconds
                        import time
                        time.sleep(2)
                        st.switch_page("pages/0_Login.py")
                    else:
                        st.error(f"❌ {message}")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Login link
    st.markdown(f"""
    <div class='info-box' style='text-align: center; padding: 20px; margin-top: 20px;'>
        <p style='color: #1b5e20; font-size: 16px; margin: 0;'>
            {get_text('already_account')}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(f"🔐 {get_text('login_here')}", use_container_width=True, key="goto_login"):
        st.switch_page("pages/0_Login.py")

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #666; font-size: 14px;'>
    <p>🌱 AgroDetect AI - Plant Disease Classification Engine</p>
    <p>Secure authentication powered by Firebase</p>
</div>
""", unsafe_allow_html=True)
