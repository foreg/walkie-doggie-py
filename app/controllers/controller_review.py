from flask import render_template, flash, redirect, url_for,request
from flask_login import current_user
from app.forms import ReviewForm, ViolationForm
from app.models import User, Review, Violation
from app.utils import login_required, fill_entity
from app import db
import datetime


@login_required
def AddReview(id):
    user = current_user
    review = Review() if id == -1 else Review.query.filter_by(id=id).first() 
    form = ReviewForm(obj=review)
    referrer = request.headers.get("Referer")
    if form.validate_on_submit():          
        errors, successfully = fill_entity(review, form)
        print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(review, errors, successfully)) 
        review.user_id = user.id
        review.walker_id = int(request.args.get('walker_id')) 
        db.session.add(review)  
        db.session.commit()
        flash('Спасибо за ваш отзыв!', 'success')
        return redirect(url_for('bets_owner_history', user_id = user.id))
    elif len(form.errors) > 0:
        flash('Проверьте правильность введенных данных', 'danger')
    return render_template('review.html', user=user,form=form,referrer = referrer)

@login_required
def AddViolation(id):
    user = current_user
    violation = Violation() if id == -1 else Violation.query.filter_by(id=id).first()
    form = ViolationForm(obj=violation)
    referrer = request.headers.get("Referer")
    if form.validate_on_submit():
        errors, successfully = fill_entity(violation, form)
        print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(violation, errors, successfully))
        db.session.add(violation)  
        db.session.commit()
        flash('Ваше нарушение будет обработано!', 'success')
        return redirect(url_for('bets_owner_history', user_id = user.id))
    elif len(form.errors) > 0:
        flash('Проверьте правильность введенных данных', 'danger')
    return render_template('violation.html', user=user,form=form,referrer = referrer)


