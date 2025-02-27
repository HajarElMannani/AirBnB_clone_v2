#!/usr/bin/python3
'''Script that starts a Flask application'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''Display the states and cities'''
    states = [state for state in storage.all("State").values()]
    states = sorted(states, key=lambda y: y.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    '''Closes the storage'''
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
