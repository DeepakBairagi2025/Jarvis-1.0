import asyncio
import threading
import edge_tts
import pygame
from remove_file import remove_file
from make_voice import amain

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
        # Check if the error is related to the inability to connect to the host
        if "Cannot connect to host" in str(e) and "getaddrinfo failed" in str(e):
            print("Internet is not avaiable. Ignoring the error.")
        else:
            # If ot's a different error, print the error message
            pass