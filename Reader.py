from asyncore import read
import pyttsx3
import time

reader=pyttsx3.init()
# reader.setProperty('rate')
reader.say('do you know..... ? what am i trying to say to you?')
reader.runAndWait()
