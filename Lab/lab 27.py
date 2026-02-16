import cv2
img = cv2.imread("image6.jpg")
crop = img[20:100, 50:130]

img[80:160, 180:260] = crop

# Show output
cv2.imshow("Cropped & Pasted Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
