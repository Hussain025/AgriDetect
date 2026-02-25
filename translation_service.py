"""
Central Translation Service - Gemini AI Powered
Single source of truth for all UI translations
BACKWARD COMPATIBLE with old get_text() function
"""

import streamlit as st
import json
from components.gemini_ai import init_gemini

# ==================== UI TEXT KEYS (ENGLISH BASE) ====================
# Single source of truth for all UI text in the application
UI_TEXTS = {
    # App Core
    "APP_TITLE": "AgroDetect AI",
    "APP_SUBTITLE": "AI-Powered Plant Disease Detection System",
    "LANGUAGE": "Language",
    "TIP": "💡 Tip: Upload a plant leaf image to detect diseases instantly!",
    
    # Navigation
    "NAV_HOME": "🏠 Home",
    "NAV_ABOUT": "📖 About",
    "NAV_UPLOAD": "📤 Upload",
    "NAV_RESULTS": "📊 Results",
    "NAV_CHATBOT": "🤖 AI Assistant",
    "NAV_VOICE": "🎤 Voice Assistant",
    "NAV_HISTORY": "📊 Crop History",
    "NAV_SUSTAINABILITY": "🌍 Sustainability",
    "NAV_WHY": "💡 Why AgroDetect",
    
    # Authentication
    "LOGIN_TITLE": "Login to Your Account",
    "SIGNUP_TITLE": "Create Your Account",
    "EMAIL": "Email Address",
    "PASSWORD": "Password",
    "CONFIRM_PASSWORD": "Confirm Password",
    "LOGIN_BTN": "Login",
    "SIGNUP_BTN": "Create Account",
    "LOGOUT_BTN": "Logout",
    "BACK_TO_LANDING": "Back to Landing",
    "ALREADY_ACCOUNT": "Already have an account?",
    "NO_ACCOUNT": "Don't have an account?",
    "LOGIN_HERE": "Login Here",
    "CREATE_ACCOUNT": "Create New Account",
    
    # Landing Page
    "LANDING_HERO_TITLE": "AgroDetect AI",
    "LANDING_HERO_SUBTITLE": "AI-Powered Plant Disease Detection",
    "LANDING_HERO_DESC": "Revolutionizing agriculture with artificial intelligence. Detect plant diseases instantly, get expert recommendations, and protect your crops with cutting-edge technology.",
    "GET_STARTED_LOGIN": "Get Started - Login",
    "SIGNUP_FREE": "Sign Up Free",
    "POWERFUL_FEATURES": "Powerful Features",
    "DISEASE_DETECTION": "Disease Detection",
    "DISEASE_DETECTION_DESC": "Upload plant leaf images and get instant disease classification powered by advanced AI algorithms.",
    "AI_ASSISTANT": "AI Assistant",
    "AI_ASSISTANT_DESC": "Chat with our intelligent AI assistant for plant disease advice, treatment recommendations, and care tips.",
    "VOICE_SUPPORT": "Voice Support",
    "VOICE_SUPPORT_DESC": "Interact with voice commands and get audio responses for hands-free operation in the field.",
    "MULTI_LANGUAGE": "Multi-Language",
    "MULTI_LANGUAGE_DESC": "Available in 6 languages including English, Hindi, Tamil, Telugu, Spanish, and French.",
    "HOW_IT_WORKS": "How It Works",
    "STEP_1": "Step 1",
    "STEP_2": "Step 2",
    "STEP_3": "Step 3",
    "UPLOAD_IMAGE": "Upload Image",
    "UPLOAD_IMAGE_DESC": "Take a photo of the affected plant leaf and upload it to our platform.",
    "AI_ANALYSIS": "AI Analysis",
    "AI_ANALYSIS_DESC": "Our AI model analyzes the image using deep learning and CNN technology.",
    "GET_RESULTS": "Get Results",
    "GET_RESULTS_DESC": "Receive disease classification, confidence score, and treatment recommendations.",
    "POWERED_BY": "Powered By Advanced Technology",
    "READY_TO_PROTECT": "Ready to Protect Your Crops?",
    "JOIN_FARMERS": "Join thousands of farmers and agricultural experts using AgroDetect AI",
    "LOGIN_NOW": "Login Now",
    "CREATE_ACCOUNT_BTN": "Create Account",
    
    # Home Page
    "HOME_WELCOME": "Welcome to AgroDetect AI",
    "HOME_DESC": "Our intelligent system helps you identify plant diseases quickly and accurately. Simply upload a plant leaf image, and our AI will analyze it to provide disease classification results.",
    "FEATURES_TITLE": "Key Features",
    "FEATURE1_TITLE": "🌱 Instant Disease Detection",
    "FEATURE1_DESC": "Upload a leaf image and get instant disease classification results powered by advanced AI algorithms.",
    "FEATURE2_TITLE": "🎯 High Accuracy",
    "FEATURE2_DESC": "Leveraging transfer learning with CNN architecture to deliver highly accurate disease predictions.",
    "FEATURE3_TITLE": "📊 AI Powered",
    "FEATURE3_DESC": "Scalable solution designed for farmers, gardeners, and agricultural experts worldwide.",
    "GET_STARTED": "🚀 Get Started",
    
    # Upload Page
    "UPLOAD_TITLE": "Upload Plant Leaf Image",
    "UPLOAD_DESC": "Upload a clear image of a plant leaf to detect potential diseases.",
    "SUPPORTED_FORMATS": "Supported formats: JPG, JPEG, PNG",
    "CHOOSE_IMAGE": "Choose an image...",
    "IMAGE_PREVIEW": "Uploaded Image Preview",
    "ANALYZE_BTN": "🔍 Analyze Leaf",
    "ANALYZING": "Analyzing image using AI model...",
    "ANALYSIS_COMPLETE": "Analysis complete!",
    "UPLOAD_PROMPT": "Please upload an image to continue",
    
    # Results Page
    "RESULTS_TITLE": "Analysis Results",
    "NO_RESULTS": "No analysis results available. Please upload an image first.",
    "GO_UPLOAD": "Go to Upload Page",
    "ANALYZED_IMAGE": "Analyzed Image",
    "DETECTION_RESULTS": "Detection Results",
    "DETECTED_DISEASE": "Detected Disease",
    "CONFIDENCE_SCORE": "Confidence Score",
    "RECOMMENDATIONS": "Recommendations",
    "ACTION_REQUIRED": "Action Required",
    "ANALYZE_ANOTHER": "Analyze Another Image",
    "BACK_HOME": "Back to Home",
    
    # AI Chatbot
    "CHATBOT_TITLE": "AI Assistant",
    "CHATBOT_SUBTITLE": "Plant Disease Expert",
    "CHATBOT_DESC": "Ask me anything about plant diseases, care tips, or agricultural advice!",
    "CHAT_INPUT": "Type your question here...",
    "SEND_BTN": "Send",
    "CLEAR_CHAT": "Clear Chat",
    "SAMPLE_QUESTIONS": "Sample Questions:",
    "AI_THINKING": "AI is thinking...",
    "AI_GENERATING": "AI is generating response...",
    
    # Voice Assistant
    "VOICE_TITLE": "Voice Assistant",
    "VOICE_SUBTITLE": "Multi-Language Voice Support",
    "VOICE_DESC": "Speak your question and get voice responses in your preferred language!",
    "SPEAK_BTN": "🎤 Speak Now",
    "PLAY_VOICE": "Play Voice Response",
    "RECOGNIZED_TEXT": "Recognized Speech",
    "AI_RESPONSE": "AI Response",
    "LISTENING": "Listening...",
    
    # Common
    "LOADING": "Loading...",
    "ERROR": "Error",
    "SUCCESS": "Success",
    "WARNING": "Warning",
    "INFO": "Information",
}

