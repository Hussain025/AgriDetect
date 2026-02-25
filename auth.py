"""
Firebase Authentication Component
Handles user authentication using Firebase REST API
"""

import streamlit as st
import requests
import json

# ==================== FIREBASE CONFIGURATION ====================
# Replace these with your Firebase project credentials
# You can also use st.secrets for production deployment

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyCgwCPxwM8R8vuZ1BInOu9C0ltd8rnyk6g",
    "authDomain": "agrodetect-ai.firebaseapp.com",
    "projectId": "agrodetect-ai",
    "storageBucket": "agrodetect-ai.firebasestorage.app",
    "messagingSenderId": "596519045909",
    "appId": "1:596519045909:web:23dcf1579a1ebc7c6bf71c"
}

# Firebase REST API endpoints
FIREBASE_AUTH_URL = "https://identitytoolkit.googleapis.com/v1/accounts"
API_KEY = FIREBASE_CONFIG["apiKey"]

# ==================== AUTHENTICATION FUNCTIONS ====================

def init_auth_state():
    """Initialize authentication session state"""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user_email' not in st.session_state:
        st.session_state.user_email = None
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    if 'id_token' not in st.session_state:
        st.session_state.id_token = None

def sign_up(email, password):
    """
    Create a new user account with Firebase
    
    Args:
        email (str): User email
        password (str): User password
    
    Returns:
        tuple: (success: bool, message: str, user_data: dict)
    """
    try:
        url = f"{FIREBASE_AUTH_URL}:signUp?key={API_KEY}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        
        response = requests.post(url, json=payload)
        data = response.json()
        
        if response.status_code == 200:
            return True, "Account created successfully!", data
        else:
            error_message = data.get('error', {}).get('message', 'Unknown error')
            
            # Handle common Firebase errors
            if error_message == "EMAIL_EXISTS":
                return False, "This email is already registered. Please login.", None
            elif error_message == "INVALID_EMAIL":
                return False, "Invalid email format.", None
            elif error_message == "WEAK_PASSWORD":
                return False, "Password should be at least 6 characters.", None
            else:
                return False, f"Error: {error_message}", None
                
    except Exception as e:
        return False, f"Connection error: {str(e)}", None

def sign_in(email, password):
    """
    Sign in existing user with Firebase
    
    Args:
        email (str): User email
        password (str): User password
    
    Returns:
        tuple: (success: bool, message: str, user_data: dict)
    """
    try:
        url = f"{FIREBASE_AUTH_URL}:signInWithPassword?key={API_KEY}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        
        response = requests.post(url, json=payload)
        data = response.json()
        
        if response.status_code == 200:
            # Store user data in session state
            st.session_state.authenticated = True
            st.session_state.user_email = data.get('email')
            st.session_state.user_id = data.get('localId')
            st.session_state.id_token = data.get('idToken')
            
            return True, "Login successful!", data
        else:
            error_message = data.get('error', {}).get('message', 'Unknown error')
            
            # Handle common Firebase errors
            if error_message == "EMAIL_NOT_FOUND":
                return False, "Email not found. Please sign up first.", None
            elif error_message == "INVALID_PASSWORD":
                return False, "Incorrect password. Please try again.", None
            elif error_message == "INVALID_EMAIL":
                return False, "Invalid email format.", None
            elif error_message == "USER_DISABLED":
                return False, "This account has been disabled.", None
            else:
                return False, f"Error: {error_message}", None
                
    except Exception as e:
        return False, f"Connection error: {str(e)}", None

def sign_out():
    """Sign out current user and clear session state"""
    st.session_state.authenticated = False
    st.session_state.user_email = None
    st.session_state.user_id = None
    st.session_state.id_token = None
    
    # Clear other session data
    if 'uploaded_image' in st.session_state:
        st.session_state.uploaded_image = None
    if 'analysis_done' in st.session_state:
        st.session_state.analysis_done = False
    if 'chat_history' in st.session_state:
        st.session_state.chat_history = []
    if 'voice_text' in st.session_state:
        st.session_state.voice_text = ""
    if 'voice_response' in st.session_state:
        st.session_state.voice_response = ""

def is_authenticated():
    """Check if user is authenticated"""
    return st.session_state.get('authenticated', False)

def get_current_user():
    """Get current user email"""
    return st.session_state.get('user_email', None)

def require_auth():
    """
    Decorator/function to protect pages that require authentication
    Redirects to login if user is not authenticated
    """
    if not is_authenticated():
        st.warning("⚠️ Please login to access this page.")
        st.info("👉 Redirecting to login page...")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Go to Login", use_container_width=True):
                st.switch_page("pages/0_Login.py")
        
        st.stop()

def validate_email(email):
    """Basic email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password(password):
    """
    Validate password strength
    
    Returns:
        tuple: (is_valid: bool, message: str)
    """
    if len(password) < 6:
        return False, "Password must be at least 6 characters long"
    if len(password) > 128:
        return False, "Password is too long"
    return True, "Password is valid"

# ==================== UI HELPER FUNCTIONS ====================

def render_logout_button():
    """Render logout button in sidebar"""
    if is_authenticated():
        st.sidebar.markdown("---")
        st.sidebar.success(f"👤 Logged in as:\n{get_current_user()}")
        
        if st.sidebar.button("🚪 Logout", use_container_width=True):
            sign_out()
            st.success("Logged out successfully!")
            st.rerun()
