import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from smtplib import SMTPException

engine = pyttsx3.init('sapi5') #inbuilt windows voice
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id) #it will uses 0 voice, there are differnt voices


def speak(audio):
    engine.say(audio)   #it will speak audio
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening Chandu!")  

    speak("I am Chandrakant Sir. Please tell me how may I help you")       

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     # print("Chandu")
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1 #gap to speak nextt word
#         # r.energy_threshold = 300 #for noice dont need to write here
#         audio = r.listen(source) #je kahi bolu te store krel

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         #query = r.recognize_google_cloud(audio, language='en-in') #en-in = english india
#         print(f"User said: {query}\n")

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")  
#         return "None"
#     return query

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    # print("Chandu")
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jarecs6788@gmail.com', '6788446')
    server.sendmail('jarecs6788@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    f = open("test.txt",'a+')
    # wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #je kahi bolu te lower case madhe conert hoil

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "") #query madhla wikipedia " " ne replace hoil
            results = wikipedia.summary(query, sentences=2)#ithe wikipedia query madhe je kay asel te 2 sentece send krel.
            speak("According to Wikipedia")
            print("According to Wikipedia:  ")
            print(results)
            # speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'moodle' in query:
            webbrowser.open("moodle.coep.org.in")
        elif 'portal' in query:
            webbrowser.open("portal.coep.org.in")

        elif 'coep' in query:
            webbrowser.open("coep.org.in")   


        elif 'play music' in query:
            music_dir = 'E:\music'
            songs = os.listdir(music_dir) #songs chya list madhe sagle store hotil
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0])) #index 0 che song play hoil

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'code' in query:
            codePath = "C:\\Users\\Chandrakant\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif 'email' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "chandrakantjare6788@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend Chandrakant bhai. I am not able to send this email")



        elif 'email' in query:
            try:
                speak("Please tell the name of receiver?")
                content = takeCommand()
                if content == 'vaibhavi':
                    to = "ghumarevs19.comp@coep.ac.in"
                    print("user said: ", content)
                elif content == "siddhesh":
                    to = "khadakesj19.comp@coep.ac.in"
                    print("user said: ", content)
                elif content == "abhishek":
                    to = "raiav19.comp@coep.ac.in"
                    print("user said: ", content)
                elif content == "kajal":
                    to = "kumbharkarkn19.comp@coep.ac.in"
                    print("user said: ", content)
                elif content == "prajwal":
                    to = "datirpr18.comp@coep.ac.in"
                    print("user said: ", content)
                else:
                    to = "vishaljare11@gmail.com"
                    print("user said: ", content)

                # to = "chandrakantjare6788@gmail.com"
                speak("Please tell what data which you want to sent?")
                print("Please tell what data which you want to sent?")
                content = takeCommand()    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Chandrakant bhai. I am not able to send this email")


        elif 'file' in query:
            r = sr.Recognizer()
            
            with sr.Microphone() as source:
                print("Listening for write into the file...")
                r.pause_threshold = 1 #1 sec cha gap
                audio = r.listen(source)

            try:
                print("Recognizing...")    
                query = r.recognize_google(audio, language='en-in')
                f.write(query)
                print(f"Wrie into file data as: {query}\n")

            except Exception as e:   
                print("Say that again please...")  
               

        elif 'quit' in query:
            speak("quit")
            break  
