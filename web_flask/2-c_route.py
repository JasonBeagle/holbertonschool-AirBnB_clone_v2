#!/usr/bin/python3

"""This script defines a Flask web application that responds to three routes:
    - / : returns a string "Hello HBNB!"
    - /hbnb : returns a string "HBNB"
    - /c/<text> : returns a string "C " followed by the value of the <text>
    variable with underscores replaced by spaces.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This function defines the behavior for the / route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function defines the behavior for the /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """This function defines the behavior for the /c/<text> route.
    It takes the <text> variable from the URL and returns a string that
    starts with "C " followed by the value of the <text> variable with
    underscores replaced with spaces.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
