#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_airhbnb():
    """function that Routes: /: displays “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def airhbnb():
    """function that Routes: /hbnb: display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Function that Routes: /c/<text>: display “C ”
    followed by the value of the text"""
    return "C %s" % text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Function that Routes: /python/(<text>): display “Python ”
    followed by the value of the text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<n>", strict_slashes=False)
def number_n(n):
    """Function that routes: /number/<n>: display “n is a number”
    only if n is an integer"""
    if n is int:
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
