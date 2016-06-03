# if you'r on a 32 bit OS:
# import Image

from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
import time

np.seterr(over='ignore')

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

            imagePixSize = len(imagePix[:3])
            imagePixApply = lambda x, y: x + y
            imagePixReduce = reduce(lambda x, y: x + y, imagePix[:3])
            imagePixDiv = imagePixReduce / imagePixSize

            avgNum = imagePixDiv

            balanceArray.append(avgNum)

    balanceArraySize = len(balanceArray)
    balanceArrayApply = lambda x, y: x + y
    balanceArrayReduce = reduce(lambda x, y: x + y, balanceArray)
    balanceArrayDiv = balanceArrayReduce / balanceArraySize

    balance = balanceArrayDiv

    for imageRow in newArray:
        for imagePix in imageRow:

            imagePixSize = len(imagePix[:3])
            imagePixApply = lambda x, y: x + y
            imagePixReduce = reduce(lambda x, y: x + y, imagePix[:3])
            imagePixDiv = imagePixReduce / imagePixSize

            avgNum = imagePixDiv

            if avgNum > balance:
                imagePix[0] = 255
                imagePix[1] = 255
                imagePix[2] = 255
                imagePix[3] = 255

            else:
                imagePix[0] = 0
                imagePix[1] = 0
                imagePix[2] = 0
                imagePix[3] = 255

    return newArray



image1 = Image.open('images/img19.png')
imageArray1 = np.array(image1)

image2 = Image.open('images/img19.png')
imageArray2 = np.array(image2)

threshhold(imageArray1)
#threshhold(imageArray2)

# Position of the matplot windows

fig = plt.figure()
aux1 = plt.subplot2grid((8, 6), (1, 0), rowspan = 10, colspan = 3)
aux2 = plt.subplot2grid((8, 6), (1, 3), rowspan = 10, colspan = 3)

aux1.imshow(imageArray1)
aux2.imshow(imageArray2)

plt.show()
