# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-31 01:17:33
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 20:32:30
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
