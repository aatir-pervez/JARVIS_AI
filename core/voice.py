import speech_recognition as sr


def listen_command():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening for command...")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=8,
                phrase_time_limit=6
            )

        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        return command

    except sr.WaitTimeoutError:
        print("No speech detected")
        return ""

    except sr.UnknownValueError:
        print("Could not understand")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""