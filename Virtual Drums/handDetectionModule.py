import math
import cv2
import time
import mediapipe as mp


class handDetector():
    def __init__(self, mode = False, maxHands = 2, modelComplexity = 1, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.modelComplexity = modelComplexity

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20, 25, 29, 33, 37, 41]

    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        return img

    def findPosition(self, img, handNo = 0, draw = True):
        xList = []
        yList = []
        self.lmList = []

        if self.results.multi_hand_landmarks:
            handCount = len(self.results.multi_hand_landmarks)
            id = 0
            for handNumber in range(handCount):
                myHand = self.results.multi_hand_landmarks[handNumber]
                
                for lm in myHand.landmark:
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    xList.append(cx)
                    yList.append(cy)
                    self.lmList.append([id, cx, cy])
                    id += 1
                    
        return self.lmList

    
