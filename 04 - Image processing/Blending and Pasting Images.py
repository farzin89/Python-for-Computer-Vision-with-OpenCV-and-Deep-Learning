import cv2
import matplotlib.pyplot as plt

img= cv2.imread('farzin.jpg')
#cv2.imshow("farzin",img)

img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
#cv2.imshow("pic",img)

img1 = cv2.imread("farzin.jpg")

img2 = cv2.imread("soheyb.jpg")

#cv2.imshow("image1",img1)
#cv2.imshow("image2",img2)

# Blenbing images of the same size
img1 = cv2.resize(img1,(400,400))
img2 = cv2.resize(img2,(400,400))

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

blended = cv2.addWeighted(src1=img1,alpha=0.6,src2=img2,beta=0.3,gamma=0) # we use "addweighted" when our pictures have same size
#cv2.imshow('blended',blended)

"""Overaly small image on top of a larger image (no blending)
Numpy reassingment"""

img1 = cv2.imread("farzin.jpg")
img2 = cv2.imread("soheyb.jpg")
img2 = cv2.resize(img2,(300,300))
cv2.imshow("resize2",img2)

large_img = img1
small_img = img2

x_offset = 0
y_offset = 0

x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]

large_img[y_offset:y_end,x_offset:x_end] = small_img
cv2.imshow("larg_img",large_img)
cv2.waitKey(0)