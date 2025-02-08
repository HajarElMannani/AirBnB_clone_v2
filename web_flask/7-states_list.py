#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask
from models import storage
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    state = storage.all("State").values()
    states = sorted(state, key=lambda y: y.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(excep):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
