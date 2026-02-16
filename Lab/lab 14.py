import cv2
import numpy as np
img = cv2.imread("image1.jpg")
if img is None:
    print("Error: Could not load image. Check the file path.")
else:
    src = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    dst = np.float32([[50, 50], [250, 0], [0, 250], [300, 300]])
    
    H = cv2.findHomography(src, dst)[0]
    
    result = cv2.warpPerspective(img, H, (300, 300))
    cv2.imshow("Homography", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()