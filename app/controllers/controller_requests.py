from flask import render_template, flash, redirect, url_for, request as flask_request, jsonify, Response
from flask_login import current_user
from sqlalchemy import and_
from app.forms import RequestForm, BetForm
from app.models import Pet, Request, Pet_requests, Bet, Walker
from app.utils import login_required, fill_entity
from app.constants import RequestStatuses, Roles
from app import db, scheduler
from datetime import datetime, timedelta


@login_required
def BetsOwnerHistory(user_id):
    user = current_user        
    bets = Bet.query.all()
    current_bets = []
    for bet in bets:
        if bet.request.status_id == RequestStatuses.auctionStarted and \
        bet.request.pets[0].pet.user_id == user_id and bet.request.auctionEndDate >= datetime.now():
            current_bets.append(bet)
    return render_template('bets_owner_history.html', user=user, current_bets=current_bets)

@login_required
def BetsHistory(user_id):
    user = current_user        
    bets = Bet.query.filter_by(walker_id=user_id).all()
    current_bets = []
    past_bets = []
    for bet in bets:
        if bet.request.status_id == RequestStatuses.auctionStarted:
            current_bets.append(bet)
        else:
            past_bets.append(bet)
    return render_template('bets_history.html', user=user, current_bets=current_bets, past_bets=past_bets)

@login_required
def RequestPage(pet_id, request_id):
    user = current_user        
    request = Request() if request_id == -1 else Request.query.filter_by(id=request_id).first() 
    pet = Pet.query.get(pet_id)
    request.address = pet.user.address
    request.walkStartDate = datetime.now()
    if request is None:
        flash('Заявка не найдена', 'danger')
        return redirect(url_for('pets'))
    form=RequestForm(obj=request)
    if request.status_id == None:
        if form.validate_on_submit():
            errors, successfully = fill_entity(request, form)
            print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(request, errors, successfully)) 
            request.auctionStartDate = datetime.now()
            request.auctionEndDate = request.walkStartDate - timedelta(hours=1)
            request.status_id = RequestStatuses.auctionStarted
            db.session.add(request)        
            db.session.commit()
            scheduler.add_job(func=EndRequestAuction, trigger='date', run_date=request.auctionEndDate, args=[request.id])
            pet_request = Pet_requests(pet_id=pet_id, request_id=request.id) if request_id == -1 else Pet_requests.query.filter_by(pet_id=pet_id, request_id=request.id).first() 
            db.session.add(pet_request)        
            db.session.commit()
            flash('Все изменения сохранены!', 'success')
            return redirect(url_for('current_requests',user=user))
        elif len(form.errors) > 0:
            flash('Проверьте правильность введенных данных', 'danger')
    else:
        if form.validate_on_submit():
            if flask_request.form['submit'] == 'Закончить выгул(выгульщик)':
                request.walkerEndMarkDate = datetime.now()
            if flask_request.form['submit'] == 'Закончить выгул(хозяин)':
                request.ownerEndMarkDate = datetime.now()
            if request.ownerEndMarkDate != None and request.walkerEndMarkDate != None:
                request.status_id = RequestStatuses.ended
            db.session.add(request)        
            db.session.commit()
    referrer = flask_request.headers.get("Referer")
    return render_template('request.html',user=user,form=form,request=request, referrer=referrer, now=datetime.now())

@login_required
def CurrentRequests():
    user = current_user
    if not user.check_role(Roles.walker):
        return redirect(url_for('index'))
    
    requests = Request.query.filter(and_(Request.auctionEndDate>=datetime.now(), Request.status_id==RequestStatuses.auctionStarted)).all()
    return render_template('current_requests.html', user=user,requests=requests)

@login_required
def BetForRequestPage(pet_id, request_id, bet_id):
    user = current_user        
    bet = Bet() if bet_id == -1 else Bet.query.filter_by(id=bet_id).first() 
    pet = Pet.query.get(pet_id)
    request = Request.query.get(request_id)
    if not user.check_role(Roles.walker):
        return redirect(url_for('index'))
    if request is None or bet is None:
        flash('Заявка не найдена', 'danger')
        return redirect(url_for('pets'))
    form=BetForm(obj=bet)
    if form.validate_on_submit():             
        errors, successfully = fill_entity(bet, form)
        print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(bet, errors, successfully)) 
        if request.status_id == RequestStatuses.auctionStarted:
            if int(bet.summ) >= request.lowest_bet().summ:
                flash('Нужно сделать ставку ниже, чем существующая', 'danger')
            else:
                bet.request_id = request.id
                bet.walker_id = user.id
                db.session.add(bet)        
                db.session.commit()
                flash('Ставка принята!', 'success')
                return redirect(url_for('current_requests',user=user))
        else:
            flash('Нельзя сделать ставку на аукцион, который уже закончился', 'danger')
    elif len(form.errors) > 0:
        flash('Проверьте правильность введенных данных', 'danger')
    return_to =  flask_request.args.get('return_to')
    referrer = url_for(return_to) if return_to else url_for('current_requests')
    return render_template('bet.html',user=user,form=form,bet=bet, referrer=referrer)

def EndRequestAuction(request_id):
    request = Request.query.get(request_id)
    request.status_id = RequestStatuses.auctionEnded
    request.walker_id = request.lowest_bet().walker_id
    request.finalPrice = request.lowest_bet().summ
    db.session.add(request)        
    db.session.commit()

# ALTER TABLE public.request ALTER COLUMN "auctionEndDate" TYPE timestamp USING "auctionEndDate"::timestamp;
# ALTER TABLE public.request ALTER COLUMN "auctionStartDate" TYPE timestamp USING "auctionStartDate"::timestamp;
# ALTER TABLE public.request ALTER COLUMN "ownerEndMarkDate" TYPE timestamp USING "ownerEndMarkDate"::timestamp;
# ALTER TABLE public.request ALTER COLUMN "walkStartDate" TYPE timestamp USING "walkStartDate"::timestamp;
# ALTER TABLE public.request ALTER COLUMN "walkerEndMarkDate" TYPE timestamp USING "walkerEndMarkDate"::timestamp;
