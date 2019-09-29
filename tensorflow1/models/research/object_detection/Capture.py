import cv2

cap = cv2.VideoCapture(1)


_, frame = cap.read()
if cap.isOpened():
	cv2.imwrite('teeest.jpg', frame)


cap.release()