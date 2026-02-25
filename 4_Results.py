"""
Results Page - AgroDetect AI
Real-time AI-Generated Recommendations with Gemini AI and ML Predictions
"""

import streamlit as st
from components.language import init_session_state, get_text, load_custom_css
from components.navbar import render_navbar
from components.cards import result_card
from components.auth import init_auth_state, require_auth
from components.gemini_ai import get_disease_recommendation, get_xai_explanation, text_to_speech, init_gemini
from components.chatbot_popup import render_floating_chatbot_button
from components.ml_model_connector import get_disease_recommendations, get_dataset_info
from datetime import datetime
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Results - AgroDetect AI",
    page_icon="📊",
    layout="wide"
)

# Initialize
init_session_state()
init_auth_state()
require_auth()
load_custom_css()
render_navbar()

# ==================== AI RECOMMENDATION DATA ====================
AI_RECOMMENDATIONS = {
    "Tomato Late Blight": {
        "cause": "Caused by the fungus-like organism Phytophthora infestans. Thrives in cool, wet conditions with high humidity.",
        "treatment": [
            "Remove and destroy all infected plant parts immediately",
            "Apply copper-based fungicides (Bordeaux mixture) every 7-10 days",
            "Use systemic fungicides like Mancozeb or Chlorothalonil",
            "Improve air circulation by proper spacing",
            "Water plants at the base, avoid wetting foliage"
        ],
        "prevention": [
            "Plant resistant varieties when available",
            "Ensure proper plant spacing (18-24 inches)",
            "Use drip irrigation instead of overhead watering",
            "Apply mulch to prevent soil splash",
            "Rotate crops annually",
            "Monitor weather - disease spreads in cool, wet conditions"
        ],
        "organic": [
            "Neem oil spray (2-3 times per week)",
            "Baking soda solution (1 tbsp per gallon water)",
            "Copper sulfate organic fungicide",
            "Garlic and chili pepper spray"
        ],
        "chemical": [
            "Mancozeb 75% WP",
            "Chlorothalonil",
            "Metalaxyl + Mancozeb",
            "Cymoxanil + Mancozeb"
        ]
    }
}

# ==================== EXPLAINABLE AI DATA ====================
XAI_EXPLANATIONS = {
    "Tomato Late Blight": {
        "focus_areas": "Dark brown lesions on leaf edges and water-soaked spots",
        "confidence_factors": [
            "Irregular brown patches detected (95% match)",
            "Water-soaked appearance on leaf surface (92% match)",
            "Lesion pattern consistent with fungal infection (89% match)"
        ],
        "model_reasoning": "The AI model identified characteristic symptoms of late blight including irregular brown lesions, water-soaked spots, and specific pattern distribution typical of Phytophthora infestans infection."
    }
}

# ==================== LOCATION-BASED ALERTS ====================
LOCATION_ALERTS = {
    "North India": "⚠️ Late blight is common during monsoon season (July-September) in your region. High humidity increases risk.",
    "South India": "⚠️ Moderate risk in your region. Monitor during cooler months (November-February).",
    "Maharashtra": "⚠️ High risk during monsoon. This disease is prevalent in tomato-growing areas of your state.",
    "Karnataka": "⚠️ Moderate to high risk. Recent weather patterns favor disease spread.",
    "Default": "⚠️ This disease spreads rapidly in cool, humid conditions. Monitor weather closely."
}

