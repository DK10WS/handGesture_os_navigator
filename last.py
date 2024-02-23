import cv2
import mediapipe as mp
import time

def camera():
    mp_draw = mp.solutions.drawing_utils
    mp_hand = mp.solutions.hands
    tipIds = [4, 8, 12, 16, 20]

    previousTime=0
    video = cv2.VideoCapture(0)

    with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while True:
            ret, image = video.read()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            lmList = []
            currentTime=time.time()
            
            FPS= 1/ (currentTime - previousTime)
            cv2.putText(image ,f" FPS ={int(FPS)} ", (0,30),cv2.FONT_HERSHEY_TRIPLEX, 1 ,(255,0,0) , 2) # image, FPS , postion on the window , font , size , colour , thickness
            previousTime=currentTime
    

            if results.multi_hand_landmarks:
                for hand_landmark in results.multi_hand_landmarks:
                    myHands = results.multi_hand_landmarks[0]
                    for id, lm in enumerate(myHands.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                    mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
            fingers = []
            if len(lmList) != 0:
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1, 5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                total = fingers.count(1)

                if total == 0:
                    cv2.putText(image, "No Fingers", (470, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                elif total == 1:
                    cv2.putText(image, "1 Finger", (470, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                elif total == 2:
                    cv2.putText(image, "2 Fingers", (470, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                elif total == 3:
                    cv2.putText(image, "3 Fingers", (470, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                elif total == 4:
                    cv2.putText(image, "4 Fingers", (470, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

                elif total == 5:
                    cv2.putText(image, "5 Fingers", (470, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            cv2.imshow("kys", image)
            k = cv2.waitKey(1)
            if k == ord('q') or k==-1:
                break
    video.release()
    cv2.destroyAllWindows()
    return total

