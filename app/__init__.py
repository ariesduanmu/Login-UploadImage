# -*- coding: utf-8 -*-

from flask import Flask

from sql import db

from .extensions import bootstrap
from .extensions import login_manager

from config.routers import ROUTERS

login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    for url_prefix, blueprint in ROUTERS:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
    
    return app


    