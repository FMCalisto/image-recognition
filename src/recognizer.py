# Author: Francisco Maria Calisto
# E-Mail: email@franciscocalisto.me
# GitHub: https://github.com/FMCalisto

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


def createImages():

    numberArrayImages = open('numArrayImages.txt', 'a')
    numbersRange = range(1, 2) # <-- FIXME
    versionsRange = range(1, 10) # <-- FIXME

    for num in numbersRange:
        for ver in versionsRange:

            print str(num) + '.' + str(ver)

            imgFilePath = 'images/numbers/' + str(num) + '.' + str(ver) + '.png'
            image = Image.open(imgFilePath)
            imageArray = np.array(image)
            imageArrayToList = str(imageArray.tolist())

            lineToWrite = str(num) + '::' + imageArrayToList + '\n'
            numberArrayImages.write(lineToWrite)


# this function will change the values of the array

def threshhold(imageArrayArg):

    balanceArray = []


    newArray = imageArrayArg

    for imageRow in imageArrayArg:
        for imagePix in imageRow:

            imagePixSize = len(imagePix[:3])
            imagePixApply = lambda x, y: x + y
            imagePixReduce = reduce(imagePixApply, imagePix[:3])
            imagePixDiv = imagePixReduce / imagePixSize

            avgNum = imagePixDiv

            balanceArray.append(avgNum)

    balanceArraySize = len(balanceArray)
    balanceArrayApply = lambda x, y: x + y
    balanceArrayReduce = reduce(balanceArrayApply, balanceArray)
    balanceArrayDiv = balanceArrayReduce / balanceArraySize

    balance = balanceArrayDiv

    for imageRow in newArray:
        for imagePix in imageRow:

            imagePixSize = len(imagePix[:3])
            imagePixApply = lambda x, y: x + y
            imagePixReduce = reduce(imagePixApply, imagePix[:3])
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
