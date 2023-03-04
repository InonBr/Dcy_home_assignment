from flask_wtf import FlaskForm
from wtforms import StringField, validators


class NewPostValidator(FlaskForm):
    post_text = StringField('Post Text', [validators.InputRequired()])
