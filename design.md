# Plant Disease Classification - Design Document

## System Architecture

### High-Level Architecture
```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   User      │─────▶│  Streamlit   │─────▶│   Model     │
│  Browser    │◀─────│  Web App     │◀─────│  (PyTorch)  │
└─────────────┘      └──────────────┘      └─────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │  Hugging     │
                     │  Face Hub    │
                     └──────────────┘
```

### Component Architecture

#### 1. Frontend Layer (Streamlit UI)
- User interface components
- Image upload widget
- Results display
- Sidebar information
- Error handling UI

#### 2. Application Layer
- Image preprocessing
- Model inference orchestration
- Result formatting
- State management

#### 3. Model Layer
- Pre-trained Vision Transformer
- Image processor
- Classification logic
- Confidence scoring

#### 4. External Services
- Hugging Face Hub (model hosting)
- Streamlit Cloud (deployment)

## Detailed Component Design

### 1. Web Application (Streamlit)

#### 1.1 Main Application Flow
```python
Initialize App
    ├── Load Configuration
    ├── Set Page Config
    └── Display Title/Description
    
Load Model (Cached)
    ├── Check Model Source (Hub/Local)
    ├── Load Image Processor
    ├── Load Classification Model
    └── Handle Loading Errors
    
User Interaction Loop
    ├── Display Upload Widget
    ├── Accept Image Upload
    ├── Validate Image
    ├── Preprocess Image
    ├── Run Inference
    ├── Display Results
    └── Show Recommendations
```

#### 1.2 Key Functions

**load_model()**
- Purpose: Load and cache the ML model
- Input: Model path or Hugging Face model ID
- Output: Processor and model objects
- Caching: @st.cache_resource decorator
- Error handling: Try-catch with user feedback

**preprocess_image(image)**
- Purpose: Prepare image for model input
- Input: PIL Image object
- Output: Tensor ready for inference
- Operations: Resize, normalize, convert to tensor

**predict(image, model, processor)**
- Purpose: Run inference on image
- Input: Image, model, processor
- Output: Predictions with confidence scores
- Processing: Forward pass, softmax, top-k results

**display_results(predictions)**
- Purpose: Show classification results
- Input: Prediction dictionary
- Output: Formatted UI display
- Features: Color coding, confidence bars, descriptions

### 2. Machine Learning Model

#### 2.1 Model Architecture
- Base: Vision Transformer (ViT) or ConvNeXt
- Input: 224x224 RGB images
- Output: 8-class probability distribution
- Framework: PyTorch + Hugging Face Transformers

#### 2.2 Model Specifications
```
Input Shape: (3, 224, 224)
Architecture: ViT-Base or similar
Parameters: ~86M (ViT-Base)
Output Classes: 8
Activation: Softmax
Loss Function: Cross-Entropy
Optimizer: AdamW
```

#### 2.3 Class Labels
```python
DISEASE_CLASSES = {
    0: "Tomato_Bacterial_spot",
    1: "Tomato_Early_blight",
    2: "Tomato_Late_blight",
    3: "Tomato_Leaf_Mold",
    4: "Tomato_Septoria_leaf_spot",
    5: "Tomato_Yellow_Leaf_Curl_Virus",
    6: "Tomato_mosaic_virus",
    7: "Tomato_healthy"
}
```

### 3. Data Pipeline

#### 3.1 Training Pipeline
```
Raw Images
    ├── Data Loading
    ├── Data Augmentation
    │   ├── Random Rotation
    │   ├── Random Flip
    │   ├── Color Jitter
    │   └── Random Crop
    ├── Normalization
    ├── Train/Val/Test Split
    └── DataLoader Creation
```

#### 3.2 Inference Pipeline
```
User Image
    ├── Format Validation
    ├── Load with PIL
    ├── Resize to 224x224
    ├── Normalize (ImageNet stats)
    ├── Convert to Tensor
    ├── Add Batch Dimension
    └── Model Input
```

### 4. User Interface Design

