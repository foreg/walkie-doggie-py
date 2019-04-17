from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField,DateField,SelectField,TextAreaField, FileField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo,Regexp
from app.models import User, Pet, Breed
from dateutil.relativedelta import relativedelta
from datetime import datetime


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
    middlename= StringField('Middlename')
    address=StringField('Addres',validators=[DataRequired(message='Заполните поле адрес!')])
    phone=StringField('Phone',validators=[DataRequired(message='Заполните поле телефон!'),Regexp('^8[\d]{10}$', message = "Введите номер в формате 8XXXXXXXXXX!")])
    info=TextAreaField('Text')
    avatar = FileField('Avatar')
    submit = SubmitField('Save')
    
    ignored_fields = set(['submit', 'csrf_token'])

class WalkerProfileForm(FlaskForm):
    addresspr= StringField('Addresspr',validators=[DataRequired(message='Заполните поле адрес проживания!')])
    addressreg= StringField('Addressreg',validators=[DataRequired(message='Заполните поле адрес регистрации!')])
    height= StringField('Height',validators=[DataRequired(message='Заполните поле рост!'),Regexp('^[12]\d{2}$', message = "Неправильно введен рост!")])
    weight= StringField('Weight',validators=[DataRequired(message='Заполните поле вес!'),Regexp('^\d{2,3}$', message = "Неправильно введен вес!")])
    gender= SelectField('Gender', choices=[('муж.', 'муж.'), ('жен.', 'жен.')])
    rating=StringField('Rating',validators=[DataRequired(message='Заполните поле рейтинг!')])
    series=StringField('Series',validators=[DataRequired(message='Заполните поле серия!'),Regexp('^[\d]{4}$', message = "Неправильно введена серия!")])
    number=StringField('Number',validators=[DataRequired(message='Заполните поле номер!'),Regexp('^[\d]{6}$', message = "Неправильно введен номер!")])
    issuedBy= StringField('IssuedBy',validators=[DataRequired(message='Заполните поле кем выдан!')])
    issueDate= DateField('IssueDate',validators=[DataRequired(message='Выберите дату!')])
    birthDate= DateField('BirthDate',validators=[DataRequired(message='Выберите дату!')])
    rating=StringField('Rating')
    score=StringField('Score')
    submit = SubmitField('Save')

    ignored_fields = set(['submit', 'csrf_token'])

    def validate_weight(self, weight):
        if (int(weight.data)) < 39:
            raise ValidationError('Минимальный вес 40 кг!')

    def validate_birthDate(self, birthDate):
        if (relativedelta(datetime.today(),birthDate.data).years) < 17:
            raise ValidationError('Чтобы стать выгульщиком,вам должно быть 18 лет!')

    def validate_issueDate(self, issueDate):
        today=datetime.today() 
        today=today.date() 
        if (issueDate.data) > today:
            raise ValidationError('Дата выдачи не может быть в будущем!')

    def __init__(self, **kwargs):
        # self.addresspr.data = self.addresspr.data or kwargs['obj'].address_pr
        # self.addressreg.data = self.addresspr.data or kwargs['obj'].address_reg
        kwargs['obj'].addresspr = kwargs['obj'].address_pr
        kwargs['obj'].addressreg = kwargs['obj'].address_reg
        super().__init__(**kwargs)

class PetProfileForm(FlaskForm):
    name= StringField('Name',validators=[DataRequired(message='Заполните поле кличка!')])
    gender= SelectField('Gender', choices=[('кобель', 'кобель'), ('сука', 'сука')])
    age= StringField('Age',validators=[DataRequired(message='Заполните поле возраст!'),Regexp('^[1-9]\d{0,1}$', message = "Неправильно введен возраст!")])
    weight= StringField('Weight',validators=[DataRequired(message='Заполните поле вес!'),Regexp('^[1-9]\d{0,1}$', message = "Неправильно введен вес!")])
    breed_id = SelectField('Breed', choices=[(x.id,x.name) for x in Breed.query.all()], coerce=int)
    info=TextAreaField('Text')
    avatar = FileField('Avatar')
    submit = SubmitField('Save')
    
    ignored_fields = set(['submit', 'csrf_token'])
