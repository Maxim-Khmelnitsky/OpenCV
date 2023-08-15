# chapter 2
import cv2
import numpy as np
kernel = np.ones((5, 5),np.uint8)

img = cv2.imread("Resources/KEREN.jpeg")
img = cv2.resize(img,(647,440))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #change colores
imgblur = cv2.GaussianBlur(imgGray,(99,99),0)
imgcanny = cv2.Canny(img,100,120)
imgDialation = cv2.dilate(imgcanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("imgblur",imgblur)
cv2.imshow("imgGray",imgGray)
cv2.imshow("imgcanny",imgcanny)
cv2.imshow("imgDialation",imgDialation)
cv2.imshow("imgEroded",imgEroded)
cv2.waitKey(0)