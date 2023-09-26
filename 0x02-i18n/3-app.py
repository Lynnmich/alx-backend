#!/usr/bin/env python3
"""Basic flask app"""
from flask import Flask, render_template, request
from flask-babel import Babel


class Config(object):
    """Config class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__, static_url_path="")
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Gets locale from request object"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index() -> str:
    """route renders 2-index.html"""
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
