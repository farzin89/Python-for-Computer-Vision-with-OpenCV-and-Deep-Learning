import cv2
import matplotlib.pyplot as plt

img = cv2.imread("farzin.jpg",0) # when we put 0 our image will be gray
cv2.imshow("me",img)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("thresh1",thresh1)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) # inverse
cv2.imshow("thresh1_inv",thresh1)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) # TRUNC
cv2.imshow("thresh1_Trunc",thresh1)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) # ToZERO
cv2.imshow("thresh1_TOZERO",thresh1)


img = cv2.imread("puzel.PNG",0)
cv2.imshow("puzel",img)


def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img)
show_pic(img)
# this def does not work


ret,th1 = cv2.threshold(img,180,255,cv2.THRESH_BINARY)
cv2.imshow("th1",th1)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
cv2.imshow("th2",th2)

blended = cv2.addWeighted(src1=th1,alpha=0.6,src2=th2,beta=0.4,gamma=0)
cv2.imshow("blended",blended)





cv2.waitKey(0)