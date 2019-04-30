from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo

class TitleForm(FlaskForm):
    title = StringField('What should the title say?', validators=[DataRequired()])
    submit = SubmitField('Change Title')

class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    username = StringField("Username", validators=[DataRequired(), Email()])
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    age = IntegerField('Age')
    bio = TextAreaField("Bio")
    url = StringField("Profile Pic URL")
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")
