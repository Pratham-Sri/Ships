import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

# Point the image to a certain colour
# blank[200:300 , 300:400] = 0,255,0
# cv.imshow('Green',blank)

# # Draw a rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

# # Draw a circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)

# # Draw a line
# cv.line(blank,(100,250), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('Line',blank)

# write text
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('text',blank)

cv.waitKey(0)