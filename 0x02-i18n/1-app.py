#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template
from flask-babel import Babel


app = Flask(__name__, static_url_path="")
babel = Babel(app)


class Config:
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route("/", strict_slashes=False)
def index() -> str:
    """route renders 1-index.html"""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
