#-*- coding: utf-8 -*-
import argparse
import kmeans2
import random

import cv2

parser = argparse.ArgumentParser()

parser.add_argument('--iter', type = int, default='4', help='the number of itmes of iteration')
parser.add_argument('--clus', type = int, default='4', help='the number of cluster')

args = parser.parse_args()

image = cv2.imread("image.bmp", 0)

K = args.clus
I = args.iter


kmeans2.kmeans(image, K, I)
