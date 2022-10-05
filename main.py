import pyttsx3
import datetime

def sound(command):
    reader=pyttsx3.init()
    reader.say('do you know..... ? what am i trying to say to you?')
    reader.runAndWait()
