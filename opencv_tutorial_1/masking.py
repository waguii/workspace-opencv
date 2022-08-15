import cv2 as cv
import numpy as np


img = cv.imread('data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (2).jpeg')
cv.imshow('Original', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask_circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 200, 255, -1)
mask_rectangle = cv.rectangle(blank, (30,30),\
(img.shape[1]//2 +100,img.shape[0]//2 +100), 255, -1)

weird_mask = cv.bitwise_not(mask_circle, mask_rectangle)
cv.imshow('test', weird_mask)

masked = cv.bitwise_and(img, img, mask=weird_mask)
cv.imshow('Masked', masked)

cv.waitKey(0)