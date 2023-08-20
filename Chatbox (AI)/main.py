import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import scrolledtext, END

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

def send_message(event=None):  # Accept an event parameter for binding
    user_input = input_text.get("1.0", "end-1c")
    response = simple_chatbot(user_input)
    
    chat_log.tag_configure("user_tag", justify="right", background="#0B50FB")
    
    
    
    user_input_length = len(user_input)
    response_length = len(response)
    
    chat_log.insert(tk.END, f"You: {user_input}\n", "user_tag")
    chat_log.insert(tk.END, f"Chatbot: {response}\n\n", "bot_tag")
    
    input_text.delete("1.0", tk.END)
    

# Create the main window
window = tk.Tk()
window.title("Chatbot GUI")

# Create the chat log display
chat_log = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, font="cambria",bg="#0BBAFB",fg="white")
chat_log.pack()

# Create the input text box and send button
input_text = tk.Text(window, wrap=tk.WORD, width=40, height=3, font="cambria")
input_text.pack(padx=(0, 10))
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Bind the Return key to the send message function
window.bind("<Return>", send_message)

# Start the GUI event loop
window.mainloop()
