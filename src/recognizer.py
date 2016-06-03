# if you'r on a 32 bit OS:
# import Image

from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
import time

# img = Image.open('images/img2.png')

# an array that corresponds into 'img' image
# and the image array will come out in a 3 dim array

# Array => (R, G, B, Alpha)

# imageArray = np.asarray(img)

# print imageArray

# plt.imshow(imageArray)
# plt.show()

# this function will change the values of the array

def threshhold(imageArrayArg):

    balanceArray = []
    newArray = imageArrayArg

    for imageRow in imageArrayArg:
        for imagePix in imageRow:

            print imagePix


image1 = Image.open('images/img2.png')
imageArray1 = np.array(image1)

image2 = Image.open('images/img17.png')
imageArray2 = np.array(image2)

threshhold(imageArray2)

# Position of the matplot windows

'''fig = plt.figure()
aux1 = plt.subplot2grid((8, 6), (1, 0), rowspan = 10, colspan = 3)
aux2 = plt.subplot2grid((8, 6), (1, 3), rowspan = 10, colspan = 3)

aux1.imshow(imageArray1)
aux2.imshow(imageArray2)

plt.show()'''
