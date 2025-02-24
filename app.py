from flask import Flask, request, jsonify, render_template
import json
import random

app = Flask(__name__)

# Load intents
with open('intents.json') as file:
    intents = json.load(file)

# Function to get a response
def get_response(user_input):
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input.lower():
                return random.choice(intent['responses'])
    return "Sorry, I didn't understand that."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form['msg']
    return get_response(user_input)

if __name__ == '__main__':
    app.run(debug=True)
