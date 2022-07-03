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


class EditForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Change')


class DeleteForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Delete')
