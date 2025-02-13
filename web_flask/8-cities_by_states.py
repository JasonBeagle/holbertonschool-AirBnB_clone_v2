#!/usr/bin/python3
"""
Flask web application that displays a list of cities by state
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a list of cities by state
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", state_list=states)


@app.teardown_appcontext
def teardown_db(self):
    """
    Removes the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
