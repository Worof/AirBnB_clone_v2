#!/usr/bin/python3
"""
This module starts a Flask web application with specified routes.
The application listens on all network interfaces (0.0.0.0) and on port 5000.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' as a text response at the root route. """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' as a text response at the '/hbnb' route. """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Displays 'C ' followed by the text, underscores in text are replaced by spaces. """
    return 'C ' + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
