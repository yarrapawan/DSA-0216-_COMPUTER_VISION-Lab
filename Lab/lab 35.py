import cv2
import numpy as np

# Read image
img = cv2.imread("image2.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create kernel
kernel = np.ones((9,9), np.uint8)

# Apply Black Hat
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

# Show output
cv2.imshow("Original Image", gray)
cv2.imshow("Black Hat Image", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
