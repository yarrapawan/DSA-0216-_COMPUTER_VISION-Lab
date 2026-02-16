import cv2
img = cv2.imread("image2.jpg")
cv2.putText(img, "Pawan Yarra",
            (50,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (0,0,255), 2)
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()