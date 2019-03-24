from flask import render_template, flash, redirect, url_for

def Index():
    return render_template('index.html')

def Login():
    return render_template('login.html')

def Register():
    return render_template('register.html')