import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("farzin.jpg.jpg")
cv2.imshow('farzin',img)

new_img = img.copy()
new_img = cv2.flip(new_img,0)
cv2.imshow('new image',new_img)

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
pt1 = (400,85)
pt2 = (760,441)
cv2.rectangle(img_rgb,pt1=pt1,pt2=pt2,color=(255,0,0),thickness=10)
cv2.imshow("me",img_rgb)

# Draw blue triangle

vertics = np.array([[370,500],[581,11],[825,500]],np.int32)
print(vertics)
pts = vertics.reshape((-1,1,2))
print(pts)
print(pts.shape)

cv2.polylines(img_rgb,[pts],isClosed=True,color=(0,0,255),thickness=20)
cv2.imshow("F",img_rgb)

# fill triangle (replace polykines with fillpoly
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.fillPoly(img_rgb,[pts],color=(0,0,255))
cv2.imshow("F",img_rgb)

# Create a script a script that opens the picture and allow us to draw empty red circles whenever you click the Right Mouse Button down

import cv2
import numpy as np

def create_circle(event,x,y,flags,parm):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),thickness=10)

img = cv2.imread("farzin.jpg.jpg")
cv2.namedWindow(winname="Farziiin")
cv2.setMouseCallback("Farziiin",create_circle)

while True:
    cv2.imshow('Farziiin',img)
    if cv2.waitKey(20) & 0xFF== 27:
        break

cv2.waitKey(0)
