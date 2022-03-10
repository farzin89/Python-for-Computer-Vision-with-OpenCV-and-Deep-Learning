# -*- coding: utf-8 -*-
"""Numpy_ and_Image_basics .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19veTRmi_HdlPjyAzWMYIaWyTPU-9nlYR
"""

import numpy as np
mylist = [1,2,3]
type(mylist)

myarray = np.array(mylist)

myarray

type(myarray)

np.arange(0,10,2)

from numpy.core.fromnumeric import shape
np.zeros(shape = (10,5))

type(0)

type(0.)

np.ones(shape=(2,4))

np.random.seed(101)
arr = np.random.randint(0,100,10)
arr

arr2 = np.random.randint(0,100,10)
arr2

arr.max()

arr.argmax()

arr.min()

arr.argmin()

arr.mean()

arr.reshape((5,2))

mat = np.arange(0,100).reshape(10,10)
mat

row = 0
col = 1

mat[row,col]

mat[4,6]

mat[:,1].reshape(10,1)

mat[2,:]

mat[0:3,0:3]

mat[0:3,0:3]= 0
mat

mynewmat = mat.copy()
 mynewmat[0:6,:] = 999
 mynewmat

# Commented out IPython magic to ensure Python compatibility.
#Image and numpy
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

from PIL import Image

pic = Image.open("/content/drive/MyDrive/dataset/test/with_mask/0_0_0 copy 10.jpg")
pic

type (pic)

pic_arr = np.asarray(pic)
pic_arr

type(pic_arr)

pic_arr.shape

plt.imshow(pic_arr)

pic_red = pic_arr.copy()
plt.imshow(pic_red)

pic_red.shape

# R G B
pic_red[:,:,0]

plt.imshow(pic_red[:,:,0])

# RED channel values 0 no red,pure black -255 full pure red

plt.imshow(pic_red[:,:,0],cmap='gray') # closer, more red

plt.imshow(pic_red[:,:,1])

plt.imshow(pic_red[:,:,2])

# GREEN CHANNEL
pic_red[:,:,1] = 0
plt.imshow(pic_red)

c[:,:,2] = 0
plt.imshow(pic_red)

pic_red.shape