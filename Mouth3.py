import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    #pitch=180
    rate=180
    volume=1
    voice_id = engine.getProperty('voices')

    if voice_id:
        voices = engine.getProperty('voices')
        try:
            engine.setProperty('voice', voices[1].id)
        except IndexError:
            print("Voice ID not found. Using the default voice.")

    # Set properties (adjust as needed)
    engine.setProperty('rate', rate) # Speed of speech
    engine.setProperty('volume', volume) # Volume (0.0 to 1.0)
   # engine.setProperty('pitch', pitch) # Pitch level (0-100)

    # Real-time speaking
    print(text)
    engine.say(text)
    engine.runAndWait()


# Speak the text with customized parameters
""" speak("Hello sir I am Jarvis and I am here to assist you.") """
