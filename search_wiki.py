import wikipedia
import threading
from Brain import print_animated_message, qa_dict, save_qa_data, qa_file_path, google_search
from Mouth import speak

def wiki_search(prompt):
    search_prompt = prompt.replace("jarvis", "").replace("wikipedia", "")

    try:
        wiki_summary = wikipedia.summary(search_prompt, sentences=2)
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))

        speak_thread.start()

        speak_thread.join()

        # Assuming 'search_propmt' is defined somewhere
        qa_dict[search_prompt] = wiki_summary # Store in qa_dict
        save_qa_data(qa_file_path, qa_dict) # Save updated qa_dict
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There is a disambiguation page for the given query. Please provide more information.")
        #print("There is a disambiguation page for the given query. Please provide more information.")

    except wikipedia.exceptions.PageError:
        google_search(prompt)
""" 
wiki_search("who is maggie") """