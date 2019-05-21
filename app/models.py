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
    walker_id = db.Column(db.Integer, db.ForeignKey('walker.id'))
    walker_info = db.relationship('Walker', backref='user')
    avatar_id = db.Column(db.Integer, db.ForeignKey('file.id'))
    avatar_info = db.relationship('File', backref='user')
    pets = db.relationship('Pet', backref='user', lazy='dynamic')
    bets = db.relationship('Bet', backref='walker', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def check_role(self, role):
        for user_role in self.roles.all():
            if user_role.role_id == role:
                return True
        return False

    def add_role(self, role):
        if not self.check_role(int(role)):
            user_roles = User_roles(user=self, role=Role.query.get(int(role)))
            db.session.add(user_roles)
            db.session.commit()

    def __repr__(self):
        return '<User {}>'.format(self.surname) 

class Walker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    gender=db.Column(db.String(10))
    age=db.Column(db.Integer)
    weight=db.Column(db.String(10))
    info=db.Column(db.Text)
    avatar_info = db.relationship('File', backref='pet')
    archiveDate = db.Column(db.DateTime(4))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    breed_id = db.Column(db.Integer, db.ForeignKey('breed.id'))
    avatar_id = db.Column(db.Integer, db.ForeignKey('file.id'))

    requests = db.relationship('Pet_requests', backref='pet', lazy='dynamic')

class Breed(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50)) 
    info=db.Column(db.Text) 

    pets = db.relationship('Pet', backref='breed', lazy='dynamic')

    def __repr__(self):
        return '<Breed {}>'.format(self.id) 

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creationDate=db.Column(db.DateTime(), default=datetime.datetime.now())
    walkStartDate=db.Column(db.DateTime())
    walkDuration=db.Column(db.Integer)
    auctionStartDate=db.Column(db.DateTime())
    auctionEndDate=db.Column(db.DateTime())
    address=db.Column(db.Text)
    startingPrice=db.Column(db.Integer)
    finalPrice=db.Column(db.Integer)
    ownerEndMarkDate=db.Column(db.DateTime())
    walkerEndMarkDate=db.Column(db.DateTime())

    walker_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))

    pets = db.relationship('Pet_requests', backref='request', lazy='dynamic')
    bets = db.relationship('Bet', backref='request', lazy='dynamic')

    

    def lowest_bet(self):
        class Object(object):
            pass
        try:
            return min(self.bets.all(), key=lambda x: x.summ)
        except:
            obj = Object()
            setattr(obj, 'summ', float("inf"))
            setattr(obj, 'walker_id', -1)
            return obj
            
    
class Status(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    key=db.Column(db.String(50)) 
    name=db.Column(db.Text) 

    requests = db.relationship('Request', backref='status', lazy='dynamic')

class Bet(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    summ=db.Column(db.Integer)
    creationDate=db.Column(db.DateTime(4), default=datetime.datetime.now())

    request_id = db.Column(db.Integer, db.ForeignKey('request.id'))
    walker_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Pet_requests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'))
    request_id = db.Column(db.Integer, db.ForeignKey('request.id'))

# class Review(db.Model): 
#     id = db.Column(db.Integer, primary_key=True)
#     comment=db.Column(db.Text) 
#     rating=db.Column(db.Integer) 
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     walker_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     violations = db.relationship('Review_violations', backref='review', lazy='dynamic')


# class Violation(db.Model): 
#     id = db.Column(db.Integer, primary_key=True)
#     name=db.Column(db.String(50)) 
#     description=db.Column(db.Text) 

#     reviews = db.relationship('Review', backref='violation', lazy='dynamic')

# class Review_violations(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     review_id = db.Column(db.Integer, db.ForeignKey('review.id'))
#     violation_id = db.Column(db.Integer, db.ForeignKey('violation.id'))