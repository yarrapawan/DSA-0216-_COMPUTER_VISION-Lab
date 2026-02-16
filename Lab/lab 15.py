import cv2
import numpy as np
img = cv2.imread("image2.jpg")
src = np.float32([[0,0],[200,0],[0,200],[200,200]])
dst = np.float32([[10,100],[200,50],[100,250],[250,200]])
H, _ = cv2.findHomography(src, dst, method=0)  # DLT
output = cv2.warpPerspective(img, H, (300,300))
cv2.imshow("DLT", output)
cv2.waitKey(0)
cv2.destroyAllWindows()