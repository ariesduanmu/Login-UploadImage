# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-30 23:49:30
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 20:35:10
import os
from app import create_app, db
from sql.user import User
from sql.importdata import ImportData
from flask_script import Manager, Server

env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app(f'config.config.{env.capitalize()}Config')

manager = Manager(app)
manager.add_command("server", Server(host="127.0.0.1", port=1337))

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, ImportData=ImportData)

if __name__ == "__main__":
    manager.run()
