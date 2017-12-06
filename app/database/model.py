# -*- coding: utf-8 -*-

from .base import BaseMethod
from app import SQLAlchemyDB as db
#from passlib.apps import custom_app_context as pwd_context

# 用户表
class User(db.Model, BaseMethod):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(250), nullable=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(250), nullable=True)
    username = db.Column(db.String(32), index = True, nullable=False)
    active = db.Column(db.Integer, nullable=True, default=0)
    avatar = db.Column(db.String(128), nullable=True)
    handle_id = db.Column(db.Integer, nullable=True)
    admin = db.Column(db.Boolean, nullable=True)
    creation_time = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    last_login = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def dict(self):
        rst = {}
        rst['id'] = self.id
        rst['name'] = self.name
        rst['avatar'] = self.avatar
        rst['active'] = self.active
        rst['last_login'] = self.last_login
        rst['email'] = self.email
        rst['username'] = self.username
        rst['handle_id'] = self.handle_id
        rst['admin'] = self.admin
        return rst
