# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-31 18:41:53
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 12:32:54
from flask_restful import reqparse

from werkzeug.datastructures import FileStorage

upload_parser = reqparse.RequestParser()
upload_parser.add_argument(
    'info',
    type=str,
    required=True,
    help="Auth Token is required to edit posts"
    )
upload_parser.add_argument(
    'picture', 
    type=FileStorage, 
    location='files',
    required=True,
) 
