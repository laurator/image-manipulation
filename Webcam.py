import cv2
import numpy as np

# Webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam could not be opened")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("One frame could not be read")
        break

    # Show webcam
    cv2.imshow('WEBCAM', frame)

    if cv2.waitKey(1) == ord(' '):
        break

cap.release()
cv2.destroyWindow('WEBCAM')
