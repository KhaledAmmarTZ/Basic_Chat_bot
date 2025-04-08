from flask import Flask, request, jsonify, render_template
import json
import random
import re

app = Flask(__name__)

# Load intents
with open('intents.json') as file:
    intents = json.load(file)

# Function to get a response
def get_response(user_input):
    user_input = user_input.lower().strip()

    # Exact match
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if user_input == pattern.lower().strip():
                return random.choice(intent['responses'])

    # Regex or partial match
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if re.search(re.escape(pattern.lower()), user_input):
                return random.choice(intent['responses'])

    return "Sorry, I didn't understand that."

# Load index.html but start with profile.html content
@app.route('/')
def index():
    return render_template('index.html', page='profile.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', layout=False)  

@app.route('/class_routine')
def class_routine():
    return render_template('class_routine.html', layout=False)

@app.route('/class_test')
def class_test():
    return render_template('class_test.html', layout=False)

@app.route('/midterm_exam')
def midterm_exam():
    return render_template('midterm_exam.html', layout=False)

@app.route('/final_exam')
def final_exam():
    return render_template('final_exam.html', layout=False)


@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form.get('msg', '')
    return get_response(user_input)

if __name__ == '__main__':
    app.run(debug=True)
