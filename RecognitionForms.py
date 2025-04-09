import cv2
import numpy as np

# Read image with forms
frame = cv2.imread("media/billar.jpeg")

# Transform to grey image
grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Any pixel with any intensity of grey bigger than 100  make it 255
_, threshold = cv2.threshold(grey, 100, 255, cv2.THRESH_BINARY)

# Recognise circles between 10 - 100 radius
circles = cv2.HoughCircles(threshold, cv2.HOUGH_GRADIENT, dp=1.5, minDist=100, param1=50, param2=30, minRadius=10, maxRadius=100)
circles = circles.astype(int)

# If circles were recognised, show them
if circles is not None:
    for c in circles[0]:
        x, y, r = c
        cv2.circle(frame, (x,y), r, (0,0,255), 2)



cv2.imshow("ORIGINAL", frame)
cv2.imshow("THRESHOLD", threshold)
cv2.waitKey()
cv2.destroyAllWindows()
