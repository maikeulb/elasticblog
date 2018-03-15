from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import User


class PostForm(FlaskForm):
    title = TextAreaField('Say something', validators=[DataRequired()])
    body = TextAreaField('Say something', validators=[DataRequired()])
    category_id = SelectField('Mount', coerce=int, validators=[DataRequired()])
    tags = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    q = StringField('Search', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)
