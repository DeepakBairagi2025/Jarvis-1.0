import random
import pyautogui as ui
import time
from Mouth import speak
from dlg import  *
import webbrowser
import difflib


def appopen(text):
    text = text.replace("open", "")
    text = text.strip()
    random_dlg = random.choice(open_dlg)
    speak(random_dlg + text)
    ui.press("win")
    time.sleep(0.5)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")
    randomsuccess = random.choice(success_open)
    speak(randomsuccess)

def openweb(text):
    # Convert the input to lowercase for case-insensitive matching
    website_name_lower = text.lower()

    #Check if the exact name exists in the dictionary
    if website_name_lower in websites:
        random_dlg = random.choice(open_dlg)
        speak(random_dlg + text)
        url = websites[website_name_lower]
        webbrowser.open(url)
        randomsuccess = random.choice(success_open)
        speak(randomsuccess)
    else:
        # Find the closest matching website using string similarity
        matches = difflib.get_close_matches(website_name_lower, websites.keys(), n=1, cutoff=0.6)
        if matches:
            random_dlg = random.choice(open_dlg)
            randomopen2 = random.choice(open_maybe)
            closest_match = matches[0]
            speak(randomopen2 + random_dlg + text)
            url = websites[closest_match]
            webbrowser.open(url)
            randomsuccess = random.choice(success_open)
            speak(randomsuccess)
            
        else:
            randomsorry = random.choice(sorry_open)
            speak(randomsorry +" named " + text)

def open(text):
    if "website" in text or "site" in text:
        text = text.replace("open", "")
        text = text.replace("website", "")
        text = text.replace("site", "")
        text = text.strip()
        openweb(text)
    elif "app" in text or "application" in text:
        text = text.replace("open", "")
        text = text.replace("app", "")
        text = text.replace("application", "")
        text = text.strip()
        appopen(text)
    else:
        text = text.replace("open", "")
        text = text.strip()
        appopen(text)

    

#open("google website")

""" if __name__ == "__main__":
    # Example usage
    user_input = input("Enter the name of the website you want to open: ")
    openweb(user_input) """