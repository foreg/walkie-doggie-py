from app import app, db
from flask import render_template, flash, redirect, url_for
from app.controllers import controller_index, controller_profile
from flask_login import login_required
# from app.controllers.controller_profile import UserProfile


@app.route('/')
@app.route('/index')
@login_required
def index():
    return controller_index.Index()

@app.route('/profile')
def UserProfile():
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