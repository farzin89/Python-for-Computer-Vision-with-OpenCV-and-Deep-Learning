
# Morphological Operators are sets of kernels that can achieve a variety of effects, such as reducing noise.
# Certain operators are very good at reducing black points on a white background (and vice versa)
# certain operators can also achieve an erosion and dilation effect that can add or erode from an existing image.
# This effect is most easily seen on text data, so we will practice various morphological operators on some simple
# white text on a blackground.

import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    black_img = np.zeros((600,600))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(black_img,text="ABCDE",org=(50,300),fontFace=font,fontScale=5,color=(255,255,255),thickness=10)
    return black_img

img = load_img()
cv2.imshow("img",img)

kernel = np.ones((5,5))
print(kernel)

result = cv2.erode(img,kernel,iterations=2)
cv2.imshow("result",result)

# opening ( is a erosion flow by )

img = load_img()
white_noise = np.random.randint(low=0,high=2,size=(600,600))
print(white_noise)
#cv2.imshow("white_noise",white_noise)
print(img.max())
white_noise = white_noise * 255
print(white_noise)
#cv2.imshow("white_noise",white_noise)

noise_img = white_noise + img
cv2.imshow('noise',noise_img)

opening = cv2.morphologyEx(noise_img,cv2.MORPH_OPEN,kernel)
cv2.imshow('opening',opening)


black_noise = np.random.randint(low=0,high=2,size=(600,600))
print(black_noise)
black_noise = black_noise * -255
print(black_noise)
black_noise_img = img + black_noise
print(black_noise_img)
black_noise_img[black_noise_img==-255] = 0
print(black_noise_img.min())
cv2.imshow("black_noise_img",black_noise_img)
closing = cv2.morphologyEx(black_noise_img,cv2.MORPH_CLOSE,kernel)
cv2.imshow('closing',closing)

# morphological gradiant(for edge detection)
img = load_img()
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
cv2.imshow('gradient',gradient)


cv2.waitKey(0)