#### 4.1 Layout Structure
```
┌─────────────────────────────────────────┐
│  Header: Title + Description            │
├─────────────────────────────────────────┤
│  Sidebar          │  Main Content       │
│  ├── Model Info   │  ├── Upload Widget  │
│  ├── Instructions │  ├── Image Preview  │
│  ├── About        │  ├── Predict Button │
│  └── Stats        │  └── Results Panel  │
└─────────────────────────────────────────┘
```

#### 4.2 UI Components

**Header Section**
- Application title with icon
- Brief description
- Model status indicator

**Sidebar**
- Model information
- Usage instructions
- Disease categories list
- About section
- Performance metrics

**Main Content Area**
- File uploader widget
- Image preview (uploaded image)
- Predict button
- Results display with:
  - Predicted disease name
  - Confidence percentage
  - Confidence bar chart
  - Disease description
  - Treatment recommendations

**Footer**
- Credits
- Links to documentation
- Version information

#### 4.3 Color Scheme
```python
COLORS = {
    'primary': '#2E7D32',      # Green
    'secondary': '#FFA726',    # Orange
    'success': '#66BB6A',      # Light Green
    'warning': '#FFA726',      # Orange
    'danger': '#EF5350',       # Red
    'info': '#42A5F5',         # Blue
    'background': '#FFFFFF',   # White
    'text': '#212121'          # Dark Gray
}
```

### 5. Model Training Design

#### 5.1 Training Configuration
```python
TRAINING_CONFIG = {
    'batch_size': 32,
    'learning_rate': 2e-5,
    'num_epochs': 10,
    'weight_decay': 0.01,
    'warmup_steps': 500,
    'eval_strategy': 'epoch',
    'save_strategy': 'epoch',
    'load_best_model': True,
    'metric_for_best_model': 'accuracy'
}
```

#### 5.2 Data Augmentation
```python
AUGMENTATION = {
    'train': [
        'RandomResizedCrop(224)',
        'RandomHorizontalFlip()',
        'RandomRotation(15)',
        'ColorJitter(0.2, 0.2, 0.2)',
        'Normalize(ImageNet)'
    ],
    'val': [
        'Resize(256)',
        'CenterCrop(224)',
        'Normalize(ImageNet)'
    ]
}
```

### 6. Deployment Architecture

#### 6.1 Deployment Options

**Option 1: Streamlit Cloud**
- Pros: Free, easy deployment, automatic updates
- Cons: Limited resources, public only
- Best for: MVP and demos

**Option 2: Hugging Face Spaces**
- Pros: ML-optimized, model integration, free tier
- Cons: Learning curve, resource limits
- Best for: ML applications

**Option 3: Docker Container**
- Pros: Portable, scalable, full control
- Cons: Requires infrastructure, cost
- Best for: Production deployment

#### 6.2 Deployment Flow
```
Local Development
    ├── Code in Git Repository
    ├── Push to GitHub
    └── Trigger Deployment
    
Cloud Platform
    ├── Pull Code
    ├── Install Dependencies
    ├── Download Model
    ├── Start Application
    └── Expose Public URL
```

### 7. File Structure

```
project/
├── .streamlit/
│   └── config.toml              # Streamlit configuration
├── essential_files/
│   ├── streamlit_app.py         # Main app (Hub model)
│   ├── streamlit_app_local.py   # Local model version
│   ├── run_streamlit.bat        # Windows launcher
│   ├── scripts/
│   │   ├── train_model.py       # Training script
│   │   └── evaluate_model.py    # Evaluation script
│   ├── notebooks/
│   │   └── exploration.ipynb    # Data exploration
│   └── config/
│       └── model_config.json    # Model configuration
├── datasets/
│   └── [training data]          # Image datasets
├── archives/
│   └── [dataset archives]       # Compressed datasets
├── requirements.txt             # Python dependencies
├── requirements.md              # Project requirements
├── design.md                    # This document
├── README.md                    # Project documentation
└── .gitignore                   # Git ignore rules
```

### 8. API Design

#### 8.1 Internal Functions

