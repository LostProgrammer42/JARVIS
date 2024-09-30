import time
import os
import pyttsx3 
from playsound import playsound


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',145)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


reminderfile = 'E:\Jarvis\Reminder.txt'
if __name__ == "__main__":
    while True:
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
            playsound('C:\Windows\Media\Alarm05.wav')
            speak("sir alarm for")
            speak(remindertext)
            time.sleep(1)
        
