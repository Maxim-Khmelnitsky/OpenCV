#chapter 7
import cv2
import numpy as np

def empty(a):pass

path = 'Resources/car.jpg'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue max","TrackBars",179,179,empty)
cv2.createTrackbar("set min","TrackBars",0,255,empty)
cv2.createTrackbar("set max","TrackBars",255,255,empty)
cv2.createTrackbar("val min","TrackBars",0,255,empty)
cv2.createTrackbar("val max","TrackBars",255,255,empty)


#12 ,21 , 7 ,255 , 35 ,255
while True:
    img = cv2.imread(path)
    imgResize = cv2.resize(img,(647,440))
    imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue max","TrackBars")
    sat_min = cv2.getTrackbarPos("set min","TrackBars")
    sat_max = cv2.getTrackbarPos("set max","TrackBars")
    val_min = cv2.getTrackbarPos("val min","TrackBars")
    val_max = cv2.getTrackbarPos("val max","TrackBars")

    # print(h_min,h_max,sat_min,sat_max,val_min,val_max)
    lower = np.array([h_min,sat_min,val_min])
    upper = np.array([h_max,sat_max,val_max])
    mask = cv2.inRange(imgHSV,lower ,upper)
    imgResult = cv2.bitwise_and(imgResize, imgResize, mask=mask)

    cv2.imshow("Mask", mask)
    cv2.imshow("Original",imgResize)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("imgResult", imgResult)
    cv2.waitKey(1)