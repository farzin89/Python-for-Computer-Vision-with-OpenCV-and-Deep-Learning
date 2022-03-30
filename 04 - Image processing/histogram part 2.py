# -Histogram on a masked portion of the image
# - Histogram Equalization (is a method of contrast adjustment based on the image's histogram.


import cv2
import numpy as np
import matplotlib.pyplot as plt

rainbow= cv2.imread('rainbow.PNG')
show_rainbow = cv2.cvtColor(rainbow,cv2.COLOR_BGR2RGB)
img = rainbow
print(img.shape)

mask =np.zeros(img.shape[:2])
#plt.imshow(mask,cmap='gray')
#plt.show()

mask[300:400,100:400] = 255
#plt.imshow(mask,cmap="gray")
#plt.show()

#masked_img =cv2.bitwise_and(img,img,mask=mask)
#masked_imgg= cv2.bitwise_and(rainbow,rainbow,mask=mask)
#plt.imshow(masked_imgg)
#plt.show()

# B G R
#hist_mask_values_red = cv2.calcHist([show_rainbow],channels=[2],mask=mask,histSize=[256],ranges=[0,256])
#hist_values_red = cv2.calcHist([rainbow],channels=[2],mask=None,histSize=[256],ranges=[0,256])
#plt.plot(hist_mask_values_red)
#plt.title('RED HISTOGRAM FOR MASKED RAINBOW')
#plt.show()

# Histogram part 3

farzin = cv2.imread('farzin2.jpg',0)
def display(img,cmap=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)
display(farzin,cmap="gray")
#plt.show()

print(farzin.shape)

hist_values = cv2.calcHist([farzin],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist_values)
#plt.show()

eq_farzin = cv2.equalizeHist(farzin)
display(eq_farzin,cmap='gray')
#plt.show()

hist_values = cv2.calcHist([eq_farzin],channels=[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist_values)
plt.title("eq")
#plt.show()

color_farzin = cv2.imread("farzin2.jpg")
show_farzin = cv2.cvtColor(color_farzin,cv2.COLOR_BGR2RGB)
display(show_farzin)
plt.show()

hsv = cv2.cvtColor(color_farzin,cv2.COLOR_RGB2HSV)
print(hsv[:,:,2].min())
hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])
eq_color_farzin = cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)
display(eq_color_farzin)
plt.show()


cv2.waitKey(0)