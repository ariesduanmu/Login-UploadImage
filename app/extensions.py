# -*- coding: utf-8 -*-

from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_httpauth import HTTPBasicAuth

bootstrap = Bootstrap()
login_manager = LoginManager()
auth = HTTPBasicAuth()