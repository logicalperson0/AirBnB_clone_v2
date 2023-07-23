#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_app(exception):
    """teardown_app"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """/states_list: display a HTML page"""
    states_lists = storage.all(State).values()
    # sorted(entries, key=lambda d: d['title'])
    states_lists = sorted(states_lists, key=lambda d: d.name)

    return render_template("7-states_list.html", states_lists=states_lists)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
