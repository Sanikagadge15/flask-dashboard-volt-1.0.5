# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask, Blueprint

app = Flask(__name__)
blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix=''
)
