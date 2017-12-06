from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from app.basemodels import db
from app.database.model import *
from passlib.apps import custom_app_context as pwd_context

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)

def get_hash(pwd):
    return pwd_context.encrypt(pwd)

@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()

@manager.command
def initdb():
    db.session.commit()
    db.drop_all()
    db.create_all()

@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(username='18551656881', password_hash=get_hash('123456'), admin=True))
    db.session.commit()


@manager.command
def create_data():
    """Creates sample data."""
    pass


if __name__ == '__main__':
    manager.run()
