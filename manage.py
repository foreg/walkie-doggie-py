from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import Role, User
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

def seedRoles():
    role1 = Role(id=1, key='admin', name='Администратор')
    role2 = Role(id=2, key='moderator', name='Модератор')
    role3 = Role(id=3, key='expert', name='Эксперт')
    role4 = Role(id=4, key='owner', name='Хозяин питомца')
    role5 = Role(id=5, key='walker', name='Выгульщик')
    role6 = Role(id=6, key='user', name='Пользователь')
    db.session.add(role1)
    db.session.add(role2)
    db.session.add(role3)
    db.session.add(role4)
    db.session.add(role5)
    db.session.add(role6)
    db.session.commit()
    print('seedRoles done')

def seedUsers():
    user = User(email='1', password_hash='1')
    db.session.add(user)
    db.session.commit()
    print('seedUsers done')

if __name__ == "__main__":
    # Uncomment folowing strings to seed dedicated tables
    # and then run python manage.py in commandLine
    #seedRoles()
    #seedUsers()
    