# ==================== SUPPORTED LANGUAGES ====================
SUPPORTED_LANGUAGES = [
    "English",
    "Hindi",
    "Tamil",
    "Telugu",
    "Spanish",
    "French"
]

# ==================== TRANSLATION CACHE ====================
def init_translation_state():
    """Initialize translation-related session state"""
    if 'language' not in st.session_state:
        st.session_state.language = 'English'
    
    if 'translations' not in st.session_state:
        # Start with English as default
        st.session_state.translations = UI_TEXTS.copy()
    
    if 'translation_cache' not in st.session_state:
        # Cache translations by language to avoid repeated API calls
        st.session_state.translation_cache = {
            'English': UI_TEXTS.copy()
        }

# ==================== GEMINI BATCH TRANSLATION ====================
def translate_all_ui_texts(target_language: str) -> dict:
    """
    Translate ALL UI texts to target language using Gemini AI in ONE batch request.
    This is the CORE translation function - all translations go through here.
    
    Args:
        target_language: Target language name (e.g., "Hindi", "Spanish")
    
    Returns:
        Dictionary with same keys as UI_TEXTS but translated values
    """
    
    # If English, return original
    if target_language == "English":
        return UI_TEXTS.copy()
    
    # Check cache first
    if target_language in st.session_state.translation_cache:
        return st.session_state.translation_cache[target_language]
    
    # Initialize Gemini
    model = init_gemini()
    if not model:
        # Fallback to English if Gemini not available
        st.error("⚠️ Gemini AI not configured. Please add API key to .streamlit/secrets.toml")
        return UI_TEXTS.copy()
    
    try:
        # Show progress
        st.info(f"🤖 Translating to {target_language} using Gemini AI...")
        
        # Create translation prompt for Gemini
        prompt = f"""You are a professional translator for an agricultural AI application.

TASK: Translate the following UI text from English to {target_language}.

IMPORTANT RULES:
1. Maintain the EXACT same JSON structure
2. Translate ONLY the values, keep keys unchanged
3. Use simple, farmer-friendly language
4. Keep technical terms clear (AI, CNN, etc.)
5. Preserve emojis and special characters
6. Return ONLY valid JSON, no explanations

UI TEXTS TO TRANSLATE:
{json.dumps(UI_TEXTS, indent=2, ensure_ascii=False)}

Return the translated JSON now:"""

        # Call Gemini for batch translation
        response = model.generate_content(prompt)
        
        # Parse response
        response_text = response.text.strip()
        
        # Extract JSON from response (handle markdown code blocks)
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0].strip()
        
        # Parse JSON
        translated_texts = json.loads(response_text)
        
        # Validate that all keys are present (silent validation)
        missing_keys = set(UI_TEXTS.keys()) - set(translated_texts.keys())
        if missing_keys:
            # Fill missing keys with English (no warning)
            for key in missing_keys:
                translated_texts[key] = UI_TEXTS[key]
        
        # Cache the translation
        st.session_state.translation_cache[target_language] = translated_texts
        
        # Show success
        st.success(f"✅ Translated to {target_language}!")
        
        return translated_texts
        
    except json.JSONDecodeError as e:
        # Show error and fallback to English
        st.error(f"❌ Translation parsing error. Using English.")
        return UI_TEXTS.copy()
    
    except Exception as e:
        # Show error and fallback to English
        st.error(f"❌ Translation error: {str(e)}. Using English.")
        return UI_TEXTS.copy()

