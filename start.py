import os
import speech_recognition as sr
import nltk
from Speak import Say

def Listen():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"You Said : {query}")

    except:
        return ""

    query = str(query)
    return query.lower()

while True:
    wake_up = Listen()
    
    if "wake up" in wake_up:
        os.startfile('C:\\Users\\joel\\jarvis\\Jarvis.py')
    
    else:
        print("listening...")
