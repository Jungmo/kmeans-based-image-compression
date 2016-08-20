#-*- coding: utf-8 -*-
import argparse
import kmeans
import os
import cv2

dirpath = "/Users/jungmo/Documents/github/birdnest/repo/train/"
parser = argparse.ArgumentParser()

parser.add_argument('--iter', type = int, default='5', help='the number of itmes of iteration')
parser.add_argument('--clus', type = int, default='4', help='the number of cluster')

args = parser.parse_args()

filelist = os.listdir(dirpath)

def fuc(filename):
    print filename
    if filename.count(".bmp") == 0 :
        return

    image = cv2.imread(dirpath+filename, 0)

    K = args.clus
    I = args.iter

    change = kmeans.kmeans(image, K, I)

    filename = os.path.splitext(filename)[0]
    cv2.imwrite(filename+"_modified.bmp", change)

for filename in filelist:
    fuc(filename)


