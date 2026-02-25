# 🔐 Authentication System Guide

## Overview

AgroDetect AI now includes a complete Firebase Authentication system with login, signup, and access control features.

## 🎯 Features Implemented

### 1. User Registration (Signup)
- Email and password input fields
- Password confirmation validation
- Minimum password length (6 characters)
- Email format validation
- Firebase account creation
- Success message and redirect to login

### 2. User Login
- Email and password authentication
- Error handling for invalid credentials
- Session state management
- Automatic redirect to Home page on success
- Remember user across page navigation

### 3. User Logout
- Logout button in sidebar (visible when logged in)
- Clears all session data
- Redirects to login page
- Secure session termination

### 4. Access Control
- Protected pages require authentication
- Unauthenticated users redirected to login
- Login and Signup pages accessible without auth
- Session persistence across page navigation

## 📂 File Structure

```
components/
└── auth.py                 # Firebase authentication logic

pages/
├── 0_Login.py             # Login page (public)
├── 0_Signup.py            # Signup page (public)
├── 1_Home.py              # Protected page
├── 2_About.py             # Protected page
├── 3_Upload.py            # Protected page
├── 4_Results.py           # Protected page
├── 5_AI_Assistant.py      # Protected page
└── 6_Voice_Assistant.py   # Protected page
```

## 🔧 How It Works

### Authentication Flow

```
User visits app.py
    ↓
Check if authenticated?
    ↓
NO → Redirect to 0_Login.py
YES → Redirect to 1_Home.py
    ↓
User navigates to any page
    ↓
Page calls require_auth()
    ↓
Check if authenticated?
    ↓
NO → Show warning + redirect to login
YES → Show page content
```

### Session State Variables

```python
st.session_state.authenticated    # Boolean: Is user logged in?
st.session_state.user_email       # String: User's email
st.session_state.user_id          # String: Firebase user ID
st.session_state.id_token         # String: Firebase ID token
```

## 🔑 Key Functions in `components/auth.py`

### `init_auth_state()`
Initializes authentication session state variables.

```python
from components.auth import init_auth_state
init_auth_state()
```

### `sign_up(email, password)`
Creates a new user account with Firebase.

```python
success, message, user_data = sign_up(email, password)
if success:
    print("Account created!")
```

### `sign_in(email, password)`
Authenticates existing user and updates session state.

```python
success, message, user_data = sign_in(email, password)
if success:
    print("Logged in!")
```

### `sign_out()`
Logs out current user and clears session data.

```python
from components.auth import sign_out
sign_out()
```

### `is_authenticated()`
Checks if user is currently logged in.

```python
if is_authenticated():
    print("User is logged in")
```

### `require_auth()`
Protects pages - redirects to login if not authenticated.

```python
# At the top of any protected page
from components.auth import require_auth
require_auth()
```

### `get_current_user()`
Returns the email of the currently logged-in user.

```python
email = get_current_user()
print(f"Current user: {email}")
```

## 🎨 UI Components

### Login Page (`0_Login.py`)
- Clean, centered form
- Email input field
- Password input field (masked)
- Login button
- Link to signup page
- Error messages for invalid credentials

### Signup Page (`0_Signup.py`)
- Email input field
- Password input field (masked)
- Confirm password field (masked)
- Create account button
- Password validation
- Link to login page
- Success message on account creation

### Sidebar (Updated `navbar.py`)
- Shows user email when logged in
- Logout button (only visible when authenticated)
- Language selector
- Tips and footer

## 🔒 Security Features

### Password Validation
- Minimum 6 characters (Firebase requirement)
- Maximum 128 characters
- Client-side validation before API call

### Email Validation
- Regex pattern matching
- Format: `user@domain.com`
- Validated before Firebase API call

### Error Handling
- Invalid email format
- Email already exists
- Wrong password
- User not found
- Account disabled
- Connection errors

### Session Security
- Session data cleared on logout
- No password storage in session
- Firebase ID token for API calls
- Automatic session expiration (Firebase handles)

## 🚀 Usage Examples

### Protecting a New Page

```python
# pages/7_New_Page.py
import streamlit as st
from components.auth import init_auth_state, require_auth

st.set_page_config(page_title="New Page")

init_auth_state()
require_auth()  # This protects the page

# Your page content here
st.title("Protected Content")
```

### Checking Authentication Status

```python
from components.auth import is_authenticated, get_current_user

if is_authenticated():
    user_email = get_current_user()
    st.success(f"Welcome, {user_email}!")
else:
    st.warning("Please login to continue")
```

### Custom Logout Button

```python
from components.auth import sign_out

if st.button("Logout"):
    sign_out()
    st.success("Logged out!")
    st.rerun()
```

## 🧪 Testing the System

### Test Signup Flow:
1. Run `streamlit run app.py`
2. You'll be redirected to Login page
3. Click "Create New Account"
4. Enter email: `test@example.com`
5. Enter password: `test123456`
6. Confirm password: `test123456`
7. Click "Create Account"
8. Should see success message and redirect to login

### Test Login Flow:
1. On login page, enter the credentials you just created
2. Click "Login"
3. Should see success message and redirect to Home
4. Check sidebar - should show your email

### Test Protected Pages:
1. While logged in, navigate to any page (Home, About, Upload, etc.)
2. All pages should be accessible
3. Logout using sidebar button
4. Try to access any protected page
5. Should be redirected to login

### Test Session Persistence:
1. Login to the application
2. Navigate between different pages
3. Session should persist
4. Refresh the page
5. Should remain logged in (until browser session ends)

## ⚠️ Important Notes

### Firebase Configuration Required
Before using authentication, you MUST:
1. Create a Firebase project
2. Enable Email/Password authentication
3. Get your Firebase config
4. Update `components/auth.py` with your credentials

See `FIREBASE_SETUP.md` for detailed instructions.

### Demo Mode
The current configuration has placeholder Firebase credentials:
```python
FIREBASE_CONFIG = {
    "apiKey": "YOUR_FIREBASE_API_KEY",
    # ... other fields
}
```

Replace these with your actual Firebase project credentials.

### Production Deployment
For production:
1. Use Streamlit secrets (`.streamlit/secrets.toml`)
2. Never commit credentials to Git
3. Enable email verification in Firebase
4. Set up password reset functionality
5. Monitor authentication in Firebase Console

## 🐛 Troubleshooting

### "API key not valid" Error
- You haven't replaced the placeholder Firebase config
- Follow `FIREBASE_SETUP.md` to get your credentials

### "Connection error" Message
- Check internet connection
- Verify Firebase project is active
- Ensure API key is correct

### Pages Not Protected
- Make sure `require_auth()` is called at the top of the page
- Check that `init_auth_state()` is called before `require_auth()`

### Logout Not Working
- Check that `sign_out()` is being called
- Verify `st.rerun()` is called after logout
- Clear browser cache if issues persist

## 📚 Additional Resources

- Firebase Authentication Docs: https://firebase.google.com/docs/auth
- Firebase REST API: https://firebase.google.com/docs/reference/rest/auth
- Streamlit Session State: https://docs.streamlit.io/library/api-reference/session-state

## 🎓 Learning Points

This authentication system demonstrates:
- Firebase REST API integration
- Session state management in Streamlit
- Page protection and access control
- Form validation and error handling
- User experience design for auth flows
- Secure credential management
