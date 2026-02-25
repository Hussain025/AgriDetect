"""
Crop History Dashboard - AgroDetect AI
User disease detection history with analytics
"""

import streamlit as st
from components.language import init_session_state, get_text, load_custom_css
from components.navbar import render_navbar
from components.auth import init_auth_state, require_auth
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="My Crop History - AgroDetect AI",
    page_icon="📊",
    layout="wide"
)

# Initialize
init_session_state()
init_auth_state()
require_auth()
load_custom_css()
render_navbar()

# ==================== CROP HISTORY PAGE ====================

# Header
st.markdown("""
<h1 style='text-align: center; color: #2e7d32; font-size: 42px;'>
    📊 My Crop History Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; color: #558b2f; font-size: 18px; margin-bottom: 30px;'>
    Track your disease detections and crop health over time
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Check if history exists
if 'disease_history' not in st.session_state or len(st.session_state.disease_history) == 0:
    st.info("📝 No disease detection history yet. Upload and analyze plant images to build your history!")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📤 Go to Upload", use_container_width=True):
            st.switch_page("pages/3_Upload.py")
else:
    # Get history data
    history = st.session_state.disease_history
    
    # Summary Statistics
    st.markdown("<h2 style='color: #2e7d32;'>📈 Summary Statistics</h2>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style='padding: 20px; background-color: #e8f5e9; border-radius: 10px; text-align: center;'>
            <h3 style='color: #2e7d32; margin: 0;'>{len(history)}</h3>
            <p style='color: #558b2f; margin: 5px 0;'>Total Scans</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        unique_diseases = len(set([h['disease'] for h in history]))
        st.markdown(f"""
        <div style='padding: 20px; background-color: #fff3e0; border-radius: 10px; text-align: center;'>
            <h3 style='color: #e65100; margin: 0;'>{unique_diseases}</h3>
            <p style='color: #ef6c00; margin: 5px 0;'>Unique Diseases</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_confidence = sum([h['confidence'] for h in history]) / len(history)
        st.markdown(f"""
        <div style='padding: 20px; background-color: #e3f2fd; border-radius: 10px; text-align: center;'>
            <h3 style='color: #1565c0; margin: 0;'>{avg_confidence:.1f}%</h3>
            <p style='color: #1976d2; margin: 5px 0;'>Avg Confidence</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        unique_crops = len(set([h['crop'] for h in history]))
        st.markdown(f"""
        <div style='padding: 20px; background-color: #f3e5f5; border-radius: 10px; text-align: center;'>
            <h3 style='color: #7b1fa2; margin: 0;'>{unique_crops}</h3>
            <p style='color: #8e24aa; margin: 5px 0;'>Crop Types</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # History Table
    st.markdown("<h2 style='color: #2e7d32;'>📋 Detection History</h2>", unsafe_allow_html=True)
    
    # Convert to DataFrame
    df = pd.DataFrame(history)
    df = df[['date', 'crop', 'disease', 'confidence']]
    df.columns = ['Date', 'Crop Type', 'Disease Detected', 'Confidence (%)']
    
    # Display table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Disease Distribution
    st.markdown("<h2 style='color: #2e7d32;'>📊 Disease Distribution</h2>", unsafe_allow_html=True)
    
    disease_counts = {}
    for h in history:
        disease = h['disease']
        disease_counts[disease] = disease_counts.get(disease, 0) + 1
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Bar chart using Streamlit's native chart
        chart_data = pd.DataFrame({
            'Disease': list(disease_counts.keys()),
            'Count': list(disease_counts.values())
        })
        st.bar_chart(chart_data.set_index('Disease'))
    
    with col2:
        st.markdown("""
        <div style='padding: 20px; background-color: white; border-radius: 10px; 
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);'>
            <h4 style='color: #2e7d32; margin-bottom: 15px;'>📌 Insights</h4>
        """, unsafe_allow_html=True)
        
        most_common = max(disease_counts, key=disease_counts.get)
        st.markdown(f"<p style='color: #1b5e20; margin: 8px 0;'>• Most common: <strong>{most_common}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #1b5e20; margin: 8px 0;'>• Total detections: <strong>{len(history)}</strong></p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #1b5e20; margin: 8px 0;'>• Avg confidence: <strong>{avg_confidence:.1f}%</strong></p>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Recent Activity
    st.markdown("<h2 style='color: #2e7d32;'>🕐 Recent Activity</h2>", unsafe_allow_html=True)
    
    recent_history = history[-5:] if len(history) > 5 else history
    recent_history.reverse()
    
    for item in recent_history:
        st.markdown(f"""
        <div style='padding: 15px; margin: 10px 0; background-color: #f5f5f5; 
                    border-left: 4px solid #4CAF50; border-radius: 5px;'>
            <p style='color: #2e7d32; margin: 0;'><strong>{item['date']}</strong></p>
            <p style='color: #1b5e20; margin: 5px 0;'>
                🌱 Crop: {item['crop']} | 🦠 Disease: {item['disease']} | 
                📈 Confidence: {item['confidence']}%
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📤 New Analysis", use_container_width=True):
            st.switch_page("pages/3_Upload.py")
    
    with col2:
        if st.button("🤖 AI Assistant", use_container_width=True):
            st.switch_page("pages/5_AI_Assistant.py")
    
    with col3:
        if st.button("🏠 Home", use_container_width=True):
            st.switch_page("pages/1_Home.py")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Export option
    with st.expander("📥 Export History"):
        st.markdown("Download your crop history data for record keeping")
        
        csv = df.to_csv(index=False)
        st.download_button(
            label="📄 Download as CSV",
            data=csv,
            file_name=f"agrodetect_history_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )
