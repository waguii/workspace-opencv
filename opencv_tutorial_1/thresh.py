import cv2 as cv

img = cv.imread('data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (2).jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Threshold Binary', thresh)

#thresholding inversed
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Threshold Binary Inverse', thresh_inv)

# adaptive thresholding
thresh_adapt = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 2)
cv.imshow('Adaptive Threshold Mean', thresh_adapt)

cv.waitKey(0)