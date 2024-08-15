from picamera2 import Picamera2
import cvzone
from cvzone.PoseModule import PoseDetector
import cv2
from cvzone.FPS import FPS

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={'format': 'RGB888', 'size': (480,360)}))
picam2.start()
detector = PoseDetector(staticMode=False, modelComplexity=1, smoothLandmarks=True, enableSegmentation=False, smoothSegmentation=True, detectionCon=0.5, trackCon=0.5)

while True:
    img = picam2.capture_array()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)
    
    if lmList:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (0, 255, 0), cv2.FILLED)
        length, img, info = detector.findDistance(lmList[11][0:2], lmList[15][0:2], img=img, color=(0, 255, 0), scale=10)
        angle, img = detector.findAngle(lmList[11][0:2], lmList[13][0:2], lmList[15][0:2], img=img, color=(0, 255, 0), scale=10)
        isCloseAngle50 = detector.angleCheck(myAngle=angle, targetAngle=50, offset=10)
        print(isCloseAngle50)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
