import cv2
import numpy as np

img = cv2.imread("image3.jpg", 0)

kernel = np.array([[0,-1,0],
                   [-1,4,-1],
                   [0,-1,0]])

lap = cv2.filter2D(img, -1, kernel)
sharp = cv2.subtract(img, lap)

cv2.imshow("Sharpened Positive", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
