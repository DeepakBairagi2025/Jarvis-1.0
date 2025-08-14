import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, Style, init
import time

init(autoreset=True)

# Define wake and bye keywords if they're not defined in dlg.py
try:
    from dlg import wake_key_word, bye_key_word
except ImportError:
    print(Fore.YELLOW + "Warning: wake_key_word or bye_key_word not found in dlg.py. Using defaults." + Style.RESET_ALL)
    # Default wake keywords
    wake_key_word = [
        "wake up", "hey jarvis", "hello jarvis", "ok jarvis", "jarvis", 
        "are you there", "you there", "buddy", "hey buddy"
    ]
    # Default bye keywords
    bye_key_word = [
        "bye", "goodbye", "exit", "quit", "shutdown", "sleep", "go to sleep",
        "good night", "see you later", "bye jarvis", "goodbye jarvis"
    ]

def Trans_hindi_to_english(txt):
    english_txt = translate(txt, to_language='en-in')
    return english_txt

def Trans_hindi_to_english(txt):
    english_txt = translate(txt, to_language='en-in')
    return english_txt

def listen():
    """Listen for speech input with settings optimized for laptop microphones"""
    recognizer = sr.Recognizer()
    
    # Settings optimized for laptop built-in microphones
    recognizer.dynamic_energy_threshold = True
    recognizer.energy_threshold = 2500  # Lower threshold for better sensitivity with laptop mic
    recognizer.dynamic_energy_adjustment_damping = 0.15  # More stable adjustment
    recognizer.dynamic_energy_ratio = 1.5  # Increased ratio for better sensitivity
    recognizer.pause_threshold = 0.8  # Longer pause to detect end of speech
    recognizer.phrase_threshold = 0.3  # Higher threshold for phrase detection
    recognizer.non_speaking_duration = 0.5  # Longer duration to detect silence
    
    with sr.Microphone() as source:
        print(Fore.YELLOW + "Adjusting for ambient noise... Please wait." + Style.RESET_ALL)
        # Longer adjustment period for better ambient noise calibration
        recognizer.adjust_for_ambient_noise(source, duration=1.5)
        print(Fore.GREEN + "Listening for your command..." + Style.RESET_ALL)
        
        try:
            # Increased timeout and phrase time limit for better recognition
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            print(Fore.LIGHTYELLOW_EX + "Got it! Recognizing..." + Style.RESET_ALL)
            
            try:
                recognized_txt = recognizer.recognize_google(audio, language='en-IN').lower()
                if recognized_txt:
                    translated_txt = Trans_hindi_to_english(recognized_txt)
                    print(Fore.BLUE + "Mr.Zeno: " + translated_txt + Style.RESET_ALL)
                    return translated_txt
            except sr.UnknownValueError:
                print(Fore.RED + "Sorry, I couldn't understand that." + Style.RESET_ALL)
                return ""
            except sr.RequestError as e:
                print(Fore.RED + f"Could not request results; {e}" + Style.RESET_ALL)
                return ""
        except sr.WaitTimeoutError:
            print(Fore.RED + "Listening timed out. Please try again." + Style.RESET_ALL)
            return ""
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)
            return ""
    
    return ""

#original code 
""" import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

def Trans_hindi_to_english(txt):
    english_txt = translate(txt, to_language='en-in')
    return english_txt

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True
    recognizer.energy_threshold = 4000  # Lower threshold for laptop mic
    recognizer.dynamic_energy_adjustment_damping = 0.15  # More stable adjustment
    recognizer.dynamic_energy_ratio = 1.5  # Increased ratio for better sensitivity
    recognizer.pause_threshold = 0.8  # Longer pause to detect end of speech
    recognizer.operation_timeout = None
    recognizer.phrase_threshold = 0.3  # Higher threshold for phrase detection
    recognizer.non_speaking_duration = 0.5  # Longer duration to detect silence

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.GREEN + "Listening for your command..." + Style.RESET_ALL)

        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            print(Fore.LIGHTYELLOW_EX + "Got it, recognizing..." + Style.RESET_ALL)
            recognized_txt = recognizer.recognize_google(audio).lower()
            if recognized_txt:
                translated_txt = Trans_hindi_to_english(recognized_txt)
                print(Fore.BLUE + "Mr.Zeno: " + translated_txt + Style.RESET_ALL)
                return translated_txt
        except sr.UnknownValueError:
            print(Fore.RED + "Sorry, I couldn't understand. Try again." + Style.RESET_ALL)
            return ""
        except sr.WaitTimeoutError:
            print(Fore.RED + "Listening timed out. No speech detected." + Style.RESET_ALL)
            return ""
        except Exception as e:
            print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)
            return ""
 """