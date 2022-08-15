import cv2 as cv
import numpy as np

img = cv.imread('data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (2).jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
# cv.imshow('Laplacian', lap)

#sobel
sobelX = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelX, sobelY)

# cv.imshow('Sobel X', sobelX)
# cv.imshow('Sobel Y', sobelY)
# cv.imshow('Combined Sobel', combined_sobel)

#canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)