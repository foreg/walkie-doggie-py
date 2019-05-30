from flask import render_template, flash, redirect, url_for,request
from flask_login import current_user
from app.forms import ReviewForm, ViolationForm
from app.models import User, Review
# , Violation
from app.utils import login_required, fill_entity
from app import db
import datetime

@login_required
def Review():
    user = current_user
    # review = Review() if id == -1 else Review.query.filter_by(id=id).first() 
    form = ReviewForm(obj=user)
    if form.validate_on_submit():          
        errors, successfully = fill_entity(user, form)
        print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(user, errors, successfully)) 
        user.user_id = user.id 
        db.session.add(user)  
        db.session.commit()
        flash('Все изменения сохранены!', 'success')
        # return redirect(url_for('pets', pet_id=pet.id))
    elif len(form.errors) > 0:
        flash('Проверьте правильность введенных данных', 'danger')
    return render_template('review.html', user=user,form=form)

@login_required
def Violation():
    user = current_user
    form = ViolationForm(obj=user)
    if form.validate_on_submit():
        errors, successfully = fill_entity(user, form)
        print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(user, errors, successfully)) 
        db.session.commit()
        flash('Все изменения сохранены!', 'success')
        # return redirect(url_for('pets', pet_id=pet.id))
    elif len(form.errors) > 0:
        flash('Проверьте правильность введенных данных', 'danger')
    return render_template('violation.html', user=user,form=form)


