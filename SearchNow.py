import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    print(f"Speaking: {audio}")
    subprocess.run([sys.executable, "speaker.py", audio])

def searchGoogle(query):
    if "google" in query:
        query = query.replace("google", "search")
    query = query.replace("jarvis", "")
    query = query.replace("google", "")
    speak("This is what I found on Google")
    #speak("Searching Google for " + query)

    try:
        pywhatkit.search(query)
        results = googleScrap.summary(query,1)
        speak
        
    except:
        speak("Noe speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        query = query.replace("youtube", "")
        query = query.replace("youtube search", "")
        query = query.replace("jarvis", "")
        speak("This is what I found on YouTube")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")
        try:
            pywhatkit.playonyt(query)
        except:
            speak("No speakable output available")

def searchWikipedia(query):
    if "wikipedia" in query:
        query = query.replace("wikipedia", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("jarvis", "")
        speak("Searching From Wikipedia....")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        try:
            results = wikipedia.summary(query, 1)
            speak(results)
        except:
            speak("No speakable output available")