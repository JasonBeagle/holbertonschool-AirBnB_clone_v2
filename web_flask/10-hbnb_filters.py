#!/usr/bin/python3
"""
    Starts a Flask web application to display an HTML page
        with Airbnb search filters.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False

# Define the teardown function to close the SQLAlchemy session
def teardown(exception):
    storage.close()

# Register the teardown function with the app context
@app.teardown_appcontext
def handle_teardown(exception):
    teardown(exception)

# Define the view function to display the HTML page
@app.route("/hbnb_filters")
def hbnb_filters():
    """
        Displays a HTML page with Airbnb search filters
    """
    # Get all States, sorted alphabetically by name
    states = sorted(storage.all(State).values(), key=lambda state: state.name)

    # Get all Amenities, sorted alphabetically by name
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)

    # Get all Cities, sorted alphabetically by State name and City name
    cities = sorted(storage.all(City).values(),
                    key=lambda city: (city.state.name, city.name))

    # Render the HTML template with the necessary variables
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities, cities=cities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
