from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class LogInValidator(FlaskForm):
    email = StringField('Email', [validators.InputRequired(), validators.Email()])
    password = PasswordField('Password', [validators.InputRequired()])