"""
Firebase Configuration and Authentication Module
Handles Firebase Authentication and Realtime Database operations
"""

import os
from dotenv import load_dotenv
import pyrebase
import firebase_admin
from firebase_admin import credentials, auth, db
import streamlit as st
import json

# Load environment variables
load_dotenv()

# Firebase configuration from .env
firebase_config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}

# Initialize Pyrebase (for client-side auth)
try:
    firebase = pyrebase.initialize_app(firebase_config)
    firebase_auth = firebase.auth()
    firebase_db = firebase.database()
    FIREBASE_ENABLED = True
except Exception as e:
    st.error(f"❌ Firebase initialization failed: {str(e)}")
    st.error("⚠️ Please check your .env file and Firebase configuration.")
    st.stop()
    FIREBASE_ENABLED = False
    firebase_auth = None
    firebase_db = None

# Initialize Firebase Admin SDK (for server-side operations)
try:
    if not firebase_admin._apps:
        admin_cred_path = os.getenv("FIREBASE_ADMIN_CREDENTIALS")
        if admin_cred_path and os.path.exists(admin_cred_path):
            cred = credentials.Certificate(admin_cred_path)
            firebase_admin.initialize_app(cred, {
                'databaseURL': os.getenv("FIREBASE_DATABASE_URL")
            })
            FIREBASE_ADMIN_ENABLED = True
        else:
            FIREBASE_ADMIN_ENABLED = False
    else:
        FIREBASE_ADMIN_ENABLED = True
except Exception as e:
    FIREBASE_ADMIN_ENABLED = False

class FirebaseAuth:
    """Firebase Authentication Handler"""
    
    @staticmethod
    def sign_up(email, password, username):
        """
        Create a new user with Firebase Authentication
        Returns: (success, message, user_data)
        """
        if not FIREBASE_ENABLED:
            return False, "❌ Firebase is not configured. Please check your .env file.", None
        
        try:
            # Create user with email and password
            user = firebase_auth.create_user_with_email_and_password(email, password)
            
            # Get user ID token
            id_token = user['idToken']
            user_id = user['localId']
            
            # Store additional user data in Realtime Database
            user_data = {
                'username': username,
                'email': email,
                'created_at': str(st.session_state.get('timestamp', '')),
                'total_analyses': 0,
                'last_login': ''
            }
            
            firebase_db.child("users").child(user_id).set(user_data)
            
            return True, "✅ Account created successfully!", {
                'user_id': user_id,
                'email': email,
                'username': username,
                'id_token': id_token
            }
            
        except Exception as e:
            error_message = str(e)
            
            # Check for specific Firebase errors
            if "CONFIGURATION_NOT_FOUND" in error_message:
                return False, "❌ Firebase Authentication not enabled. Please enable it in Firebase Console.", None
            elif "EMAIL_EXISTS" in error_message:
                return False, "❌ Email already registered. Please login instead.", None
            elif "WEAK_PASSWORD" in error_message:
                return False, "❌ Password should be at least 6 characters", None
            elif "INVALID_EMAIL" in error_message:
                return False, "❌ Invalid email format", None
            else:
                # Return specific error without fallback message
                return False, f"❌ Firebase error: {error_message}", None
    
    @staticmethod
    def sign_in(email, password):
        """
        Sign in user with Firebase Authentication
        Returns: (success, message, user_data)
        """
        if not FIREBASE_ENABLED:
            return False, "❌ Firebase is not configured. Please check your .env file.", None
        
        try:
            # Sign in with email and password
            user = firebase_auth.sign_in_with_email_and_password(email, password)
            
            user_id = user['localId']
            id_token = user['idToken']
            
            # Get user data from database
            user_data = firebase_db.child("users").child(user_id).get().val()
            
            if not user_data:
                user_data = {
                    'username': email.split('@')[0],
                    'email': email,
                    'total_analyses': 0
                }
            
            # Update last login
            firebase_db.child("users").child(user_id).update({
                'last_login': str(st.session_state.get('timestamp', ''))
            })
            
            return True, "✅ Login successful!", {
                'user_id': user_id,
                'email': email,
                'username': user_data.get('username', email.split('@')[0]),
                'id_token': id_token,
                'total_analyses': user_data.get('total_analyses', 0)
            }
            
        except Exception as e:
            error_message = str(e)
            
            # Check for specific Firebase errors
            if "INVALID_EMAIL" in error_message:
                return False, "❌ Invalid email format", None
            elif "EMAIL_NOT_FOUND" in error_message or "USER_NOT_FOUND" in error_message:
                return False, "❌ No account found with this email. Please sign up first.", None
            elif "INVALID_PASSWORD" in error_message or "WRONG_PASSWORD" in error_message:
                return False, "❌ Incorrect password. Please try again.", None
            elif "USER_DISABLED" in error_message:
                return False, "❌ This account has been disabled.", None
            else:
                # Return specific error
                return False, f"❌ Login failed: {error_message}", None
    
    @staticmethod
    def reset_password(email):
        """Send password reset email"""
        if not FIREBASE_ENABLED:
            return False, "Firebase is not configured"
        
        try:
            firebase_auth.send_password_reset_email(email)
            return True, "Password reset email sent!"
        except Exception as e:
            return False, f"Failed to send reset email: {str(e)}"
    
    @staticmethod
    def verify_token(id_token):
        """Verify Firebase ID token"""
        if not FIREBASE_ADMIN_ENABLED:
            return None
        
        try:
            decoded_token = auth.verify_id_token(id_token)
            return decoded_token
        except Exception as e:
            return None

