# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from flask import Flask
from flask_migrate import Migrate
from sys import exit
from flask_sqlalchemy import SQLAlchemy
from decouple import config

from apps.config import config_dict
from apps import create_app, db

# import pyrebase
# firebaseConfig = {
#   "apiKey": "AIzaSyBtkN3XqRn08N9Rgwt9aQIZpW4IlrinYC4",
#   "authDomain": "flasksih.firebaseapp.com",
#   "projectId": "flasksih",
#   "storageBucket": "flasksih.appspot.com",
#   "messagingSenderId": "756421308418",
#   "appId": "1:756421308418:web:8881d941f117a013b4b71b",
#   "databaseURL": "https://console.firebase.google.com/project/flasksih/database/flasksih-default-rtdb/data"
# }

# firebase = pyrebase.initialize_app(firebaseConfig)
# auth=firebase.auth()
# db=firebase.database()

app = Flask(__name__)
db = SQLAlchemy(app)
db.create_all()
# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)

if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG))
    app.logger.info('Environment = ' + get_config_mode)
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)

if __name__ == "__main__":
    app.run()
