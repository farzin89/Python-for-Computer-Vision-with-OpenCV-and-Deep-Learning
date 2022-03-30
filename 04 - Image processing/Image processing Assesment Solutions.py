
import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(img,cmap=None):
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)

img = cv2.imread("farzin.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
display(img)
#plt.show()

# apply binary threshold onto the image.
img = cv2.imread("farzin.jpg",0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
display(thresh1,cmap='gray')

# Open the file and convert its colorspace to HSV and display the image

img = cv2.imread("farzin2.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
display(img)

# Create a low pass filter with a 4 by 4 Kernel filled with values of 1/10 (0.01) and then use 2-D convolution to blur the
#giraffer image(display to normal RGB)

kernel = np.ones(shape=(4,4),dtype=np.float32)/10
print(kernel)
img =cv2.imread('farzin.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
result = cv2.filter2D(img,-1,kernel)
display(result)

# create Horizontal sobel filter with a kernel size of 5 to the grayscale
# version of our image and then display the resulting gradient filtered version of the image.

img = cv2.imread("farzin.jpg",0)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
display(sobelx,cmap='gray')

# Plot the color histograms for the RED,BLUE,and GREEN channel of our image
#pay careful attention to the ordering of the channels.

img =cv2.imread("farzin.jpg")

color = ['b','g','r']

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
plt.title('my Histo')




plt.show()
#cv2.waitKey(0)