class FirebaseDatabase:
    """Firebase Realtime Database Handler"""
    
    @staticmethod
    def save_analysis(user_id, analysis_data):
        """Save analysis result to Firebase"""
        if not FIREBASE_ENABLED:
            return False
        
        try:
            # Save to user's analysis history
            firebase_db.child("users").child(user_id).child("analyses").push(analysis_data)
            
            # Update total analyses count
            user_data = firebase_db.child("users").child(user_id).get().val()
            current_count = user_data.get('total_analyses', 0) if user_data else 0
            firebase_db.child("users").child(user_id).update({
                'total_analyses': current_count + 1
            })
            
            return True
        except Exception as e:
            st.error(f"Failed to save analysis: {str(e)}")
            return False
    
    @staticmethod
    def get_user_analyses(user_id, limit=10):
        """Get user's analysis history from Firebase"""
        if not FIREBASE_ENABLED:
            return []
        
        try:
            analyses = firebase_db.child("users").child(user_id).child("analyses").get()
            
            if not analyses.val():
                return []
            
            # Convert to list and sort by timestamp
            analysis_list = []
            for key, value in analyses.val().items():
                value['id'] = key
                analysis_list.append(value)
            
            # Sort by timestamp (newest first)
            analysis_list.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
            
            return analysis_list[:limit]
        except Exception as e:
            st.error(f"Failed to load analyses: {str(e)}")
            return []
    
    @staticmethod
    def get_user_stats(user_id):
        """Get user statistics from Firebase"""
        if not FIREBASE_ENABLED:
            return 0, 0
        
        try:
            user_data = firebase_db.child("users").child(user_id).get().val()
            
            if not user_data:
                return 0, 0
            
            total_analyses = user_data.get('total_analyses', 0)
            
            # Get unique diseases
            analyses = firebase_db.child("users").child(user_id).child("analyses").get()
            unique_diseases = set()
            
            if analyses.val():
                for analysis in analyses.val().values():
                    unique_diseases.add(analysis.get('disease_name', ''))
            
            return total_analyses, len(unique_diseases)
        except Exception as e:
            return 0, 0
    
    @staticmethod
    def get_total_users():
        """Get total number of registered users"""
        if not FIREBASE_ENABLED:
            return 0
        
        try:
            users = firebase_db.child("users").get()
            return len(users.val()) if users.val() else 0
        except Exception as e:
            return 0
    
    @staticmethod
    def clear_user_history(user_id):
        """Clear user's analysis history"""
        if not FIREBASE_ENABLED:
            return False
        
        try:
            firebase_db.child("users").child(user_id).child("analyses").remove()
            firebase_db.child("users").child(user_id).update({'total_analyses': 0})
            return True
        except Exception as e:
            st.error(f"Failed to clear history: {str(e)}")
            return False

# Export functions
def is_firebase_enabled():
    """Check if Firebase is properly configured"""
    return FIREBASE_ENABLED

def get_firebase_config():
    """Get Firebase configuration (for debugging)"""
    return {
        'enabled': FIREBASE_ENABLED,
        'admin_enabled': FIREBASE_ADMIN_ENABLED,
        'project_id': firebase_config.get('projectId', 'Not configured')
    }
