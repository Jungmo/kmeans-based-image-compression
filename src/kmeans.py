#-*- coding: utf-8 -*-
import random

import operator


def kmeans(image, K, I):
    centroid = getRandomCentroid(image, K) # Initial centroid
    subtract = []
#### initialize finish

    for iter in range(0, I) :
        table = {}
        for i in range(0, K):
            table[centroid[i]] = []

        for i in image:
            for j in i:
                for k in range(0,K):
                    subtract.append(abs(j-centroid[k]))
                #print centroid, j, temp, temp.index(min(temp))
                table[centroid[subtract.index(min(subtract))]].append(j)
                subtract = []

#### one iteration finish

        centroid = generateNewCentroid(table)

        print iter , " - ", centroid

    return changeImage(image, centroid, K)


def generateNewCentroid(table):

    temp_centroid = []
    for i in table.keys():
        values =  table[i]

        if len(values) == 0:
            temp_centroid.append(i)
        else:
            temp_centroid.append(int(sum(values, 0.0) / len(values)))

    temp_centroid.sort()
    return temp_centroid


def getRandomCentroid(image, K):

    centroid = []
    pixel = []
    for i in image :
        for j in i :
            try :
                pixel.index(j)
            except ValueError :
                pixel.append(j)

    for i in range(0, K) :
        while 1:
            temp = random.randrange(len(pixel))
            if isValueInList(centroid, temp) == 1 :
                continue
            else:
                centroid.append(temp)
                break

    centroid.sort()

    return centroid

def isValueInList(list, value):
    for i in range(0, len(list)):
        if i == value:
            return 1
        else :
            return 0

def changeImage(image, lastCentroid, K):
    x = 0
    y = 0
    for i in image:
        for j in i:
            nearlist = abs(j - lastCentroid[0])
            nearlist_centroid = lastCentroid[0]
            for k in range(1, K):
                temp = abs(j - lastCentroid[k])
                if nearlist > temp :
                    nearlist = temp
                    nearlist_centroid = lastCentroid[k]
            image[x][y] = nearlist_centroid
            y = y+1
        x = x + 1
        y = 0
    return image

