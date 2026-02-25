"""
Sustainability & Social Impact - AgroDetect AI
Highlighting real-world impact and UN SDG alignment
"""

import streamlit as st
from components.language import init_session_state, load_custom_css
from components.navbar import render_navbar
from components.auth import init_auth_state, require_auth

# Page configuration
st.set_page_config(
    page_title="Sustainability & Impact - AgroDetect AI",
    page_icon="🌍",
    layout="wide"
)

# Initialize
init_session_state()
init_auth_state()
require_auth()
load_custom_css()
render_navbar()

# ==================== SUSTAINABILITY PAGE ====================

# Header
st.markdown("""
<h1 style='text-align: center; color: #2e7d32; font-size: 48px;'>
    🌍 Sustainability & Social Impact
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; color: #558b2f; font-size: 20px; margin-bottom: 40px;'>
    Empowering Farmers, Protecting Crops, Sustaining Our Planet
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# Impact Metrics
st.markdown("<h2 style='text-align: center; color: #2e7d32; margin-bottom: 30px;'>📊 Our Impact</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); 
                border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h2 style='color: #2e7d32; font-size: 48px; margin: 0;'>85%</h2>
        <p style='color: #558b2f; font-size: 16px; margin: 10px 0;'>Crop Loss Reduction</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); 
                border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h2 style='color: #1565c0; font-size: 48px; margin: 0;'>10K+</h2>
        <p style='color: #1976d2; font-size: 16px; margin: 10px 0;'>Farmers Supported</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%); 
                border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h2 style='color: #e65100; font-size: 48px; margin: 0;'>50K+</h2>
        <p style='color: #ef6c00; font-size: 16px; margin: 10px 0;'>Acres Protected</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); 
                border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h2 style='color: #7b1fa2; font-size: 48px; margin: 0;'>₹2Cr+</h2>
        <p style='color: #8e24aa; font-size: 16px; margin: 10px 0;'>Income Saved</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Key Benefits
st.markdown("<h2 style='color: #2e7d32; margin-bottom: 30px;'>🎯 Key Benefits</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style='padding: 25px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;'>
        <h3 style='color: #2e7d32; margin-bottom: 15px;'>🌾 For Farmers</h3>
        <ul style='color: #1b5e20; font-size: 16px; line-height: 2;'>
            <li>Early disease detection saves crops</li>
            <li>Reduced pesticide usage (30-40%)</li>
            <li>Lower treatment costs</li>
            <li>Increased crop yield</li>
            <li>Better income stability</li>
            <li>Access to expert knowledge</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='padding: 25px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h3 style='color: #2e7d32; margin-bottom: 15px;'>🌍 For Environment</h3>
        <ul style='color: #1b5e20; font-size: 16px; line-height: 2;'>
            <li>Reduced chemical pesticide use</li>
            <li>Lower carbon footprint</li>
            <li>Soil health preservation</li>
            <li>Water conservation</li>
            <li>Biodiversity protection</li>
            <li>Sustainable farming practices</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 25px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px;'>
        <h3 style='color: #2e7d32; margin-bottom: 15px;'>👥 For Society</h3>
        <ul style='color: #1b5e20; font-size: 16px; line-height: 2;'>
            <li>Food security enhancement</li>
            <li>Rural employment support</li>
            <li>Knowledge democratization</li>
            <li>Technology accessibility</li>
            <li>Community empowerment</li>
            <li>Economic development</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='padding: 25px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h3 style='color: #2e7d32; margin-bottom: 15px;'>🔬 For Agriculture</h3>
        <ul style='color: #1b5e20; font-size: 16px; line-height: 2;'>
            <li>Precision agriculture adoption</li>
            <li>Data-driven decision making</li>
            <li>Disease pattern tracking</li>
            <li>Research advancement</li>
            <li>Best practice sharing</li>
            <li>Innovation acceleration</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# UN SDG Alignment
st.markdown("<h2 style='text-align: center; color: #2e7d32; margin-bottom: 30px;'>🎯 UN Sustainable Development Goals Alignment</h2>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; color: #558b2f; font-size: 18px; margin-bottom: 30px;'>
    AgroDetect AI contributes to multiple UN SDGs
</p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='padding: 25px; background-color: #e8f5e9; border-radius: 15px; 
                border-left: 5px solid #4CAF50; margin-bottom: 20px;'>
        <h3 style='color: #2e7d32; margin-bottom: 10px;'>🍽️ SDG 2: Zero Hunger</h3>
        <p style='color: #1b5e20; line-height: 1.8;'>
            Reducing crop losses ensures food security and helps end hunger by protecting agricultural productivity.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='padding: 25px; background-color: #e3f2fd; border-radius: 15px; 
                border-left: 5px solid #2196F3;'>
        <h3 style='color: #1565c0; margin-bottom: 10px;'>🌱 SDG 12: Responsible Consumption</h3>
        <p style='color: #0d47a1; line-height: 1.8;'>
            Promoting sustainable farming practices and reducing chemical pesticide usage.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 25px; background-color: #fff3e0; border-radius: 15px; 
                border-left: 5px solid #ff9800; margin-bottom: 20px;'>
        <h3 style='color: #e65100; margin-bottom: 10px;'>💰 SDG 1: No Poverty</h3>
        <p style='color: #e65100; line-height: 1.8;'>
            Supporting small farmers' income by preventing crop losses and reducing treatment costs.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='padding: 25px; background-color: #f3e5f5; border-radius: 15px; 
                border-left: 5px solid #9c27b0;'>
        <h3 style='color: #7b1fa2; margin-bottom: 10px;'>🌍 SDG 13: Climate Action</h3>
        <p style='color: #6a1b9a; line-height: 1.8;'>
            Reducing carbon footprint through precision agriculture and optimized resource use.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='padding: 25px; background-color: #fce4ec; border-radius: 15px; 
                border-left: 5px solid #e91e63; margin-bottom: 20px;'>
        <h3 style='color: #c2185b; margin-bottom: 10px;'>🎓 SDG 4: Quality Education</h3>
        <p style='color: #ad1457; line-height: 1.8;'>
            Democratizing agricultural knowledge through AI-powered education and guidance.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='padding: 25px; background-color: #e0f2f1; border-radius: 15px; 
                border-left: 5px solid #009688;'>
        <h3 style='color: #00695c; margin-bottom: 10px;'>🤝 SDG 17: Partnerships</h3>
        <p style='color: #004d40; line-height: 1.8;'>
            Fostering collaboration between farmers, experts, and technology providers.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Success Stories
st.markdown("<h2 style='color: #2e7d32; margin-bottom: 30px;'>🌟 Success Stories</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style='padding: 25px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h4 style='color: #2e7d32; margin-bottom: 15px;'>📍 Maharashtra Farmer</h4>
        <p style='color: #1b5e20; font-size: 16px; line-height: 1.8; font-style: italic;'>
            "AgroDetect AI helped me detect late blight early. I saved 80% of my tomato crop 
            and increased my income by ₹50,000 this season."
        </p>
        <p style='color: #558b2f; margin-top: 15px;'>- Ramesh Kumar, Tomato Farmer</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='padding: 25px; background-color: white; border-radius: 15px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h4 style='color: #2e7d32; margin-bottom: 15px;'>📍 Karnataka Agricultural Expert</h4>
        <p style='color: #1b5e20; font-size: 16px; line-height: 1.8; font-style: italic;'>
            "This tool has revolutionized how we provide agricultural extension services. 
            We can now reach and help thousands of farmers remotely."
        </p>
        <p style='color: #558b2f; margin-top: 15px;'>- Dr. Priya Sharma, Agricultural Officer</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div style='text-align: center; padding: 50px 20px; background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); 
            border-radius: 20px;'>
    <h2 style='color: #2e7d32; font-size: 36px; margin-bottom: 20px;'>
        Join Us in Building a Sustainable Future
    </h2>
    <p style='color: #1b5e20; font-size: 20px; margin-bottom: 30px;'>
        Together, we can protect crops, empower farmers, and sustain our planet
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Action buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("📤 Start Analyzing", use_container_width=True):
        st.switch_page("pages/3_Upload.py")

with col2:
    if st.button("🤖 AI Assistant", use_container_width=True):
        st.switch_page("pages/5_AI_Assistant.py")

with col3:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("pages/1_Home.py")
