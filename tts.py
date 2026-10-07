import pyttsx3
text = input("Text to speak: ")
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
