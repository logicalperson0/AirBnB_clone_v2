#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """/states: display a HTML page"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """/states/<id>: display a HTML page"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
