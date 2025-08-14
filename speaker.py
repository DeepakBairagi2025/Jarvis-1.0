import sys
import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init("sapi5")
    engine.setProperty("voice", engine.getProperty("voices")[0].id)
    engine.setProperty("rate", 170)
    text = " ".join(sys.argv[1:])
    engine.say(text)
    engine.runAndWait()