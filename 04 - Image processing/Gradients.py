
# An image gradient is a directional change in the intensity or color in an image.
# Gradients can be calculated in a specific direction.

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sudoku.PNG')
cv2.imshow("sudoku",img)

sobelx= cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
cv2.imshow("sobex",sobelx)

# for clear horizontal line
sobely= cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
cv2.imshow("sobey",sobely)

# laplacian (it does not need to fix x and y )
laplacian = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("laplacian",laplacian)

# belended
blended = cv2.addWeighted(src1=sobelx,alpha=0.5,src2=sobely,beta=0.5,gamma=0)
cv2.imshow("blended",blended)

# thredhold
ret,th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imshow("th1",th1)
cv2.waitKey(0)

kernel = np.ones((4,4))
gradient = cv2.morphologyEx(blended,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("gradient",gradient)