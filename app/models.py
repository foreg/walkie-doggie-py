from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
import datetime


class Role(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    key=db.Column(db.String(25))
    name=db.Column(db.String(50))
    users = db.relationship('User_roles', backref='role', lazy='dynamic')

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    surname=db.Column(db.String(50))
    name=db.Column(db.String(50))
    middlename=db.Column(db.String(50))
    vkid = db.Column(db.Integer)
    address=db.Column(db.Text)
    phone=db.Column(db.String(11))
    info=db.Column(db.Text)
    creationDate=db.Column(db.DateTime(4), default=datetime.datetime.now())
    deletionDate=db.Column(db.DateTime(4))
    lastLoginDate=db.Column(db.DateTime(4))
    isConfirmed=db.Column(db.Boolean, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    roles = db.relationship('User_roles', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.surname) 

class Walker(User):
    __tablename__='walkers'
    id_walker = db.Column(db.Integer, db.ForeignKey('user.id'))
    address_pr=db.Column(db.Text)
    address_reg=db.Column(db.Text)
    height=db.Column(db.String(3))
    weight=db.Column(db.String(10))
    gender=db.Column(db.String(10))
    rating=db.Column(db.Integer)
    series=db.Column(db.String(4))
    number=db.Column(db.String(6))
    issuedBy=db.Column(db.Text)
    issueDate=db.Column(db.DateTime(4))
    birthDate=db.Column(db.DateTime(4))
    score=db.Column(db.Integer)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
class User_roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))