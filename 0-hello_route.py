#!/usr/bin/python3
"""
This module starts a Flask web application hosted on 0.0.0.0, port 5000.
It displays 'Hello HBNB!' at the root directory.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' as a text response. """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
