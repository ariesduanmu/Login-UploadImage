# -*- coding: utf-8 -*-
from api import create_app
from flask_cors import CORS

app = create_app("config.config.ProdConfig")
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
CORS(app, supports_credentials=True)
