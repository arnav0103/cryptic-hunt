from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo, ValidationError

from cryptic import app,db
from cryptic.models import User
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField("Log in")

class RegistrationForm(FlaskForm):
    fname = StringField('First Name',validators=[DataRequired()])
    lname = StringField('Last Name')
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    school_name = StringField('School Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match')])
    pass_confirm = PasswordField('confirm password',validators=[DataRequired()])
    submit = SubmitField('Register')

class PlayForm(FlaskForm):
    answer = StringField(label='solve the question',validators=[DataRequired()])
