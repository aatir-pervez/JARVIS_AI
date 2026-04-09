import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer

model = Model("model")

q = queue.Queue()


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def listen_wake_word():
    recognizer = KaldiRecognizer(model, 16000)

    print("Listening for wake word...")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1,
        callback=callback
    ):
        while True:
            try:
                data = q.get(timeout=1)   # 🔥 prevents freeze

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())
                    text = result.get("text", "")

                    if "jarvis" in text:
                        print("Wake word detected")

                        # 🔥 CLEAR QUEUE AFTER DETECTION
                        while not q.empty():
                            q.get()

                        return True

            except queue.Empty:
                continue