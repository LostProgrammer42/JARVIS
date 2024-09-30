import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import enum
import psutil
import platform
import smtplib,ssl
import pynput
from pynput.keyboard import Key, Controller
#import timer as tm
import time
import Reminder as rm
import re
import listmaker as lm
import quickstart as qs
import addevent as ae
import timeconverter as converter



keyboard = Controller()

sys=platform.uname()

port = 465

bool; wake = False

context = ssl.create_default_context()

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',145)
#speak function allows the program to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#wishme function wishes the user as per the time
def wishme():
    # Takes the current hour using dateandtime library in 24 hour format
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    if hour>=12 and hour<16:
        speak("good afternoon sir")
    if hour>=16 and hour<20:
        speak("good evening sir")
    if hour>=20 and hour<24:
        speak("How's your night going sir?")

#takeCommand allows program to take user voice input
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=0.5
        r.energy_threshold=100
        audio=r.listen(source)
    try:
        print("Recognising.....")
        query=r.recognize_google(audio,language='en-in')
       #query=r.recognize_ibm(audio,language='en-in')
        print(f"I Heard: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again...")
        return "None"
    return query



if __name__ == "__main__":
    wishme()

    
   
  
    
    while True:

         speech=takeCommand().lower()

        
         if 'wikipedia' in speech:
            speak('Searching wikipedia')
            speech=speech.replace("wikipedia","")
            speech=speech.replace("according to","")
            if speech =="":
                speak("Empty Search Text,i think you are confused let me search for shinchan.")
                speech="shinchan"
            results=wikipedia.summary(speech,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
         elif 'open youtube' in speech:
            
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            c=webbrowser.get('chrome')
            c.open_new_tab("www.youtube.com")
         elif speech == "none":
            print("")
         elif "play music" in speech:
            music_dir="D:\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            x=random.randint(1,110)
            os.startfile(os.path.join(music_dir,songs[x])) 
            
        
         elif "search" in speech:
            speech=speech.replace("search","")
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            d=webbrowser.get('chrome')
            d.open_new_tab("https://www.google.com/search?client=firefox-b-d&q="+speech)
         elif "report" in speech:
            speak(f"System: {sys.system}")
            speak(f"Node Name: {sys.node}")
            speak(f"Release: {sys.release}")
            speak(f"Version: {sys.version}")
            speak(f"Machine: {sys.machine}")
            speak(f"Processor: {sys.processor}")
            speak(f"Battery Level: {psutil.sensors_battery().percent } percentage")
            speak(f"Charging Status: {psutil.sensors_battery().power_plugged}")
         elif "send" in speech:
            print("What is the message?")
            speak("What is the message")
            message=takeCommand().lower()
            print(f'Sending: {message}')
            if message != "none":
             with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
              server.login("dt361291@gmail.com", password)
              server.sendmail("dt361291@gmail.com","jstavan26@yahoo.com",message)
             speak("Mail send successfully")
         elif "next window" in speech:
             keyboard.press(Key.alt)
             keyboard.press(Key.tab)

             keyboard.release(Key.alt)
             keyboard.release(Key.tab)
         elif "start screen recording" in speech:
             keyboard.press(Key.cmd)
             keyboard.press(Key.alt)
             keyboard.press("r")
             keyboard.release(Key.cmd)
             keyboard.release(Key.alt)
             keyboard.release("r")
         elif "open whatsapp" in speech:
            chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            d=webbrowser.get('chrome')
            d.open_new_tab("web.whatsapp.com")
            d.open_new_tab("www.sebexam.org")
         elif "check" in speech:
            chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            d=webbrowser.get('chrome')
            d.open_new_tab("www.sebexam.org")
         elif "set timer for" in speech:
            speak("For How many seconds?")
            time=takeCommand().lower()
            # if time != "none":
            #  tm.waittime(int(time))
         elif "set reminder" in speech:
             speak("what is the reminder name?")
             x=takeCommand().lower()
             speak("what is the time in 24 hour format?")
             t=takeCommand().lower()
             t=re.sub(r"\s+","",t,flags=re.UNICODE)
             print(t)
             n=int(t)
             print(n)
             m='%0*d'%(6,n)
             rm.addreminder(x,m)
         elif "create list" in speech:
             speak("what is the list name?")
             s=takeCommand().lower()
             a=lm.listadd(s)
             speak(a)
         elif "what is in my" in speech:
             a=speech.replace("what is in my ","")
             n=a+".txt"
             print(n)
             b=os.path.isfile(n)
             if b== True:
                 list = open(n,'r')
                 elements=list.readlines()
                 for element in elements:
                     speak(element)
        
             if b== False:
                 speak("The list does not exist")
         elif "add elements to list" in speech:
             speak("What is the list name")
             g=takeCommand().lower()
             speak("What is the element name")
             h=takeCommand().lower()

             lm.elementadd(h,g)
         elif "remove elements from list" in speech:
             speak("What is the list name")
             g=takeCommand().lower()
             speak("What is the element name")
             h=takeCommand().lower()

             lm.elementremove(h,g)
         elif "sync calendar with reminder" in speech:
             qs.calendar()
         elif "add event to calendar" in speech:
             speak("What is the event name")
             eventname=takeCommand().lower()
             speak("What is the event start time")
             eventstart=takeCommand().lower()
             eventstart = converter.convert_to_24_hour(eventstart)
             eventstart = datetime.date.today().strftime('%Y-%m-%d')+"T"+eventstart[0:2]+":"+eventstart[2:4]+":"+"00"
             speak("What is the event end time")
             eventend=takeCommand().lower()
             eventend = converter.convert_to_24_hour(eventend)
             eventend = datetime.date.today().strftime('%Y-%m-%d')+"T"+eventend[0:2]+":"+eventend[2:4]+":"+"00"

             print(eventstart)
             print(eventend)

             ae.calendar(eventname,eventstart,eventend)





        

            
        
                  
        
            
                   