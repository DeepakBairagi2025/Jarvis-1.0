import pyautogui as ui
import random
from Mouth import speak
from dlg import *

closedlg_random = random.choice(closedlg)

def close():
    speak(closedlg_random)
    ui.hotkey("alt","f4")