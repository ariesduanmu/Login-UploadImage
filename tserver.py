# -*- coding: utf-8 -*-
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import create_app

app = WSGIContainer(create_app("config.config.ProdConfig"))
http_server = HTTPServer(app)
http_server.listen(8008)
IOLoop.instance().start()
