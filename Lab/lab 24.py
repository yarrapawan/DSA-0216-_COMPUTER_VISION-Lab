import cv2

img = cv2.imread("image5.jpg")
blur = cv2.GaussianBlur(img, (5,5), 0)

mask = cv2.subtract(img, blur)
sharp = cv2.addWeighted(img, 1.5, mask, 1, 0)

cv2.imshow("High Boost", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
