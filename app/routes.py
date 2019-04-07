from flask import render_template, flash, redirect, url_for
from flask_login import login_required
from app import app, db
from app.controllers import controller_index, controller_profile

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

@app.route('/roles')
def roles():
    return controller_index.Roles()

@app.route('/profile', methods=['GET', 'POST'])
def userProfile():
    return controller_profile.UserProfile(db)

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