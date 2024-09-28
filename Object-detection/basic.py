import cv2 as cv

img = cv.imread('Object-detection\opencv-course\Resources\Photos\cat.jpg')
cv.imshow('Cat',img)

# Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur
blur  = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# Edge correction
canny = cv.Canny(blur,125,175)
cv.imshow('Canny',canny)

# Dilating the image
dilated = cv.dilate(canny,(5,5),iterations=3)
cv.imshow('dilated',dilated)

# Eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

# resize the image
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

# cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
