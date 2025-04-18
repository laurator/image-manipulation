import cv2
import numpy as np

# Read image
opencv = cv2.imread('media/icon-opencv.png', cv2.IMREAD_UNCHANGED)
# lena = cv2.imread('lena.tif')

# Get colors and alfa channel
opencv_bgr = opencv[:, :, 0:3]
opencv_alfa = opencv[:, :, :3]

# Show image with and without alfa channel
cv2.imshow('COLOR', opencv_bgr)
cv2.imshow('ALFA', opencv_alfa)
cv2.waitKey()
cv2.destroyAllWindows()
