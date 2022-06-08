from flask import Flask, Blueprint, jsonify, render_template, url_for

movies_blueprint = Blueprint("movies", __name__)

from presenter.app import app


@movies_blueprint.route("/movies")
def index():
    return render_template("movies/index.html")
