from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.forms import UserProfileForm,WalkerProfileForm
from app.models import load_user, Walker
from app.utils import login_required, fill_entity
from app.constants import Roles



def Test():
    return render_template('test.html')

@login_required
def OwnerProfile(db):
    if current_user.is_authenticated:
        user = current_user
        form = UserProfileForm(obj=user)
        if form.validate_on_submit():
            errors, successfully = fill_entity(user, form)
            print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(user, errors, successfully))   
            db.session.add(user)
            db.session.commit()
            user.add_role(Roles.owner)
            return render_template('profile.html', form=form)        
        return render_template('profile.html', form=form)
    return redirect(url_for('login'))

@login_required
def WalkerProfile(db):
    if current_user.is_authenticated:
        user = current_user
        walker = user.walker_info if user.walker_info else Walker()
        form = WalkerProfileForm(obj=walker)
        if form.validate_on_submit():
            aliases = {
                'addresspr': 'address_pr',
                'addressreg': 'address_reg',
            }
            errors, successfully = fill_entity(walker, form, aliases=aliases)
            print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(walker, errors, successfully))   
            db.session.add(walker)
            user.walker_info = walker
            user.add_role(Roles.walker)
            db.session.add(user)
            db.session.commit()
            return render_template('walker_profile.html', form=form)        
        return render_template('walker_profile.html', form=form)
    return redirect(url_for('login'))