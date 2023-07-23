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
def teardown_app(exception=None):
    """teardown_app"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """/states_list: display a HTML page"""
    states_lists = storage.all(State).values()
    # sorted(entries, key=lambda d: d['title'])
    states_lists = sorted(states_lists, key=lambda d: d.name)

    return render_template("8-cities_by_states.html",
                           states_lists=states_lists)


if __name__ == "__main__":
    storage.reload()
    app.run(host="0.0.0.0", port=5000)
