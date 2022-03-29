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
plt.imshow(mask,cmap="gray")
#plt.show()

#masked_img =cv2.bitwise_and(img,img,mask=mask)
#masked_imgg= cv2.bitwise_and(rainbow,rainbow,mask=mask)
#plt.imshow(masked_imgg)
#plt.show()

# B G R
hist_mask_values_red = cv2.calcHist([show_rainbow],channels=[2],mask=mask,histSize=[256],ranges=[0,256])
hist_values_red = cv2.calcHist([rainbow],channels=[2],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist_mask_values_red)
plt.title('RED HISTOGRAM FOR MASKED RAINBOW')
plt.show()






cv2.waitKey(0)