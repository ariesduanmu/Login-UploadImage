# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-02 10:35:35
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 13:37:51
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_httpauth import HTTPBasicAuth

bootstrap = Bootstrap()
login_manager = LoginManager()
auth = HTTPBasicAuth()