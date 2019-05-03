from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user
from app.forms import UserProfileForm,WalkerProfileForm
from app.models import load_user, Walker, File, Pet
from app.utils import login_required, fill_entity
from app.constants import Roles
from app import images


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
            if request.files['avatar'].filename != '':
                filename = images.save(request.files['avatar'])
                f = File(name=filename)
                db.session.add(f)
                db.session.commit()
                user.avatar_id = f.id
            db.session.add(user)
            db.session.commit()
            user.add_role(Roles.owner)
            flash('Все изменения сохранены!', 'success')
            # return render_template('profile.html', form=form, user=user)
        elif len(form.errors) > 0:
            flash('Проверьте правильность введенных данных', 'danger')
        img = File.query.filter_by(id=user.avatar_id).first()
        if img:
            img = img.name
        pets = Pet.query.filter_by(user_id=user.id, archiveDate=None).limit(3).all()
        return render_template('profile.html', form=form, user=user,
            img=url_for('static', filename='uploads/images/' + img), pets=pets)
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
            flash('Все изменения сохранены!', 'success')
            return render_template('walker_profile.html', form=form, user=user)
        elif len(form.errors) > 0:     
            flash('Проверьте правильность введенных данных', 'danger')
        return render_template('walker_profile.html', form=form, user=user)
    return redirect(url_for('login'))