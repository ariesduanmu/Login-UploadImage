# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-30 22:54:37
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 13:10:31
from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField

from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')
