#-*- coding: utf-8 -*-
import random

import operator


def kmeans(image, K, I):
    centroid = []
    table = {}
    temp = []
    # 첫번째 centroid 만들기
    for i in range(0, K):
        centroid.append(random.randrange(255))


    for i in range(0, K):
        table[centroid[i]] = []

    centroid.sort()
    table = sorted(table.items(), key=operator.itemgetter(0))

    print table
    print centroid

    for i in image:
        for j in i:
            for k in range(0,K):
                temp.append(abs(j-centroid[k]))
            print centroid, j, temp, temp.index(min(temp)), centroid[temp.index(min(temp))], type(table[0])
            temp = []


    print table

