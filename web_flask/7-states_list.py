#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_app(exception=None):
    """teardown_app"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """/states_list: display a HTML page"""
    states_lists = storage.all(State)
    # sorted(entries, key=lambda d: d['title'])
    states_lists = sorted(states_lists, key=lambda d: d.name)

    render_template("7-states_list.html", states_lists=states_lists)
