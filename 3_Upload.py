"""
Upload Page - AgroDetect AI
Image upload and analysis trigger with ML model integration
"""

import streamlit as st
from PIL import Image
import time
from components.language import init_session_state, get_text, load_custom_css
from components.navbar import render_navbar
from components.auth import init_auth_state, require_auth
from components.chatbot_popup import render_floating_chatbot_button
from components.ml_model_connector import (
    load_plant_disease_model,
    predict_disease,
    validate_image,
    check_model_availability
)

# Page configuration
st.set_page_config(
    page_title="Upload - AgroDetect AI",
    page_icon="📤",
    layout="wide"
)

# Initialize
init_session_state()
init_auth_state()

# Require authentication
require_auth()

load_custom_css()
render_navbar()

# ==================== UPLOAD PAGE CONTENT ====================

# Check model availability on page load
if 'model_check_done' not in st.session_state:
    with st.spinner("🔄 Initializing ML model..."):
        model_available = check_model_availability()
        st.session_state.model_check_done = True
        st.session_state.model_available = model_available
        
        if not model_available:
            st.info("💡 Running in Demo Mode - Using simulated predictions for demonstration purposes.")
            st.info("ℹ️ For real ML predictions, PyTorch needs to be properly installed with Visual C++ redistributables.")

# Header
st.markdown(f"""
<h1 style='text-align: center; color: #2e7d32; font-size: 42px;'>
    📤 {get_text('upload_title')}
</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# Description with glass effect
st.markdown(f"""
<div class='info-box' style='text-align: center; font-size: 16px; padding: 25px; margin-bottom: 30px;'>
    <p style='color: #1b5e20; margin: 0; font-size: 17px;'>{get_text('upload_desc')}</p>
    <p style='color: #2e7d32; margin: 10px 0 0 0; font-weight: 600;'>{get_text('supported_formats')}</p>
</div>
""", unsafe_allow_html=True)

# Image uploader
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    uploaded_file = st.file_uploader(
        get_text('choose_image'),
        type=['jpg', 'jpeg', 'png'],
        help=get_text('upload_desc'),
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        
        # Validate image
        is_valid, validation_msg = validate_image(image)
        
        if not is_valid:
            st.error(f"❌ {validation_msg}")
            st.stop()
        
        st.session_state.uploaded_image = image
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <h3 style='text-align: center; color: #2e7d32;'>
            📷 {get_text('image_preview')}
        </h3>
        """, unsafe_allow_html=True)
        
        # Image container with styling
        st.markdown("""
        <div class='image-container'>
        """, unsafe_allow_html=True)
        
        st.image(image, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Analyze button
        if st.button(get_text('analyze_btn'), use_container_width=True, key="analyze_btn"):
            with st.spinner(f"🤖 {get_text('analyzing')}"):
                # Load ML model
                processor, model = load_plant_disease_model()
                
                # Progress bar for user feedback
                progress_bar = st.progress(0)
                progress_bar.progress(30)
                
                # Make prediction using ML model (or demo mode)
                prediction_results = predict_disease(image, processor, model)
                progress_bar.progress(80)
                
                if prediction_results is None:
                    st.error("❌ Prediction failed. Please try again with a different image.")
                    st.stop()
                
                # Show demo mode indicator if applicable
                if prediction_results.get('demo_mode', False):
                    st.info("💡 Demo Mode: Showing simulated prediction based on image analysis")
                
                # Store results in session state
                st.session_state.ml_prediction = prediction_results
                st.session_state.analysis_done = True
                
                progress_bar.progress(100)
            
            st.success(f"✅ {get_text('analysis_complete')}")
            time.sleep(1)
            st.switch_page("pages/4_Results.py")
    
    else:
        # Show upload prompt with glass effect
        st.markdown(f"""
        <div class='feature-card' style='text-align: center; padding: 50px; margin-top: 30px; border: 2px dashed rgba(76, 175, 80, 0.5);'>
            <h2 style='color: #1b5e20; font-size: 64px; margin-bottom: 20px;'>📁</h2>
            <p style='color: #2e7d32; font-size: 18px; font-weight: 500;'>{get_text('upload_prompt')}</p>
        </div>
        """, unsafe_allow_html=True)

# Render floating chatbot button
render_floating_chatbot_button()
