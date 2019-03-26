from flask import render_template, flash, redirect, url_for
from flask_login import login_required
from app import app, db
from app.controllers import controller_index, controller_profile


@app.route('/')
@app.route('/index')
@login_required
def index():
    return controller_index.Index()

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

@app.route('/confirm/<token>')
@login_required
def confirm_email():
    return controller_index.Confirm()