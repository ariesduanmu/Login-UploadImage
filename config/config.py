# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-30 23:17:29
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 20:35:23
import os
from .dbconfig import db_url

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    UPLOAD_FOLDER = '/tmp'

class ProdConfig(Config):
    DEBUG = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or db_url