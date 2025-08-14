import threading
import webbrowser
import sys
import time
from wikipedia import wikipedia
from Model import mind
from Mouth import speak

def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(':')
                if len(parts) != 2:
                    continue
                q, a = parts
                qa_dict[q] = a
    return qa_dict


def save_qa_dict(file_path, qa_dict):
    with open(file_path, 'w', encoding='utf-8') as f:
        for q, a in qa_dict.items():
            f.write(f"{q}:{a}\n")

qa_file_path = "D:\Jarvis\qna_data.txt" #give the correct path to your qa_data.txt file
qa_dict = load_qa_data(qa_file_path)

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)  # Adjust the speed of animation
    print()  # New line after the message

def wiki_search(prompt):
    search_prompt = prompt.replace("jarvis", "")
    search_prompt = search_prompt.replace("wikipedia", "")

    try:
        wiki_summary = wikipedia.summary(search_prompt, sentences=1)
        animate_thread = threading.Thread(target=print_animated_message, args=(wiki_summary,))
        speak_thread = threading.Thread(target=speak, args=(wiki_summary,))

        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        # Assuming 'search_wikipedia' is definied somewhere
        qa_dict[search_prompt] = wiki_summary # Store in qa-dict
        save_qa_dict(qa_file_path, qa_dict)  # Save updated qa_dict
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There is a disambiguation page for the given query. Please provide more specific information.")
        print("There is a disambiguation page for the given query. Please provide more specific information.")
    except wikipedia.exceptions.PageError:
        google_search(prompt)  # Fallback to Google search

def google_search(query):
    query = query.replace("who is ", "")
    query = query.strip()

    if query:
        url = "https://www.google.com/search?q=" + query
        webbrowser.open_new_tab(url)
        speak("You can see search results for " + query + " in Google on your screen.")
        #Commenting out the speak function as it is not provided here
        print("You can see search results for " + query + " in Google on your screen.")
    else:
        speak("I didn't understand your query. Please try again.")
        #Commenting out the speak function as it is not provided here
        print("I didn't understand your query. Please try again.")


""" def brain(text):
    try:
        response = mind(text)
        if not  response:
            wiki_search(text) # If OpenAI response is empty, fallback to wiki_search
            return
        
        # Start animation and speaking concurrently
        animate_thread = threading.Thread(target=print_animated_message, args=(response,))
        speak_thread = threading.Thread(target=speak, args=(response,))

        animate_thread.start()
        speak_thread.start()

        animate_thread.join()
        speak_thread.join()

        # Assuming 'search_wikipedia' is defined somewhere
        qa_dict[text] = response  # Store in qa-dict
        save_qa_dict(qa_file_path, qa_dict)  # Save updated qa_dict
    except Exception as e:
        # Handle any exceptions that may occur
        print(f"An error occurred: {str(e)}")
        wiki_search(text) # Pass to wiki_Search on error
 """

#brain("deepak")