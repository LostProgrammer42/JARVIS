import time
import os
import pyttsx3 
reminderfile = 'D:\Jarvis\Reminder.txt'
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',145)
#speak function allows the program to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def checkreminders():
    filename=open(reminderfile,'r')
    today=time.strftime('%H%M%S')
    flag=0
    for line in filename:
        if today in line:
            line = line.split(',')
            flag=1
            for i in range(len(line)):
                if i !=0:
                    remindertext = str(line[i])
            print(remindertext)
            speak(remindertext)
            time.sleep(1)
            
def addreminder(x,t):
    filename=open(reminderfile,'a')
    reminder=f'{t},{x}'
    filename.write("{}\n".format(reminder))
