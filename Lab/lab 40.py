import cv2

# Read image
img = cv2.imread("image6.jpg")

# Draw rectangle (x1,y1) to (x2,y2)
cv2.rectangle(img,
              (100, 100),
              (300, 300),
              (0, 255, 0), 2)

# Extract object inside rectangle
crop = img[100:300, 100:300]

# Show outputs
cv2.imshow("Rectangle Drawn", img)
cv2.imshow("Extracted Object", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
