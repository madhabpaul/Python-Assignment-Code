#!/usr/bin/python3
import speech_recognition as sr 
r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)

try:
    print('You said :'+r.recognize_google(audio))
except Exception:
    print('Sorry could not recognize your voice')