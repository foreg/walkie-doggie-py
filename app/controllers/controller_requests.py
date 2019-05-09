from flask import render_template, flash, redirect, url_for, request, jsonify, Response
from flask_login import current_user
from app.forms import RequestForm
from app.models import Pet, Request, Pet_requests
from app.utils import login_required, fill_entity
from app.constants import RequestStatuses
from app import db
from datetime import datetime, timedelta


@login_required
def RequestPage(pet_id, request_id):
    user = current_user        
    request = Request() if request_id == -1 else Request.query.filter_by(id=request_id).first() 
    pet = Pet.query.get(pet_id)
    request.address = pet.user.address
    if request is None:
        flash('Заявка не найдена', 'danger')
        return redirect(url_for('pets'))
    form=RequestForm(obj=request)
    if form.validate_on_submit():             
        errors, successfully = fill_entity(request, form)
        print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(request, errors, successfully)) 
        request.auctionStartDate = datetime.now()
        request.auctionEndDate = request.walkStartDate - timedelta(hours=1)
        request.status_id = RequestStatuses.created
        db.session.add(request)        
        db.session.commit()
        pet_request = Pet_requests(pet_id=pet_id, request_id=request.id) if request_id == -1 else Pet_requests.query.filter_by(pet_id=pet_id, request_id=request.id).first() 
        db.session.add(pet_request)        
        db.session.commit()
        flash('Все изменения сохранены!', 'success')
    elif len(form.errors) > 0:
        flash('Проверьте правильность введенных данных', 'danger')
    return render_template('request.html',user=user,form=form,request=request)