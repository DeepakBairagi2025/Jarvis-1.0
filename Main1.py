import threading
from Ear import *
from check_online_offline import is_online
from Fspeak import fspeak
from random_advice import get_random_advice
from command import cmd
from battery import *

    
def advice():
    while True:
        x = [600, 550, 580, 400, 3000, 800, 700, 8200, 8000, 50, 568]
        x = random.choice(x)
        time.sleep(x)
        speak("I have some suggestion for you, sir")
        text = listen().lower()
        if "yes tell me " in text or "yes" in text:
            advice = get_random_advice()
            speak(advice)
        else:
            speak("no problem, i think you need some advice so i give")

def jarvis():
    t1 = threading.Thread(target=cmd)
    t2 = threading.Thread(target=advice)
    t3 = threading.Thread(target=battery_alert)
    t4 = threading.Thread(target=check_plugin_status)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

def check_jarvis():
    if is_online():
        """ x = random.choice(online_dlg)
        fspeak(x) """
        jarvis()
    else:
        x = random.choice(offline_dlg)
        fspeak(x)

check_jarvis()
