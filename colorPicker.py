import cv2
import numpy as np

framewidth = 640
framehight = 480

cap = cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,framehight)
cap.set(10,150)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("Hue min","HSV",0,179,empty)
cv2.createTrackbar("sat min","HSV",0,255,empty)
cv2.createTrackbar("val min","HSV",0,255,empty)
cv2.createTrackbar("Hue max","HSV",179,179,empty)
cv2.createTrackbar("sat max","HSV",255,255,empty)
cv2.createTrackbar("val max","HSV",255,255,empty)
while True:
    _, img = cap.read()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "HSV")
    h_max = cv2.getTrackbarPos("Hue max", "HSV")
    sat_min = cv2.getTrackbarPos("sat min", "HSV")
    sat_max = cv2.getTrackbarPos("sat max", "HSV")
    val_min = cv2.getTrackbarPos("val min", "HSV")
    val_max = cv2.getTrackbarPos("val max", "HSV")

    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    Result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img,mask,Result])
    cv2.imshow('Horizotal stacking',hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()