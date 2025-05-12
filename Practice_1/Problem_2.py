# Problem 2: Text to Speech
# import pyttsx3 from the library pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.say("How are you doing today?")
engine.runAndWait()