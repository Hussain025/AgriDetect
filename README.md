# 🌱 AgroDetect AI - Plant Disease Classification Engine

A modern, modular Streamlit frontend application for plant disease detection with multi-language support and Firebase authentication.

## 📁 Project Structure

```
AgroDetect_AI/
│
├── app.py                      # Main entry point with auth check
├── pages/                      # Streamlit multipage structure
│   ├── 0_Login.py             # User login page
│   ├── 0_Signup.py            # User registration page
│   ├── 1_Home.py              # Landing page with features
│   ├── 2_About.py             # Project overview & technologies
│   ├── 3_Upload.py            # Image upload interface
│   ├── 4_Results.py           # Analysis results display
│   ├── 5_AI_Assistant.py      # Chatbot interface
│   └── 6_Voice_Assistant.py   # Voice interaction demo
│
├── components/                 # Reusable UI components
│   ├── auth.py                # Firebase authentication logic
│   ├── navbar.py              # Sidebar navigation with logout
│   ├── cards.py               # Card components
│   ├── chatbot_ui.py          # Chat interface
│   ├── voice_ui.py            # Voice interface
│   └── language.py            # Translation management
│
├── assets/                     # Static assets
│   ├── styles.css             # Custom CSS styling
│   └── logo.png               # Application logo
│
├── requirements.txt            # Python dependencies
├── README.md                  # Documentation
├── FIREBASE_SETUP.md          # Firebase setup guide
└── PROJECT_STRUCTURE.md       # Detailed structure docs
```

## ✨ Features

- 🔐 **Authentication** - Secure login/signup with Firebase
- 🏠 **Home Page** - Welcome screen with feature cards and CTA
- 📖 **About Page** - Project overview, transfer learning explanation, tech stack
- 📤 **Upload Page** - Image upload with preview and analysis trigger
- 📊 **Results Page** - Disease classification with recommendations
- 🤖 **AI Assistant** - Interactive chatbot for plant disease Q&A
- 🎤 **Voice Assistant** - Multi-language voice interaction demo
- 🌍 **Multi-Language Support** - English, Hindi, Tamil, Telugu, Spanish, French
- 🔒 **Access Control** - Protected pages require authentication

## 🚀 Installation

1. Install Python (3.8 or higher)

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Firebase Authentication:
   - Follow the detailed guide in `FIREBASE_SETUP.md`
   - Update `components/auth.py` with your Firebase credentials

## 🎯 Running the Application

Run the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📖 Usage

### First Time Users:
1. Click "Create New Account" on the login page
2. Enter your email and password (min 6 characters)
3. Confirm your password
4. Click "Create Account"
5. Login with your new credentials

### Returning Users:
1. Enter your email and password
2. Click "Login"
3. Access all features of the application

### Navigation:
1. Select your preferred language from the sidebar
2. Navigate through pages using Streamlit's page navigation
3. Upload a plant leaf image on the Upload page
4. Click "Analyze Leaf" to see results
5. Interact with AI Assistant for plant disease questions
6. Try Voice Assistant for voice-based interaction
7. Click "Logout" in sidebar when done

## 🔒 Authentication Features

- **Secure Login** - Firebase email/password authentication
- **User Registration** - Create new accounts with validation
- **Password Protection** - Minimum 6 characters, masked input
- **Session Management** - Persistent login across pages
- **Access Control** - Protected pages require authentication
- **Logout** - Clear session and redirect to login

## 🛠️ Technologies Used

### Frontend
- **Python** - Core programming language
- **Streamlit** - Web application framework
- **Pillow (PIL)** - Image processing

### Authentication
- **Firebase Authentication** - User management
- **Requests** - HTTP library for Firebase REST API

### AI Concepts (Frontend Demo)
- **Transfer Learning** - MobileNetV2 architecture
- **CNN** - Convolutional Neural Networks
- **Deep Learning** - Disease classification

## 🎨 Design Features

- Clean, modern UI with eco-friendly green theme
- Responsive layout with card-based design
- Custom CSS styling for professional appearance
- Modular component architecture for reusability
- Session state management for smooth navigation
- Secure authentication flow

## 📝 Note

This is a **frontend-only** application with placeholder results. No actual ML model or backend is included. The application demonstrates UI/UX design, user authentication, and interaction flows for an AI-powered plant disease detection system.

## 🔧 Customization

- **Firebase Config**: Edit `components/auth.py` to update credentials
- **Translations**: Edit `components/language.py` to add/modify languages
- **Styling**: Modify `assets/styles.css` for custom themes
- **Components**: Extend components in `components/` directory
- **Pages**: Add new pages in `pages/` directory following naming convention

## 🔐 Security Notes

- Never commit Firebase credentials to version control
- Use Streamlit secrets or environment variables for production
- Add `.streamlit/secrets.toml` to `.gitignore`
- Follow Firebase security best practices
- Enable email verification for production use

## 📚 Documentation

- `FIREBASE_SETUP.md` - Complete Firebase setup guide
- `PROJECT_STRUCTURE.md` - Detailed project structure documentation
- `README.md` - This file

## 🚀 Deployment

For deployment on Streamlit Cloud or other platforms:
1. Push code to GitHub (without secrets)
2. Configure secrets in platform dashboard
3. Ensure all dependencies are in requirements.txt
4. Follow platform-specific deployment guides
