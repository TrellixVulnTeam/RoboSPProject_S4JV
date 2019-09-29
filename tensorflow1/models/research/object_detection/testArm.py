import speech_recognition as sr
def getInput():
	r = sr.Recognizer()

	with sr.Microphone() as source:
		print("Waiting voice command: ")
		audio = r.listen(source)

		try:
			text = r.recognize_google(audio)
			print(text)
			return text
		except:
			print('Couldnt recognize')
			return None
print(getInput())