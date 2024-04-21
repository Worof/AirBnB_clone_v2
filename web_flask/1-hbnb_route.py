#!/usr/bin/python3
"""
This module starts a Flask web application that listens on 0.0.0.0, port 5000.
It defines two routes: '/' and '/hbnb'. Each route displays text responses.
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
