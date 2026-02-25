# 🌱 AgroDetect AI - Streamlit Cloud Deployment

## Quick Start Guide for Hackathon Demo

---

## 🚀 ONE-COMMAND DEPLOYMENT

### Prerequisites:
1. GitHub account
2. Streamlit Cloud account
3. Gemini API key
4. Firebase project

### Deploy in 5 Minutes:

```bash
# 1. Push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. Go to Streamlit Cloud
# https://share.streamlit.io

# 3. Click "New app"
# Select your repository
# Main file: app.py
# Click Deploy

# 4. Add secrets in dashboard
# Settings > Secrets > Paste your keys

# 5. Done! App is live
```

---

## 📋 REQUIRED SECRETS

Add these in Streamlit Cloud dashboard (Settings > Secrets):

```toml
GEMINI_API_KEY = "your-key-here"
FIREBASE_API_KEY = "your-key-here"
FIREBASE_AUTH_DOMAIN = "your-project.firebaseapp.com"
FIREBASE_PROJECT_ID = "your-project-id"
FIREBASE_STORAGE_BUCKET = "your-project.appspot.com"
FIREBASE_MESSAGING_SENDER_ID = "your-sender-id"
FIREBASE_APP_ID = "your-app-id"
```

---

## ✅ DEPLOYMENT VERIFICATION

### Test These Features:
1. ✅ Landing page loads
2. ✅ Can signup/login
3. ✅ Language switching works (6 languages)
4. ✅ AI Chatbot responds
5. ✅ Can upload images
6. ✅ Voice assistant accessible

---

## 🐛 TROUBLESHOOTING

### App Won't Start:
- Check deployment logs
- Verify requirements.txt
- Check Python version (3.9+)

### Gemini Not Working:
- Verify API key in secrets
- Check key has no spaces
- Ensure API is enabled

### Firebase Auth Fails:
- Verify all Firebase secrets
- Check Firebase project is active
- Enable Email/Password auth

---

## 📱 DEMO TIPS

### For Judges:
1. Show language switching (impressive!)
2. Demonstrate AI chatbot
3. Upload sample plant image
4. Explain real-time translation

### Live URL:
```
https://your-app-name.streamlit.app
```

---

## 📞 SUPPORT

- **Docs**: See `DEPLOYMENT_GUIDE.md`
- **Checklist**: See `DEPLOYMENT_CHECKLIST.md`
- **Issues**: Check Streamlit logs

---

## 🎉 READY TO DEPLOY!

Follow the detailed guide in `DEPLOYMENT_GUIDE.md` for step-by-step instructions.

**Good luck with your hackathon!** 🚀
