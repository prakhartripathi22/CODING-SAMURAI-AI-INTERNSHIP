import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('stopwords')

conversations = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "what's your name?": "I'm a chatbot created to assist you.",
    "how are you?": "I'm just a bunch of code, but I'm here to help!",
    "bye": "Goodbye! Have a great day!",
    "what's the weather like?": "I'm just a text-based chatbot and don't have access to real-time data. Sorry!"
}

stop_words = set(stopwords.words('english'))

def preprocess_input(user_input):
    tokens = word_tokenize(user_input.lower())
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return tokens

def get_response(user_input):
    tokens = preprocess_input(user_input)
    for key in conversations.keys():
        key_tokens = preprocess_input(key)
        if all(token in key_tokens for token in tokens):
            return conversations[key]
    return "Sorry, I don't understand that."

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

chatbot()