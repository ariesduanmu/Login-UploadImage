# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-31 01:17:51
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 20:38:04
import os
import requests

from werkzeug.utils import secure_filename

from flask import render_template
from flask import flash
from flask import current_app

from flask_login import current_user
from flask_login import login_required

from . import main

from .forms import ImportDataForm

from config.paths import MAIN_UPLOAD

from sql import db
from sql.importdata import ImportData

from app.utils.upload_utils import allowed_file

from app.utils.flash_utils import FAID_UPLOAD_DATA

UPLOAD_HTML = 'main/upload.html'
SUCCESS_HTML = 'main/success.html'

@main.route(MAIN_UPLOAD, methods=['GET','POST'])
@login_required
def upload():
    form = ImportDataForm()
    if form.validate_on_submit():
        picture_data = form.picture.data
        info_data = form.info.data
        user_id = current_user.id
        if picture_data and allowed_file(picture_data.filename):
            picturename = secure_filename(picture_data.filename)
            picture_path = os.path.join(current_app.config['UPLOAD_FOLDER'], picturename)
            picture_data.save(picture_path)
            data = ImportData(info_data, picture_path, user_id)
            db.session.add(data)
            db.session.commit()
            return render_template(SUCCESS_HTML)
        else:
            flash(FAID_UPLOAD_DATA)
    return render_template(UPLOAD_HTML, form=form)



