import cv2
import numpy as np

# Read image
img = cv2.imread("image1.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create kernel
kernel = np.ones((9,9), np.uint8)

# Apply Top Hat
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

# Show output
cv2.imshow("Original Image", gray)
cv2.imshow("Top Hat Image", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
