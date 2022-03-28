import cv2
import matplotlib.pyplot as plt
import numpy as np
img1 = cv2.imread("farzin.jpg")
img2 = cv2.imread("soheyb.jpg")
print(img1.shape)


img2 = cv2.resize(img2,(300,300))

cv2.imshow("img1",img1)
x_offset = 750 - 500
y_offset = 1334 - 500

print(img2.shape)

roi = img1[y_offset:1401,x_offset:943]
cv2.imshow("roi",roi)

# Creating masks

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("img2gray",img2gray)

mask_inv = cv2.bitwise_not(img2gray)
cv2.imshow("mask_inv",mask_inv)

print(mask_inv.shape)

white_background = np.full(img2.shape,255)
print(white_background.shape)

# white_background
bk = cv2.bitwise_or(white_background,white_background,mask=mask_inv)
print(bk.shape)

fg = cv2.bitwise_or(img2,img2,mask=mask_inv)
cv2.imshow("fg",fg)



cv2.waitKey(0)


