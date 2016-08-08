#-*- coding: utf-8 -*-
import argparse
import kmeans

import cv2

parser = argparse.ArgumentParser()

parser.add_argument('--iter', type = int, default='5', help='the number of itmes of iteration')
parser.add_argument('--clus', type = int, default='12', help='the number of cluster')

args = parser.parse_args()


image = cv2.imread("../image/image.bmp", 0)
original = cv2.imread("../image/image.bmp", 0)
K = args.clus
I = args.iter

change = kmeans.kmeans(image, K, I)

cv2.namedWindow("change", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("original", cv2.WINDOW_AUTOSIZE)

cv2.imshow("original", original)
cv2.imshow("change", change)

cv2.waitKey(0)