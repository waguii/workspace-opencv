import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (2).jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


