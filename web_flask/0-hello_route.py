#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_HBNB():
<<<<<<< HEAD
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
    '''Function that displays Hello HBNB'''
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> c679e13c9cf25ea1cb9827b9510fd4f58eec8637
