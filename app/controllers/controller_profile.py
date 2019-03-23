from flask import render_template, flash, redirect, url_for

def UserProfile(db):
    return render_template('profile.html')