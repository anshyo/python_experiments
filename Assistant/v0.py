# _________________________________________all modules______________________________

from fileinput import close
from multiprocessing.connection import wait
import pyttsx3
import time
import datetime
import os

def say(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[10].id)
    engine.say(audio)
    engine.runAndWait()

def passw():
    print("password?")
    say("password?")
    a=input().lower()
    if a=="ansh":
        pass
    else:
        passw()

def onStart():
    """
        tells us what to say on start
    """
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("good morning , sir")
        say("good morning , sir")
    if hour>=12 and hour<4:
        print("good afternoon , sir")
        say("good afternoon , sir")
    else:
        print("good evening , sir")
        say("good evening , sir")
        
    print("I am still in development, i cant take voice but i can speak")
    say("I am still in development, i cant take voice but i can speak")


if __name__ == "__main__":
    passw()
    onStart()


    