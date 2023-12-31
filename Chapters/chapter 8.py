#shpe detaction

import cv2
import numpy as np

path = 'Resources/Shapes.jpg'
img = cv2.imread(path)


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgContour = img.copy()


def getContours(img):
    contours,Hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)

        if area>300:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if objCor == 5 : objectType = 'pentagone'
            else: objectType = 'None'

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,(x + (w // 2) - 10, y + (h // 2)), cv2.FONT_ITALIC, 0.5, (0, 0, 0), 2)

getContours(imgCanny)

cv2.imshow("Original",img)
cv2.imshow("imgGray",imgGray)
cv2.imshow("imgBlur",imgBlur)
cv2.imshow("imgCanny",imgCanny)
cv2.imshow("imgContour",imgContour)
cv2.waitKey(0)