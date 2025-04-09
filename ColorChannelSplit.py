import cv2
import numpy as np

# Read image of Lena
lena = cv2.imread('media/lena.tif', cv2.IMREAD_UNCHANGED)

# Split color channels
b, g, r = cv2.split(lena)
lenacolor = lena[:, :, :3]

# Show image
cv2.imshow('LENA COLOR', lenacolor)

# Convert to color as BGR
lenablue = cv2.cvtColor(lenacolor, cv2.COLOR_RGBA2BGR)

cv2.imshow('LENA BLUE', lenablue)

# Show color channels in Black and White
cv2.imshow('Blue channel', b)
cv2.imshow('Green channel', g)
cv2.imshow('Red channel', r)

cv2.waitKey()
cv2.destroyAllWindows()
