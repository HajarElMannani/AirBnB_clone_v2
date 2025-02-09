#!/usr/bin/python3
'''Script that starts a web application'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states():
    '''Displays hbnb filters'''
    states = [state for state in storage.all("State").values()]
    states = sorted(states, key=lambda y: y.name)
    amenities = [amenity for amenity in storage.all("Amenity").values()]
    amenities = sorted(amenities, key=lambda l: l.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    '''Closes the storage'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
