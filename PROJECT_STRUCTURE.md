# AgroDetect AI - Project Structure Documentation

## 📂 Complete File Structure

```
AgroDetect_AI/
│
├── app.py                          # Main entry point - redirects to Home
│
├── pages/                          # Streamlit multipage navigation
│   ├── 1_Home.py                  # Landing page with features & CTA
│   ├── 2_About.py                 # Project overview & technologies
│   ├── 3_Upload.py                # Image upload interface
│   ├── 4_Results.py               # Analysis results & recommendations
│   ├── 5_AI_Assistant.py          # Chatbot Q&A interface
│   └── 6_Voice_Assistant.py       # Voice interaction demo
│
├── components/                     # Reusable UI components
│   ├── language.py                # Translation management & session state
│   ├── navbar.py                  # Sidebar navigation with language selector
│   ├── cards.py                   # Reusable card components
│   ├── chatbot_ui.py              # Chat interface & response logic
│   └── voice_ui.py                # Voice assistant interface
│
├── assets/                         # Static assets
│   ├── styles.css                 # Custom CSS styling
│   └── logo.png                   # Application logo (placeholder)
│
├── requirements.txt                # Python dependencies
├── README.md                      # Main documentation
└── PROJECT_STRUCTURE.md           # This file
```

## 🎯 Component Responsibilities

### app.py
- Application entry point
- Initializes session state
- Loads custom CSS
- Redirects to Home page

### Pages

#### 1_Home.py
- Welcome message
- Feature cards (3 columns)
- "Get Started" CTA button
- Navigation to Upload page

#### 2_About.py
- Project description
- Transfer learning explanation (MobileNetV2)
- How it works (3-step process)
- Technology stack display

#### 3_Upload.py
- File uploader (JPG, JPEG, PNG)
- Image preview
- "Analyze Leaf" button with progress bar
- Navigation to Results page

#### 4_Results.py
- Display uploaded image
- Show disease name (placeholder)
- Display confidence score (96.5%)
- Recommendations list
- Action buttons (Analyze Another, Back Home)

#### 5_AI_Assistant.py
- Chat interface
- Sample questions
- Chat history display
- Send/Clear buttons
- Contextual responses

#### 6_Voice_Assistant.py
- "Speak Now" button
- Simulated voice recognition
- Display recognized text
- AI response display
- "Play Voice Response" button

### Components

#### language.py
- TRANSLATIONS dictionary (6 languages)
- init_session_state() - Initialize all session variables
- get_text(key) - Get translated text
- load_custom_css() - Load CSS file
- get_available_languages() - Return language list

#### navbar.py
- render_navbar() - Sidebar with language selector and tip

#### cards.py
- feature_card() - Feature display cards
- result_card() - Result display cards
- info_card() - Info/warning boxes
- tech_card() - Technology stack cards
- step_card() - How it works step cards

#### chatbot_ui.py
- CHATBOT_RESPONSES - Response templates
- get_chatbot_response() - Generate responses
- render_chat_message() - Display single message
- render_chatbot() - Complete chat interface

#### voice_ui.py
- render_voice_assistant() - Complete voice interface
- Simulated voice recognition
- Voice playback simulation

### Assets

#### styles.css
- Main background styling
- Button styles with hover effects
- Card components (feature, result, tech)
- Chat message bubbles
- Info/warning boxes
- Responsive design elements

## 🔄 Data Flow

1. **User starts app** → app.py → Redirects to 1_Home.py
2. **Language selection** → Updates st.session_state.language → All pages refresh with new language
3. **Image upload** → Stored in st.session_state.uploaded_image → Available across pages
4. **Analysis trigger** → Sets st.session_state.analysis_done = True → Navigates to Results
5. **Chat interaction** → Appends to st.session_state.chat_history → Persists during session
6. **Voice interaction** → Updates st.session_state.voice_text and voice_response

## 🌍 Multi-Language Support

Supported languages:
- English (default)
- Hindi (हिंदी)
- Tamil (தமிழ்)
- Telugu (తెలుగు)
- Spanish (Español)
- French (Français)

All UI text is translated dynamically using the get_text() function.

## 🎨 Design Principles

1. **Modular Architecture** - Reusable components
2. **Clean Code** - Well-commented and organized
3. **Responsive Design** - Works on different screen sizes
4. **Consistent Styling** - Unified color scheme (green/eco-friendly)
5. **User-Friendly** - Clear navigation and feedback
6. **Professional UI** - Card-based layout with shadows and hover effects

## 🚀 Running the Application

```bash
streamlit run app.py
```

Access at: http://localhost:8501

## 📝 Notes

- This is a **frontend-only** application
- No actual ML model integration
- Placeholder results for demonstration
- All AI responses are simulated
- Voice recognition is simulated (no actual speech-to-text)
