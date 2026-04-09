import cv2
import mediapipe as mp
from core import state
import time
from core.speak import speak


def gesture_control():
    print("GESTURE THREAD STARTED") 
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot access camera")
        return

    print("Gesture control started")

    last_action_time = 0

    while True:
        ret, frame = cap.read()

        if not ret or frame is None:
            continue   # 🔥 no print spam

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:

                # 🔥 OPTIONAL (you can remove if you want more performance)
                mp_draw.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

                thumb_tip = hand_landmarks.landmark[4]
                index_tip = hand_landmarks.landmark[8]

                current_time = time.time()

                # 🔥 STABILITY CONTROL (IMPORTANT)
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

        # 🔥 CRITICAL: reduce CPU load
        time.sleep(0.3)

    cap.release()