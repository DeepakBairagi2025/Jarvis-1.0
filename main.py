import pyttsx3
import speech_recognition 
import time 
import threading
import subprocess
import sys

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    print(f"Speaking: {audio}")
    subprocess.run([sys.executable, "speaker.py", audio])

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    time.sleep(5)
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query or "i'm fine" in query:
                    speak("That's good sir!")
                # Add more conversation rules here
                elif "search google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "search youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "search wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "exit" in query or "quit" in query:
                    speak("Goodbye sir, have a nice day!")
                    break
