import cv2 as cv

img = cv.imread('data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (2).jpeg')

cv.imshow('Original', img)

#average blur
blur = cv.blur(img, (5,5))
cv.imshow('Average Blur', blur)

#Gausian blur
gblur = cv.GaussianBlur(img, (5,5), 0)
cv.imshow('Gaussian Blur', gblur)

#median blur
mblur = cv.medianBlur(img, 5)
cv.imshow('Median Blur', mblur)

#bilateral blur
bblur = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral Blur', bblur)

cv.waitKey(0)