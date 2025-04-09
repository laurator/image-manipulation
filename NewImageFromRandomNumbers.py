import cv2 # OpenCV library
import numpy as np

# Create new matrix, dimensions (250 x 250 x 3) with random numbers between 0 - 255
rgb = np.random.randint(255, size=(250,250,3), dtype=np.uint8)

# Show random color image
cv2.imshow('RANDOM', rgb) 

# When pressing any key, close the window
cv2.waitKey()
cv2.destroyWindow('RANDOM')
