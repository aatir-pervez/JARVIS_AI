import cv2
import os
import numpy as np

def train_model():
    path = "dataset"

    faces = []
    labels = []

    label_id = 0

    for file in os.listdir(path):
        img_path = os.path.join(path, file)

        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        faces.append(img)
        labels.append(label_id)

    labels = np.array(labels)

    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(faces, labels)

    model.save("face_model.yml")

    print("Model trained successfully")
    