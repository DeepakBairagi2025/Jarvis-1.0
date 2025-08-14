from Mouth import speak
from dlg import *
import random

def welcome():
    welcome = random.choice(welcome_dlg)
    speak(welcome)