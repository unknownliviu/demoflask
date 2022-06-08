from flask import Flask
import time
from presenter.configuration import config

app = Flask(__name__)

from presenter.controllers.movies import movies_blueprint

app.register_blueprint(movies_blueprint)
app.config.update(config().as_dict())
