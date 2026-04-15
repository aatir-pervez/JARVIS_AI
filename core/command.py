import webbrowser
import os
from core.speak import speak
from ai.gemini import ask_gemini
import musicLibrary
from modules.weather import get_weather
from modules.news import get_news
from modules.stocks import get_stock
from modules.gmail import read_emails
from ai.memory import set_topic, get_topic
import random
from modules.vision import detect_face
from modules.capture_face import capture_face
from modules.train_model import train_model
from modules.recognize import recognize_user
from core import state
import threading



def process_command(command):
  
    topic = get_topic()

    if not state.jarvis_active:
        speak("Jarvis is paused")
        return

    if "tesla" in command:
         set_topic("Tesla")
    elif "ai" in command or "artificial intelligence" in command:
         set_topic("Artificial Intelligence")

         topic = get_topic()

    if topic and ("its" in command or "that" in command):
        command = f"{topic} {command}"

    # 🟢 BASIC COMMANDS
    if "hello" in command:
        speak("Hello boss")

    elif "your name" in command:
        speak("I am Jarvis")

    # 🌐 OPEN WEBSITES
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # 💻 OPEN APPLICATIONS (Mac)
    elif "open vs code" in command:
        speak("Opening Visual Studio Code")
        os.system("open -a 'Visual Studio Code'")

    elif "open chrome" in command:
        speak("Opening Chrome")
        os.system("open -a 'Google Chrome'")

    # 🎵 MUSIC (basic placeholder)
    elif "play music" in command:
        speak("Playing music")
        webbrowser.open("https://www.youtube.com/watch?v=ZbZSe6N_BXs")

    # 📅 DATE (REAL FIX — NO AI)
    elif "date" in command:
        from datetime import datetime
        today = datetime.now().strftime("%A, %d %B %Y")
        speak(today)

        # 🎵 MUSIC SYSTEM (ADVANCED)
    elif command.startswith("play"):
        words = command.split()

        if len(words) > 1:
            song = words[1]

            if song in musicLibrary.music:
                speak(f"Playing {song}")
                webbrowser.open(musicLibrary.music[song])
            else:
                speak("Song not found in your library")
        else:
            speak("Please tell me the song name")

    elif "weather" in command:
          
          
          responses = ["Got it boss", "Checking now", "On it"]
          speak(random.choice(responses))

          words = command.split()

          if "in" in words:
             city = command.split("in", 1)[1].strip()
          else:
             city = "kolkata"

          get_weather(city)
          return
        # 📰 NEWS
    elif "news" in command:
        
        responses = ["Here are the latest headlines", "Let me get the news", "Checking updates"]
        speak(random.choice(responses))
        
        get_news() 

        # 📈 STOCK SYSTEM
    elif "stock" in command:
        
        responses = ["Let me check that", "Fetching stock data", "One moment"]
        speak(random.choice(responses))

        company_map = {
        "apple": "AAPL",
        "tesla": "TSLA",
        "google": "GOOGL",
        "amazon": "AMZN",
        "microsoft": "MSFT",
        "netflix": "NFLX",
        "meta": "META"
        }

        for company in company_map:
           if company in command:
               get_stock(company_map[company])
               return   # 🔥 VERY IMPORTANT

        speak("Sorry, I don't recognize that company")
        return   # 🔥 IMPORTANT

    elif "email" in command:
         read_emails()
         return
    elif "open camera" in command or "face detection" in command:
         speak("Starting face detection")
         detect_face()
    elif "capture face" in command:
        speak("Capturing your face data")
        capture_face()
    elif "train model" in command:
        speak("Training your face model")
        train_model()
    elif "recognise me" in command:
        speak("Recognizing you")
        recognize_user() 
    elif "gesture control" in command:
        import subprocess

        speak("Starting gesture control")

        subprocess.Popen([
            "/Users/aatirpervez/Documents/JARVIS_V2/gesture_env/bin/python",
            "modules/gesture.py"
        ])

        return

    
    # 🤖 DEFAULT → GEMINI
    
    else:
        responses = ["Let me think", "Give me a second", "Processing"]
        speak(random.choice(responses))

        reply = ask_gemini(command)
        speak(reply)
        return reply