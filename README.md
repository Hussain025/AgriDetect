# AgroDetect AI - Plant Disease Classification Engine

A modern, responsive front-end website for an AI-powered plant disease detection system.

## 🌱 Project Overview

AgroDetect AI is a hackathon-ready front-end website that showcases an AI system for detecting plant diseases from leaf images. The project uses transfer learning and MobileNetV2 CNN architecture.

## 📁 Project Structure

```
AgroDetect-AI/
│
├── templates/
│   ├── home.html          # Landing page with hero, features, stats
│   ├── about.html         # Project overview, tech stack, how it works
│   ├── upload.html        # Disease detection page with image upload
│   ├── result.html        # Results display with predictions
│   └── contact.html       # Contact form
│
├── static/
│   ├── style.css          # Complete stylesheet for all pages
│   └── images/            # Folder for images (placeholders included)
│
└── README.md              # This file
```

## 🎨 Features

- **Fully Responsive Design**: Works seamlessly on mobile, tablet, and desktop
- **Modern UI/UX**: Clean, professional design with smooth animations
- **Agriculture Theme**: Green color palette with earthy tones
- **Interactive Elements**: Drag & drop upload, image preview, hover effects
- **No Backend Required**: Pure HTML, CSS, and minimal JavaScript

## 🚀 Getting Started

1. **Open the website**: Simply open `templates/home.html` in your web browser
2. **Navigate**: Use the navigation bar to explore different pages
3. **Test Upload**: Go to "Detect Disease" page to test the image upload functionality

## 🎯 Pages Overview

### Home Page (home.html)
- Hero section with call-to-action buttons
- Features showcase (Instant Detection, High Accuracy, Farmer-Friendly)
- Statistics section (38+ diseases, 10+ crops, 95% accuracy)
- Call-to-action banner

### About Page (about.html)
- Project overview and mission
- Technology stack display
- Step-by-step "How It Works" section
- Use cases for different user types

### Upload Page (upload.html)
- Drag & drop image upload
- Image preview before analysis
- Supported crops information
- Interactive JavaScript functionality

### Result Page (result.html)
- Uploaded image display
- Disease prediction with confidence score
- Status badge (Healthy/Diseased)
- Recommendations and action buttons

### Contact Page (contact.html)
- Contact form with validation
- Contact information display
- Form submission handling (front-end only)

## 🛠️ Technology Stack

- **HTML5**: Semantic markup
- **CSS3**: Modern styling with Flexbox and Grid
- **JavaScript**: Minimal vanilla JS for interactivity
- **Google Fonts**: Inter font family

## 🎨 Design Features

- **Color Palette**:
  - Primary Green: #4a7c2c
  - Dark Green: #2d5016
  - Light Green: #6ba83e
  - Background: #f5f9f3
  
- **Typography**: Inter font family (clean and professional)
- **Animations**: Fade-in effects, hover transitions
- **Icons**: Emoji-based icons for simplicity

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: 480px - 767px
- **Small Mobile**: Below 480px

## 🔧 Customization

### Changing Colors
Edit the CSS variables in `static/style.css`:
```css
:root {
    --primary-green: #4a7c2c;
    --dark-green: #2d5016;
    /* ... other colors */
}
```

### Adding Images
Place your images in `static/images/` and update the image paths in HTML files.

### Modifying Content
Edit the HTML files in the `templates/` folder to change text, add sections, or modify layout.

## 🌟 Key Features

✅ No backend or framework dependencies  
✅ Pure HTML, CSS, and JavaScript  
✅ Fully responsive and mobile-friendly  
✅ Modern, clean design  
✅ Easy to customize  
✅ Hackathon-ready  
✅ Professional appearance  

## 📝 Notes

- This is a **front-end only** project (no backend functionality)
- Image upload and analysis are simulated (no actual AI processing)
- Form submissions show alerts (no data is sent to a server)
- The result page shows placeholder data for demonstration

## 🎓 Use Cases

- **Hackathon Projects**: Ready-to-present front-end
- **Portfolio**: Showcase web development skills
- **Prototyping**: Quick mockup for AI agriculture projects
- **Learning**: Study modern HTML/CSS/JS practices

## 📄 License

This project is open-source and available for educational and commercial use.

## 🤝 Contributing

Feel free to fork, modify, and enhance this project for your needs!

---

**AgroDetect AI** - Empowering Smart Agriculture 🌱
