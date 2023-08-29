#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template


app = Flask (__name__)

@app.route("/")
def index():
    """route for index.html"""
    return render_template("0-index.html")
