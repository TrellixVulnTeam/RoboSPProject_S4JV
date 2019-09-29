from Object_detection_image import detectObjects
from armDetection import armDetection
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import pydobot
from math import sqrt, asin, pi, degrees
from serial.tools import list_ports
from time import sleep
from pydobot import Dobot
import speech_recognition as sr
# import win32com.client as wincl
# from simpleTest import armMotor, modelInit, modelExit
# import SpeechRecognition as sr
 

def modelInit():
	pass
port = list_ports.comports()[1].device
device = Dobot(port=port, verbose=True)
modelInit()
def sendToModel():
	pass
	# arrToModel = []
	# (_, __, ___, ____, arrToModel[0], arrToModel[1], arrToModel[2], arrToModel[3]) = device.pose()
	# armMotor(arrToModel)
def findLine(a, b):
	return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def talk(words):
	# Qscvbnnbvcsq11
	# speak = wincl.Dispatch("SAPI.SpVoice")
	# speak.Speak(words)
	pass
def getInput():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		talk("Say something")
		print("Waiting voice command: ")
		audio = r.listen(source)

		try:
			text = r.recognize_google(audio)
			print(text)
			return text
		except:
			print('Couldnt recognize')
			talk('couldnt recognize please try again')
			return None
def toBox(us_obj):
	z = Z
	if us_obj == 1:
		device.suck(True)
		(x, y, zz, r, j1, j2, j3, j4) = device.pose()
		device.move_to_xyz(x, y, Z, r, wait=True)
		sendToModel()
		device.move_to(J1+180, J2, J3, J4, wait=True)
		sendToModel()
		sleep(1)
		device.suck(False)
		device.move_to(J1, J2, J3, J4, wait=True)
		sendToModel()
	elif us_obj == 2:
		device.suck(True)
		(x, y, zz, r, j1, j2, j3, j4) = device.pose()
		device.move_to_xyz(x, y, Z+15, r, wait=True)
		sendToModel()
		device.move_to(J1, J2, J3, J4, wait=True)
		sendToModel()
		sleep(1)
		(x, y, zz, r, j1, j2, j3, j4) = device.pose()
		device.move_to_xyz(x, y, zz-20, r, wait=True)
		sendToModel()
		device.suck(False)
		device.move_to(J1, J2, J3, J4, wait=True)
		sendToModel()
	elif us_obj == 3:
		device.suck(True)
		(x, y, zz, r, j1, j2, j3, j4) = device.pose()
		device.move_to_xyz(x, y, Z, r, wait=True)
		sendToModel()
		device.move_to(J1, J2+30, J3, J4, wait=True)
		sendToModel()
		sleep(1)
		device.suck(False)
		device.move_to(J1, J2, J3, J4, wait=True)
		sendToModel()

