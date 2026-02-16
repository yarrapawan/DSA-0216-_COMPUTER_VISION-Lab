import cv2
import numpy as np

img = cv2.imread("image2.jpg", 0)

kernel = np.array([[1,1,1],
                   [1,-8,1],
                   [1,1,1]])

lap = cv2.filter2D(img, -1, kernel)
sharp = cv2.add(img, lap)

cv2.imshow("Sharpened Diagonal", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
