import cv2
import numpy as np

# Read 2 images
lena = cv2.imread('media/lena.tif')
opencv = cv2.imread('media/icon-opencv.png', cv2.IMREAD_UNCHANGED)

# Set sizes and transparency channel
bg = lena
hbg, wbg, _ = bg.shape

fg = opencv[:, :, 0:3]
hfg, wfg, _ = fg.shape

alfa = opencv[:, :, 3]
afla = 255 - alfa

alfa = cv2.cvtColor(alfa, cv2.COLOR_GRAY2BGR) / 255
afla = cv2.cvtColor(afla, cv2.COLOR_GRAY2BGR) / 255

x = wbg//2 - wfg//2
y = hbg//2 - hfg//2

# Show the two images with transparency. The logo is smaller
mixture = bg
mixture[y:y+hfg, x:x+wfg] = mixture[y:y+hfg, x:x+wfg]*afla + fg*alfa

cv2.imshow('MIXTURE', mixture)
cv2.waitKey()
cv2.destroyAllWindows()
