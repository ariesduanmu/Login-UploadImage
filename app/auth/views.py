# -*- coding: utf-8 -*-
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
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data

        user = User.query.filter_by(username=username).first()
        if user is not None and user.verify_password(password):
            login_user(user, remember_me)
            return redirect(url_for(MAIN_UPLOAD_URL))
            
        flash(INVALID_USERNAME_PASSWORD)
    return render_template(LOGIN_HTML, form=form)

