from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.fields import BooleanField, StringField, PasswordField, \
    SubmitField


class LoginForm(Form):
    username = StringField('Username: ', [validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired()])
    submit = SubmitField('Log In!')


class ForgotPasswordForm(Form):
    email = EmailField('E-mail address:', [validators.DataRequired()])
    submit = SubmitField('Get new password!')


class RegistrationForm(Form):
    username = StringField('Username: ', [validators.DataRequired()])
    first_name = StringField('First name: ', [validators.DataRequired()])
    last_name = StringField('Last name: ', [validators.DataRequired()])
    email = EmailField('E-mail address: ', [validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired()])
    password2 = PasswordField('Password again: ', [validators.DataRequired()])
    accept = BooleanField('Okay! ', [validators.DataRequired()])
    submit = SubmitField('Register!')
