import cv2
import numpy as np
import time

# Get video information and open it
video = cv2.VideoCapture("media/Jellyfish.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
numframes = video.get(cv2.CAP_PROP_FRAME_COUNT)

if not video.isOpened():
    print("The video could not be opened")
    exit()

# Start time
counter = 1
begin = time.time()

while True:
    ret, frame = video.read()

    # Read Screenbug image and resize
    opencv = cv2.imread('media/icon-opencv.png', cv2.IMREAD_UNCHANGED)
    miniopencv = cv2.resize(opencv, None, fx=0.2, fy=0.2)

    # Transparency, color of Screenbug image
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

    mixture = bg
    mixture[y:y+hfg, x:x+wfg] = mixture[y:y+hfg, x:x+wfg]*afla + fg*alfa
    # End Screenbug part

    # Dynamic adjustment of frame showing
    start = time.time()
    limitframe = begin + (counter / fps)
    marco = counter/fps
    # Debug info
    # print("start: ", start)
    # print("begin + (counter / fps): ", limitframe)
    # print("(counter / fps): ", marco)

    if (start < limitframe):
        if not ret:
            print("One frame could not be read")
            break

        cv2.imshow('MIXTURE', mixture)
        time.sleep(limitframe-start)
        # To play the video slower:
        # time.sleep(0.04)
        #counter

    counter = counter+1
    #End of dynamic adjustment of frames

    if cv2.waitKey(1) == ord(' '):
        break

end = time.time()
video.release()

print("FPS: ", fps)
print("Number of frames: ", numframes)
print("Duration: ", end-inicio, " seconds")
print("Efective FPS: ", numframes/(end-inicio))


cv2.destroyWindow('VIDEO')
