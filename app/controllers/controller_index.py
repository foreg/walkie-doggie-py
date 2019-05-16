from flask import render_template, flash, redirect, url_for,request
from flask_login import current_user, login_user, logout_user
from app.forms import LoginForm, RegistrationForm, UserProfileForm, PetProfileForm
from app.models import User, Role, User_roles, Pet
from app.token import generate_confirmation_token, confirm_token
from app.email import send_email
from app.utils import login_required, fill_entity
from app import db
import datetime


def Index():
    return render_template('index.html')

def Walker():
    return render_template('walker.html')

def UserAgreement():
    return render_template('UserAgreement.html') 

@login_required
def UserProfile():
    user = current_user
    return render_template('roles.html', user=user)    

def Login():
    if current_user.is_authenticated:
        # return render_template('profile.html', user=user, form=formUser)
        return redirect(url_for('profile', user=user))
    email = request.args.get('email')
    form = LoginForm(email=email)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильный логин или пароль!','danger')
            return redirect(url_for('login', email=form.email.data))
        if not user.isConfirmed:
            flash('Подтвердите свой email, перейдя по ссылке в письме','info')
            return redirect(url_for('login', email=form.email.data))
        login_user(user, remember=form.remember_me.data)
        # return render_template('profile.html', user=user, form=formUser)
        return redirect(url_for('profile'))
    return render_template('login.html', form=form)

def Register():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        token = generate_confirmation_token(user.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('activate.html', confirm_url=confirm_url)
        subject = "Пожалуйста, подтвердите свой e-mail."
        send_email(user.email, subject, html)

        user_roles = User_roles(user=user, role=Role.query.get(6)) # User
        db.session.add(user_roles)
        db.session.commit()
        flash('Вы успешно зарегистрировались!','success')

        return redirect(url_for('login', email=user.email))
    return render_template('register.html', form=form)

def Logout():
    logout_user()
    return render_template('index.html')

def Confirm(token):
    try:
        email = confirm_token(token)
    except:
        flash('Ссылка для подтверждения недействительна или просрочена.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.isConfirmed:
        flash('Аккаунт уже подтвержден. Пожалуйста, авторизуйтесь.', 'success')
    else:
        user.isConfirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('Аккаунт подтвержден!', 'success')
    return redirect(url_for('login', email=email))