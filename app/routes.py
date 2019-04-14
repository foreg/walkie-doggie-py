from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user
from app import app, db
from app.controllers import controller_index, controller_profile
from app.constants import Roles

@app.route('/test')
def test():
    return controller_profile.Test()

@app.route('/')
@app.route('/index')
def index():
    return controller_index.Index()

@app.route('/walker')
def walker():
    return controller_index.Walker()

@app.route('/pet', methods=['GET', 'POST'])
def pet_profile():
    return controller_index.PetProfile(db)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    become = request.args.get('become')
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if become == 'walker':
        return controller_profile.WalkerProfile(db)
    if become == 'owner':
        return controller_profile.OwnerProfile(db)
    if become == 'user':
        return controller_index.UserProfile()
    if current_user.check_role(Roles.admin):
        pass
    if current_user.check_role(Roles.moderator):
        pass
    if current_user.check_role(Roles.expert):
        pass
    if current_user.check_role(Roles.walker):
        return controller_profile.WalkerProfile(db)
    if current_user.check_role(Roles.owner):
        return controller_profile.OwnerProfile(db)
    if current_user.check_role(Roles.user): # should be checked last since everyone has it
        return controller_index.UserProfile()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return controller_index.Login()

@app.route('/register',methods=['GET', 'POST'])
def register():
    return controller_index.Register()

@app.route('/logout')
def logout():
    return controller_index.Logout()

@app.route('/confirm/<string:token>')
def confirm_email(token):
    return controller_index.Confirm(token)