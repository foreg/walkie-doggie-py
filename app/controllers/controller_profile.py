from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.forms import UserProfileForm
from app.models import load_user


def UserProfile(db):
    if current_user.is_authenticated:
        form = UserProfileForm()
        user = current_user
        if form.validate_on_submit():
            user.surname = form.surname.data   
            user.name = form.name.data      
            user.middlename = form.middlename.data
            user.address = form.address.data    
            user.phone = form.phone.data     
            user.info = form.info.data      
            db.session.add(user)
            db.session.commit()
            return render_template('profile.html', form=form)        
        form.surname.data = user.surname
        form.name.data = user.name
        form.middlename.data = user.middlename
        form.address.data = user.address
        form.phone.data = user.phone
        form.info.data = user.info
        
        return render_template('profile.html', form=form)
    return redirect(url_for('login'))