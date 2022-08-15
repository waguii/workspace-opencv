import cv2 as cv

#read imame from file
img = cv.imread('data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (1).jpeg')
cv.imshow('Initial', img)
#transform image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
#Blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
#Edge cascade
# canny = cv.Canny(img, 125,175)
# cv.imshow('Canny', canny)
# #Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)
# #eroding the image
# eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('Eroded', eroded)
# #resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)
#cropping
cropped = img[0:500, 0:1000]
cv.imshow('Cropped', cropped)
#wait indefinitely for key to exit
cv.waitKey(0)
