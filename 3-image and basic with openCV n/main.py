import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('farzin.jpg.jpg')
cv2.imshow("farzin",img)
cv2.rectangle(img,pt1=(760,100)# top left corner
                 ,pt2=(450,500) # buttem right corner
                  ,color=(0,255,0)
                  ,thickness=10)
cv2.imshow("farzin",img)
cv2.circle(img,center=(100,100),radius=50,color=(255,0,0),thickness=8)
cv2.imshow("farzin",img)
cv2.circle(img,center=(1000,700),radius=50,color=(255,0,0),thickness=-1)
cv2.imshow("farzin",img)
cv2.line(img,pt1=(0,0),pt2=(512,512),color=(102,255,255),thickness=5)
cv2.imshow("farzin",img)

cv2.waitKey(0)


