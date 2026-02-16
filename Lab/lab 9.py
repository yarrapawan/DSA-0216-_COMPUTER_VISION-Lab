import cv2
img = cv2.imread("image5.jpg")
h, w = img.shape[:2]
M = cv2.getRotationMatrix2D((w/2, h/2), 90, 1)
N = cv2.getRotationMatrix2D((w/2, h/2), -90, 1)
cv2.imshow("Original Image", img)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Anti Clock Wise", rotated)
rotated_90 = cv2.warpAffine(img, N, (w, h))
cv2.imshow("Clock Wise", rotated_90)
cv2.waitKey(0)
cv2.destroyAllWindows()