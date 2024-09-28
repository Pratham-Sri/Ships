import cv2 as cv

img = cv.imread("Object-detection\opencv-course\Resources\Photos\cat_large.jpg")

def rescaleFrame(frame,scale = 0.75):
    # will work for images, videos and live-videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('image',resized_image)

# cv.waitkey(0)

capture = cv.VideoCapture("Object-detection\opencv-course\Resources\Videos\dog.mp4")

def changeRes(width,height):
    # work on live-video
    capture.set(3,width)
    capture.set(4,height)

while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()