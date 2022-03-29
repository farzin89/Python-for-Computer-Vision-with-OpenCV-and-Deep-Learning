
import cv2
import numpy as np
import matplotlib.pyplot as plt

dark_horse = cv2.imread('Black horse.PNG')
show_dark_horse = cv2.cvtColor(dark_horse,cv2.COLOR_BGR2RGB)

rainbow= cv2.imread('rainbow.PNG')
show_rainbow = cv2.cvtColor(dark_horse,cv2.COLOR_BGR2RGB)

blue_briks = cv2.imread('blue bricks.PNG')
show_bricks = cv2.cvtColor(blue_briks,cv2.COLOR_BGR2GRAY)

cv2.imshow("Dark_horse",dark_horse)

hist_values = cv2.calcHist([show_bricks],channels=[0],mask=None,histSize=[256],ranges=[0,255])
print(hist_values.shape)
plt.plot(hist_values)
#plt.show()

# for horse
hist_value= cv2.calcHist([show_dark_horse],channels=[0],mask=None,histSize=[256],ranges=[0,255])
plt.plot(hist_value)
#plt.show()

# for 3 color histograms
img = blue_briks
color = ("b","g","r")
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,256])
plt.title('HISTOGRAM FORBLUE BRICKS')
#plt.show()

# for horse
img = dark_horse
color = ("b","g","r")
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color=col)
    plt.xlim([0,50])
    plt.ylim([0,50000])
plt.title('HISTOGRAM FORBLUE BRICKS')
plt.show()


cv2.waitKey(0)