import asyncio
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
    
    # Add delay before file removal
    time.sleep(0.5)
    remove_file(output_file)

    # Aslo remove any stray speak.mp3 left by amain/play
    legacy = os.path.join(os.getcwd(), "speak.mp3")
    if os.path.isfile(legacy):
        remove_file(legacy)
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