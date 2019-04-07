from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.forms import UserProfileForm
from app.models import load_user
from app.utils import login_required, fill_entity



def Test():
    return render_template('test.html')

@login_required
def UserProfile(db):
    if current_user.is_authenticated:
        user = current_user
        form = UserProfileForm(obj=user)
        if form.validate_on_submit():
            errors, successfully = fill_entity(user, form)
            print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(user, errors, successfully))   
            db.session.add(user)
            db.session.commit()
            return render_template('profile.html', form=form)        
        return render_template('profile.html', form=form)
    return redirect(url_for('login'))