# ==================== LANGUAGE CHANGE HANDLER ====================
def change_language(new_language: str):
    """
    Handle language change - triggers re-translation and UI update.
    This is called when user selects a new language.
    
    Args:
        new_language: New language to switch to
    """
    
    if new_language == st.session_state.language:
        return  # No change needed
    
    # Show loading indicator
    with st.spinner(f"🌍 Switching to {new_language}..."):
        # Translate all UI texts
        translated_texts = translate_all_ui_texts(new_language)
        
        # Update session state
        st.session_state.language = new_language
        st.session_state.translations = translated_texts
    
    # Force UI refresh
    st.rerun()

# ==================== TEXT RETRIEVAL FUNCTION ====================
def t(key: str) -> str:
    """
    Get translated text for a given key.
    This is the ONLY function that should be used to retrieve UI text.
    
    Args:
        key: UI text key (e.g., "HOME_TITLE", "LOGIN_BTN")
    
    Returns:
        Translated text in current language
    
    Usage:
        st.title(t("HOME_TITLE"))
        st.button(t("LOGIN_BTN"))
    """
    
    # Ensure translation state is initialized
    if 'translations' not in st.session_state:
        init_translation_state()
    
    # Get translated text
    translated_text = st.session_state.translations.get(key, None)
    
    # Fallback to English if key not found
    if translated_text is None:
        translated_text = UI_TEXTS.get(key, key)
        # Don't show warning - just use fallback silently
    
    return translated_text

