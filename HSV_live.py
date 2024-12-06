import cv2 as cv
import numpy as np

Winname = "Frame:"

def nothing(x):
    pass

cv.namedWindow('Frame:')
# H, S,V are for Lower Boundaries
#H2,S2,V2 are for Upper Boundaries
cv.createTrackbar('H_min',Winname,0,255,nothing)
cv.createTrackbar('S_min',Winname,0,255,nothing)
cv.createTrackbar('V_min',Winname,0,255,nothing)
cv.createTrackbar('H_max',Winname,0,255,nothing)
cv.createTrackbar('S_max',Winname,0,255,nothing)
cv.createTrackbar('V_max',Winname,0,255,nothing)


cap = cv.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    H = cv.getTrackbarPos('H_min', 'Frame:')
    S = cv.getTrackbarPos('S_min', 'Frame:')
    V = cv.getTrackbarPos('V_min', 'Frame:')
    H2 = cv.getTrackbarPos('H_max', 'Frame:')
    S2 = cv.getTrackbarPos('S_max', 'Frame:')
    V2 = cv.getTrackbarPos('V_max', 'Frame:')
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_boundary = np.array([H, S, V])
    upper_boundary = np.array([H2,S2,V2])
    mask = cv.inRange(hsv, lower_boundary, upper_boundary)
    final = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow("Frame:", final)

    if cv.waitKey(1) == ord('q'): break

cap.release()
cv.destroyAllWindows()