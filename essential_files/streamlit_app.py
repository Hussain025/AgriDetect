"""
Plant Disease Classification - Streamlit Demo
Step 5: Interactive Web Application
"""

import streamlit as st
from PIL import Image
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Plant Disease Classifier",
    page_icon="🌱",
    layout="wide"
)

# Title and description
st.title("🌱 Plant Disease Classification")
st.markdown("""
Upload an image of a plant leaf to detect diseases using AI.
This model was trained on 1,600 images across 8 different plant disease categories.
""")

# Model loading with caching
@st.cache_resource
def load_model():
    """Load the trained model and processor from Hugging Face Hub"""
    model_name = "Warrior025/plant-disease-model"
    
    try:
        processor = AutoImageProcessor.from_pretrained(model_name)
        model = AutoModelForImageClassification.from_pretrained(model_name)
        return processor, model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.info("Make sure you have internet connection to download the model from Hugging Face Hub.")
        return None, None

# Load model
with st.spinner("Loading model..."):
    processor, model = load_model()

if processor is None or model is None:
    st.stop()

st.success("✅ Model loaded successfully!")

# Sidebar with info
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    **Model**: ResNet-50 (Fine-tuned)
    
    **Dataset**: 
    - 1,600 images
    - 8 disease classes
    - 224×224 resolution
    
    **Classes**:
    1. Apple Scab
    2. Corn Common Rust
    3. Grape Black Rot
    4. Pepper Bacterial Spot
    5. Potato Late Blight
    6. Strawberry Leaf Scorch
    7. Tomato Early Blight
    8. Tomato Healthy
    """)
    
    st.header("📊 Model Info")
    st.markdown("""
    - **Architecture**: ResNet-50
    - **Training**: Transfer Learning
    - **Framework**: Hugging Face Transformers
    """)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📤 Upload Image")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a plant leaf image...",
        type=["jpg", "jpeg", "png"],
        help="Upload a clear image of a plant leaf"
    )
    
    # Info about supported formats
    st.markdown("---")
    st.info("💡 Supported formats: JPG, JPEG, PNG")

with col2:
    st.header("🔍 Prediction Results")
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        # Predict button
        if st.button("🔬 Analyze Image", type="primary"):
            with st.spinner("Analyzing..."):
                # Preprocess image
                inputs = processor(images=image, return_tensors="pt")
                
                # Make prediction
                with torch.no_grad():
                    outputs = model(**inputs)
                    logits = outputs.logits
                    probabilities = torch.nn.functional.softmax(logits, dim=-1)
                
                # Get prediction
                predicted_class_idx = logits.argmax(-1).item()
                confidence = probabilities[0][predicted_class_idx].item()
                predicted_label = model.config.id2label[predicted_class_idx]
                
                # Display results
                st.success("✅ Analysis Complete!")
                
                # Main prediction
                st.markdown("### 🎯 Detected Disease")
                st.markdown(f"## **{predicted_label}**")
                st.markdown(f"**Confidence**: {confidence*100:.2f}%")
                
                # Confidence bar
                st.progress(confidence)
                
                # All predictions
                st.markdown("---")
                st.markdown("### 📊 All Predictions")
                
                # Get all probabilities
                all_probs = probabilities[0].numpy()
                sorted_indices = np.argsort(all_probs)[::-1]
                
                for idx in sorted_indices:
                    label = model.config.id2label[idx]
                    prob = all_probs[idx]
                    
                    # Color code based on probability
                    if prob > 0.5:
                        color = "🟢"
                    elif prob > 0.2:
                        color = "🟡"
                    else:
                        color = "⚪"
                    
                    st.markdown(f"{color} **{label}**: {prob*100:.2f}%")
                    st.progress(float(prob))
                
                # Recommendations
                st.markdown("---")
                st.markdown("### 💡 Recommendations")
                
                if "healthy" in predicted_label.lower():
                    st.info("✅ The plant appears healthy! Continue regular care and monitoring.")
                else:
                    st.warning(f"""
                    ⚠️ Disease detected: **{predicted_label}**
                    
                    **Recommended Actions**:
                    - Isolate affected plants
                    - Remove infected leaves
                    - Apply appropriate treatment
                    - Consult agricultural expert for severe cases
                    - Monitor other plants for symptoms
                    """)
    else:
        st.info("👆 Upload an image to get started")
        
        # Display placeholder
        st.markdown("""
        ### How to use:
        1. Upload a clear image of a plant leaf
        2. Click "Analyze Image"
        3. View the prediction and confidence score
        4. Check recommendations
        
        **Tips for best results**:
        - Use clear, well-lit images
        - Focus on the leaf showing symptoms
        - Avoid blurry or dark images
        - Ensure the leaf fills most of the frame
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🌱 Plant Disease Classification System | Built with Streamlit & Hugging Face Transformers</p>
    <p>Model trained on 1,600 images | 8 disease categories | ResNet-50 architecture</p>
</div>
""", unsafe_allow_html=True)