# Описание констант
(x, y, Z, RR, J1, J2, J3, J4) = device.pose()
(x, y, z, r, j1, j2, j3, j4) = device.pose()
sendToModel()
device.move_to(J1, J2, J3, J4, wait=True)
sendToModel()
op_dot_x_1, op_dot_y_1 = armDetection()
# device.move_to(J1-180, J2, J3, J4, wait=True)
# device.move_to(J1, J2, J3, J4, wait=True)
device.move_to(J1+180, J2, J3, J4, wait=True)
sendToModel()
op_dot_x_2, op_dot_y_2 = armDetection()
device.move_to(J1, J2, J3, J4, wait=True)
sendToModel()
talk("calibration completed")
obj_image, coords = detectObjects()
cv2.imshow("obj_image", obj_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
while True:
	sendToModel()
	# user_object = int(input("Choose the object:\n1)Money\n2)Bottle\n3)Convert\n4)Banana\n5)Exit::"))
	while True:
		while True:
			voiceIn = getInput()
			if voiceIn != None:
				break
		if voiceIn == "sort money":
			user_object = 1
			talk('ill do it')
			break
		if voiceIn == "sort bottles":
			user_object = 2
			talk('ill do it')
			break
		if voiceIn == "sort mail":
			user_object = 3
			talk('ill do it')
			break
		if voiceIn == "sort bananas":
			user_object = 4
			talk('ill do it')
			break
		if voiceIn == "exit":
			user_object = 5
			talk('ill do it')
			break

	if user_object == 5:
		device.move_to(J1, J2, J3, J4, wait=True)
		sendToModel()
		modelExit()
		exit()
	radius = findLine([op_dot_x_1, op_dot_y_1], [op_dot_x_2, op_dot_y_2])/2
	R = radius
	sendToModel()
	center_x = op_dot_x_2 + radius
	center_y = op_dot_y_2
	(x, y, z, r, j1, j2, j3, j4) = device.pose()
	device.move_to_xyz(x, y, Z, RR, wait=True)
	sendToModel()
	POPR = 70
	# Выбор обьекта
	# Движение на начальную позицию
	
	# obj_image = cv2.circle(obj_image, ((user_objs[i]['xmin'] + user_objs[i]['xmax'])//2, (user_objs[i]['ymin'] + user_objs[i]['ymax'])//2), 5, (0,0,0), 1)
	# obj_image = cv2.circle(obj_image, (int(center_x), int(center_y)), int(R), (0,0,0), 1)
	# Вывод изображения для отладки

	
	# Сканирование обьектов
	
	print(coords) # 1 - money 2 - bottle 3 - convert 4 - banana 
	user_objs = []
	sendToModel()
	for i in range(len(coords)):
		if coords[i]['className'] == user_object:
			user_objs.append(coords[i])

	for i in range(len(user_objs)):


		sendToModel()

		(x, y, z, r, j1, j2, j3, j4) = device.pose()
		xn, yn = (user_objs[i]['xmin'] + user_objs[i]['xmax'])/2, (user_objs[i]['ymin'] + user_objs[i]['ymax'])/2
		b_x = xn
		b_y = center_y
		b = findLine([center_x, center_y], [b_x, b_y])
		obj_dot_x = b_x
		print("----------\n\n\n\nR="+str(R)+"\nb="+str(b)+"\ncenter_x, center_y="+str(center_x), str(center_y)+"\n\n\n---------")
		print(op_dot_x_1, op_dot_y_1)
		print(op_dot_x_2, op_dot_y_2)
		obj_dot_y = b_y + sqrt(R**2 - b**2)
		xaaa, xbbb = armDetection()
		h = (findLine([op_dot_x_1, op_dot_y_1], [obj_dot_x, obj_dot_y]))/(2*R)
		alpha = 2*(asin(h))
		alpha = degrees(alpha)
		print(alpha)
		(x, y, z, r, j1, j2, j3, j4) = device.pose()
		print("---------------\n-----------------\n----------------\n-----------------\n----------\n-----------\n\n\n\n")
		# MODE_PTP_MOVJ_ANGLE
		(x, y, z, r, j1, j2, j3, j4) = device.pose()
		device.move_to(J1, J2, J3, J4, wait=True)
		sendToModel()
		(x, y, z, r, j1, j2, j3, j4) = device.pose()
		device.move_to(j1+alpha+15, j2, j3, j4, wait=True)
		sendToModel()
		try:
			while True:
				(x, y, z, r, j1, j2, j3, j4) = device.pose()
				xnnn, ynnn = armDetection()
				if xn>xnnn:
					break
				device.move_to(j1+1, j2, j3, j4, wait=True)
				sendToModel()
		except:
			device.move_to(j1+1, j2, j3, j4, wait=True)
		try:
			while True:
				(x, y, z, r, j1, j2, j3, j4) = device.pose()
				xnnn, ynnn = armDetection()
				if xn<xnnn:
					break
				device.move_to(j1-1, j2, j3, j4, wait=True)
				sendToModel()
		except:
			device.move_to(j1-1, j2, j3, j4, wait=True)
		try:
			while True:
				(x, y, z, r, j1, j2, j3, j4) = device.pose()
				xnnn, ynnn = armDetection()
				if yn-POPR>ynnn:
					break
				device.move_to(j1, j2+3, j3, j4, wait=True)
				sendToModel()
		except:
			device.move_to(j1, j2+3, j3, j4, wait=True)
		try:
			while True:
				(x, y, z, r, j1, j2, j3, j4) = device.pose()
				xnnn, ynnn = armDetection()
				if yn-POPR<ynnn:
					break
				device.move_to(j1, j2-3, j3, j4, wait=True)
				sendToModel()
		except:
			device.move_to(j1, j2-3, j3, j4, wait=True)
		# while True:
		# 	(x, y, z, r, j1, j2, j3, j4) = device.pose()
		# 	xnnn, ynnn = armDetection()
		# 	if yn>ynnn:
		# 		break
		# 	device.move_to(j1, j2, j3, j4+1, wait=True)
		# while True:
		# 	(x, y, z, r, j1, j2, j3, j4) = device.pose()
		# 	xnnn, ynnn = armDetection()
		# 	if yn<ynnn:
		# 		break
		# 	device.move_to(j1, j2, j3, j4-1, wait=True)
		if user_object == 1:
			(x, y, z, r, j1, j2, j3, j4) = device.pose()
			device.move_to_xyz(x, y, -62, r, wait=True)
			sendToModel()
			toBox(1)
		if user_object == 2:
			(x, y, z, r, j1, j2, j3, j4) = device.pose()
			device.move_to_xyz(x, y, 75, r, wait=True)
			sendToModel()
			toBox(2)
		if user_object == 3:
			(x, y, z, r, j1, j2, j3, j4) = device.pose()
			device.move_to_xyz(x, y, -71, r, wait=True)
			sendToModel()
			toBox(3)
	try:
		user_objs.pop(0)
		user_objs.pop(0)
	except:
		pass
	# Решить Пропорцию