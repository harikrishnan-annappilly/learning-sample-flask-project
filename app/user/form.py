from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Login')


class DeleteForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Delete')
