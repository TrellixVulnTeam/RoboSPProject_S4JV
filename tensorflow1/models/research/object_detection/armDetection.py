import cv2
import numpy as np

def armDetection():
	def nothing(x):
		pass
	cap = cv2.VideoCapture(1)
	while True:
		_, frame = cap.read()

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		l_b = np.array([123, 60, 200])
		u_b = np.array([255, 255, 255])


		mask = cv2.inRange(hsv, l_b, u_b)
		
		moments = cv2.moments(mask, 1)
		dM01 = moments['m01']
		dM10 = moments['m10']
		dArea = moments['m00']

		if dArea > 100:
			x = int(dM10 / dArea)
			y = int(dM01 / dArea)
		return x, y
	
	cap.release()
	cv2.destroyAllWindows()
