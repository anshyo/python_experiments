from asyncore import read
import pyttsx3

reader=pyttsx3.init()
reader.setProperty('rate' , 10)
reader.say('do you know..... ?')
reader.runAndWait()
