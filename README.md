# flask-template
> flask 后端开发基础，随意玩玩~

## 安装依赖

``` sh
virtualenv venv

win: . ./venv/Scripts/activate
mac: . ./venv/bin/activate
pip install -r requirements.txt
```

// 创建数据库
``` sh
python manage.py create_db
python manage.py db init
python manage.py db migrate
python manage.py create_admin
python manage.py create_data
```


// 启动服务
``` sh
gunicorn run:app --worker-class gevent --access-logfile log.log
-D可挂起
```
