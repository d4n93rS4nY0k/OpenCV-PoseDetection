
# OpenCV PoseDetection

The project is based on Raspberry Pi 4 and RPicameraV2

Used programming languages: Python (100%)


## Used Libraries

Necessary libraries for working with source code:

**Picamera2 0.3.18 (or newer)**
```bash
  pip install picamera2
```

**CVzone 1.6.1 (or newer)**
```bash
  pip install cvzone
```

**OpenCV 4.10.0.84 (or newer)**
```bash
  pip install opencv-python
```

Make sure that all libraries have been installed **correctly**:

Open terminal. Run commands:
```bash
  python

  import cv2

  import cvzone
```

## Picamera2 verification

Run a simple example **testopencamera.py** to see if the picamera2 works great

```python
import cv2
from picamera2 import Picamera2

cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main = {'format': 'XRGB8888', 'size': (640, 480)}))
picam2.start()

while True:
	im = picam2.capture_array()
	cv2.imshow('camera', im)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
```
## Code explanation

- **Libraries import section**
Importing: *cv2*, *cvzone* and some sub-libraries from *cvzone*.
```python
from picamera2 import Picamera2
import cvzone
from cvzone.PoseModule import PoseDetector
import cv2
from cvzone.FPS import FPS
```
- **Camera initialization**
Configuration of the camera image format and its resolution.

Camera startup and pose detection function imported from the library.
```python
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={'format': 'RGB888', 'size': (480,360)}))
picam2.start()
detector = PoseDetector(staticMode=False, modelComplexity=1, smoothLandmarks=True, enableSegmentation=False, smoothSegmentation=True, detectionCon=0.5, trackCon=0.5)
```
- **Main while True loop**
The loop captures the image and draws pose detection in the *lmList* condition.
```python
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
```



## Viewers count

![Visitor Count](https://profile-counter.glitch.me/d4n93rS4nY0k/count.svg)



## Authors

- [@d4n93rS4nY0k](https://github.com/d4n93rS4nY0k)

