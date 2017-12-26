# -*- coding: utf-8 -*-

from app import app, v
from app.utils import ResponseUtil, RequestUtil
from app.database.model import User
from app import SQLAlchemyDB as db



# 获取登录用户
@app.route('/api/v1/login_user', methods=['GET'])
def get_login_user():
    rst = RequestUtil.get_login_user()
    if(rst is None):
        return ResponseUtil.standard_response(1, '请重新登录')
    return ResponseUtil.standard_response(0, rst)
