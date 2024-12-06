import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(0)
while(True):
    rec , frame = cap.read()

    #convert BGR to HSV
    frame_hsv = cv.cvtColor(frame , cv.COLOR_BGR2HSV)


    #BLUE
    lower_blue = np.array([100,150,50])
    upper_blue = np.array([135,255,255])
    mask_blue = cv.inRange(frame_hsv , lower_blue , upper_blue)
    frame_masked_blue = cv.bitwise_and(frame,frame,mask=mask_blue)
#------------------------------------------------------------------------------------------------

    #GREEN
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([102, 255, 255])
    mask_green = cv.inRange(frame_hsv , lower_green , upper_green)
    frame_masked_green = cv.bitwise_and(frame,frame,mask=mask_green)
#------------------------------------------------------------------------------------------------

    #RED
    lower_red = np.array([-10, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask_red = cv.inRange(frame_hsv , lower_red , upper_red)
    frame_masked_red = cv.bitwise_and(frame,frame,mask=mask_red)
#------------------------------------------------------------------------------------------------


#show in desktap 
    cv.imshow('frame' , frame)
    cv.imshow('frame_masked_blue', frame_masked_blue)
    cv.imshow('frame_masked_green',frame_masked_green)
    cv.imshow('frame_masked_red',frame_masked_red)
    kayexit=cv.waitKey(5) 
    if kayexit==ord('q'):
        break

cv.destroyAllWindows()
cap.release()