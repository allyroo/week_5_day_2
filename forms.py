from flask_wtf import FlaskForm
from wtforms import Stringfield, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password - PasswordField('Password', validators = [DataRequired(), Email()])
    submit_button = SubmitField()