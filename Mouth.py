import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless") # Run in headless mode (without opening a browser window)

# Specify the path to your Chrome driver executable
chrome_driver_path = r'D:\Jarvis\chromedriver.exe'

# Create a Service object with the specified executable path
chrome_service = Service(chrome_driver_path)

# Create a Chrome driver instance with the specified options and service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the website
driver.get("https://tts.5e7en.me/")

def speak(text):

    # Navigate to the website
    driver.get("https://tts.5e7en.me/")
    # Wait for the element to be clickable
    element_to_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='text']"))
    )

    # Perform the click action
    element_to_click.click()

    # Input text into the element
    text_to_input = text
    element_to_click.send_keys(text_to_input)
    print(text_to_input)

    # Calculate sleep duration based on sentence length
    sleep_duration = min(0.5 + len(text) // 10, 10) # Minimum sleep in 3 seconds, maximum is 10 seconds

    # Wait for the button to be clickable
    button_to_click = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='button']"))
    )

    # Perform the click action
    button_to_click.click()

    # Sleep fir dynamically calculated duration
    time.sleep(sleep_duration)

    # Clear the text box for the next sentence
    element_to_click.clear()

# Set up Chrome options to run it the background


# Example usage with different length sentences

speak("Hello")
speak("This is a longer sentence.")
speak("This is an even longer sentence that exceeds the previous condition.")

# Remember to close the driver when done
driver.quit()





""" import asyncio
import threading
import time
import os

from play_file import play_audio
from remove_file import remove_file
from make_voice import amain

VOICE = "en-AU-WilliamNeural"
BuFFER_SIZE = 1024

def speak(TEXT, output_file=None):

    # Give each file a uniue name to avoid locks
    if output_file is None:
        ts = int(time.time() * 1000)
        output_file = f"{os.getcwd()}/speak_{ts}.mp3"
        print(TEXT)
    # Generate TTS file
    asyncio.run(amain(TEXT, output_file))

    # Play audio with proper synchronization
    thread_audio = threading.Thread(target=play_audio, args=(output_file,))
    thread_audio.start()
    thread_audio.join()
    
    # Reduced delay for faster performance
    time.sleep(0.2)
    remove_file(output_file)

    # Aslo remove any stray speak.mp3 left by amain/play
    legacy = os.path.join(os.getcwd(), "speak.mp3")
    if os.path.isfile(legacy):
        remove_file(legacy) """
""" 
speak("and i am, iron, man") """

# Removed old speak function that used threading to call speak1

# Example run
# speak("Hello i am now advance")

#SECOND ORIGINAL CODE
"""
import asyncio
import threading
import time
import os
from play_file import play_audio
from remove_file import *
from make_voice import *

VOICE = "en-AU-WilliamNeural"
BuFFER_SIZE = 1024

def speak(TEXT, output_file=None):

    # Give each file a uniue name to avoid locks
    if output_file is None:
        output_file = f"{os.getcwd()}/speak.mp3"
        print(TEXT)
    asyncio.run(amain(TEXT, output_file))

    # Play audio with proper synchronization
    thread_audio = threading.Thread(target=play_audio, args=(output_file,))
    thread_audio.start()
    thread_audio.join()
    
    # Add delay before file removal
    time.sleep(0.5)
    remove_file(output_file)
"""







#original code is below

""" import asyncio
import threading
import os
import edge_tts
import pygame
import sys
import time

VOICE = "en-AU-WilliamNeural"
BuFFER_SIZE = 1024

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07)  # Adjust the speed of animation
    print()  # New line after the message

def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            with open(file_path, 'wb'):
                pass
            os.remove(file_path)
            break
        except Exception as e:
            print(f"Error : {e}")
            attempts +=1

async def amain(TEXT, output_file) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT, VOICE)
        await cm_txt.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()
    except Exception as e:
            print(f"Error : {e}")
    finally:
        remove_file(output_file)

def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.wait(10)
        pygame.quit()

    except Exception as e:
            print(f"Error : {e}")
            

def speak1(TEXT, output_file=None):
     if output_file is None:
          output_file = f"{os.getcwd()}/speak.mp3"
          asyncio.run(amain(TEXT, output_file))

def speak(text):
    t1 = threading.Thread(target=speak1, args=(text,))
    t2 = threading.Thread(target=print_animated_message, args=(text,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

speak("Hello i am now advance") """