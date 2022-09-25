import pywhatkit
import pyttsx3


def say(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[10].id)
    engine.say(audio)
    engine.runAndWait()

pywhatkit.info("hgKElc" , lines=5)

# say(info)
