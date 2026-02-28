# AgroDetect AI - Streamlit Application

A modern, interactive Streamlit web application for AI-powered plant disease detection.

## 🌱 Project Overview

AgroDetect AI is a Streamlit-based web application that showcases an AI system for detecting plant diseases from leaf images using transfer learning and MobileNetV2 CNN architecture.

## 📁 Project Structure

```
AgroDetect-AI/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README_STREAMLIT.md    # This file
│
├── templates/             # Original HTML templates (reference)
└── static/                # Original CSS and images (reference)
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install streamlit pillow
```

### Step 2: Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

## 🎨 Features

### ✅ Implemented Features:
- **Multi-page Navigation**: Home, About, Detect Disease, Contact
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Image Upload**: Drag & drop or browse to upload plant leaf images
- **Image Preview**: View uploaded images before analysis
- **Mock Disease Detection**: Simulated AI prediction results
- **Interactive UI**: Smooth transitions and user-friendly interface
- **Custom Styling**: Agriculture-themed green color palette
- **Sidebar Navigation**: Easy page switching with quick stats

### 📄 Pages:

1. **Home Page**
   - Hero section with call-to-action
   - Feature cards (Instant Detection, High Accuracy, Farmer-Friendly)
   - Statistics display (38+ diseases, 10+ crops, 95% accuracy)
   - Quick navigation buttons

2. **About Page**
   - Project overview
   - Technology stack showcase
   - Step-by-step "How It Works" section
   - Use cases for different user types

3. **Detect Disease Page**
   - Image upload functionality
   - Image preview with details
   - Mock AI analysis with loading animation
   - Results display with confidence score
   - Recommendations section
   - Action buttons (Upload Another, Go Home)

4. **Contact Page**
   - Contact form with validation
   - Contact information display
   - Form submission handling

## 🎯 Usage

### Running the App:
```bash
streamlit run app.py
```

### Uploading Images:
1. Navigate to "Detect Disease" page
2. Click "Browse files" or drag & drop an image
3. Supported formats: JPG, JPEG, PNG
4. Click "Analyze Leaf" to see mock results

### Navigation:
- Use the sidebar buttons to switch between pages
- Click action buttons on pages for quick navigation
- View quick stats in the sidebar

## 🛠️ Technology Stack

- **Streamlit**: Web application framework
- **Python**: Backend programming
- **Pillow (PIL)**: Image processing
- **HTML/CSS**: Custom styling (embedded in Streamlit)

## 🎨 Design Features

### Color Palette:
- Primary Green: `#4a7c2c`
- Dark Green: `#2d5016`
- Light Green: `#6ba83e`
- Background Light: `#f5f9f3`

### UI Components:
- Custom CSS styling
- Gradient backgrounds
- Card-based layouts
- Progress bars
- Form validation
- Responsive columns

## 📊 Current Status

**Stage: Interactive Prototype (30% Complete)**

### ✅ Completed:
- Full Streamlit UI implementation
- Multi-page navigation
- Image upload and preview
- Mock prediction results
- Responsive design
- Custom styling

### ❌ Not Implemented:
- Actual AI/ML model integration
- Real disease detection
- Database storage
- User authentication
- Result history

## 🔧 Customization

### Changing Colors:
Edit the CSS variables in `app.py`:
```python
:root {
    --primary-green: #4a7c2c;
    --dark-green: #2d5016;
    --light-green: #6ba83e;
}
```

### Adding Real AI Model:
Replace the mock prediction in `detect_disease_page()` function:
```python
# Replace this mock code:
st.session_state.prediction_result = {
    'disease': 'Tomato Late Blight',
    'confidence': 96,
    ...
}

# With actual model prediction:
prediction = model.predict(image)
st.session_state.prediction_result = prediction
```

### Modifying Pages:
Edit the respective page functions in `app.py`:
- `home_page()`
- `about_page()`
- `detect_disease_page()`
- `contact_page()`

## 📱 Responsive Design

The application automatically adapts to different screen sizes:
- **Desktop**: Full multi-column layout
- **Tablet**: Adjusted column widths
- **Mobile**: Single column stacked layout

## 🚀 Deployment Options

### Streamlit Cloud (Free):
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy with one click

### Heroku:
```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

### Docker:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 🎓 Use Cases

- **Hackathon Demo**: Interactive prototype for presentations
- **Portfolio Project**: Showcase Streamlit development skills
- **Learning Tool**: Study Streamlit and web app development
- **Prototype**: Foundation for adding real AI functionality

## 📝 Next Steps to Production

1. **Integrate ML Model**:
   - Train or load pre-trained plant disease model
   - Add TensorFlow/PyTorch dependencies
   - Implement actual prediction logic

2. **Add Database**:
   - Store user uploads and results
   - Track prediction history
   - User authentication

3. **Enhance Features**:
   - Multiple image upload
   - Batch processing
   - Export results as PDF
   - Disease information database

4. **Optimize Performance**:
   - Image caching
   - Model optimization
   - Lazy loading

## 🐛 Troubleshooting

### Port Already in Use:
```bash
streamlit run app.py --server.port 8502
```

### Module Not Found:
```bash
pip install -r requirements.txt --upgrade
```

### Image Upload Issues:
- Check file size (Streamlit default limit: 200MB)
- Verify file format (JPG, PNG only)
- Ensure proper file permissions

## 📄 License

This project is open-source and available for educational and commercial use.

## 🤝 Contributing

Feel free to fork, modify, and enhance this project!

---

**AgroDetect AI** - Empowering Smart Agriculture with Streamlit 🌱
