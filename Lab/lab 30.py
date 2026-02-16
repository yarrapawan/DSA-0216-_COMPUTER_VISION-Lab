import cv2
import numpy as np

img = cv2.imread("image3.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.uint8)

dilated = cv2.dilate(gray, kernel, iterations=1)

cv2.imshow("Original Image", gray)
cv2.imshow("Dilated Image", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
