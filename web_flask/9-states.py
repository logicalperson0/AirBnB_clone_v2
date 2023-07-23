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
    states_lists = storage.all("State").values()
    states_lists = sorted(states_lists, key=lambda d: d.name)
    return render_template("9-states.html", state_lists=state)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """/states/<id>: display a HTML page"""
    states_lists = storage.all("State").values()
    states_lists = sorted(states_lists, key=lambda d: d.name)
    for states_list in states_lists:
        if states_list.id == id:
            return render_template("9-states.html", states_list=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
