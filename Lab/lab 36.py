import cv2

# Read image
img = cv2.imread("watch.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges,
                               cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Filter only watch-like size
    if 50 < w < 200 and 50 < h < 200:
        # Also restrict to lower-right region (hand area)
        if x > img.shape[1]//2 and y > img.shape[0]//2:
            
            cv2.rectangle(img, (x,y),
                          (x+w, y+h),
                          (0,255,0), 2)
            
            cv2.putText(img, "Watch",
                        (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0,255,0), 2)

# Show output
cv2.imshow("Watch Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
