import cv2
import numpy as np

path = r"img/Beautiful.png"
img = cv2.imread(path)
B, G, R = cv2.split(img)
img = cv2.merge([R,R,G])
cv2.imshow('B', B)
cv2.imshow('G', G)
cv2.imshow('R', R)
cv2.imshow('Image Original', img)


img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
cv2.imshow('HS Image', img)
cv2.waitKey(0)