**Model Loading API**
```python
def load_model(model_path: str) -> Tuple[Processor, Model]:
    """Load model and processor from path or Hub"""
    
def validate_model(model: Model) -> bool:
    """Verify model is loaded correctly"""
```

**Image Processing API**
```python
def load_image(file: UploadedFile) -> Image:
    """Load image from uploaded file"""
    
def preprocess_image(image: Image, processor: Processor) -> Tensor:
    """Preprocess image for model input"""
    
def validate_image(image: Image) -> bool:
    """Check image format and size"""
```

**Inference API**
```python
def predict(image: Tensor, model: Model) -> Dict:
    """Run inference and return predictions"""
    
def get_top_predictions(logits: Tensor, k: int = 3) -> List[Dict]:
    """Get top-k predictions with confidence"""
```

**Display API**
```python
def display_results(predictions: Dict) -> None:
    """Render prediction results in UI"""
    
def display_confidence_chart(predictions: Dict) -> None:
    """Show confidence scores as chart"""
```

### 9. Error Handling Strategy

#### 9.1 Error Categories

**Model Loading Errors**
- Network issues (Hub download)
- Missing model files (local)
- Incompatible model format
- Insufficient memory

**Image Processing Errors**
- Invalid file format
- Corrupted image
- Unsupported dimensions
- File size too large

**Inference Errors**
- Model inference failure
- Out of memory
- Invalid input tensor
- Unexpected output shape

#### 9.2 Error Handling Approach
```python
try:
    # Operation
except SpecificError as e:
    # Log error
    # Show user-friendly message
    # Provide recovery options
    # Graceful degradation
```

### 10. Performance Optimization

#### 10.1 Caching Strategy
- Model caching: @st.cache_resource
- Data caching: @st.cache_data
- Session state for user data

#### 10.2 Optimization Techniques
- Lazy model loading
- Image preprocessing optimization
- Batch inference (future)
- Model quantization (future)
- ONNX conversion (future)

### 11. Security Considerations

#### 11.1 Input Validation
- File type whitelist (jpg, png, jpeg)
- File size limits (< 10MB)
- Image dimension validation
- Malware scanning (future)

#### 11.2 Privacy
- No image storage
- No user tracking
- No personal data collection
- Stateless application

### 12. Testing Strategy

#### 12.1 Unit Tests
- Image preprocessing functions
- Model loading functions
- Prediction functions
- Utility functions

#### 12.2 Integration Tests
- End-to-end workflow
- Model inference pipeline
- UI component integration

#### 12.3 User Acceptance Testing
- Real-world image testing
- Cross-browser testing
- Mobile device testing
- Performance testing

### 13. Monitoring and Logging

#### 13.1 Metrics to Track
- Inference time
- Model accuracy
- User engagement
- Error rates
- Resource usage

#### 13.2 Logging Strategy
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### 14. Future Enhancements

#### 14.1 Technical Improvements
- Model ensemble for better accuracy
- Real-time inference optimization
- Progressive web app (PWA)
- Offline mode support
- API endpoint for integration

#### 14.2 Feature Additions
- Multi-plant support
- Disease severity assessment
- Treatment recommendations database
- Historical analysis
- Expert consultation integration

## Design Decisions

### Decision 1: Streamlit Framework
- Rationale: Rapid development, Python-native, ML-friendly
- Alternatives: Flask, FastAPI + React
- Trade-offs: Less customization, but faster development

### Decision 2: Vision Transformer Model
- Rationale: State-of-art accuracy, transfer learning
- Alternatives: ResNet, EfficientNet
- Trade-offs: Larger model size, but better performance

### Decision 3: Hugging Face Hub
- Rationale: Easy model sharing, version control
- Alternatives: Local storage, custom server
- Trade-offs: Requires internet, but easier deployment

### Decision 4: No Database
- Rationale: Simplicity, privacy, stateless
- Alternatives: SQLite, PostgreSQL
- Trade-offs: No history, but simpler architecture

## Conclusion

This design provides a scalable, maintainable architecture for the plant disease classification system. The modular approach allows for easy updates and feature additions while maintaining code quality and user experience.
