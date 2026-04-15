import speech_recognition as sr
import time

def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")

            # 🔥 IMPORTANT: pause before listening
            time.sleep(0.5)

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(source, timeout=10, phrase_time_limit=7)

        print("Processing...")

        command = recognizer.recognize_google(audio)
        print("You said:", command)

        return command.lower()

    except sr.WaitTimeoutError:
        print("Timeout - no speech")
        return ""

    except sr.UnknownValueError:
        print("Could not understand")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""  