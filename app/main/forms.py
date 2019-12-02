# -*- coding: utf-8 -*-
# @Author: ariesduanmu
# @Date:   2019-03-31 01:17:45
# @Last Modified by:   Li Qin
# @Last Modified time: 2019-12-02 13:38:52
from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired

from flask_wtf.file import FileField
from flask_wtf.file import FileRequired

class ImportDataForm(FlaskForm):
    info = StringField('Info', validators=[DataRequired()])
    picture = FileField(validators=[FileRequired()])
    submit = SubmitField('Submit')