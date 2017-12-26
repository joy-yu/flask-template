import os
from app import app
from flask import render_template, send_from_directory, request

@app.route('/path/<path:filename>')
def file(filename):
    return send_from_directory(os.path.join(app.root_path, 'templates'), filename)

@app.route('/index')
def index():
    return render_template('index.html')

# from app.routers.user import user_blueprint
# app.register_blueprint(user_blueprint)
