import cv2 as cv

# img = cv.imread('../data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (1).jpeg')
# cv.imshow('Tag', img)
capture = cv.VideoCapture('data/videos/ASSAI.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video Original', frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    adapt_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)

    cv.imshow('Video Threshold', adapt_threshold)

    if cv.waitKey(30) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
