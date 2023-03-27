#!/usr/bin/python3
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
    - /number_template/<n>: returns an HTML page containing the string
        "Number: <n>", formatted as an H1 tag inside the page's <body> tag.
        Only works if <n> is an integer.
    - /number_odd_or_even/<n>" returns an HTML page containing the string
    "Number: <n> is even|odd", formatted as an H1 tag inside the
        page's <body> tag.
        Only works if <n> is an integer.

The web application listens on 0.0.0.0, port 5000.
"""

from flask import Flask
from flask import Flask, render_template

# Create the Flask application instance
app = Flask(__name__)


# Set the route for the home page
@app.route('/')
def index():
    return 'Hello HBNB!'


# Set the route for /hbnb
@app.route('/hbnb')
def hbnb():
    return 'HBNB'


# Set the route for /c/<text>
@app.route('/c/<text>')
def c(text):
    return 'C {}'.format(text.replace('_', ' '))


# Set the route for /python/<text>
@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


# Set the route for /number/<n>
@app.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)


# Set the route for /number_template/<n>
@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


# Set the route for /number_odd_or_even/<n>
@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


# Start the Flask application server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
