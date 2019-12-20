#!/usr/bin/python3

'''
Below modules are required to install in the system
$ pip3 install gTTS
$ sudo apt-get install mpg321
$ pip3 install mpyg321
'''
from gtts import gTTS
import os
a=12
b=56
sum=a+b
voice_output=str(sum) 
tts = gTTS(text=voice_output, lang='en')
tts.save("voice.mp3")   #text is converted into mp3 file
os.system("mpg321 voice.mp3")  
