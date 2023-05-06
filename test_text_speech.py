import speech_recognition as sr
import pyttsx3
import imutils
import pickle
import time
def ttss(inpvoice):
    engine = pyttsx3.init()
    engine.setProperty("rate",130)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    print(inpvoice)
    engine.say(inpvoice)
    engine.runAndWait()
r = sr.Recognizer()
ttss("Hi   what is your name ")
with sr.Microphone() as source:
    print("Your Answer :")
    audio = r.listen(source,timeout=2,phrase_time_limit=10)
    print('Done, Please wait while we are processing what you said...')
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        ttss(str("welcome"+text))
        
    except:
        print("Sorry we could not recognize what you said. You can try again.")
        ttss("Sorry we could not recognize what you said. You can try again.")                                       
                                                
