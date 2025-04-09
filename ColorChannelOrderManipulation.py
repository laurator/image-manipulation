import cv2
import numpy as np

# Read image
lena = cv2.imread('media/lena.tif')

# Split color channels
b, g, r = cv2.split(lena)

# Change channel data
lena_grb = cv2.merge((g, r, b))

# Show modified image
cv2.imshow('GRB', lena_grb)

cv2.waitKey()
cv2.destroyAllWindows()
