import cv2
import numpy as np

# Read image
lena = cv2.imread('media/lena.tif')

# Resize image to the half
minilena = cv2.resize(lena, None, fx=0.5, fy=0.5)

cv2.imshow('LENA', minilena)
cv2.waitKey()
cv2.destroyAllWindows()
