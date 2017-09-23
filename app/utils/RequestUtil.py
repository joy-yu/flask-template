# -*- coding: utf-8 -*-

from flask.globals import request, session
# login user from session
def get_login_user():
    return session.get('u_id', {})


# set user login
def login_user(user):
    session['u_id'] = user


# logou user, session pop
def logout():
    session.pop('oauth_token', None)
    session.pop('u_id', None)
