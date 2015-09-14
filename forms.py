from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.fields import TextAreaField, BooleanField, StringField, \
    PasswordField, SubmitField


class SupportForm(Form):
    subject = StringField('Subject:', [validators.DataRequired()])
    email = EmailField('E-mail: ', [validators.DataRequired()])
    message = TextAreaField('Message: ', [validators.DataRequired()])
    submit = SubmitField('Send')


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
    accept = BooleanField(
        'Yeah, <a href="/privacy-policy">Privacy policy</a> is cool! ',
        [validators.DataRequired()])
    submit = SubmitField('Register!')
