import cv2 as cv

# img = cv.imread('../data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (1).jpeg')
# cv.imshow('Tag', img)
capture = cv.VideoCapture('../data/videos/ASSAI.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
