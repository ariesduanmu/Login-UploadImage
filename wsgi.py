# -*- coding: utf-8 -*-
from tornado.wsgi import WSGIContainer
from app import create_app

app = WSGIContainer(create_app("config.config.ProdConfig"))

'''
uwsgi --socket 127.0.0.1:8080 \
      --wsgi-file wsgi.py \
      --callable app \
      --processes 4 \
      --threads 2
'''