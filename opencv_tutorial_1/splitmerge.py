import cv2 as cv
import numpy as np

img = cv.imread('data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (2).jpeg')
blank = np.zeros(img.shape[:2], dtype='uint8')

cv.imshow('Original', img)

b, g, r = cv.split(img)

# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

print(img.shape )
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
# cv.imshow('Merged', merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

#wait indefinitely until a key is pressed
cv.waitKey(0)