from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError
from .models import User
from jinja2 import Markup

class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[Email(),DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[Email(),DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')   

    def validate_email(form, field):
        same_email_user = User.query.filter_by(email=field.data).first()
        if same_email_user:
            raise ValidationError("Email is Already in Use")

