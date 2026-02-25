"""
Popup Chatbot Component - Floating AI Assistant
Accessible from any page as a popup overlay
"""

import streamlit as st
from components.language import get_text
from components.gemini_ai import get_ai_chat_response, init_gemini

def render_popup_chatbot():
    """Render floating chatbot button and popup overlay"""
    
    # Initialize chatbot state
    if 'chatbot_open' not in st.session_state:
        st.session_state.chatbot_open = False
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # CSS for popup chatbot
    st.markdown("""
    <style>
    /* Floating chatbot button container */
    .floating-chat-container {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 9999;
    }
    
    /* Chat messages styling */
    .chat-message {
        margin-bottom: 15px;
        padding: 12px 16px;
        border-radius: 12px;
        animation: messageSlide 0.3s ease;
    }
    
    @keyframes messageSlide {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .user-message {
        background: #4CAF50;
        color: white;
        text-align: left;
    }
    
    .bot-message {
        background: white;
        color: #1b5e20;
        border: 1px solid #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Render popup when open
    if st.session_state.chatbot_open:
        render_chatbot_popup()

def render_chatbot_popup():
    """Render the actual chatbot popup content"""
    
    # Check Gemini initialization
    model = init_gemini()
    
    # Create popup overlay
    with st.container():
        # Header with close button
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"### 🤖 {get_text('chatbot_title')}")
        with col2:
            if st.button("✕", key="close_chatbot", help="Close"):
                st.session_state.chatbot_open = False
                st.rerun()
        
        st.markdown("---")
        
        # Check if AI is configured
        if not model:
            st.error("⚠️ AI service not configured. Please add your Gemini API key.")
            return
        
        # Chat messages area
        chat_container = st.container()
        with chat_container:
            if st.session_state.chat_history:
                for chat in st.session_state.chat_history:
                    if chat['role'] == 'user':
                        st.markdown(f"""
                        <div class='chat-message user-message'>
                            <strong>You:</strong> {chat['message']}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class='chat-message bot-message'>
                            <strong>🤖 AI:</strong> {chat['message']}
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class='chatbot-welcome'>
                    <h4>👋 {get_text('chatbot_subtitle')}</h4>
                    <p>{get_text('chatbot_desc')}</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Sample questions
        with st.expander(f"💡 {get_text('sample_questions')}", expanded=False):
            sample_questions = [
                "What are symptoms of tomato blight?",
                "How to prevent fungal diseases?",
                "Best organic fertilizers?",
                "How to improve soil health?",
                "What causes leaf yellowing?",
                "Pest control methods?",
            ]
            
            cols = st.columns(2)
            for idx, question in enumerate(sample_questions):
                col = cols[idx % 2]
                with col:
                    if st.button(question, key=f"sq_popup_{idx}", use_container_width=True):
                        process_chat_message(question)
        
        # Chat input
        st.markdown("---")
        col1, col2 = st.columns([5, 1])
        
        with col1:
            user_input = st.text_input(
                get_text('chat_input'),
                key="popup_chat_input",
                label_visibility="collapsed",
                placeholder=get_text('chat_input')
            )
        
        with col2:
            send_button = st.button("📤", use_container_width=True, key="popup_send")
        
        # Process input
        if send_button and user_input:
            process_chat_message(user_input)
        
        # Clear chat button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button(f"🗑️ {get_text('clear_chat')}", use_container_width=True, key="popup_clear"):
                st.session_state.chat_history = []
                st.rerun()

def process_chat_message(message):
    """Process a chat message and get AI response"""
    # Add user message
    st.session_state.chat_history.append({
        'role': 'user',
        'message': message
    })
    
    # Get AI response
    with st.spinner("🤖 AI is thinking..."):
        current_language = st.session_state.get('language', 'English')
        response = get_ai_chat_response(
            message,
            current_language,
            st.session_state.chat_history
        )
    
    # Add bot response
    st.session_state.chat_history.append({
        'role': 'bot',
        'message': response
    })
    
    st.rerun()

def render_floating_chatbot_button():
    """Render just the floating button (for pages that want minimal integration)"""
    
    # Initialize state
    if 'chatbot_open' not in st.session_state:
        st.session_state.chatbot_open = False
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Create columns to position button in bottom right
    st.markdown("---")
    
    # Chatbot toggle section
    col1, col2, col3 = st.columns([4, 1, 1])
    
    with col3:
        if not st.session_state.chatbot_open:
            if st.button("🤖 AI Chat", key="open_chatbot_btn", use_container_width=True, 
                        help="Open AI Assistant", type="primary"):
                st.session_state.chatbot_open = True
                st.rerun()
    
    # Show popup if open
    if st.session_state.chatbot_open:
        # Create a dialog-like interface
        st.markdown("---")
        
        # Header with close button
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"### 🤖 {get_text('chatbot_title')}")
            st.caption(get_text('chatbot_subtitle'))
        with col2:
            if st.button("✕", key="close_chatbot", help="Close", type="secondary"):
                st.session_state.chatbot_open = False
                st.rerun()
        
        st.markdown("---")
        
        # Check if AI is configured
        model = init_gemini()
        if not model:
            st.error("⚠️ AI service not configured. Please add your Gemini API key.")
            return
        
        # Chat messages area in a container
        chat_container = st.container()
        with chat_container:
            if st.session_state.chat_history:
                for chat in st.session_state.chat_history:
                    if chat['role'] == 'user':
                        st.markdown(f"""
                        <div class='chat-message user-message'>
                            <strong>You:</strong> {chat['message']}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class='chat-message bot-message'>
                            <strong>🤖 AI:</strong> {chat['message']}
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.info(f"👋 {get_text('chatbot_desc')}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Sample questions
        with st.expander(f"💡 {get_text('sample_questions')}", expanded=False):
            sample_questions = [
                "What are symptoms of tomato blight?",
                "How to prevent fungal diseases?",
                "Best organic fertilizers?",
                "How to improve soil health?",
                "What causes leaf yellowing?",
                "Pest control methods?",
            ]
            
            cols = st.columns(2)
            for idx, question in enumerate(sample_questions):
                col = cols[idx % 2]
                with col:
                    if st.button(question, key=f"sq_popup_{idx}", use_container_width=True):
                        process_chat_message(question)
        
        # Chat input
        st.markdown("---")
        col1, col2 = st.columns([5, 1])
        
        with col1:
            user_input = st.text_input(
                get_text('chat_input'),
                key="popup_chat_input",
                label_visibility="collapsed",
                placeholder=get_text('chat_input')
            )
        
        with col2:
            send_button = st.button("📤", use_container_width=True, key="popup_send", type="primary")
        
        # Process input
        if send_button and user_input:
            process_chat_message(user_input)
        
        # Clear chat button
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button(f"🗑️ {get_text('clear_chat')}", use_container_width=True, key="popup_clear"):
                st.session_state.chat_history = []
                st.rerun()
        
        st.markdown("---")
