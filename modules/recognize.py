import cv2
from core.speak import speak


def recognize_user():
    model = cv2.face.LBPHFaceRecognizer_create()
    model.read("face_model.yml")

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        speak("Camera not accessible")
        return

    print("Starting recognition...")

    recognized = False   # 🔥 FLAG
    unknown = False

    while True:
        ret, frame = cap.read()

        if not ret or frame is None:
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]

            label, confidence = model.predict(face)

            if confidence < 80:
                name = "Aatir"
                recognized = True
            else:
                name = "Unknown"
                unknown = True

            # Draw box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, name, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        cv2.imshow("Recognition", frame)

        # 🔥 SPEAK ONCE THEN EXIT
        if recognized:
            speak("Hello Aatir, how are you?")
            break

        elif unknown:
            speak("I don't recognize you")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()