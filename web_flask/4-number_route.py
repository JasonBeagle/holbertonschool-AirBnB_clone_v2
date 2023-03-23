#!/usr/bin/env python3
"""
This script defines a Flask web application that responds to several routes:
    - /: returns a string "Hello HBNB!"
    - /hbnb: returns a string "HBNB"
    - /c/<text>: returns a string "C " followed by the value of the <text>
        variable with underscores replaced by spaces.
    - /python/(<text>): returns a string "Python " followed by the value of
        the <text> variable with underscores replaced by spaces.
            If <text> is not provided, the default value of "is cool" is used.
    - /number/<n>: returns a string "<n> is a number"
        only if <n> is an integer.

The web application listens on 0.0.0.0, port 5000.

"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>,
        with underscores replaced by spaces."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Displays 'Python' followed by the value of <text>,
        with underscores replaced by spaces.
        The default value of <text> is 'is cool'.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays <n> followed by "is a number" only if <n> is an integer."""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
