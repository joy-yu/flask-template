# -*- coding: utf-8 -*-
from app.utils import ResponseUtil, RequestUtil, DateUtil
from app.database.model import *
from app import app, v, IMAGE_URL
from app import SQLAlchemyDB as db
from flask import request, send_from_directory
from werkzeug import secure_filename
import os
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/api/v1/uploads', methods=['POST'])
def upload_file():
    file = request.files['image']
    if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            unix_time = DateUtil.now_timestamp()
            ext = filename.rsplit('.',1)[1]
            new_filename = str(unix_time)+ '.' +ext
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
            return ResponseUtil.standard_response(0, IMAGE_URL+new_filename)
    return ResponseUtil.standard_response(0, '请上传图片！')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
