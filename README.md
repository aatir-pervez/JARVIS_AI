# 🤖 Jarvis AI Assistant

A futuristic AI assistant with **voice, gesture, vision, and web interaction**.

---

## 🚀 Features

- 🎤 Voice-controlled assistant (wake word + commands)
- 🌐 Flask-based web dashboard (chat + mic)
- ✋ Gesture control (pause/resume system)
- 👁 Face recognition with personalized greeting
- 🧠 Gemini AI integration (context-aware responses)
- 📊 APIs: Weather, News, Stocks
- 🔊 Speech output (gTTS + offline fallback)

---

## 🧠 Tech Stack

- Python
- Flask
- OpenCV
- MediaPipe
- SpeechRecognition
- Google Gemini API
- HTML, CSS, JavaScript

---

## 🏗️ Architecture

User Input (Voice / Web / Gesture)
        ↓
process_command()
        ↓
 ┌────────┼────────┐
 ↓        ↓        ↓
Gemini   APIs   Features
 (AI)   (Weather) (Vision)

---

## ▶️ How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Add API keys
Create `.env` file:

GEMINI_API_KEY=your_key_here  
NEWS_API_KEY=your_key_here  

### 3. Run Web App
python app.py

Open:
http://127.0.0.1:5001

---

## 🎯 Demo Commands

- "weather in kolkata"
- "open youtube"
- "recognise me"
- Use 🎤 mic button in web
- Use ✋ gesture to pause/resume

---

## 👨‍💻 Author

Aatir Pervez

---

## 🌟 Future Improvements

- Cloud deployment (Render / AWS)
- Mobile integration
- Advanced automation features