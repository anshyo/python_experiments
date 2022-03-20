# _________________________________________all modules______________________________

from fileinput import close
from multiprocessing.connection import wait
from tokenize import Number
import pyttsx3
import datetime
import os
import pywhatkit

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
    elif hour>=12 and hour<16:
        print("good afternoon , sir")
        say("good afternoon , sir")
    else:
        print("good evening , sir")
        say("good evening , sir")

    print("This is the Assistant for linux OS only(Debain)")    
    say("This is the Assistant for linux OS only(Debain)")    
    print("I am still in development, i cant take voice but i can speak")
    say("I am still in development, i cant take voice but i can speak")

def Whatsapp():
    print('here\'s list of main contacts')
    os.system('mousepad \'Assistant/contact_list.txt\'')
    today = datetime.now()
    shour = today.strftime("%H")
    mobile_no = input("Type Number of Reciever :")
    Msg = input("Type Message to send :")
    hour = int(input("Write Hour :"))
    minute = int(input("Write Minute :"))
    pywhatkit.sendwhatmsg(mobile_no , Msg , hour , minute)



if __name__ == "__main__":
    passw()
    onStart()
    os.system('mousepad \'Assistant/functions.txt\'')
    



    