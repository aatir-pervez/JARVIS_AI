import speech_recognition as sr


def listen_wake_word():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening for wake word...")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=2
            )

        word = recognizer.recognize_google(audio).lower()

        print("Heard:", word)

        if "jarvis" in word:
            print("Wake word detected")
            return True

        return False

    except:
        return False