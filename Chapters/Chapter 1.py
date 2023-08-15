#Chapter 1
import cv2
def pic():
    #how to read imeags
    img = cv2.imread("Resources/KEREN.jpeg")
    cv2.imshow("Output",img) # show you the img
    cv2.waitKey(0) #zero is inf delay else time it in milisec
    #C:\Users\maxim\PycharmProjects\OPENCV\KEREN.jpeg

# video capther
cap = cv2.VideoCapture(0) #camara input
cap.set(3,1080) # 3 is for hight
cap.set(4,480)   # 4 is for with

while True:
    success, img = cap.read()
    cv2.imshow("MAX",img)
    if cv2.waitKey(1)& 0xFF ==ord('q'):
        break






































#shpe detaction

import cv2
import numpy as np

path = 'car.jp'
img = cv2.imread(path)

cv2.imshow("Original",img)
cv2.waitKey(0)









# cv2.createTrackbar("Project","TrackBar",0,179,empty)

