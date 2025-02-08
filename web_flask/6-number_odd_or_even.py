#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return "C {}".format(escape(text.replace("_", " ")))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Display_python(text="is cool"):
    return "Python {}".format(escape(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    if (n % 2 == 0):
        odd_even = "even"
    else:
        odd_even = "odd"
    return render_template('6-number_odd_or_even.html', num=n, odd_even=odd_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
