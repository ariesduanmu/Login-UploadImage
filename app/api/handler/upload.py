# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-31 17:30:02
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 20:37:55
import os

from flask import g
from flask import current_app

from werkzeug.utils import secure_filename

from app.api import api

from ..parsers.uploadparser import upload_parser

from sql import db
from sql.importdata import ImportData

from app.utils.response_utils import response_error
from app.utils.response_utils import response_success

from app.utils.upload_utils import allowed_file

from config.paths import API_UPLOAD


@api.route(API_UPLOAD, methods=['POST'])
def upload():
    args = upload_parser.parse_args()
    
    picture_data = args.get("picture")
    info_data = args.get("info")

    user_id = g.current_user.id

    if picture_data and allowed_file(picture_data.filename):
        picturename = secure_filename(picture_data.filename)
        picture_path = os.path.join(current_app.config['UPLOAD_FOLDER'], picturename)
        picture_data.save(picture_path)
        
        data = ImportData(info_data, picture_path, user_id)
        db.session.add(data)
        db.session.commit()
        return response_success()
    
    return response_error({"error":"Fail to upload data."})
