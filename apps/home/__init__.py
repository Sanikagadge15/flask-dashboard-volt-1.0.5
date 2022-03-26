# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'sqlite:///site1.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
db = SQLAlchemy(app)
db.create_all()

app = Flask(__name__)
blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix=''
)
