# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2019-12-02 12:22:06
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 13:39:28
from config.utils import ALLOW_EXTENSIONS

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOW_EXTENSIONS


