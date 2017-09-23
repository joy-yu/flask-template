# MYSQL
mysql_db_username = 'root'
mysql_db_password = 'password'
mysql_db_name = 'flask_sql'
mysql_db_hostname = '127.0.0.1'



DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

# MySQL
DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}?charset=utf8mb4".format(DB_USER=mysql_db_username,
                                                                                DB_PASS=mysql_db_password,
                                                                                DB_ADDR=mysql_db_hostname,
                                                                                DB_NAME=mysql_db_name)
