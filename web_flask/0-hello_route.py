#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_HBNB():
    return "<p>Hello HBNB!</p>"
