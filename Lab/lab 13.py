import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    h, w = frame.shape[:2]
    pts1 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    pts2 = np.float32([[0,0],[w-50,50],[50,h],[w,h-50]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(frame, M, (w,h))
    cv2.imshow("Perspective Video", dst)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()