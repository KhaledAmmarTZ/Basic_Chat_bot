import json
import random

# Load intents
with open('intents.json') as file:
    intents = json.load(file)

# Function to get a response
def get_response(user_input):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower() or user_input.lower() in pattern.lower():
                response = random.choice(intent['responses'])
                if 'source' in intent:
                    response += f" For more information, visit: <a href='{intent['source']}' target='_blank'>{intent['source']}</a>"
                return response
    return "Sorry, I didn't understand that."

# Chat loop
print("Welcome to the Student Support Chatbot! (Type 'quit' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = get_response(user_input)
    print("Bot:", response)
