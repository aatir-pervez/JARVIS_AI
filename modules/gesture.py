import sys
import os

# 🔥 FIX: allow access to project modules when running as subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import cv2
import mediapipe as mp
from core import state
import time
from core.speak import speak


mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


def gesture_control():
    print("GESTURE THREAD STARTED")

    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

    if not cap.isOpened():
       print("❌ Camera not accessible")
       speak("Camera not accessible")
       return
    else:
       print("✅ Camera opened successfully")

    print("Gesture control started")

    last_action_time = 0

    while True:
        ret, frame = cap.read()

        if not ret or frame is None:
            continue

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:

                # Draw landmarks (optional)
                mp_draw.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

                thumb_tip = hand_landmarks.landmark[4]
                index_tip = hand_landmarks.landmark[8]

                current_time = time.time()

                # 🔥 Stability control (prevents spam)
                if current_time - last_action_time > 2:

                    if thumb_tip.y < index_tip.y:
                        if not state.jarvis_active:
                            speak("Resuming")

                        state.jarvis_active = True

                    else:
                        if state.jarvis_active:
                            speak("Paused")

                        state.jarvis_active = False

                    last_action_time = current_time

        # 🔥 Reduce CPU load
        time.sleep(0.3)

    cap.release()