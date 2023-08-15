import cv2 as cv

cap = cv.VideoCapture(0)
pertraind_model = cv.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
while True:
    bool ,frame = cap.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    coordinate_list = pertraind_model.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    for (x,y,w,h) in coordinate_list:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv.imshow("Res",frame)
        if cv.waitKey(20) == ord('x'):
            break
cap.release()
cv.destroyAllWindows()