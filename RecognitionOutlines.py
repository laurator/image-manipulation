import cv2
import numpy as np

# Read image
frame = cv2.imread("media/figures.jpg")

# Convert it to grey
grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Set a threshold value. Any pixel with any intensity of grey bigger than 200, make it 255. Below 200, make it 0.
_, threshold = cv2.threshold(grey, 200, 255, cv2.THRESH_BINARY)

# Find outlines in the threshold image. List of coordinates that define the outline
outlines, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# For every outline found
for c in outlines:
    # Get a vector of vertices. Select elements of the outline that it considers to be good vertices
    vertices = cv2.approxPolyDP(c, 0.009*cv2.arcLength(c,True), True)

    # Draw the detected outlines
    if len(vertices)==5:
        cv2.drawContours(frame, [vertices], 0, (255,0,0), 3)

    # Find forms and draw cyan rectangles. Not minimum area possible. It does not take into account rotation
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 255, 0), 2)

    # Red Rectangles with the smallest area possible that contains the forms. With rotation
    mar = cv2.minAreaRect(c)
    box = cv2.boxPoints(mar)
    cv2.polylines(frame, [box.astype(int)], True, (0,0,255), 2)

    # Find circles with the smallest area that contains the forms
    (x,y), r = cv2.minEnclosingCircle(c)
    x = int(x)
    y = int(y)
    r = int(r)
    cv2.circle(frame, (x,y), r, (255,0,255), 2)

# Show images
cv2.imshow("ORIGINAL", frame)
cv2.waitKey()
cv2.destroyAllWindows()
