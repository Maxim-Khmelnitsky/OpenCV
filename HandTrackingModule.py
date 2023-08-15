import cv2
import mediapipe as mp
import time
import math

class handDetector:
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.drawing_utils = mp.solutions.drawing_utils
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,1,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.pTime = 0

    def findHands(self, img, draw=True,fps=True,markedFingers=[]):
        ''''
        findHands help to see how to model works
            draw = True/False draws all 20 points and connected by line
        '''
        frame_height, frame_width, _ = img.shape
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        hands = results.multi_hand_landmarks
        if hands:
            for hand in hands:
                self.drawing_utils.draw_landmarks(img, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id in markedFingers:
                        cv2.circle(img=img, center=(x, y), radius=10, color=(0, 255, 255))
                if draw:
                    self.mpDraw.draw_landmarks(img, hand,
                                               self.mpHands.HAND_CONNECTIONS)

        if fps:
            cTime = time.time()
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        return img

    def findPosision(self,img,handNumber=0,draw=False):
        lmList = []
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNumber]
            for id,lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
        return lmList

    def findDistance(self, p1, p2, img,draw=False):
        lmList = self.findPosision(img)
        length=0
        if len(lmList)!=0:
            x1, y1 = lmList[p1][1:]
            x2, y2 = lmList[p2][1:]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            length = math.hypot(x2 - x1, y2 - y1)
            if draw:
                cv2.putText(img, str(int(length)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        return img,length
    # def sign(self,img):
    #     if self.findDistance(16,20)[1]<10 and self.findDistance(4,20)[1+ ]<10:
    #         return True






