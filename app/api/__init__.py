# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-31 15:27:42
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 20:33:35
from flask import Blueprint

api = Blueprint('api', __name__)

from .handler import authentication, upload




