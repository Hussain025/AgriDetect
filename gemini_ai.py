"""
Gemini AI Integration Component
Real-time multilingual AI powered by Google Gemini
"""

import streamlit as st
import google.generativeai as genai
from typing import Optional, Tuple

# ==================== GEMINI CONFIGURATION ====================

def init_gemini():
    """Initialize Gemini AI with API key from secrets"""
    try:
        # Get API key from Streamlit secrets
        api_key = st.secrets.get("GEMINI_API_KEY", None)
        
        if not api_key:
            st.error("⚠️ Gemini API key not found. Please add GEMINI_API_KEY to .streamlit/secrets.toml")
            return None
        
        genai.configure(api_key=api_key)
        
        # Initialize Gemini 1.5 Flash model (current stable model)
        model = genai.GenerativeModel('gemini-1.5-flash')
        return model
    
    except Exception as e:
        st.error(f"❌ Error initializing Gemini AI: {str(e)}")
        return None

# ==================== LANGUAGE MAPPING ====================

LANGUAGE_CODES = {
    "English": "English",
    "Hindi": "Hindi (हिंदी)",
    "Tamil": "Tamil (தமிழ்)",
    "Telugu": "Telugu (తెలుగు)",
    "Spanish": "Spanish (Español)",
    "French": "French (Français)"
}

# ==================== SYSTEM PROMPTS ====================

def get_system_prompt(language: str, context: str = "general") -> str:
    """Generate system prompt based on language and context"""
    
    lang_name = LANGUAGE_CODES.get(language, "English")
    
    base_prompt = f"""You are an expert agricultural AI assistant helping farmers with plant diseases and crop care.

CRITICAL INSTRUCTIONS:
- Respond ONLY in {lang_name}
- Use simple, farmer-friendly language
- Be concise and practical
- Provide actionable advice
- Focus on agriculture, plant diseases, and crop care
- If asked about non-agricultural topics, politely redirect to agriculture

"""
    
    if context == "disease_diagnosis":
        base_prompt += """
CONTEXT: You are helping with plant disease diagnosis and treatment.
- Explain disease causes clearly
- Provide step-by-step treatment plans
- Include both organic and chemical solutions
- Mention prevention strategies
"""
    
    elif context == "chat":
        base_prompt += """
CONTEXT: You are answering farmer questions about agriculture.
- Answer questions about plant diseases, symptoms, treatments
- Provide fertilizer and pest control advice
- Explain soil health and watering practices
- Give weather-related farming tips
"""
    
    elif context == "translation":
        base_prompt += """
CONTEXT: You are translating UI text for the application.
- Translate naturally and accurately
- Keep technical terms clear
- Maintain the original meaning
- Use appropriate formality level
"""
    
    return base_prompt

# ==================== GEMINI AI FUNCTIONS ====================

def translate_text_with_gemini(text: str, target_language: str) -> str:
    """Translate text to target language using Gemini AI"""
    try:
        model = init_gemini()
        if not model:
            return text  # Fallback to original text
        
        lang_name = LANGUAGE_CODES.get(target_language, "English")
        
        prompt = f"""Translate the following text to {lang_name}.
Keep the translation natural and appropriate for farmers.
Maintain any emojis and formatting.

Text to translate: {text}

Translation:"""
        
        response = model.generate_content(prompt)
        return response.text.strip()
    
    except Exception as e:
        st.warning(f"Translation error: {str(e)}")
        return text  # Fallback to original

def get_ai_chat_response(user_message: str, language: str, chat_history: list = None) -> str:
    """Get AI response from Gemini for chat messages"""
    try:
        model = init_gemini()
        if not model:
            return "AI service temporarily unavailable. Please try again."
        
        # Build conversation context
        system_prompt = get_system_prompt(language, "chat")
        
        # Include recent chat history for context
        context = system_prompt + "\n\n"
        if chat_history:
            recent_history = chat_history[-6:]  # Last 3 exchanges
            for chat in recent_history:
                role = "Farmer" if chat['role'] == 'user' else "AI Assistant"
                context += f"{role}: {chat['message']}\n"
        
        context += f"\nFarmer: {user_message}\nAI Assistant:"
        
        # Generate response
        response = model.generate_content(context)
        return response.text.strip()
    
    except Exception as e:
        return f"Error generating response: {str(e)}"

