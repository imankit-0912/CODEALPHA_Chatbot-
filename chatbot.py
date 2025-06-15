# Simple chatbot without NLTK

import random

# Define simple rules and responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey 👋!"],
    "hello": ["Hi!", "Hello! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "Doing fine, thank you!"],
    "what is your name": ["I'm a Python chatbot 🤖.", "People call me ChatBot!"],
    "help": ["Sure! I'm here to assist you.", "What do you need help with?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
}

# Default fallback response
default_responses = [
    "I'm not sure I understand 🤔.",
    "Can you say that differently?",
    "Interesting... tell me more!",
    "Hmm, let's talk about something else?"
]

# Make input matching case-insensitive and simple
def get_response(user_input):
    user_input = user_input.lower().strip()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(default_responses)

# Start the conversation
print("=" * 50)
print("🤖 Welcome to ChatBot! Type 'bye' to exit.")
print("=" * 50)

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("ChatBot: " + random.choice(responses["bye"]))
        break
    else:
        reply = get_response(user_input)
        print("ChatBot:", reply)
