# -*- coding: utf-8 -*-

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

from config.paths import MAIN_INDEX
from config.paths import MAIN_UPLOAD

from sql import db
from sql.importdata import ImportData

from app.utils.upload_utils import allowed_file

from app.utils.flash_utils import FAID_UPLOAD_DATA

INDEX_HTML = 'index.html'
UPLOAD_HTML = 'main/upload.html'
SUCCESS_HTML = 'main/success.html'

@main.route(MAIN_INDEX, methods=['GET'])
@login_required
def index():
    return render_template(INDEX_HTML)


@main.route(MAIN_UPLOAD, methods=['GET','POST'])
@login_required
def upload():
    form = ImportDataForm()
    if form.validate_on_submit():
        picture_data = form.picture.data
        info_data = form.info.data
        user_id = current_user.id

        picture_data_filename = picture_data.filename
        print(allowed_file(picture_data.filename))

        if picture_data and allowed_file(picture_data_filename):
            picturename = secure_filename(picture_data_filename)
            picture_path = os.path.join(current_app.config['UPLOAD_FOLDER'], picturename)
            picture_data.save(picture_path)
            data = ImportData(info_data, picture_path, user_id)
            db.session.add(data)
            db.session.commit()
            return render_template(SUCCESS_HTML)
        else:
            flash(FAID_UPLOAD_DATA)
    return render_template(UPLOAD_HTML, form=form)



