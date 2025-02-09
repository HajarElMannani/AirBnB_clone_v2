#!/usr/bin/python3
'''Script that starts a web application'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    '''Displays all states'''
    states = [state for state in storage.all("State").values()]
    states = sorted(states, key=lambda y: y.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_with_city(id):
    '''Displays the state'''
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exception):
    '''Closes the storage'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
