import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    # Video capture
    ret, frame = cap.read()
    cv2.imshow('WEBCAM', frame)

    # Read the image of the logo of OpenCV
    opencv = cv2.imread('media/icon-opencv.png', cv2.IMREAD_UNCHANGED)

    # Resize the logo
    miniopencv = cv2.resize(opencv, None, fx=0.2, fy=0.2)

    # Transparency and color of logo
    bg = frame
    hbg, wbg, _ = bg.shape
    fg = miniopencv[:, :, 0:3]
    hfg, wfg, _ = fg.shape
    alfa = miniopencv[:, :, 3]
    afla = 255 - alfa

    alfa = cv2.cvtColor(alfa, cv2.COLOR_GRAY2BGR) / 255
    afla = cv2.cvtColor(afla, cv2.COLOR_GRAY2BGR) / 255

    x = wbg - wfg
    y = hbg - hfg

    # Joining both images in one
    mixture = bg
    mixture[y:y+hfg, x:x+wfg] = mixture[y:y+hfg, x:x+wfg]*afla + fg*alfa

    cv2.imshow('MIXTURE', mixture)

    if cv2.waitKey(1) == ord(' '):
        break

cv2.waitKey()
cv2.destroyAllWindows()
