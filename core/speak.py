import os
import pyttsx3
from gtts import gTTS
import pygame


engine = pyttsx3.init()


def speak(text):
    print("Jarvis:", text)

    try:
        # 🔥 TRY ONLINE (gTTS)
        tts = gTTS(text)
        tts.save("temp.mp3")

        pygame.mixer.init()
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        pygame.mixer.music.unload()
        os.remove("temp.mp3")

    except Exception as e:
        print("gTTS failed, switching to offline...")

        # 🔥 FALLBACK OFFLINE
        engine.say(text)
        engine.runAndWait()