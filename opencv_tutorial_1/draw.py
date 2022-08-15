import cv2 as cv
import numpy as np

#creates a blank image
blank = np.zeros((500,500,3), dtype='uint8')
#create a retangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), 2)
# cv.imshow('Blank', blank)

#create a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (0,255,0), 3)
# cv.imshow('Circle', blank)

#create a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), 3)
# cv.imshow('Line', blank)

#write text
cv.putText(blank, 'Hello World', (10,50), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
