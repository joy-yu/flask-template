# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.utils.validator import Validator
from flask_sse import sse


__version__ = '0.0.1'

root_url = os.path.abspath(__name__)
UPLOAD_FOLDER = os.path.join(root_url,'uploads')
secret_key = os.urandom(24)
v = Validator()

app = Flask(__name__, static_folder='static', template_folder="template")
app.secret_key = secret_key
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["REDIS_URL"] = "redis://:root@localhost"
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.register_blueprint(sse, url_prefix='/stream')
SQLAlchemyDB = SQLAlchemy(app)



#socketio = SocketIO(app)
# from flask import render_template, send_from_directory
# import os

# @app.route('/<path:filename>')
# def file(filename):
#     return send_from_directory(os.path.join(app.root_path, 'templates'), filename)

# @app.route('/')
# def index():
#     return render_template('index.html')

# from app.routers.user import user_blueprint
# app.register_blueprint(user_blueprint)
