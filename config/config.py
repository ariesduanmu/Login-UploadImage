# -*- coding: utf-8 -*-

import os
from .dbconfig import db_url

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    UPLOAD_FOLDER = 'file/'

class ProdConfig(Config):
    DEBUG = False

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or db_url