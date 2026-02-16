import cv2
import numpy as np

img = cv2.imread("image1.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.uint8)

closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original Image", gray)
cv2.imshow("Closing Image", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
