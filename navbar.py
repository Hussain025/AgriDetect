"""
Navigation Bar Component
Displays different navigation based on authentication status
"""

import streamlit as st
from components.translation_service import t, render_language_selector, init_translation_state
from components.auth import is_authenticated, get_current_user, sign_out

def render_navbar():
    """Render sidebar navigation with conditional content based on auth status"""
    
    # Initialize translation state
    init_translation_state()
    
    # App title in sidebar
    st.sidebar.title(f"🌱 {t('APP_TITLE')}")
    st.sidebar.markdown("---")
    
    # Check authentication status
    if is_authenticated():
        # ========== AUTHENTICATED USER NAVIGATION ==========
        
        # Show user info
        st.sidebar.success(f"👤 **Logged in as:**\n{get_current_user()}")
        
        # Logout button
        if st.sidebar.button(f"🚪 {t('LOGOUT_BTN')}", use_container_width=True, key="logout_btn"):
            sign_out()
            st.success("✅ Logged out successfully!")
            st.info("Redirecting to landing page...")
            st.switch_page("pages/0_Landing.py")
        
        st.sidebar.markdown("---")
        
        # Navigation info for authenticated users
        st.sidebar.info("📍 **Navigation:**\nUse the page selector above to navigate between features.")
        
    else:
        # ========== PUBLIC / UNAUTHENTICATED NAVIGATION ==========
        
        st.sidebar.info("🔓 **Public Access**\nLogin to unlock all features!")
        
        st.sidebar.markdown("---")
        
        # Quick access buttons for public pages
        st.sidebar.markdown("### 🚀 Quick Access")
        
        if st.sidebar.button("🏠 Landing Page", use_container_width=True, key="nav_landing"):
            st.switch_page("pages/0_Landing.py")
        
        if st.sidebar.button(f"🔐 {t('LOGIN_BTN')}", use_container_width=True, key="nav_login"):
            st.switch_page("pages/0_Login.py")
        
        if st.sidebar.button(f"📝 {t('SIGNUP_BTN')}", use_container_width=True, key="nav_signup"):
            st.switch_page("pages/0_Signup.py")
        
        st.sidebar.markdown("---")
        
        # Feature preview for non-authenticated users
        st.sidebar.markdown("### 🔒 Protected Features")
        st.sidebar.markdown("""
        <div style='font-size: 14px; color: #666; line-height: 1.6;'>
        Login to access:
        • 🏠 Home Dashboard
        • 📖 About & Technology
        • 📤 Upload & Analyze
        • 📊 Results & Reports
        • 🎤 Voice Assistant
        • 📊 Crop History
        • 🌍 Sustainability
        </div>
        """, unsafe_allow_html=True)
    
    st.sidebar.markdown("---")
    
    # Language selector (available for all users)
    render_language_selector()
    
    st.sidebar.markdown("---")
    
    # Tip (conditional based on auth status)
    if is_authenticated():
        st.sidebar.info(t('TIP'))
    else:
        st.sidebar.success("💡 **Tip:** Create a free account to start detecting plant diseases!")
    
    st.sidebar.markdown("---")
    
    # Footer
    st.sidebar.markdown("""
    <div style='text-align: center; padding: 10px; color: #666;'>
        <small>© 2024 AgroDetect AI<br>Plant Disease Detection</small>
    </div>
    """, unsafe_allow_html=True)
