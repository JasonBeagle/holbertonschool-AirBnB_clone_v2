#!/usr/bin/python3

"""Import necessary modules."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

"""Create a Flask app instance."""
app = Flask(__name__)
"""Set strict_slashes attribute to False to allow
    both "/states" and "/states/" to be valid routes."""
app.url_map.strict_slashes = False


"""Define a Flask route that displays a list of all State objects
    in the database. If an id is provided, display the State object
    with that id."""


@app.route("/states")
@app.route("/states/<id>")
def states_id_route(id=None):
    """Retrieve all State objects from the database using
        the storage engine."""
    states = storage.all(State)
    """Pass the list of State objects to the 9-states.html template
        along with the id parameter."""
    return render_template("9-states.html", state_list=states, id=id)


"""Define a function to be called when the Flask app context is torn down.
    This function closes the storage engine to prevent resource leaks."""


@app.teardown_appcontext
def teardown(stuff):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
