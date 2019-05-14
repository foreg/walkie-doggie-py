from flask import render_template, flash, redirect, url_for, request, jsonify, Response
from flask_login import current_user
from app.forms import PetProfileForm
from app.models import Pet, Breed, File, Pet_requests
from app.utils import login_required, fill_entity
from app import db
from app import images
from datetime import datetime


@login_required
def PetHistory(id):
    user = current_user        
    pet = Pet() if id == -1 else Pet.query.filter_by(id=id, archiveDate=None).first() 
    if pet is None:
        flash('Питомец не найден', 'danger')
        return redirect(url_for('pets'))
    requests = [row.request for row in Pet_requests.query.filter_by(pet_id=pet.id).all()]
    return render_template('pet_history.html', user=user, pet=pet, requests=requests)

@login_required
def PetProfile(id):
    user = current_user        
    pet = Pet() if id == -1 else Pet.query.filter_by(id=id, archiveDate=None).first() 
    if pet is None:
        flash('Питомец не найден', 'danger')
        return redirect(url_for('pets'))
    form=PetProfileForm(obj=pet)
    if form.validate_on_submit():             
        errors, successfully = fill_entity(pet, form)
        print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(pet, errors, successfully)) 
        if request.files['avatar'].filename != '':
            filename = images.save(request.files['avatar'])
            f = File(name=filename)
            db.session.add(f)
            db.session.commit()
            pet.avatar_id = f.id
        pet.user_id = user.id 
        db.session.add(pet)        
        db.session.commit()
        flash('Все изменения сохранены!', 'success')
        #return redirect(url_for('pets', pet.id)) #pet_id=
    elif len(form.errors) > 0:
        flash('Проверьте правильность введенных данных', 'danger')
    img = File.query.filter_by(id=pet.avatar_id).first()
    if img:
        img = img.name
    else:
        img = 'dog.png'
    breed = Breed.query.filter_by(id=pet.breed_id).first()
    if breed:
        breed = breed.name

    requests = [row.request for row in Pet_requests.query.filter_by(pet_id=pet.id).all()]
    return render_template('pet_profile.html',user=user,form=form, img='../static/uploads/images/' + img,pet=pet,breed=breed, requests=requests)

@login_required
def AddProfile(id):
    user = current_user        
    pet = Pet() if id == -1 else Pet.query.filter_by(id=id, archiveDate=None).first() 
    if pet is None:
        flash('Питомец не найден', 'danger')
        return redirect(url_for('pets'))
    form=PetProfileForm(obj=pet)
    if form.validate_on_submit():             
        errors, successfully = fill_entity(pet, form)
        print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(pet, errors, successfully)) 
        if request.files['avatar'].filename != '':
            filename = images.save(request.files['avatar'])
            f = File(name=filename)
            db.session.add(f)
            db.session.commit()
            pet.avatar_id = f.id
        pet.user_id = user.id 
        db.session.add(pet)        
        db.session.commit()
        flash('Все изменения сохранены!', 'success')
        return redirect(url_for('pets', pet_id=pet.id))
    elif len(form.errors) > 0:
        flash('Проверьте правильность введенных данных', 'danger')
    img = File.query.filter_by(id=pet.avatar_id).first()
    if img:
        img = img.name
    else:
        img = 'dog.png'
    breed = Breed.query.filter_by(id=pet.breed_id).first()
    if breed:
        breed = breed.name
    return render_template('add_pet.html',user=user,form=form, img='../static/uploads/images/' + img,pet=pet,breed=breed)


@login_required
def AllPets():
    user = current_user
    items = Pet.query.filter_by(archiveDate=None).order_by(Pet.name).all()
    for item in items:
        if item.avatar_info:
            item.img = item.avatar_info.name
    return render_template('all_pets.html',user=user,items=items)

@login_required
def ArchivePet(id):
    pet = Pet.query.filter_by(id=id, archiveDate=None).first() 
    if pet:
        pet.archiveDate = datetime.now()
        db.session.add(pet)
        db.session.commit()
    return Response(status=204)