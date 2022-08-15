import cv2 as cv

# img = cv.imread('../data/photos/WhatsApp Image 2022-08-12 at 20.24.22 (1).jpeg')
# cv.imshow('Tag', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('../data/videos/ASSAI.mp4')

while True:
    isTrue, frame = capture.read()
    frameScaled = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frameScaled)
    #wait for key to exit
    if cv.waitKey(100) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
