from flask_migrate import Migrate
from app import  app
from app.basemodels import db

migrate = Migrate(app, db)

from models import *  # noqa


@app.cli.command()
def initdb():
    db.session.commit()
    db.drop_all()
    db.create_all()