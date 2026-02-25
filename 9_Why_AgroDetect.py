"""
Why AgroDetect AI - Value Proposition & Comparison
Traditional vs AI-powered diagnosis
"""

import streamlit as st
from components.language import init_session_state, load_custom_css
from components.navbar import render_navbar
from components.auth import init_auth_state, require_auth

# Page configuration
st.set_page_config(
    page_title="Why AgroDetect AI",
    page_icon="⭐",
    layout="wide"
)

# Initialize
init_session_state()
init_auth_state()
require_auth()
load_custom_css()
render_navbar()

# ==================== WHY AGRODETECT AI PAGE ====================

# Header
st.markdown("""
<h1 style='text-align: center; color: #2e7d32; font-size: 48px;'>
    ⭐ Why Choose AgroDetect AI?
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; color: #558b2f; font-size: 20px; margin-bottom: 40px;'>
    The Future of Plant Disease Diagnosis is Here
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Comparison Table
st.markdown("<h2 style='text-align: center; color: #2e7d32; margin-bottom: 30px;'>📊 Traditional vs AgroDetect AI</h2>", unsafe_allow_html=True)

# Create comparison data
comparison_data = {
    "Feature": [
        "⏱️ Diagnosis Speed",
        "💰 Cost",
        "🎯 Accuracy",
        "📍 Accessibility",
        "🌍 Availability",
        "📚 Knowledge Base",
        "🔄 Updates",
        "📱 Device Required",
        "🌐 Language Support",
        "📊 History Tracking"
    ],
    "Traditional Method": [
        "2-7 days (lab testing)",
        "₹500-2000 per test",
        "70-80% (varies by expert)",
        "Limited to urban areas",
        "Office hours only",
        "Expert dependent",
        "Slow, manual",
        "Physical visit required",
        "Limited languages",
        "Manual record keeping"
    ],
    "AgroDetect AI": [
        "< 30 seconds",
        "Free / Minimal cost",
        "95%+ (AI-powered)",
        "Anywhere with internet",
        "24/7 availability",
        "Vast AI database",
        "Real-time, automatic",
        "Just a smartphone",
        "6+ languages",
        "Automatic digital tracking"
    ]
}

# Display as styled table
st.markdown("""
<style>
.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    border-radius: 10px;
    overflow: hidden;
}
.comparison-table th {
    background-color: #2e7d32;
    color: white;
    padding: 15px;
    text-align: left;
    font-size: 18px;
}
.comparison-table td {
    padding: 15px;
    border-bottom: 1px solid #e0e0e0;
    font-size: 16px;
}
.comparison-table tr:nth-child(even) {
    background-color: #f5f5f5;
}
.comparison-table tr:hover {
    background-color: #e8f5e9;
}
.traditional-col {
    color: #d32f2f;
}
.agrodetect-col {
    color: #2e7d32;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

table_html = "<table class='comparison-table'>"
table_html += "<tr><th>Feature</th><th>Traditional Method</th><th>AgroDetect AI ✨</th></tr>"

for i in range(len(comparison_data["Feature"])):
    table_html += f"""
    <tr>
        <td><strong>{comparison_data["Feature"][i]}</strong></td>
        <td class='traditional-col'>{comparison_data["Traditional Method"][i]}</td>
        <td class='agrodetect-col'>{comparison_data["AgroDetect AI"][i]}</td>
    </tr>
    """

table_html += "</table>"
st.markdown(table_html, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Key Advantages
st.markdown("<h2 style='color: #2e7d32; margin-bottom: 30px;'>🚀 Key Advantages</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='padding: 25px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;'>
        <h3 style='color: #2e7d32; text-align: center; margin-bottom: 20px;'>⚡ Speed & Efficiency</h3>
        <ul style='color: #1b5e20; font-size: 16px; line-height: 2;'>
            <li>Instant diagnosis in seconds</li>
            <li>No waiting for lab results</li>
            <li>Real-time recommendations</li>
            <li>Immediate action possible</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 25px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;'>
        <h3 style='color: #2e7d32; text-align: center; margin-bottom: 20px;'>💡 Intelligence & Accuracy</h3>
        <ul style='color: #1b5e20; font-size: 16px; line-height: 2;'>
            <li>AI-powered analysis</li>
            <li>95%+ accuracy rate</li>
            <li>Continuous learning</li>
            <li>Expert knowledge base</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='padding: 25px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;'>
        <h3 style='color: #2e7d32; text-align: center; margin-bottom: 20px;'>🌍 Accessibility & Reach</h3>
        <ul style='color: #1b5e20; font-size: 16px; line-height: 2;'>
            <li>Available 24/7</li>
            <li>Works anywhere</li>
            <li>Multi-language support</li>
            <li>Smartphone compatible</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ROI Calculator
st.markdown("<h2 style='color: #2e7d32; margin-bottom: 30px;'>💰 Return on Investment Calculator</h2>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div style='padding: 25px; background-color: #e8f5e9; border-radius: 15px;'>
        <h4 style='color: #2e7d32; margin-bottom: 20px;'>Calculate Your Savings</h4>
    """, unsafe_allow_html=True)
    
    farm_size = st.slider("Farm Size (acres)", 1, 100, 10)
    crop_value = st.slider("Crop Value per acre (₹)", 10000, 200000, 50000, step=10000)
    disease_risk = st.slider("Disease Risk (%)", 10, 50, 20)
    
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Calculate savings
    potential_loss = farm_size * crop_value * (disease_risk / 100)
    with_agrodetect = potential_loss * 0.15  # 85% reduction in loss
    savings = potential_loss - with_agrodetect
    
    st.markdown(f"""
    <div style='padding: 25px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h4 style='color: #2e7d32; margin-bottom: 20px;'>Your Potential Savings</h4>
        <div style='padding: 15px; background-color: #ffebee; border-radius: 8px; margin: 10px 0;'>
            <p style='color: #c62828; margin: 0;'>Without AgroDetect AI:</p>
            <h3 style='color: #d32f2f; margin: 5px 0;'>₹{potential_loss:,.0f} loss</h3>
        </div>
        <div style='padding: 15px; background-color: #e8f5e9; border-radius: 8px; margin: 10px 0;'>
            <p style='color: #2e7d32; margin: 0;'>With AgroDetect AI:</p>
            <h3 style='color: #4CAF50; margin: 5px 0;'>₹{with_agrodetect:,.0f} loss</h3>
        </div>
        <div style='padding: 15px; background-color: #fff3e0; border-radius: 8px; margin: 10px 0;'>
            <p style='color: #e65100; margin: 0;'>Total Savings:</p>
            <h2 style='color: #ff9800; margin: 5px 0;'>₹{savings:,.0f}</h2>
        </div>
        <p style='color: #558b2f; font-size: 14px; margin-top: 15px; font-style: italic;'>
            *Based on 85% crop loss reduction with early detection
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Testimonials
st.markdown("<h2 style='color: #2e7d32; margin-bottom: 30px;'>💬 What Users Say</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='padding: 20px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <p style='color: #1b5e20; font-size: 16px; line-height: 1.8; font-style: italic;'>
            "Game changer for small farmers like me. Saved my entire crop!"
        </p>
        <p style='color: #558b2f; margin-top: 15px;'>⭐⭐⭐⭐⭐</p>
        <p style='color: #2e7d32; font-weight: 500;'>- Suresh, Farmer</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 20px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <p style='color: #1b5e20; font-size: 16px; line-height: 1.8; font-style: italic;'>
            "Incredibly accurate and easy to use. Highly recommended!"
        </p>
        <p style='color: #558b2f; margin-top: 15px;'>⭐⭐⭐⭐⭐</p>
        <p style='color: #2e7d32; font-weight: 500;'>- Dr. Patel, Agronomist</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='padding: 20px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <p style='color: #1b5e20; font-size: 16px; line-height: 1.8; font-style: italic;'>
            "24/7 availability is a lifesaver. No more waiting for experts!"
        </p>
        <p style='color: #558b2f; margin-top: 15px;'>⭐⭐⭐⭐⭐</p>
        <p style='color: #2e7d32; font-weight: 500;'>- Lakshmi, Farmer</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div style='text-align: center; padding: 50px 20px; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); 
            border-radius: 20px;'>
    <h2 style='color: #2e7d32; font-size: 36px; margin-bottom: 20px;'>
        Ready to Transform Your Farming?
    </h2>
    <p style='color: #1b5e20; font-size: 20px; margin-bottom: 30px;'>
        Join thousands of farmers already using AgroDetect AI
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Action buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("📤 Start Now", use_container_width=True):
        st.switch_page("pages/3_Upload.py")

with col2:
    if st.button("📊 View Impact", use_container_width=True):
        st.switch_page("pages/8_Sustainability.py")

with col3:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("pages/1_Home.py")
