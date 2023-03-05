from flask_wtf import FlaskForm
from wtforms import StringField, validators


class BlogTextValidator(FlaskForm):
    blog_text = StringField('Post Text', [validators.InputRequired()])
