#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown_app(exception=None):
    """teardown_app"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """/states: display a HTML page"""
    states_lists = storage.all("State")
    return render_template("9-states.html", state_lists=state)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """/states/<id>: display a HTML page"""
    for states_lists in storage.all("State").values():
        if states_lists.id == id:
            return render_template("9-states.html", states_lists=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
