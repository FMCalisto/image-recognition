# Author: Francisco Maria Calisto
# E-Mail: email@franciscocalisto.me
# GitHub: https://github.com/FMCalisto

# if you'r on a 32 bit OS:
# import Image

from PIL import Image

import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

np.seterr(over='ignore')


def createImages():

    numberArrayImages = open('numArrayImages.txt', 'a')
    numbersRange = range(0,10)
    versionsRange = range(1,10)

    for num in numbersRange:
        for ver in versionsRange:

            #print str(num) + '.' + str(ver)

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


def getNum(filePath):
    matchedArray = []
    loadImages = open('numArrayImages.txt', 'r').read()
    loadImages = loadImages.split('\n')

    image = Image.open(filePath)
    imageArray = np.array(image)
    imageArrayToList = imageArray.tolist()

    imageArrayToString = str(imageArrayToList)

    for image in loadImages:
        if len(image) > 3:
            splitImage = image.split('::')
            currentNum = splitImage[0]
            currentArray = splitImage[1]

            imagePix = currentArray.split('],')
            imagePixArrayToString = imageArrayToString.split('],')

            i = 0

            while i < len(imagePix):
                if imagePix[i] == imagePixArrayToString[i]:
                    matchedArray.append(int (currentNum))

                i += 1

    print(matchedArray)

    i = Counter(matchedArray)

    print(i)

    graphX = []
    graphY = []

    for infoPix in i:
        print infoPix
        graphX.append(infoPix)
        print i[infoPix]
        graphY.append(i[infoPix])

    fig = plt.figure()
    aux1 = plt.subplot2grid((4,4), (0,0), rowspan = 1, colspan = 4)
    aux2 = plt.subplot2grid((4,4), (1,0), rowspan = 3, colspan = 4)

    aux1.imshow(imageArray)
    aux2.bar(graphX, graphY, align = 'center')
    plt.ylim(100)

    iLoc = plt.MaxNLocator(12)

    aux2.xaxis.set_major_locator(iLoc)
    
    plt.show()

getNum('images/test.png')



    
