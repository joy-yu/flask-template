# flask-template
> flask 框架模板~

## 安装依赖

``` sh
virtualenv venv
# 指定版本：virtualenv -p /usr/bin/python3 venv

win: . ./venv/Scripts/activate
mac: . ./venv/bin/activate
pip install -r requirements.txt -i https://pypi.douban.com/simple
```

#### 创建数据库
``` sh
# 详见manage.py
python manage.py create_db
python manage.py db init
python manage.py db migrate
python manage.py create_admin
python manage.py create_data
```


#### 启动服务
``` sh
python run.py
# or #
gunicorn run:app --worker-class gevent --access-logfile log.log -b 127.0.0.1:8000 # -D可挂起

```

#### 文件目录
``` sh
config.py  # 变量配置
manage.py  # 命令行Python相关操作
requirements.txt  # Python依赖包
run.py  # 服务器启动

app/
    __init__.py  #初始化应用，汇集了各种组件
    views/  # 路由定义所在的文件
    database/  # 数据库模型定义
    static/  # 静态资源
    templates/  # 模板所在目录
    uploads/  # 上传图片
```
