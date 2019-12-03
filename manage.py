# -*- coding: utf-8 -*-
import os

from app import create_app

from sql import db
from sql.user import User
from sql.importdata import ImportData

from flask_script import Manager
from flask_script import Server

from flask_migrate import Migrate
from flask_migrate import MigrateCommand



env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app(f'config.config.{env.capitalize()}Config')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("server", Server(host="127.0.0.1", port=1337))
manager.add_command("db", MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, ImportData=ImportData)

if __name__ == "__main__":
    manager.run()
