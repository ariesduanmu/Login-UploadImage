# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-30 22:54:42
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 20:37:59
import requests
from requests.auth import HTTPBasicAuth

from flask import render_template
from flask import flash
from flask import url_for
from flask import redirect

from flask_login import login_user
from flask_login import logout_user

from . import auth
from .forms import LoginForm

from config.paths import AUTH_LOGIN

from sql.user import User

from app.utils.flash_utils import INVALID_USERNAME_PASSWORD


LOGIN_HTML = 'auth/login.html'

MAIN_UPLOAD_URL = 'main.upload'

@auth.route(AUTH_LOGIN, methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for(MAIN_UPLOAD_URL))
        flash(INVALID_USERNAME_PASSWORD)
    return render_template(LOGIN_HTML, form=form)