def get_disease_recommendation(disease_name: str, language: str) -> dict:
    """Get AI-generated disease treatment recommendations"""
    try:
        model = init_gemini()
        if not model:
            return None
        
        lang_name = LANGUAGE_CODES.get(language, "English")
        
        prompt = f"""You are an agricultural expert. Provide comprehensive information about {disease_name} in {lang_name}.

Structure your response as follows:

CAUSE:
[Explain what causes this disease in 2-3 sentences]

TREATMENT:
[List 5 specific treatment steps, numbered]

PREVENTION:
[List 5 prevention measures, numbered]

ORGANIC SOLUTIONS:
[List 4 organic treatment options]

CHEMICAL SOLUTIONS:
[List 4 chemical treatment options with product names]

Keep language simple and farmer-friendly. Be specific and actionable."""
        
        response = model.generate_content(prompt)
        
        # Parse response into structured format
        text = response.text
        
        # Simple parsing (you can enhance this)
        return {
            "full_text": text,
            "language": language
        }
    
    except Exception as e:
        st.error(f"Error generating recommendations: {str(e)}")
        return None

def get_xai_explanation(disease_name: str, language: str) -> dict:
    """Get explainable AI reasoning for disease prediction"""
    try:
        model = init_gemini()
        if not model:
            return None
        
        lang_name = LANGUAGE_CODES.get(language, "English")
        
        prompt = f"""Explain why an AI model would predict {disease_name} from a plant leaf image.
Respond in {lang_name}.

Provide:
1. FOCUS AREAS: What visual features the AI looks for (2-3 sentences)
2. CONFIDENCE FACTORS: 3 specific visual indicators that confirm this disease
3. MODEL REASONING: How the AI makes this prediction (2-3 sentences)

Keep it simple and educational."""
        
        response = model.generate_content(prompt)
        
        return {
            "explanation": response.text,
            "language": language
        }
    
    except Exception as e:
        st.error(f"Error generating XAI explanation: {str(e)}")
        return None

# ==================== VOICE INTEGRATION ====================

def transcribe_speech_to_text(audio_data, language: str) -> Optional[str]:
    """Convert speech to text using speech recognition"""
    try:
        import speech_recognition as sr
        
        recognizer = sr.Recognizer()
        
        # Language codes for speech recognition
        lang_codes = {
            "English": "en-US",
            "Hindi": "hi-IN",
            "Tamil": "ta-IN",
            "Telugu": "te-IN",
            "Spanish": "es-ES",
            "French": "fr-FR"
        }
        
        lang_code = lang_codes.get(language, "en-US")
        
        # Recognize speech
        text = recognizer.recognize_google(audio_data, language=lang_code)
        return text
    
    except Exception as e:
        st.error(f"Speech recognition error: {str(e)}")
        return None

def text_to_speech(text: str, language: str) -> Optional[bytes]:
    """Convert text to speech using gTTS"""
    try:
        from gtts import gTTS
        import io
        
        # Language codes for TTS
        lang_codes = {
            "English": "en",
            "Hindi": "hi",
            "Tamil": "ta",
            "Telugu": "te",
            "Spanish": "es",
            "French": "fr"
        }
        
        lang_code = lang_codes.get(language, "en")
        
        # Generate speech
        tts = gTTS(text=text, lang=lang_code, slow=False)
        
        # Save to bytes
        audio_bytes = io.BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        
        return audio_bytes.read()
    
    except Exception as e:
        st.error(f"Text-to-speech error: {str(e)}")
        return None

# ==================== UI TEXT TRANSLATION ====================

def get_translated_ui_text(key: str, language: str) -> str:
    """Get UI text translated in real-time using Gemini"""
    
    # Cache translations in session state to avoid repeated API calls
    if 'ui_translations' not in st.session_state:
        st.session_state.ui_translations = {}
    
    cache_key = f"{key}_{language}"
    
    # Return cached translation if available
    if cache_key in st.session_state.ui_translations:
        return st.session_state.ui_translations[cache_key]
    
    # For English, use original text
    if language == "English":
        from components.language import TRANSLATIONS
        return TRANSLATIONS["English"].get(key, key)
    
    # Translate using Gemini for other languages
    try:
        from components.language import TRANSLATIONS
        english_text = TRANSLATIONS["English"].get(key, key)
        
        translated = translate_text_with_gemini(english_text, language)
        
        # Cache the translation
        st.session_state.ui_translations[cache_key] = translated
        
        return translated
    
    except Exception as e:
        # Fallback to static translations
        from components.language import TRANSLATIONS
        return TRANSLATIONS.get(language, TRANSLATIONS["English"]).get(key, key)
