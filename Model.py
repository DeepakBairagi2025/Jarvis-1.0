import nltk

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Mouth import speak  # Make sure your Mouth.py has a valid speak() function

# Load your Q&A dataset from a text file
def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':') for line in lines if ':' in line]
        dataset = [{'question': q.strip(), 'answer': a.strip()} for q, a in qna_pairs]
    return dataset

# Preprocess the text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower(), preserve_line=True)

    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)

# Train the TF-IDF vectorizer
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X

# Retrieve the most relevant answer
def get_answer(question, vectorizer, X, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, X)
    best_match_index = similarities.argmax()
    return dataset[best_match_index]['answer']

# Main function
def mind(text):
    dataset_path = r"D:\Jarvis\qna_data.txt"  # Make sure this file exists
    dataset = load_dataset(dataset_path)

    vectorizer, X = train_tfidf_vectorizer(dataset)
    user_question = text
    answer = get_answer(user_question, vectorizer, X, dataset)
    return answer

# Loop
""" if __name__ == "__main__":
    while True:
        x = input("You: ")
        if x.lower() in ["exit", "quit", "bye"]:
            speak("Goodbye sir!")
            break
        mind(x) """

#maybe i use the above loop for some other file as integrated
# use the below code 
'''
if __name__ == "__main__":
    while True:
        x = input("You: ")
        if x.lower() in ["exit", "quit", "bye"]:
            speak("Goodbye sir!")
            break
        answer = mind(x)
        speak(answer)
 '''