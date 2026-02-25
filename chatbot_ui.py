"""
Chatbot UI Component - Real Gemini AI Integration
Enhanced Agriculture-Focused AI Assistant
"""

import streamlit as st
from components.language import get_text
from components.gemini_ai import get_ai_chat_response, init_gemini

def render_chat_message(role, message):
    """Render a single chat message"""
    if role == 'user':
        st.markdown(f"""
        <div class='chat-message user-message'>
            <strong>You:</strong> {message}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='chat-message bot-message'>
            <strong>🤖 AI Agricultural Assistant:</strong> {message}
        </div>
        """, unsafe_allow_html=True)

def render_chatbot():
    """Render complete chatbot interface with real Gemini AI"""
    
    # Check Gemini initialization
    model = init_gemini()
    if not model:
        st.error("⚠️ AI service not configured. Please add your Gemini API key to .streamlit/secrets.toml")
        st.code("""
# Create .streamlit/secrets.toml file with:
GEMINI_API_KEY = "your-api-key-here"
        """)
        return
    
    # Chat history display
    chat_container = st.container()
    with chat_container:
        if st.session_state.chat_history:
            for chat in st.session_state.chat_history:
                render_chat_message(chat['role'], chat['message'])
        else:
            st.info("👋 " + get_text('chatbot_desc'))
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Sample questions
    with st.expander(get_text('sample_questions')):
        col1, col2 = st.columns(2)
        
        sample_questions = [
            ("What are symptoms of tomato blight?", "sq1"),
            ("How to prevent fungal diseases?", "sq2"),
            ("Best organic fertilizers?", "sq3"),
            ("How to improve soil health?", "sq4"),
            ("What causes leaf yellowing?", "sq5"),
            ("Pest control methods?", "sq6"),
        ]
        
        for idx, (question, key) in enumerate(sample_questions):
            col = col1 if idx % 2 == 0 else col2
            with col:
                if st.button(question, key=key, use_container_width=True):
                    # Add user message
                    st.session_state.chat_history.append({
                        'role': 'user',
                        'message': question
                    })
                    
                    # Get AI response
                    with st.spinner("🤖 AI is thinking..."):
                        current_language = st.session_state.get('language', 'English')
                        response = get_ai_chat_response(
                            question, 
                            current_language,
                            st.session_state.chat_history
                        )
                    
                    # Add bot response
                    st.session_state.chat_history.append({
                        'role': 'bot',
                        'message': response
                    })
                    
                    st.rerun()
    
    # Chat input
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input(
            get_text('chat_input'),
            key="chat_input_field",
            label_visibility="collapsed",
            placeholder=get_text('chat_input')
        )
    
    with col2:
        send_button = st.button(get_text('send_btn'), use_container_width=True)
    
    # Process chat with real AI
    if send_button and user_input:
        # Add user message
        st.session_state.chat_history.append({
            'role': 'user',
            'message': user_input
        })
        
        # Get AI response from Gemini
        with st.spinner("🤖 AI is generating response..."):
            current_language = st.session_state.get('language', 'English')
            bot_response = get_ai_chat_response(
                user_input,
                current_language,
                st.session_state.chat_history
            )
        
        # Add bot response
        st.session_state.chat_history.append({
            'role': 'bot',
            'message': bot_response
        })
        
        st.rerun()
    
    # Clear chat button
    if st.button(get_text('clear_chat')):
        st.session_state.chat_history = []
        st.rerun()
