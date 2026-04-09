from core.command import process_command
from core.speak import speak
from core.voice import listen_command
from wakeword.listener import listen_wake_word
from core import state
import time


def main():
    speak("Jarvis initialized")

    while True:
        print("\nWaiting for wake word...")

        # 🔥 WAKE WORD LOOP
        while True:
            if listen_wake_word():
                speak("Yes boss")
                break
            time.sleep(0.3)

        # 🔥 ACTIVE MODE (VOICE + GESTURE PARALLEL)
        while True:

            # 🔥 IF PAUSED → DO NOTHING (NO MIC)
            if not state.jarvis_active:
                # (No print → clean UX)
                time.sleep(0.5)
                continue

            # 🔥 ONLY LISTEN WHEN ACTIVE
            command = listen_command()

            if not command:
                continue

            command = command.lower().strip()   # 🔥 safety normalization
            print("Command:", command)

            ignore_words = ["resuming", "paused"]

            if any(word in command for word in ignore_words):
               continue

            # 🔥 EXIT ACTIVE MODE
            if "stop" in command or "exit" in command:
                speak("Going back to sleep")
                break

            # 🔥 PROCESS COMMAND
            try:
                process_command(command)
            except Exception as e:
                print("Error in command:", e)
                speak("Something went wrong")

            time.sleep(0.2)


if __name__ == "__main__":
    main()