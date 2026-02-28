# 🔧 Firebase Troubleshooting Guide

## Error: "CONFIGURATION_NOT_FOUND"

### What This Means:
Firebase Authentication is not properly enabled in your Firebase Console.

### Quick Fix (2 minutes):

#### Step 1: Go to Firebase Console
Visit: https://console.firebase.google.com/project/agrodetect-ai

#### Step 2: Enable Authentication
1. Click **"Authentication"** in the left sidebar
2. Click **"Get started"** button
3. Click **"Sign-in method"** tab
4. Click **"Email/Password"**
5. Toggle the **"Enable"** switch to ON
6. Click **"Save"**

#### Step 3: Restart Your App
```bash
# Stop the current server (Ctrl+C)
# Then restart:
streamlit run app.py
```

#### Step 4: Test Again
Try creating an account - it should work now!

---

## Alternative: Use Local Database (No Firebase Setup Needed)

### Option 1: Disable Firebase Temporarily
Comment out Firebase credentials in `.env`:

```env
# FIREBASE_API_KEY=your_key
# FIREBASE_AUTH_DOMAIN=your_domain
# ... (comment all Firebase lines)
```

The app will automatically use SQLite local database.

### Option 2: Let It Auto-Fallback
The app is designed to automatically fall back to local database if Firebase fails. Just continue using it - it will work with SQLite!

---

## Current Status of Your App

### ✅ What's Working:
- Local SQLite database authentication
- User registration and login
- Disease detection
- Analysis history
- All core features

### ⚠️ What Needs Firebase Setup:
- Cloud-based authentication
- Cross-device data sync
- Real-time database updates

### 💡 Recommendation:
**For Hackathon Demo:** The local database works perfectly! You can present your project without Firebase.

**For Production:** Follow the setup steps above to enable Firebase.

---

## Complete Firebase Setup Checklist

### In Firebase Console:

- [ ] **Step 1:** Create Firebase project
  - Go to https://console.firebase.google.com/
  - Click "Add project"
  - Name: "agrodetect-ai"

- [ ] **Step 2:** Enable Authentication
  - Click "Authentication" → "Get started"
  - Click "Sign-in method" tab
  - Enable "Email/Password"
  - Click "Save"

- [ ] **Step 3:** Enable Realtime Database
  - Click "Realtime Database"
  - Click "Create Database"
  - Choose location
  - Start in "Test mode"
  - Click "Enable"

- [ ] **Step 4:** Get Configuration
  - Click gear icon → "Project settings"
  - Scroll to "Your apps"
  - Click web icon `</>`
  - Register app
  - Copy config values

- [ ] **Step 5:** Update .env File
  - Paste all Firebase values
  - Save file
  - Restart app

### Verify Setup:

- [ ] Can create new account
- [ ] User appears in Firebase Console → Authentication
- [ ] Can login successfully
- [ ] Analysis saves to Firebase Console → Realtime Database

---

## Common Issues & Solutions

### Issue 1: "Firebase is not configured"
**Solution:** Check your `.env` file has all required values

### Issue 2: "Module not found: firebase_config"
**Solution:** 
```bash
pip install firebase-admin pyrebase4 python-dotenv
```

### Issue 3: "INVALID_API_KEY"
**Solution:** 
- Go to Firebase Console → Project Settings
- Copy the correct API key
- Update `.env` file

### Issue 4: "Permission denied" (Database)
**Solution:**
1. Go to Firebase Console → Realtime Database
2. Click "Rules" tab
3. Use these rules:
```json
{
  "rules": {
    "users": {
      "$uid": {
        ".read": "$uid === auth.uid",
        ".write": "$uid === auth.uid"
      }
    }
  }
}
```
4. Click "Publish"

### Issue 5: App won't start
**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Clear cache
streamlit cache clear

# Restart
streamlit run app.py
```

---

## Testing Without Firebase

### Your app works perfectly without Firebase!

**What you can do:**
✅ Create accounts (stored locally)
✅ Login/logout
✅ Detect diseases
✅ View history
✅ All features work

**What you can't do:**
❌ Access data from other devices
❌ Cloud backup
❌ Real-time sync

### For Hackathon:
**Local database is sufficient!** Your project is fully functional.

---

## Quick Commands

### Check if Firebase is working:
```python
# In Python console:
from firebase_config import is_firebase_enabled
print(is_firebase_enabled())
# True = Firebase working
# False = Using local database
```

### View local database:
```bash
# Install SQLite browser
# Open: agrodetect_users.db
# View tables: users, analysis_history
```

### Reset everything:
```bash
# Delete local database
rm agrodetect_users.db

# Restart app
streamlit run app.py
```

---

## Firebase Console URLs

### Your Project:
- **Console:** https://console.firebase.google.com/project/agrodetect-ai
- **Authentication:** https://console.firebase.google.com/project/agrodetect-ai/authentication/users
- **Database:** https://console.firebase.google.com/project/agrodetect-ai/database
- **Settings:** https://console.firebase.google.com/project/agrodetect-ai/settings/general

---

## Decision Tree

```
Do you need Firebase?
│
├─ YES (for production/cloud features)
│  └─ Follow setup steps above
│
└─ NO (for hackathon/local demo)
   └─ Use local database (already working!)
```

---

## Support

### Still having issues?

1. **Check the error message** in the app
2. **Look at terminal output** for detailed errors
3. **Verify Firebase Console** settings
4. **Try local database** as fallback

### The app is designed to work either way!
- With Firebase = Cloud features
- Without Firebase = Local features

Both modes are fully functional for your hackathon! 🎉

---

## Summary

**Current Status:** Your app is working with local SQLite database.

**To enable Firebase:** Follow Step 2 above (Enable Authentication in Firebase Console)

**For Hackathon:** You're ready to present! Local database works great.

**For Production:** Complete Firebase setup for cloud features.

---

**Need more help?** Check `FIREBASE_SETUP_GUIDE.md` for detailed instructions!
