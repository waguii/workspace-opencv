import cv2 as cv
import numpy as np
#read imame from file
img = cv.imread('data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (1).jpeg')
# cv.imshow('Initial', img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# translated = translate(img, 100, 100)
# cv.imshow('Translated', translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, 45)
# cv.imshow('Rotated', rotated)

#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

#flipping
flipped = cv.flip(resized, 1)
cv.imshow('Flipped', flipped)

#cropping
cropped = resized[0:250, 0:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
