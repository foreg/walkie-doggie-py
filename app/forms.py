from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Заполните поле e-mail!')])
    password = PasswordField('Password', validators=[DataRequired(message='Заполните поле пароль!')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Заполните поле e-mail!'), Email(message='Неккоректный e-mail!')])
    password = PasswordField('Password', validators=[DataRequired(message='Заполните поле пароль!')])
    password2 = PasswordField('Repeat Password', 
        validators=[DataRequired(message='Повторите пароль!'), EqualTo('password', message='Введенные пароли не совпадают!')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Данный e-mail уже используется.')

    def validate_password(self, password):
        if len(password.data) < 6:
            raise ValidationError('Пароль должен содержать минимум 6 символов')
class UserProfileForm(FlaskForm):
    surname= StringField('Surname')
    name= StringField('Name')
    middlename= StringField('Middlename')
    address=StringField('Addres')
    phone=StringField('Phone')
    info=StringField('Text')
    submit = SubmitField('Save')