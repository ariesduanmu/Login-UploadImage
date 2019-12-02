# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-02 10:52:14
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 20:37:39
from .paths import AUTH_PRE
from .paths import MAIN_PRE
from .paths import API_PRE

from app.auth import auth as auth_blueprint
from app.main import main as main_blueprint
from app.api import api as api_blurprint


ROUTERS = [

(AUTH_PRE, auth_blueprint),
(MAIN_PRE, main_blueprint),
(API_PRE, api_blurprint),

]