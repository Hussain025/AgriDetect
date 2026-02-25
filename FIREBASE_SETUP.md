# Firebase Authentication Setup Guide

## 🔥 Firebase Project Setup

Follow these steps to set up Firebase Authentication for AgroDetect AI:

### Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project" or "Create a project"
3. Enter project name: `agrodetect-ai` (or your preferred name)
4. Disable Google Analytics (optional for this project)
5. Click "Create project"

### Step 2: Enable Email/Password Authentication

1. In your Firebase project, click on "Authentication" in the left sidebar
2. Click "Get started"
3. Go to "Sign-in method" tab
4. Click on "Email/Password"
5. Enable the first toggle (Email/Password)
6. Click "Save"

### Step 3: Get Firebase Configuration

1. Click on the gear icon (⚙️) next to "Project Overview"
2. Select "Project settings"
3. Scroll down to "Your apps" section
4. Click on the web icon (</>) to add a web app
5. Register app with nickname: "AgroDetect AI Web"
6. Copy the Firebase configuration object

It will look like this:

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  authDomain: "your-project-id.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project-id.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:abcdef1234567890"
};
```

### Step 4: Update Application Configuration

Open `components/auth.py` and replace the `FIREBASE_CONFIG` dictionary with your values:

```python
FIREBASE_CONFIG = {
    "apiKey": "YOUR_API_KEY_HERE",
    "authDomain": "your-project-id.firebaseapp.com",
    "projectId": "your-project-id",
    "storageBucket": "your-project-id.appspot.com",
    "messagingSenderId": "YOUR_SENDER_ID",
    "appId": "YOUR_APP_ID"
}
```

### Step 5 (Optional): Use Streamlit Secrets

For production deployment, use Streamlit secrets instead of hardcoding:

1. Create `.streamlit/secrets.toml` file in your project root:

```toml
[firebase]
apiKey = "YOUR_API_KEY_HERE"
authDomain = "your-project-id.firebaseapp.com"
projectId = "your-project-id"
storageBucket = "your-project-id.appspot.com"
messagingSenderId = "YOUR_SENDER_ID"
appId = "YOUR_APP_ID"
```

2. Update `components/auth.py` to use secrets:

```python
import streamlit as st

# Try to load from secrets, fallback to hardcoded config
try:
    FIREBASE_CONFIG = {
        "apiKey": st.secrets["firebase"]["apiKey"],
        "authDomain": st.secrets["firebase"]["authDomain"],
        "projectId": st.secrets["firebase"]["projectId"],
        "storageBucket": st.secrets["firebase"]["storageBucket"],
        "messagingSenderId": st.secrets["firebase"]["messagingSenderId"],
        "appId": st.secrets["firebase"]["appId"]
    }
except:
    # Fallback to hardcoded config
    FIREBASE_CONFIG = {
        "apiKey": "YOUR_API_KEY_HERE",
        # ... rest of config
    }
```

## 🧪 Testing Authentication

### Test Signup:
1. Run the application: `streamlit run app.py`
2. Navigate to Signup page
3. Enter email: `test@example.com`
4. Enter password: `test123456`
5. Confirm password: `test123456`
6. Click "Create Account"

### Test Login:
1. Navigate to Login page
2. Enter the email and password you just created
3. Click "Login"
4. You should be redirected to Home page

### Test Logout:
1. Click "Logout" button in the sidebar
2. You should be redirected to Login page

## 🔒 Security Best Practices

1. **Never commit secrets to Git**
   - Add `.streamlit/secrets.toml` to `.gitignore`
   - Use environment variables or Streamlit secrets

2. **Enable Email Verification** (Optional)
   - In Firebase Console → Authentication → Templates
   - Customize email verification template

3. **Set Password Policy**
   - Firebase enforces minimum 6 characters by default
   - Consider adding additional client-side validation

4. **Monitor Authentication**
   - Check Firebase Console → Authentication → Users
   - Monitor sign-in attempts and errors

## 🚀 Deployment

### Streamlit Cloud:
1. Push code to GitHub (without secrets)
2. Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
3. Add secrets in Streamlit Cloud dashboard:
   - Go to app settings → Secrets
   - Paste your `secrets.toml` content

### Other Platforms:
- Set environment variables for Firebase config
- Ensure `requests` package is installed
- Configure secrets management per platform

## 📝 API Endpoints Used

This application uses Firebase REST API:
- **Sign Up**: `https://identitytoolkit.googleapis.com/v1/accounts:signUp`
- **Sign In**: `https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword`

No additional Firebase SDK installation required!

## ❓ Troubleshooting

### "API key not valid" error:
- Check that you copied the correct API key from Firebase Console
- Ensure the API key is not restricted

### "EMAIL_EXISTS" error:
- User already registered with that email
- Try logging in instead of signing up

### "INVALID_PASSWORD" error:
- Check password is correct
- Password is case-sensitive

### Connection errors:
- Check internet connection
- Verify Firebase project is active
- Check API key is correct

## 📚 Additional Resources

- [Firebase Authentication Documentation](https://firebase.google.com/docs/auth)
- [Firebase REST API Reference](https://firebase.google.com/docs/reference/rest/auth)
- [Streamlit Secrets Management](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management)
