from flask import Flask, request, jsonify, render_template
import json
import random
import re

app = Flask(__name__)

with open('intents.json') as file:
    intents = json.load(file)

def get_response(user_input):
    user_input = user_input.lower()  
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if re.search(pattern.lower(), user_input): 
                response = random.choice(intent['responses'])
                return response  
    return "Sorry, I didn't understand that."


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



@app.route('/get', methods=['POST'])
def get_bot_response():
    user_input = request.form['msg']
    return get_response(user_input)

if __name__ == '__main__':
    app.run(debug=True)
