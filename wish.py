from datetime import date
import datetime
from Mouth import speak
from dlg import *
import random

today = date.today()
formated_date = today.strftime("%d %b %y")
now = datetime.datetime.now()


def wish():
    current_hour = now.hour
    if 5 <= current_hour < 12:
        gm_dlg = random.choice(good_morningdlg)
        speak(gm_dlg)
    elif 12 <= current_hour < 18:
        ga_dlg = random.choice(good_afternoondlg)
        speak(ga_dlg)
    elif 18 <= current_hour < 21:
        ge_dlg = random.choice(good_eveningdlg)
        speak(ge_dlg)
    else:
        gn_dlg = random.choice(good_nightdlg)
        speak(gn_dlg)

    # You can add more personalized wishes here
    # For example: you might check if it's a special day or if the user has a specific task for the day

# Only call wish() when this file is run directly
""" if __name__ == "__main__":
    wish() """