import tkinter as tk
import threading
from core.command import process_command
from core.speak import speak
from core import state
from modules.gesture import gesture_control
import speech_recognition as sr


# 🔥 SEND COMMAND
def send_command():
    print("SEND BUTTON CLICKED")  # ✅ DEBUG

    command = entry.get().strip().lower()
    entry.delete(0, tk.END)

    if not command:
        return

    output.insert(tk.END, "You: " + command + "\n")

    # 🔥 HANDLE GESTURE FIRST
    if "gesture control" in command:
        output.insert(tk.END, "Starting Gesture Control...\n\n")

        threading.Thread(
            target=gesture_control,
            daemon=True
        ).start()

        return

    # 🔥 CHECK PAUSE
    if not state.jarvis_active:
        output.insert(tk.END, "Jarvis is Paused (Gesture)\n\n")
        return

    # 🔥 NORMAL COMMAND
    process_command(command)


# 🔥 STATUS UPDATE
def update_status():
    if state.jarvis_active:
        status_label.config(text="Status: ACTIVE 🟢", fg="green")
    else:
        status_label.config(text="Status: PAUSED 🔴", fg="red")

    root.after(500, update_status)


# 🔥 MIC BUTTON
def mic_click():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone(device_index=0) as source:
            output.insert(tk.END, "🎤 Listening...\n")
            root.update()

            recognizer.adjust_for_ambient_noise(source, duration=1)

            # 🔥 FIXED LISTEN SETTINGS
            audio = recognizer.listen(
                source,
                timeout=10,            # wait longer to start speaking
                phrase_time_limit=8    # max speaking time
            )

            output.insert(tk.END, "Processing...\n")
            root.update()

            command = recognizer.recognize_google(audio).lower()

            output.insert(tk.END, "You (voice): " + command + "\n")

            # 🔥 HANDLE GESTURE
            if "gesture control" in command:
                output.insert(tk.END, "Starting Gesture Control...\n\n")
                threading.Thread(target=gesture_control, daemon=True).start()
                return

            if not state.jarvis_active:
                output.insert(tk.END, "Jarvis is Paused (Gesture)\n\n")
                return

            process_command(command)

    except sr.WaitTimeoutError:
        output.insert(tk.END, "⏱ No speech detected, try again\n\n")

    except sr.UnknownValueError:
        output.insert(tk.END, "❌ Could not understand\n\n")

    except Exception as e:
        output.insert(tk.END, "Mic Error: " + str(e) + "\n\n")


# 🟣 MAIN WINDOW
root = tk.Tk()
root.title("Jarvis AI Assistant")
root.geometry("500x650")


# 🟣 OUTPUT BOX
output = tk.Text(root, height=25, width=60)
output.pack(pady=10)


# 🟣 STATUS LABEL
status_label = tk.Label(root, text="Status: ACTIVE 🟢", font=("Arial", 12))
status_label.pack()


# 🟣 INPUT FIELD
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

entry.focus()  # 🔥 AUTO FOCUS

# 🔥 ENTER KEY SUPPORT
entry.bind("<Return>", lambda event: send_command())


# 🟣 BUTTON FRAME
frame = tk.Frame(root)
frame.pack(pady=10)


# 🟣 SEND BUTTON
send_btn = tk.Button(frame, text="Send", width=15, command=lambda: send_command())
send_btn.grid(row=0, column=0, padx=5)


# 🟣 MIC BUTTON
mic_btn = tk.Button(frame, text="🎤 Mic", width=15, command=mic_click)
mic_btn.grid(row=0, column=1, padx=5)


# 🔥 START STATUS LOOP
update_status()


# 🚀 RUN GUI
root.mainloop()