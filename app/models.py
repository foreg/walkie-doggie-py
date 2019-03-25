# todo write models in this file
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin
from app import login
class Role(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    key=db.Column(db.String(25))
    name=db.Column(db.String(50))
    #roles = db.relationship('User', backref='role', lazy='dynamic')
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    surname=db.Column(db.String(50))
    name=db.Column(db.String(50))
    middlename=db.Column(db.String(50))
    vkid = db.Column(db.Integer)
    addres=db.Column(db.Text)
    phone=db.Column(db.String(11))
    info=db.Column(db.Text)
    creationDate=db.Column(db.DateTime(4))
    deletionDate=db.Column(db.DateTime(4))
    lastLoginDate=db.Column(db.DateTime(4))
    isConfirmed=db.Column(db.Boolean)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

def __repr__(self):
    return '<User {}>'.format(self.username) 
    
class User_roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer)
    roles_fk = db.Column(db.Integer, db.ForeignKey('role.id'))
    users_fk = db.Column(db.Integer, db.ForeignKey('user.id'))