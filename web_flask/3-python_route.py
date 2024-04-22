#!/usr/bin/python3
"""
This module defines a Flask application with several routes that display different texts.
The application listens on all network interfaces and on port 5000.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' at the root route. """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' at the '/hbnb' route. """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Displays 'C ' followed by the text. Underscores are replaced by spaces. """
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Displays 'Python ' followed by the text. Underscores are replaced by spaces. """
    return 'Python ' + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
