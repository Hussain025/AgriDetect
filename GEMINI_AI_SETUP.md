# Gemini AI Integration Setup Guide

## Overview
AgroDetect AI now uses **Google Gemini AI** for real-time multilingual support and intelligent responses.

## Features Implemented

### 1. Real-Time Multilingual AI Chat
- Powered by Gemini Pro model
- Responds in 6 languages: English, Hindi, Tamil, Telugu, Spanish, French
- Context-aware conversations
- Agriculture-focused responses

### 2. Real-Time Voice Assistant
- Speech-to-Text (STT) in multiple languages
- Gemini AI processing
- Text-to-Speech (TTS) responses
- Hands-free operation for farmers

### 3. AI-Generated Disease Recommendations
- Dynamic treatment plans
- Prevention strategies
- Organic and chemical solutions
- Adapts to selected language

### 4. Explainable AI (XAI)
- AI reasoning explanations
- Visual focus areas
- Confidence factors
- Multilingual explanations

## Setup Instructions

### Step 1: Get Gemini API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### Step 2: Configure Secrets

1. Open `.streamlit/secrets.toml`
2. Replace `your-gemini-api-key-here` with your actual API key:

```toml
GEMINI_API_KEY = "AIzaSy..."
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- `google-generativeai` - Gemini AI SDK
- `SpeechRecognition` - Speech-to-text
- `gTTS` - Text-to-speech
- `pydub` - Audio processing

### Step 4: Run the Application

```bash
streamlit run app.py
```

## How It Works

### Chat Assistant Flow
1. User types question in any language
2. Gemini AI receives question with language context
3. AI generates response in selected language
4. Response displayed in chat interface

### Voice Assistant Flow
1. User speaks question (or types for demo)
2. Speech converted to text (STT)
3. Text sent to Gemini AI
4. AI generates response in selected language
5. Response converted to speech (TTS)
6. Audio played to user

### Disease Recommendations Flow
1. Disease detected from image
2. User selects language
3. Gemini AI generates comprehensive recommendations
4. Recommendations displayed in selected language
5. Optional: Convert to speech for voice output

## Language Support

| Language | Chat | Voice | TTS |
|----------|------|-------|-----|
| English  | ✅   | ✅    | ✅  |
| Hindi    | ✅   | ✅    | ✅  |
| Tamil    | ✅   | ✅    | ✅  |
| Telugu   | ✅   | ✅    | ✅  |
| Spanish  | ✅   | ✅    | ✅  |
| French   | ✅   | ✅    | ✅  |

## API Usage & Costs

### Gemini API (Free Tier)
- 60 requests per minute
- 1,500 requests per day
- Free for development and testing

### Speech Recognition (Google)
- Free tier available
- Internet connection required

### Text-to-Speech (gTTS)
- Free Google TTS service
- No API key required

## Troubleshooting

### "API key not found" Error
- Ensure `.streamlit/secrets.toml` exists
- Check API key is correctly formatted
- Restart Streamlit after adding key

### "Speech recognition failed" Error
- Check microphone permissions
- Ensure internet connection
- Try typing question manually

### "Voice generation failed" Error
- Check internet connection
- Verify gTTS is installed
- Try shorter text responses

## Security Notes

- Never commit `.streamlit/secrets.toml` to version control
- Add to `.gitignore`:
  ```
  .streamlit/secrets.toml
  ```
- Keep API keys private
- Rotate keys if exposed

## Performance Optimization

### Caching
- UI translations cached in session_state
- AI recommendations cached per language
- Reduces API calls and improves speed

### Response Time
- Typical Gemini response: 1-3 seconds
- Voice generation: 1-2 seconds
- Total voice interaction: 3-5 seconds

## Future Enhancements

- [ ] Real-time audio recording from microphone
- [ ] Streaming responses for faster feedback
- [ ] Voice activity detection
- [ ] Offline mode with cached responses
- [ ] Custom voice models
- [ ] Dialect support

## Support

For issues or questions:
1. Check Gemini AI documentation: https://ai.google.dev/docs
2. Review Streamlit docs: https://docs.streamlit.io
3. Test API key at: https://makersuite.google.com

## Credits

- **Gemini AI**: Google
- **Speech Recognition**: Google Speech API
- **Text-to-Speech**: Google TTS (gTTS)
- **Framework**: Streamlit
