"""
Reusable Card Components
"""

import streamlit as st

def feature_card(icon, title, description):
    """Render a feature card with glassmorphic styling"""
    st.markdown(f"""
    <div class='feature-card' style='padding: 35px;'>
        <h2 style='text-align: center; font-size: 52px; animation: pulse 2s ease-in-out infinite;'>{icon}</h2>
        <h4 style='text-align: center; color: #1b5e20; margin: 18px 0; font-weight: 600; font-size: 20px;'>{title}</h4>
        <p style='text-align: center; color: #2e7d32; line-height: 1.7; font-size: 16px;'>{description}</p>
    </div>
    """, unsafe_allow_html=True)

def result_card(title, content, icon=""):
    """Render a result card"""
    st.markdown(f"""
    <div class='result-card'>
        <h4 style='color: #2e7d32; margin-bottom: 10px;'>{icon} {title}</h4>
        <h2 style='color: #1b5e20; margin: 5px 0;'>{content}</h2>
    </div>
    """, unsafe_allow_html=True)

def info_card(title, content, card_type="info"):
    """Render an info/warning card"""
    card_class = "info-box" if card_type == "info" else "warning-box"
    st.markdown(f"""
    <div class='{card_class}'>
        <h4 style='color: #2e7d32; margin-bottom: 10px;'>{title}</h4>
        <p style='color: #1b5e20; line-height: 1.8;'>{content}</p>
    </div>
    """, unsafe_allow_html=True)

def tech_card(title, items):
    """Render a technology stack card"""
    items_html = "".join([f"<li>{item}</li>" for item in items])
    st.markdown(f"""
    <div class='tech-card'>
        <h4 style='color: #2e7d32; margin-bottom: 15px;'>{title}</h4>
        <ul style='font-size: 16px; line-height: 1.8; color: #1b5e20;'>
            {items_html}
        </ul>
    </div>
    """, unsafe_allow_html=True)

def step_card(step_num, icon, title, description):
    """Render a step card for how it works section with glassmorphic styling"""
    st.markdown(f"""
    <div class='tech-card' style='text-align: center; padding: 30px; height: 240px;'>
        <h2 style='font-size: 52px; animation: pulse 2s ease-in-out infinite;'>{icon}</h2>
        <h4 style='color: #1b5e20; margin: 12px 0; font-weight: 600;'>Step {step_num}</h4>
        <p style='color: #2e7d32; line-height: 1.7; font-size: 15px;'>{description}</p>
    </div>
    """, unsafe_allow_html=True)
