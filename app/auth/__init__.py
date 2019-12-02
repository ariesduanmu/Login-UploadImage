# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-30 22:54:19
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 20:32:35
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views


