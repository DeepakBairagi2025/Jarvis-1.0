import random
import pyautogui as ui
import time
from Mouth import speak
from dlg import open_dlg

random_dlg = random.choice(open_dlg)

def appopen(text):
    text = text.replace("open", "")
    text = text.strip()
    speak(random_dlg+text)
    ui.press("win")
    time.sleep(0.5)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")

appopen("open explorer")