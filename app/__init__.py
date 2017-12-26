# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.utils.validator import Validator
from flask_sse import sse


__version__ = '0.0.1'

root_url = os.path.abspath(__name__)
UPLOAD_FOLDER = os.path.join(root_url,'uploads')
IMAGE_URL = 'http://0.0.0.0/uploads/'
v = Validator()

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.register_blueprint(sse, url_prefix='/stream')
SQLAlchemyDB = SQLAlchemy(app)


from app import views
