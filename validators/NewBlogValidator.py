from flask_wtf import FlaskForm
from wtforms import StringField, validators


class NewBlogValidator(FlaskForm):
    blog_text = StringField('Post Text', [validators.InputRequired()])
