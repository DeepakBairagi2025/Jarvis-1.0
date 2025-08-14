import random
import psutil
import time
from Model import mind
from model2 import get_response
from wish import wish
from welcome import welcome
from open import open
from close import close
from Ear import *
from dlg import *
from Mouth import speak
import pyautogui as gui
import webbrowser
from battery import *

def cmd():
    wish()

    # announce once, immediately after your greeting
    plugged = psutil.sensors_battery().power_plugged
    if plugged:
        speak(random.choice(plug_in))
    else:
        speak(random.choice(plug_out))

    while True:
        text = listen().lower()
        if text in wake_key_word:
            welcome()
        elif text in bye_key_word:
            res_random = random.choice(res_bye)
            speak(res_random)
            break
        elif text.startswith(("jarvis","buddy","jar")):
            text = text.replace("jarvis", "")
            text = text.replace("vis", "")
            text = text.replace("buddy", "")
            text = text.replace("jar", "")
            text = text.strip()
            text= mind(text)
            speak(text)
        elif text.endswith(("jarvis","buddy","jar")):
            text = text.replace("jarvis", "")
            text = text.replace("vis", "")
            text = text.replace("buddy", "")
            text = text.replace("jar", "")
            text = text.strip()
            text= mind(text)
            speak(text)

        elif "jarvis" in text or "jar" in text or "jarvis " in text:
            response = get_response(text)
            speak(response)

        elif text.startswith(("open", "kholo", "show me")):
            text = text.replace("kholo", "")
            text = text.replace("show me", "")
            text = text.replace("open", "")
            text = text.strip()
            open(text)

        elif text in open_input:
            text = text.replace("big", "")
            text = text.replace("khologe", "")
            text = text.replace("kholo", "")
            text = text.strip()
            open(text)

        elif text in close_input:
            close()

        elif "check battery persent" in text or "check battery persentage" in text or "battery kitni hai" in text:
            battery_persentage()

        elif "write" in text or "likho" in text or "right" in text:
            speak("writing..")
            text = text.replace("write", "").replace("likho", "").replace("right", "")
            gui.write(text)

        elif "enter" in text or "press enter" in text or "send" in text:
            gui.press("enter")
        
        elif "select all" in text or "select all paragraph" in text:
            gui.hotkey("ctrl", "a")
        
        elif "copy" in text or "cpoy this" in text:
            gui.hotkey("ctrl", "c")
        
        elif "paste" in text or "paste here" in text:
            gui.hotkey("ctrl", "v")
            
        elif "undo" in text or "undo karo" in text:
            gui.hotkey("ctrl", "z")
            
        elif "copy last paragraph" in text:
            gui.hotkey("ctrl", "shift", "c")
            
        elif "increase volume" in text or "volume badhao" in text:
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            speak("Volume increased.")
            print("Volume increased.")
            
        elif "decrease volume" in text or "volume kam karo" in text:
            gui.press("volumedown")
            gui.press("volumedown")
            gui.press("volumedown")
            gui.press("volumedown")
            gui.press("volumedown")
            speak("Volume decreased.")
            print("Volume decreased.")
                
        elif "full volume" in text or "full volume kar do" in text or "volume full kar do" in text or "volume full kr do" in text:
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            gui.press("volumeup")
            speak("now your system in full volume")
            print("now your system in full volume")

        elif "mute" in text or "mute karo" in text or "mute the volume" in text or "volume mute karo" in text:
            gui.press("volumemute")
            print("Volume muted.")

        elif "unmute" in text or "unmute karo" in text or "unmute the volume" in text or "volume unmute karo" in text:
            gui.press("volumemute")
            print("Volume unmuted.")

        elif "visit" in text:
            Nameofweb = text.replace("visit ", "")
            speak(f"visiting {Nameofweb}")
            Link = f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)

        elif "lanuch" in text:
            Nameofweb = text.replace("launch ", "")
            speak(f"launching {Nameofweb}")
            Link = f"https://www.{Nameofweb}.com"
            webbrowser.open(Link)

        elif "play" in text or "pause" in text or "stop" in text:
            gui.hotkey("space")

        elif text.startswith("search"):
            gui.hotkey("/")
            text = text.replace("search", "")
            gui.write(text)
            speak(f"searching {text}")
            print(f"searching {text}")
            time.sleep(1)
            gui.press("enter")
        
        elif "minimise" in text or "minimise the window" in text or "minimize karo" in text:
            speak("minimizing..")
            gui.hotkey('win', 'down')
            gui.hotkey('win', 'down')

        elif "maximize" in text or "maximize the window" in text or "maximize karo" in text:
            speak("maximizing..")
            gui.hotkey('win', 'up')
            gui.hotkey('win', 'up')

        elif "restore window" in text:
            speak("Restoring Window")
            gui.hotkey("win", "shift", "up")

        elif "switch window" in text or "next window" in text:
            speak("Switching to Next Window")
            gui.hotkey("alt", "tab")

        elif "previous window" in text or "back window" in text:
            speak("Switching to Previous Window.")
            gui.hotkey("alt", "shift", "tab")
        
        elif "new window" in text or "open new window" in text:
            speak("Opening New Window")
            gui.hotkey("ctrl", "n")

        elif "close window" in text:
            speak("Closing Window")
            gui.hotkey("alt", "f4")

        elif "open incognito" in text or "private window" in text or "open private window" in text:
            speak("Opening Incognito Window.")
            gui.hotkey("ctrl", "shift", "n")

        elif "bookmark page" in text or "save page" in text:
            speak("Bookmarking Page.")
            gui.hotkey("ctrl", "d")

        elif "go to history" in text or "browse history" in text:
            speak("Opening Browsing History.")
            gui.hotkey("ctrl", "h")

        elif "downloads" in text or "download history" in text:
            speak("Oening Download History.")
            gui.hotkey("ctrl", "j")

        elif "inspect element" in text or "open developer tools" in text:
            speak("Opening Developer Tools.")
            gui.hotkey("ctrl", "shift", "i")

        elif "clear cookies" in text or "delete cookies" in text:
            speak("CLearing Cookies.")
            gui.hotkey("ctrl", "shift", "del")

        elif "fullscreen" in text or "full screen" in text:
            speak("Entering Fullscreen Mode.")
            gui.hotkey("f11")

        elif "toggle dark mode" in text or "dark theme" in text:
            speak("Toggling Dark Mode.")
            gui.hotkey("ctrl", "shift", "e")

        elif "mute tab" in text:
            speak("Muting Tab.")
            gui.hotkey("ctrl", "m")

        elif "unmute tab" in text:
            speak("Unmuting Tab.")
            gui.hotkey("ctrl", "shift", "m")

        elif "open extensions" in text or "manage extensions" in text:
            speak("Opening Extensions.")
            gui.hotkey("ctrl", "shift", "a")

        elif "open settings" in text or "browser settings" in text:
            speak("Opening Settings.")
            gui.hotkey("ctrl", ",")

        elif "save page as" in text or "save as" in text:
            speak("Saving Page As.")
            gui.hotkey("ctrl", "s")

        elif "print page" in text or "print the page" in text:
            speak("Printing Page.")
            gui.hotkey("ctrl", "p")

        elif "clear browsing data" in text or "clear history" in text:
            speak("Cleaning Browsing Data.")
            gui.hotkey("ctrl", "shift", "del")

        elif "open bookmarks" in text or "view bookmarks" in text:
            speak("Opening Bookmarks.")
            gui.hotkey("ctrl", "b")

        elif "reload page" in text or "refresh page" in text:
            speak("Reloading Page.")
            gui.hotkey("ctrl", "r")

        elif "go back" in text or "back" in text:
            speak("Going Back.")
            gui.hotkey("alt", "left")

        elif "go forward" in text or "forward" in text:
            speak("Going Forward.")
            gui.hotkey("alt", "right")

        elif "stop loading" in text or "stop" in text:
            speak("Stopping Page Load.")
            gui.hotkey("esc")

        elif "scroll up" in text or "scroll down" in text or "niche jaayo" in text:
            speak("Scrolling Page.")
            gui.scroll(3)

        elif "scroll down" in text or "scroll page down" in text or "upar jaayo" in text:
            speak("Scrolling Down.")
            gui.scroll(-3)

        elif "scroll to top" in text:
            speak("Scrolling to Top.")
            gui.press("home")

        elif "scroll to bottom" in text:
            speak("Scrolling to Bottom.")
            gui.press("end")

        elif "open new tab" in text or "new tab" in text:
            speak("Opening New Tab.")
            gui.hotkey("ctrl", "t")

        elif "reopen last tab" in text or "reopen closed tab" in text:
            speak("Reopening Last Closed Tab.")
            gui.hotkey("ctrl", "shift", "t")

        elif "open notification center" in text or "show notification" in text:
            speak("Showing Action Center.")
            gui.hotkey("win", "a")

        elif "lock screen" in text or "lock computer" in text:
            speak("Locking Screen.")
            gui.hotkey("win", "l")

        elif "shutdown" in text or "shutdown the computer" in text:
            speak("Shutting Down Computer.")
            gui.hotkey("win", "d")
            time.sleep(1)
            gui.hotkey("alt", "f4")
            time.sleep(1)
            gui.press("enter")

        elif "restart" in text or "restart the computer" in text:
            speak("Restarting Computer.")
            gui.hotkey("win", "d")
            time.sleep(1)
            gui.hotkey("alt", "f4")
            time.sleep(0.5)
            gui.press("down")
            time.sleep(0.5)
            gui.press("enter")

        elif "sleep" in text or "put computer to sleep" in text:
            speak("Putting Computer to Sleep.")
            gui.hotkey("win", "d")
            time.sleep(1)
            gui.hotkey("alt", "f4")
            time.sleep(0.5)
            gui.press("up")
            time.sleep(0.5)
            gui.press("enter")

        elif "open file explorer" in text or "file explorer" in text:
            speak("Opening File Explorer.")
            gui.hotkey("win", "e")

        else:
            pass