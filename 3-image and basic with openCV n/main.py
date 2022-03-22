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

# writing something on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,text='farzin',org=(700,300),fontFace=font,fontScale=2,color=(255,255,255),thickness=3,lineType=cv2.LINE_AA)
cv2.imshow("farzin",img)

cap = cv2.imread('cap.JPG')

#percent by which the image is resized
scale_percent = 20
#calculate the 50 percent of original dimensions
width = int(cap.shape[1] * scale_percent / 100)
height = int(cap.shape[0] * scale_percent / 100)
# dsize
dsize = (width, height)

cap_resize = cv2.resize(cap,dsize=dsize)

cv2.imshow('cap',cap_resize)

vertices = np.array([ [100,300],[200,200],[400,300] ,[200,400] ],dtype=np.int32)
print(vertices)
print(vertices.shape)
pts = vertices.reshape((-1,1,2))
print(pts)
cv2.polylines(cap_resize,[pts],isClosed=True,color=(255,0,0),thickness=5)
cv2.imshow('cap',cap_resize)

cv2.waitKey(0)


