# ChatGPT can assist you in brainstorming project ideas or providing templates to kickstart your coding.
# Ask ChatGPT : “Can you help me set up a basic Flask web application?”
# Example: Simple Flask Application

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
