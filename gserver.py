# -*- coding: utf-8 -*-
from gevent.pywsgi import WSGIServer
from app import create_app

app = create_app("config.config.ProdConfig")
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

server = WSGIServer(('', 8009), app)
server.serve_forever()
