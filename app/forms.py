from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Regexp
from app.models import User
import re


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Заполните поле e-mail!')])
    password = PasswordField('Password', validators=[DataRequired(message='Заполните поле пароль!')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    ignored_fields = set(['submit', 'csrf_token', 'remember_me'])

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Заполните поле e-mail!'), Email(message='Неккоректный e-mail!')])
    password = PasswordField('Password', validators=[DataRequired(message='Заполните поле пароль!')])
    password2 = PasswordField('Repeat Password', 
        validators=[DataRequired(message='Повторите пароль!'), EqualTo('password', message='Введенные пароли не совпадают!')])
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')

    ignored_fields = set(['submit', 'csrf_token', 'password2', 'recaptcha'])

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Данный e-mail уже используется.')

    def validate_password(self, password):
        if len(password.data) < 6:
            raise ValidationError('Пароль должен содержать минимум 6 символов')
class UserProfileForm(FlaskForm):
    surname= StringField('Surname',validators=[DataRequired(message='Заполните поле фамилия!')])
    name= StringField('Name',validators=[DataRequired(message='Заполните поле имя!')])
    middlename= StringField('Middlename',validators=[DataRequired(message='Заполните поле отчество!')])
    address=StringField('Addres',validators=[DataRequired(message='Заполните поле адрес!')])
    phone=StringField('Phone',validators=[DataRequired(message='Заполните поле телефон!'),Regexp('^[8][\d]{10}', message = "Неправильно введен номер!")])
    info=StringField('Text',validators=[DataRequired(message='Заполните поле о себе!')])
    submit = SubmitField('Save')
    
    ignored_fields = set(['submit', 'csrf_token'])

    def validate_phone(self, phone): 
        if len(phone.data) != 11:
            raise ValidationError('Номер должен состоять из 11 цифр.')