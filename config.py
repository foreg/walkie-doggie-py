import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/wd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RECAPTCHA_PUBLIC_KEY = '6LdkJ5oUAAAAAKHBrRg9v0vv6nCMCyq84NrmuYu2'
    RECAPTCHA_PRIVATE_KEY = '6LdkJ5oUAAAAANrFAvYYgO5PfSb4orqwPhpGRatg'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'walkiedoggie72@gmail.com'
    MAIL_PASSWORD = 'dimasNorm444'
    MAIL_DEFAULT_SENDER = 'walkiedoggie72@gmail.com'