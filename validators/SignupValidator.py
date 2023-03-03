from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class SignupValidator(FlaskForm):
    first_name = StringField('First Name', [validators.InputRequired()])
    last_name = StringField('Last Name', [validators.InputRequired()])
    email = StringField('Email', [validators.InputRequired(), validators.Email()])
    password = PasswordField('Password', [validators.InputRequired()])
    password_repeat = PasswordField('Repeat Password', [validators.InputRequired(),
                                                        validators.EqualTo('password', message='Passwords must match')])
