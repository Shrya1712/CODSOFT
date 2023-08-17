import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

def get_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)["compound"]
    if sentiment_score > 0.1:
        return "positive"
    elif sentiment_score < -0.1:
        return "negative"
    else:
        return "neutral"

def simple_chatbot(user_input):
    if re.search(r'\b(hi|hello|hey)\b', user_input, re.IGNORECASE):
        return "Hello! How can I assist you today?"
    
    elif re.search(r'\b(how are you|how\'s it going)\b', user_input, re.IGNORECASE):
        return "I'm just a chatbot, but I'm here to help!"
    
    elif re.search(r'\b(goodbye|bye)\b', user_input, re.IGNORECASE):
        return "Goodbye! Have a great day!"
    
    elif re.search(r'\b(thank you|thanks)\b', user_input, re.IGNORECASE):
        return "You're welcome!"
    
    elif re.search(r'\b(weather|forecast)\b', user_input, re.IGNORECASE):
        return "I'm sorry, I don't have access to real-time weather data."
    
    elif re.search(r'\b(joke|funny)\b', user_input, re.IGNORECASE):
        return "Sure, here's a joke: Why don't scientists trust atoms? Because they make up everything!"
    
    else:
        sentiment = get_sentiment(user_input)
        if sentiment == "positive":
            return "I'm glad to hear that!"
        elif sentiment == "negative":
            return "I'm sorry to hear that. Is there anything I can do to help?"
        else:
            return "I'm here to assist you."

# Main loop for interacting with the chatbot
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
