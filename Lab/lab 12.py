import cv2
import numpy as np
img = cv2.imread("image2.jpg")
pts1 = np.float32([[0,0],[300,0],[0,300],[300,300]])
pts2 = np.float32([[0,0],[250,50],[50,300],[300,250]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (300,300))
cv2.imshow("Perspective", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()