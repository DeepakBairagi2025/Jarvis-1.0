from transformers import pipeline

def open_website_by_name(website_name):
    # You can use a more advanced nodel for better language understanding
    nlp = pipeline(task:"ner", model=dbmdz/bert-large-cased-finetuned-conll03-english")
                   
    #extract entities (website names) from the website name
    entities = nlp(website_name)

    # Extract the first entity (assuming it's the main one)
    if entities and "text" in entities[0]:
        website_name = entities[0]["text"].lower()
        print(f"User mentioned: {website_name}")

        # You can use a more comprehensive method to map names to URLs
        url = get_website_url(website_name)
        if url:
            webbrowser.open(url)
            print(f"Opening {website_name} at {url}")
        else:
        print(f"Sorry, I don't have information about the website '{website_name}',")

    else:
        print("No recognizable website mentioned in the input.")

def get_website_url(website_name):
    # Add your own logic to map website names to URLs
    # This could involve querying a database, using an API, or other methods
    websites = {
        'google': 'https://www.google.com',
        'youtube': 'https://www.youtube.com',
        'example': 'https://www.example.com',
        # Add more websites as needed
    }

    return websites.get(website_name)

if __name__ == "__main__":
    import webbrowser

    # Example usage
    user_input = input("Eter the website name to open: ")
    open_website_by_name(user_input)