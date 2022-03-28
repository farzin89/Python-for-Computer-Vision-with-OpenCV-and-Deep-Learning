import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    img = cv2.imread("farzin.jpg").astype(np.float32)/255
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

#print(load_img())

i = load_img()
cv2.imshow("load",load_img())

gamma = 1/4
result= np.power(i,gamma)
cv2.imshow("result",result)

# put tex
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text="bricks",org=(10,600),fontFace=font,fontScale=9,color=(255,0,0),thickness=4)

cv2.imshow("img",img)

# Blurring
kernel = np.ones(shape=(5,5),dtype=np.float)/25
print(kernel)

dst = cv2.filter2D(img,-1,kernel)
cv2.imshow("dst",dst)

# reset the image

img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text="bricks",org=(10,600),fontFace=font,fontScale=9,color=(255,0,0),thickness=4)

# Blurring with "blur" command

blurred = cv2.blur(img,ksize=(5,5))
cv2.imshow("blurred",blurred)

# GaussianBlur
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text="bricks",org=(10,600),fontFace=font,fontScale=9,color=(255,0,0),thickness=4)

blurred_img = cv2.GaussianBlur(img,(5,5),10)
cv2.imshow("blurred_img",blurred_img)

# medianblur (for reducing image noise )
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text="bricks",org=(10,600),fontFace=font,fontScale=9,color=(255,0,0),thickness=4)

median_result= cv2.medianBlur(img,5)
cv2.imshow("median_result",median_result)

# example
img = cv2.imread("soheyb.jpg")
cv2.imshow("so",img)
median = cv2.medianBlur(img,5)
cv2.imshow("so_median",median)

# bilateralFilter
img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text="bricks",org=(10,600),fontFace=font,fontScale=9,color=(255,0,0),thickness=4)

blur = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("so_biladeral",blur)



cv2.waitKey(0)