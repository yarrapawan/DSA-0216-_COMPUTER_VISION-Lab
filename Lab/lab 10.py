import cv2
import numpy as np
img = cv2.imread("image4.jpg")
M = np.float32([[1, 0, 100], [0, 1, 50]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()