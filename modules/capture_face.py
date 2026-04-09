import cv2
import os

def capture_face():
    cap = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    count = 0
    os.makedirs("dataset", exist_ok=True)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            cv2.imwrite(f"dataset/user_{count}.jpg", face)
            count += 1

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.imshow("Capturing Face", frame)

        if count >= 150:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()