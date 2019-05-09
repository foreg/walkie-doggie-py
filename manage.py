from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import Role, User, Breed, Status
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

def seedRequestStatuses():
    status1 = Status(id=1, key='created', name='Заявка создана')
    status2 = Status(id=2, key='auctionStarted', name='Аукцион начался')
    status3 = Status(id=3, key='auctionEnded', name='Аукцион закончился')
    status4 = Status(id=4, key='ended', name='Заявка завершена')
    db.session.add(status1)
    db.session.add(status2)
    db.session.add(status3)
    db.session.add(status4)
    db.session.commit()
    print('seedStatuses done')

def seedUsers():
    user = User(email='1', password_hash='1')
    db.session.add(user)
    db.session.commit()
    print('seedUsers done')

def seedBreeds():
    breed1 = Breed(name='овчарка', info='описание овчарка')
    breed2 = Breed(name='мопс', info='описание мопс')
    breed3 = Breed(name='сиба-ину', info='описание сиба-ину')
    db.session.add(breed1)
    db.session.add(breed2)
    db.session.add(breed3)
    db.session.commit()
    print('seedBreeds done')

if __name__ == "__main__":
    #seedRoles()
    #seedUsers()
    #seedBreeds()
    #seedRequestStatuses()
    # Uncomment one or more of the folowing strings to seed dedicated tables
    # and then run python manage.py in commandLine
    
    
