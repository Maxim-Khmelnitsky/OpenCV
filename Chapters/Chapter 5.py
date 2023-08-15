# chapter 5 selecting points in image and warping them
import numpy as np
import cv2
img = cv2.imread("cards.jfif")
width,height = 250,350
pts1 = np.float32([[934,297],[517,138],[694,852],[311,691]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)