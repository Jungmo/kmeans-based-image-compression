import random
import numpy

def kmeans(image, K, I):
    for iter in range(0,1):
        centroid = []
        summ = []
        d={}
        for i in range(0, K):
            centroid.append(random.randrange(255))

        centroid.sort()
        print centroid

        for i in range(0, K):
            d[centroid[i]] = []

        for i in image:
            for j in i:
                temp = findMin(K, centroid,d, j)
                temp.append(j)


        for i in range(0,K):
            if len(d[centroid[i]]) != 0 :
                summ.append(sum(d[centroid[i]])/len(d[centroid[i]]))
            else:
                summ.append(centroid[i])
                print "devide by 0"
       # print summ

    sub = []
    for i in range(0,200):
        for j in range(0,200):
            for p in range(0, K):
                sub.append(abs(j - centroid[p]))


            b = sub.index(min(sub))
            sub = []



def findMin(K, centroid,d, j):
    sub = []
    for i in range(0, K) :
        sub.append(abs(j-centroid[i]))


    return d[centroid[sub.index(min(sub))]]

