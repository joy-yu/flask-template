# -*- coding: utf-8 -*-

from flask import session
from app import app, v
from app import SQLAlchemyDB as db
from app.utils import ResponseUtil, RequestUtil, DateUtil, verifyUtil
from app.database.model import User
from passlib.apps import custom_app_context as pwd_context
from io import BytesIO
from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
import urllib


clnt = YunpianClient('.........................')


def get_hash(pwd):
    return pwd_context.encrypt(pwd)

def verify_password(pwd, sql_pwd):
    return pwd_context.verify(pwd, sql_pwd)


# 获取图片验证码
@app.route('/api/v1/pecode', methods=['GET'])
def get_pecode():
    code_img, strs = verifyUtil.create_validate_code()
    session['pecode'] = strs
    buf = BytesIO()
    code_img.save(buf,'JPEG',quality=70)
    buf_str = buf.getvalue()
    response = app.make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    return response

# 验证图片验证码
@app.route('/api/v1/pecode', methods=['POST'])
@v.param({
    'pecode': v.str()
})
def check_pecode(pecode):
    sess = session.get('pecode', '')
    if(sess == pecode):
        return ResponseUtil.standard_response(0, 'check_pecode ok!')
    else:
         return ResponseUtil.standard_response(1, '图片验证码不正确！')


# 发送手机验证码
@app.route('/api/v1/register_send_sms', methods=['POST'])
@v.param({
    'username': v.str()
})
def req_send_sms(username):
    code_img, strs = verifyUtil.create_validate_code()
    session['mecode'] = strs
    param = {
        YC.MOBILE: username,
        YC.TPL_ID: 123456,
        YC.TPL_VALUE : urllib.parse.quote("#code#") + "=" + urllib.parse.quote(strs)
}
    r = clnt.sms().tpl_single_send(param)
    if(r.code() != 0):
        return ResponseUtil.standard_response(1, r.detail())
    print(r.code(),r.detail())
    return ResponseUtil.standard_response(0, 'req receive.')


# 检查手机验证码
@app.route('/api/v1/check_sms', methods=['POST'])
@v.param({
    'sms_code': v.str()
})
def req_check_sms(sms_code):
    sess = session.get('mecode', '')
    if(sess == sms_code):
        return ResponseUtil.standard_response(0, 'check_mecode ok!')
    else:
         return ResponseUtil.standard_response(1, '手机验证码不正确！')


# 注册
@app.route('/api/v1/register', methods=['POST'])
@v.param({
    'username': v.str(),
    'password': v.str()
})
def register(username,password):
    if User.query.filter_by(username = username).first() is not None:
        return ResponseUtil.standard_response(1, '用户已存在！')

    user = User(
        username= username,
        password_hash= get_hash(password)
    )

    user.save()
    db.session.commit()

    return ResponseUtil.standard_response(0, user.dict())




# 登录
@app.route('/api/v1/login', methods=['POST'])
@v.param({
    'username': v.str(),
    'password': v.str()
})
def loginApi(username, password, is_backend):
    user = User.query.filter_by(username= username).first()
    if(not user):
        return ResponseUtil.standard_response(1, '用户名不存在或密码错误')
    if(not verify_password(password, user.password_hash)):
        return ResponseUtil.standard_response(1, '用户名不存在或密码错误')

    user.last_login = DateUtil.now_datetime()
    user.save()
    RequestUtil.login_user(user.dict())
    return ResponseUtil.standard_response(0, user.dict())



# 忘记密码
@app.route('/api/v1/modify', methods=['POST'])
@v.param({
    'username': v.str(),
    'password': v.str()
})
def modify(username,password):
    user = User.query.filter_by(username = username).first()
    if user is None:
        return ResponseUtil.standard_response(1, '用户不存在！')

    user.password_hash = get_hash(password)
    user.save()
    return ResponseUtil.standard_response(0, user.dict())


# 登出
@app.route('/api/v1/logout', methods=['GET'])
def logout():
    RequestUtil.logout()
    return ResponseUtil.standard_response(0, 'logout success!')
