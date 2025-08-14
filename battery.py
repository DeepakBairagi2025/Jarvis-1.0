import psutil
import time
from Mouth import speak
import random
from dlg import *

def battery_alert():
    while True:
        time.sleep(10)
        battery = psutil.sensors_battery()
        percent = int(battery.percent)

        if percent < 30:
            random_low = random.choice(low_b)
            speak(random_low)

        elif percent < 10:
            random_low = random.choice(last_low)
            speak(random_low)

        elif percent == 100:
            random_low = random.choice(full_battery)
            speak(random_low)
        else:
            pass

        time.sleep(1500)


def battery_persentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)

    speak(f"the device is running on {percent}% battery power")


def check_plugin_status():
    
    previous_state = psutil.sensors_battery().power_plugged

    # Only announce when the state actually changes
    while True:
        battery = psutil.sensors_battery()

        if battery.power_plugged != previous_state:
            if battery.power_plugged:
                random_low = random.choice(plug_in)
                speak(random_low)
            else:
                random_low = random.choice(plug_out)
                speak(random_low)
            previous_state = battery.power_plugged

        # Check agian after a minute
        time.sleep(5)
    
""" 
battery_alert() """