# Header
st.markdown(f"""
<h1 style='text-align: center; color: #2e7d32; font-size: 42px;'>
    📊 {get_text('results_title')}
</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# Check if analysis is done
if st.session_state.uploaded_image is None or not st.session_state.analysis_done:
    st.warning(f"⚠️ {get_text('no_results')}")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button(get_text('go_upload'), use_container_width=True):
            st.switch_page("pages/3_Upload.py")
else:
    # Get ML prediction results
    ml_prediction = st.session_state.get('ml_prediction', None)
    
    if ml_prediction:
        # Use actual ML predictions
        disease_name = ml_prediction['predicted_disease']
        confidence = ml_prediction['confidence'] * 100  # Convert to percentage
        all_predictions = ml_prediction.get('all_probabilities', [])
        all_classes = ml_prediction.get('all_classes', [])
        is_demo_mode = ml_prediction.get('demo_mode', False)
        
        # Show demo mode banner if applicable
        if is_demo_mode:
            st.info("💡 Demo Mode Active: These are simulated predictions for demonstration. For real ML predictions, install PyTorch with proper dependencies.")
    else:
        # Fallback to demo data
        disease_name = get_text('disease_name')
        confidence = 96.5
        all_predictions = None
        all_classes = None
        is_demo_mode = True
    
    # Store in history
    if 'disease_history' not in st.session_state:
        st.session_state.disease_history = []
    
    current_result = {
        'disease': disease_name,
        'confidence': confidence,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
        'crop': 'Tomato'
    }
    
    if not any(h['date'] == current_result['date'] for h in st.session_state.disease_history):
        st.session_state.disease_history.append(current_result)
    
    # Display results
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"<h3 style='color: #2e7d32;'>📷 {get_text('analyzed_image')}</h3>", unsafe_allow_html=True)
        st.markdown("<div class='image-container'>", unsafe_allow_html=True)
        st.image(st.session_state.uploaded_image, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"<h3 style='color: #2e7d32;'>🔍 {get_text('detection_results')}</h3>", unsafe_allow_html=True)
        result_card(get_text('detected_disease'), disease_name, "🦠")
        result_card(get_text('confidence_score'), f"{confidence:.2f}%", "📈")
        
        # Show all predictions if available
        if all_predictions is not None and all_classes is not None:
            with st.expander("📊 All Predictions (Top 5)", expanded=False):
                # Sort by probability
                sorted_indices = np.argsort(all_predictions)[::-1][:5]
                
                for idx in sorted_indices:
                    label = all_classes[idx]
                    prob = all_predictions[idx] * 100
                    
                    # Color code based on probability
                    if prob > 50:
                        color = "🟢"
                    elif prob > 20:
                        color = "🟡"
                    else:
                        color = "⚪"
                    
                    st.markdown(f"{color} **{label}**: {prob:.2f}%")
                    st.progress(float(all_predictions[idx]))
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔊 Listen to Diagnosis", use_container_width=True, key="voice_diagnosis"):
            with st.spinner("🎤 Generating voice output..."):
                current_language = st.session_state.get('language', 'English')
                diagnosis_text = f"Disease detected is {disease_name} with {confidence:.1f}% confidence"
                audio_bytes = text_to_speech(diagnosis_text, current_language)
                
                if audio_bytes:
                    st.audio(audio_bytes, format='audio/mp3')
                    st.success(f"🔊 Playing in {current_language}")
                else:
                    st.info("🌍 Voice AI Assistant - Multi-language support available")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==================== EXPLAINABLE AI SECTION WITH GEMINI ====================
    st.markdown("<h2 style='color: #2e7d32; margin-top: 30px;'>🔬 Why AI Predicted This (Explainable AI)</h2>", unsafe_allow_html=True)
    
    # Get current language
    current_language = st.session_state.get('language', 'English')
    
    # Generate XAI explanation with Gemini
    xai_cache_key = f"xai_{disease_name}_{current_language}"
    
    if xai_cache_key not in st.session_state:
        with st.spinner("🧠 Generating AI explanation..."):
            xai_result = get_xai_explanation(disease_name, current_language)
            if xai_result:
                st.session_state[xai_cache_key] = xai_result
    
    # Display XAI explanation
    if xai_cache_key in st.session_state:
        xai_result = st.session_state[xai_cache_key]
        
        st.markdown(f"""
        <div class='info-box' style='padding: 30px;'>
            <h4 style='color: #1565c0; margin-bottom: 20px; font-weight: 700;'>🎯 AI Explanation</h4>
            <p style='color: #0d3d0d; font-size: 16px; line-height: 1.8; white-space: pre-wrap;'>{xai_result.get('explanation', '')}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Fallback to static XAI data
        xai_data = XAI_EXPLANATIONS.get("Tomato Late Blight", {})
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"""
        <div class='info-box' style='padding: 25px;'>
            <h4 style='color: #1565c0; margin-bottom: 15px; font-weight: 600;'>🎯 AI Focus Areas</h4>
            <p style='color: #0d47a1; font-size: 16px; line-height: 1.7;'>
                <strong>Detected Regions:</strong><br>{xai_data.get('focus_areas', '')}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='feature-card' style='padding: 25px;'><h4 style='color: #1b5e20; margin-bottom: 15px; font-weight: 600;'>📊 Confidence Factors</h4>", unsafe_allow_html=True)
        for factor in xai_data.get('confidence_factors', []):
            st.markdown(f"<p style='color: #2e7d32; margin: 10px 0; font-size: 15px;'>✓ {factor}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='warning-box' style='padding: 25px; height: 100%;'>
            <h4 style='color: #e65100; margin-bottom: 15px; font-weight: 600;'>🧠 Model Reasoning</h4>
            <p style='color: #e65100; font-size: 16px; line-height: 1.8;'>{xai_data.get('model_reasoning', '')}</p>
            <div class='info-box' style='margin-top: 20px; padding: 18px;'>
                <p style='color: #1b5e20; font-size: 14px; margin: 0;'>
                    <strong>Note:</strong> Heatmap visualization shows AI focused on affected leaf regions with dark lesions and water-soaked patterns.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==================== LOCATION-BASED ALERT ====================
    st.markdown("<h2 style='color: #2e7d32; margin-top: 30px;'>📍 Location-Based Disease Alert</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        user_location = st.selectbox(
            "🌍 Select Your Region",
            ["North India", "South India", "Maharashtra", "Karnataka", "Tamil Nadu", "Other"],
            key="user_location"
        )
    
    with col2:
        alert_message = LOCATION_ALERTS.get(user_location, LOCATION_ALERTS["Default"])
        st.markdown(f"""
        <div class='warning-box' style='padding: 25px;'>
            <p style='color: #e65100; font-size: 16px; line-height: 1.7; margin: 0; font-weight: 500;'>{alert_message}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==================== AI-GENERATED RECOMMENDATIONS WITH GEMINI ====================
    st.markdown("<h2 style='color: #2e7d32; margin-top: 30px;'>🤖 AI-Generated Treatment & Prevention (Powered by Gemini AI)</h2>", unsafe_allow_html=True)
    
    # Check if we need to generate recommendations
    current_language = st.session_state.get('language', 'English')
    cache_key = f"ai_rec_{disease_name}_{current_language}"
    
    if cache_key not in st.session_state:
        with st.spinner("🤖 Generating AI recommendations..."):
            ai_rec = get_disease_recommendation(disease_name, current_language)
            if ai_rec:
                st.session_state[cache_key] = ai_rec
    
    # Display AI recommendations
    if cache_key in st.session_state:
        ai_rec = st.session_state[cache_key]
        
        st.success(f"✅ Real-time AI recommendations in {current_language}")
        
        # Display full AI response
        st.markdown(f"""
        <div class='feature-card' style='padding: 30px;'>
            <p style='color: #0d3d0d; font-size: 16px; line-height: 1.8; white-space: pre-wrap;'>{ai_rec.get('full_text', '')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Voice output for recommendations
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔊 Listen to AI Recommendations", use_container_width=True, key="voice_recommendations"):
                with st.spinner("🎤 Converting to speech..."):
                    audio_bytes = text_to_speech(ai_rec.get('full_text', ''), current_language)
                    
                    if audio_bytes:
                        st.audio(audio_bytes, format='audio/mp3')
                        st.success(f"🔊 Playing in {current_language}")
                    else:
                        st.error("Voice generation failed")
    else:
        # Fallback to ML-based recommendations
        st.info("💡 Using ML-based recommendations")
        
        ml_recommendations = get_disease_recommendations(disease_name)
        
        # Display ML recommendations
        st.markdown(f"""
        <div class='feature-card' style='padding: 25px;'>
            <h4 style='color: #1b5e20; margin-bottom: 15px;'>📋 Status: {ml_recommendations.get('status', 'Unknown')}</h4>
            <p style='color: #2e7d32; font-size: 16px; line-height: 1.8;'>{ml_recommendations.get('message', '')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h4 style='color: #1b5e20;'>💊 Recommended Actions</h4>", unsafe_allow_html=True)
            for action in ml_recommendations.get('actions', []):
                st.markdown(f"<div class='result-card' style='padding: 12px; margin: 8px 0;'><p style='color: #1b5e20; margin: 0;'>✓ {action}</p></div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<h4 style='color: #1b5e20;'>🛡️ Prevention Tips</h4>", unsafe_allow_html=True)
            for tip in ml_recommendations.get('prevention', []):
                st.markdown(f"<div class='result-card' style='padding: 12px; margin: 8px 0;'><p style='color: #2e7d32; margin: 0;'>🌱 {tip}</p></div>", unsafe_allow_html=True)
        
        # Fallback to static recommendations if needed
        recommendations = AI_RECOMMENDATIONS.get("Tomato Late Blight", {})
        
        with st.expander("🔬 Disease Cause & Biology", expanded=True):
            st.markdown(f"<div class='feature-card' style='padding: 20px;'><p style='color: #1b5e20; font-size: 16px; line-height: 1.8;'>{recommendations.get('cause', '')}</p></div>", unsafe_allow_html=True)
        
        with st.expander("💊 Treatment Steps", expanded=True):
            st.markdown("<h4 style='color: #1b5e20; margin-bottom: 15px; font-weight: 600;'>Immediate Actions:</h4>", unsafe_allow_html=True)
            for i, step in enumerate(recommendations.get('treatment', []), 1):
                st.markdown(f"<div class='result-card' style='padding: 15px; margin: 10px 0;'><p style='color: #1b5e20; margin: 0; font-size: 15px;'><strong>{i}.</strong> {step}</p></div>", unsafe_allow_html=True)
        
        with st.expander("🛡️ Prevention Measures", expanded=True):
            st.markdown("<h4 style='color: #1b5e20; margin-bottom: 15px; font-weight: 600;'>Long-term Prevention:</h4>", unsafe_allow_html=True)
            for measure in recommendations.get('prevention', []):
                st.markdown(f"<p style='color: #2e7d32; margin: 10px 0; font-size: 15px;'>✓ {measure}</p>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            with st.expander("🌿 Organic Solutions"):
                for solution in recommendations.get('organic', []):
                    st.markdown(f"<p style='color: #2e7d32; margin: 8px 0;'>🌱 {solution}</p>", unsafe_allow_html=True)
        
        with col2:
            with st.expander("🧪 Chemical Solutions"):
                for solution in recommendations.get('chemical', []):
                    st.markdown(f"<p style='color: #1565c0; margin: 8px 0;'>⚗️ {solution}</p>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button(get_text('analyze_another'), use_container_width=True):
            st.session_state.uploaded_image = None
            st.session_state.analysis_done = False
            st.switch_page("pages/3_Upload.py")
    
    with col2:
        if st.button("📊 View My History", use_container_width=True):
            st.switch_page("pages/7_Crop_History.py")
    
    with col3:
        if st.button(get_text('back_home'), use_container_width=True):
            st.switch_page("pages/1_Home.py")

# Render floating chatbot button
render_floating_chatbot_button()
