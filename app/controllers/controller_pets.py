from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.forms import PetProfileForm
from app.models import Pet, Breed
from app.utils import login_required, fill_entity
from app import db


@login_required
def PetProfile(id):
    user = current_user        
    pet = Pet() if id == -1 else Pet.query.filter_by(id=id).first() 
    if pet is None:
        flash('Питомец не найден', 'danger')
        return redirect(url_for('pet_profile', pet_id=-1)) # todo redirect to list of all pets instead of redirecting to 'create new' page
    form=PetProfileForm(obj=pet)
    if form.validate_on_submit():             
        errors, successfully = fill_entity(pet, form)
        print ("ENTITY {} FILLED WITH {} ERRORS, SUCCESSFULLY {}".format(pet, errors, successfully)) 
        pet.user_id = user.id 
        db.session.add(pet)        
        db.session.commit()
        flash('Все изменения сохранены!', 'success')
        return redirect(url_for('pet_profile', pet_id=pet.id))
    elif len(form.errors) > 0:
        flash('Проверьте правильность введенных данных', 'danger')
    return render_template('pet_profile.html',user=user,form=form)