from flask import Flask
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

from app import routes
