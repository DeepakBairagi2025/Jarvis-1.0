import pywhatkit
from Mouth import speak
from dlg import *
import random

def search_google(text):
    dlg = random.choice(search_result)
    pywhatkit.search(text)
    speak(dlg)

""" search_google("nethytech") """