from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

class TitleForm(FlaskForm):
    title = StringField('What should the title say?', validators=[DataRequired()])
    submit = SubmitField('Change Title')

class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')
