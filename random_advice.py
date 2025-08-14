import requests
#from Mouth import speak
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

""" 
advice = get_random_advice()
speak(advice) """
