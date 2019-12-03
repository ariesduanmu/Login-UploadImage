# -*- coding: utf-8 -*-

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