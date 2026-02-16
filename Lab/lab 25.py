import cv2
import numpy as np

img = cv2.imread("image5.jpg", 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)

grad = np.sqrt(sobelx**2 + sobely**2)
sharp = cv2.add(img, grad.astype('uint8'))

cv2.imshow("Gradient Sharpen", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
