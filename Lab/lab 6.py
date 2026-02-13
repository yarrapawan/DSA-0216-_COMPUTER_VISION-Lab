



import cv2

print("Choose playback mode:")
print("1 - Normal")
print("2 - Slow motion")
print("3 - Fast motion")

choice = input("Enter choice: ")

cap = cv2.VideoCapture(r"C:\Users\pawan\OneDrive\Desktop\COPUTER VISION\Lab6 Vedio.mp4") 

if choice == '1':
    delay = 30
elif choice == '2':
    delay = 120
elif choice == '3':
    delay = 1
else:
    print("Invalid choice")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video Playback", frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
