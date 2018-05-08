import os

# MYSQL
mysql_username = 'root'
mysql_password = 'password'
mysql_name = 'flask_sql'
mysql_hostname = '127.0.0.1'

SECRET_KEY = os.urandom(24)
REDIS_URL = 'redis://:yourPassword@localhost'

DEBUG = True
PORT = 8000
HOST = '127.0.0.1'
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

# MySQL
DATABASE_URI = 'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}?charset=utf8mb4'.format(DB_USER=mysql_username,
                                                                                                DB_PASS=mysql_password,
                                                                                                DB_ADDR=mysql_hostname,
                                                                                                DB_NAME=mysql_name)