# ==================== LANGUAGE SELECTOR COMPONENT ====================
def render_language_selector():
    """
    Render language selector dropdown.
    Should be called in sidebar or header of every page.
    """
    
    # Initialize state
    init_translation_state()
    
    # Get current language
    current_language = st.session_state.language
    
    # Language selector with unique key
    selected_language = st.sidebar.selectbox(
        f"🌍 {t('LANGUAGE')}",
        SUPPORTED_LANGUAGES,
        index=SUPPORTED_LANGUAGES.index(current_language) if current_language in SUPPORTED_LANGUAGES else 0,
        key="language_selector_main"
    )
    
    # Handle language change - THIS IS THE FIX
    if selected_language != current_language:
        # Show loading message
        with st.spinner(f"🌍 Switching to {selected_language}..."):
            # Translate all UI texts
            translated_texts = translate_all_ui_texts(selected_language)
            
            # Update session state
            st.session_state.language = selected_language
            st.session_state.translations = translated_texts
        
        # Force UI refresh
        st.rerun()

# ==================== UTILITY FUNCTIONS ====================
def get_available_languages() -> list:
    """Get list of supported languages"""
    return SUPPORTED_LANGUAGES.copy()

def get_current_language() -> str:
    """Get currently selected language"""
    if 'language' not in st.session_state:
        init_translation_state()
    return st.session_state.language

def clear_translation_cache():
    """Clear translation cache (useful for debugging)"""
    if 'translation_cache' in st.session_state:
        st.session_state.translation_cache = {
            'English': UI_TEXTS.copy()
        }
        st.success("✅ Translation cache cleared")

# ==================== PRELOAD TRANSLATIONS (OPTIONAL) ====================
def preload_translations(languages: list = None):
    """
    Preload translations for specified languages.
    Useful to avoid delays on first language switch.
    
    Args:
        languages: List of languages to preload (default: all supported)
    """
    
    if languages is None:
        languages = SUPPORTED_LANGUAGES
    
    init_translation_state()
    
    with st.spinner("🌍 Preloading translations..."):
        for lang in languages:
            if lang != "English" and lang not in st.session_state.translation_cache:
                translate_all_ui_texts(lang)
    
    st.success(f"✅ Preloaded {len(languages)} languages")


# ==================== BACKWARD COMPATIBILITY ====================
# Support old get_text() function for existing pages

