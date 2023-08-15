# chapter 3 Cropping & resizing images
import cv2
import numpy

img = cv2.imread("Resources/KEREN.jpeg")
imgResize = cv2.resize(img,(400,450))
print(img.shape)
imgCropped = img[0:533,100:1000]
# OG_shape = img.shape
# cv2.imshow("Img",img)
cv2.imshow("imgResize",imgResize)
cv2.imshow("imgCropped",imgCropped)

cv2.waitKey(0)