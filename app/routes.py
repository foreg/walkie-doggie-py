from app import app, db
from flask import render_template, flash, redirect, url_for
from app.controllers import controller_index, controller_profile
# from app.controllers.controller_profile import UserProfile


@app.route('/')
@app.route('/index')
def index():
    return controller_index.Index()

@app.route('/profile')
def UserProfile():
    return controller_profile.UserProfile(db)

@app.route('/login')
def login():
    return controller_index.Login()

@app.route('/register')
def register():
    return controller_index.Register()