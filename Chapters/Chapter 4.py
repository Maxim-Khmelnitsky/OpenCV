# chapter 4 shape and text
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# img[200:300,200:300] = 255,0,0
# cv2.line(img,(0,0),(300,300),(0,255,0),3)
# cv2.rectangle(img,(0,0),(250,300),(0,255,0),cv2.FILLED)
# cv2.line(img,(300,0),(0,300),(0,255,0),3)
cv2.putText(img,"Open CV",(50,300),cv2.FONT_HERSHEY_COMPLEX,5,(0,100,0),1)
cv2.imshow("Image",img)
cv2.waitKey(0)