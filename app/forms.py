from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    ignored_fields = set(['submit', 'csrf_token', 'remember_me'])

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', 
        validators=[DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    ignored_fields = set(['submit', 'csrf_token', 'password2', 'recaptcha'])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class UserProfileForm(FlaskForm):
    surname= StringField('Surname')
    name= StringField('Name')
    middlename= StringField('Middlename')
    address=StringField('Addres')
    phone=StringField('Phone')
    info=StringField('Text')
    submit = SubmitField('Save')
    
    ignored_fields = set(['submit', 'csrf_token'])