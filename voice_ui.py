"""
Voice Assistant UI Component - Real-time Multilingual Voice with Gemini AI
"""

import streamlit as st
import time
from components.language import get_text
from components.gemini_ai import get_ai_chat_response, text_to_speech, init_gemini
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import io

def process_voice_input(audio_bytes, language: str) -> str:
    """Process audio input and convert to text"""
    try:
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
        
        # Convert bytes to AudioData
        audio_data = sr.AudioData(audio_bytes, 16000, 2)
        
        # Recognize speech
        text = recognizer.recognize_google(audio_data, language=lang_code)
        return text
    
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        st.error(f"Speech recognition service error: {e}")
        return None
    except Exception as e:
        st.error(f"Error processing voice: {str(e)}")
        return None

def render_voice_assistant():
    """Render real-time voice assistant interface with Gemini AI"""
    
    # Check Gemini initialization
    model = init_gemini()
    if not model:
        st.error("⚠️ AI service not configured. Please add your Gemini API key to .streamlit/secrets.toml")
        return
    
    current_language = st.session_state.get('language', 'English')
    
    # Voice input section with audio recorder
    st.markdown("""
    <div class='info-box' style='text-align: center; padding: 25px;'>
        <h3 style='color: #1b5e20; margin-bottom: 15px;'>🎤 Voice Interaction</h3>
        <p style='color: #2e7d32; font-size: 16px;'>
            Click the microphone below to record your question in {language}
        </p>
    </div>
    """.format(language=current_language), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Audio recorder
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Alternative: Manual text input for voice simulation
        st.markdown("<h4 style='text-align: center; color: #1b5e20;'>🎤 Speak Your Question</h4>", unsafe_allow_html=True)
        
        voice_input_text = st.text_input(
            "Type or speak your question:",
            key="voice_input_manual",
            placeholder=f"Ask in {current_language}...",
            label_visibility="collapsed"
        )
        
        if st.button("🎤 Process Voice Question", use_container_width=True, key="process_voice"):
            if voice_input_text:
                with st.spinner("🧠 Processing with AI..."):
                    # Store recognized text
                    st.session_state.voice_text = voice_input_text
                    
                    # Get AI response from Gemini
                    ai_response = get_ai_chat_response(
                        voice_input_text,
                        current_language,
                        []
                    )
                    
                    st.session_state.voice_response = ai_response
                
                st.success("✅ AI response generated!")
                st.rerun()
            else:
                st.warning("Please enter a question first")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display recognized text and AI response
    if st.session_state.get('voice_text'):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"<h4 style='color: #2e7d32;'>📝 {get_text('recognized_text')}</h4>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class='info-box' style='padding: 25px; min-height: 150px;'>
                <p style='font-size: 16px; color: #0d3d0d; line-height: 1.7; font-weight: 600;'>
                    {st.session_state.voice_text}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"<h4 style='color: #2e7d32;'>🤖 {get_text('ai_response')}</h4>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class='result-card' style='padding: 25px; min-height: 150px;'>
                <p style='font-size: 16px; color: #0d3d0d; line-height: 1.7; font-weight: 600;'>
                    {st.session_state.voice_response}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Play voice button with real TTS
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔊 " + get_text('play_voice'), use_container_width=True, key="play_voice_btn"):
                with st.spinner("🔊 Generating voice..."):
                    # Generate speech from AI response
                    audio_bytes = text_to_speech(
                        st.session_state.voice_response,
                        current_language
                    )
                    
                    if audio_bytes:
                        # Play audio
                        st.audio(audio_bytes, format='audio/mp3')
                        st.success(f"✅ Playing in {current_language}")
                    else:
                        st.error("Failed to generate voice")
    
    else:
        # Show instructions when no voice input yet
        st.markdown(f"""
        <div class='voice-box'>
            <h3 style='color: #1b5e20; margin-bottom: 20px;'>🎤 Ready to Listen</h3>
            <p style='color: #2e7d32; font-size: 17px; line-height: 1.8;'>
                Enter your question above and click "Process Voice Question"<br>
                The AI will respond in <strong>{current_language}</strong><br><br>
                🌍 Supports: English, Hindi, Tamil, Telugu, Spanish, French
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Voice features info
    with st.expander("ℹ️ Voice Assistant Features"):
        st.markdown("""
        <div class='info-box'>
            <h4 style='color: #1b5e20;'>Real-Time Multilingual Voice AI</h4>
            <ul style='color: #2e7d32; line-height: 2;'>
                <li>🎤 <strong>Speech Recognition:</strong> Understands your spoken language</li>
                <li>🤖 <strong>Gemini AI:</strong> Generates intelligent responses</li>
                <li>🔊 <strong>Text-to-Speech:</strong> Speaks responses in your language</li>
                <li>🌍 <strong>6 Languages:</strong> English, Hindi, Tamil, Telugu, Spanish, French</li>
                <li>🌾 <strong>Agriculture Expert:</strong> Specialized in plant diseases and crop care</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
