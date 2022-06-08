from flask import Flask, Blueprint, jsonify, render_template, url_for

movies_blueprint = Blueprint("movies", __name__)

from presenter.app import app, db
from presenter.models.movie import Movie


@movies_blueprint.route("/movies")
def index():
    db.create_all()
    movie = Movie(url="https://www.imdb.com/title/tt0110912/", title="Pulp Fiction")
    db.session.add(movie)
    db.session.commit()
    print(Movie.query.all())
    return render_template("movies/index.html")