def get_text(key: str) -> str:
    """
    Backward compatible function for old pages.
    Maps old lowercase keys to new UPPERCASE keys.
    """
    # Map old keys to new keys (comprehensive mapping)
    key_mapping = {
        # Core
        "app_title": "APP_TITLE",
        "app_subtitle": "APP_SUBTITLE",
        "language": "LANGUAGE",
        "tip": "TIP",
        
        # Navigation
        "nav_home": "NAV_HOME",
        "nav_about": "NAV_ABOUT",
        "nav_upload": "NAV_UPLOAD",
        "nav_results": "NAV_RESULTS",
        "nav_chatbot": "NAV_CHATBOT",
        "nav_voice": "NAV_VOICE",
        "nav_history": "NAV_HISTORY",
        "nav_sustainability": "NAV_SUSTAINABILITY",
        "nav_why": "NAV_WHY",
        
        # Authentication
        "login_title": "LOGIN_TITLE",
        "signup_title": "SIGNUP_TITLE",
        "email": "EMAIL",
        "password": "PASSWORD",
        "confirm_password": "CONFIRM_PASSWORD",
        "login_btn": "LOGIN_BTN",
        "signup_btn": "SIGNUP_BTN",
        "logout_btn": "LOGOUT_BTN",
        "back_to_landing": "BACK_TO_LANDING",
        "already_account": "ALREADY_ACCOUNT",
        "no_account": "NO_ACCOUNT",
        "login_here": "LOGIN_HERE",
        "create_account": "CREATE_ACCOUNT",
        
        # Landing Page
        "landing_hero_title": "LANDING_HERO_TITLE",
        "landing_hero_subtitle": "LANDING_HERO_SUBTITLE",
        "landing_hero_desc": "LANDING_HERO_DESC",
        "get_started_login": "GET_STARTED_LOGIN",
        "signup_free": "SIGNUP_FREE",
        "powerful_features": "POWERFUL_FEATURES",
        "disease_detection": "DISEASE_DETECTION",
        "disease_detection_desc": "DISEASE_DETECTION_DESC",
        "ai_assistant": "AI_ASSISTANT",
        "ai_assistant_desc": "AI_ASSISTANT_DESC",
        "voice_support": "VOICE_SUPPORT",
        "voice_support_desc": "VOICE_SUPPORT_DESC",
        "multi_language": "MULTI_LANGUAGE",
        "multi_language_desc": "MULTI_LANGUAGE_DESC",
        "how_it_works": "HOW_IT_WORKS",
        "step_1": "STEP_1",
        "step_2": "STEP_2",
        "step_3": "STEP_3",
        "upload_image": "UPLOAD_IMAGE",
        "upload_image_desc": "UPLOAD_IMAGE_DESC",
        "ai_analysis": "AI_ANALYSIS",
        "ai_analysis_desc": "AI_ANALYSIS_DESC",
        "get_results": "GET_RESULTS",
        "get_results_desc": "GET_RESULTS_DESC",
        "powered_by": "POWERED_BY",
        "ready_to_protect": "READY_TO_PROTECT",
        "join_farmers": "JOIN_FARMERS",
        "login_now": "LOGIN_NOW",
        "create_account_btn": "CREATE_ACCOUNT_BTN",
        
        # Home Page
        "home_welcome": "HOME_WELCOME",
        "home_desc": "HOME_DESC",
        "features_title": "FEATURES_TITLE",
        "feature1_title": "FEATURE1_TITLE",
        "feature1_desc": "FEATURE1_DESC",
        "feature2_title": "FEATURE2_TITLE",
        "feature2_desc": "FEATURE2_DESC",
        "feature3_title": "FEATURE3_TITLE",
        "feature3_desc": "FEATURE3_DESC",
        "get_started": "GET_STARTED",
        
        # Upload Page
        "upload_title": "UPLOAD_TITLE",
        "upload_desc": "UPLOAD_DESC",
        "supported_formats": "SUPPORTED_FORMATS",
        "choose_image": "CHOOSE_IMAGE",
        "image_preview": "IMAGE_PREVIEW",
        "analyze_btn": "ANALYZE_BTN",
        "analyzing": "ANALYZING",
        "analysis_complete": "ANALYSIS_COMPLETE",
        "upload_prompt": "UPLOAD_PROMPT",
        
        # Results Page
        "results_title": "RESULTS_TITLE",
        "no_results": "NO_RESULTS",
        "go_upload": "GO_UPLOAD",
        "analyzed_image": "ANALYZED_IMAGE",
        "detection_results": "DETECTION_RESULTS",
        "detected_disease": "DETECTED_DISEASE",
        "confidence_score": "CONFIDENCE_SCORE",
        "recommendations": "RECOMMENDATIONS",
        "action_required": "ACTION_REQUIRED",
        "analyze_another": "ANALYZE_ANOTHER",
        "back_home": "BACK_HOME",
        
        # Chatbot
        "chatbot_title": "CHATBOT_TITLE",
        "chatbot_subtitle": "CHATBOT_SUBTITLE",
        "chatbot_desc": "CHATBOT_DESC",
        "chat_input": "CHAT_INPUT",
        "send_btn": "SEND_BTN",
        "clear_chat": "CLEAR_CHAT",
        "sample_questions": "SAMPLE_QUESTIONS",
        "ai_thinking": "AI_THINKING",
        "ai_generating": "AI_GENERATING",
        
        # Voice Assistant
        "voice_title": "VOICE_TITLE",
        "voice_subtitle": "VOICE_SUBTITLE",
        "voice_desc": "VOICE_DESC",
        "speak_btn": "SPEAK_BTN",
        "play_voice": "PLAY_VOICE",
        "recognized_text": "RECOGNIZED_TEXT",
        "ai_response": "AI_RESPONSE",
        "listening": "LISTENING",
        
        # Common
        "loading": "LOADING",
        "error": "ERROR",
        "success": "SUCCESS",
        "warning": "WARNING",
        "info": "INFO",
    }
    
    # Convert old key to new key
    new_key = key_mapping.get(key, key.upper())
    
    # Use t() function (no warnings)
    return t(new_key)

def init_session_state():
    """Backward compatible - calls init_translation_state()"""
    init_translation_state()

def load_custom_css():
    """Load custom CSS from assets/styles.css"""
    try:
        with open("assets/styles.css", "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass  # Silently fail if CSS not found
