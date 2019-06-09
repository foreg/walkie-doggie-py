from flask import render_template, flash, redirect, url_for, request, send_from_directory
from flask_login import current_user
from app import app, db
from app.controllers import controller_index, controller_profile, controller_pets, controller_requests, controller_map, controller_review
from app.constants import Roles
from config import Config

@app.route('/test')
def test():
    return controller_profile.Test()

@app.route('/')
@app.route('/index')
def index():
    return controller_index.Index()

@app.route('/walker')
def walker():
    return controller_index.Walker()

@app.route('/walkerShow/<int(signed=True):walker_id>')
def show_walker_profile(walker_id):
    return controller_profile.ShowWalkerProfile(walker_id)

@app.route('/walkersRating')
def walkers_rating():
    return controller_requests.WalkersRating()

@app.route('/userAgreement')
def userAgreement():
    return controller_index.UserAgreement()

@app.route('/pets/<int(signed=True):pet_id>', methods=['GET', 'POST'])
def pet_profile(pet_id):
    return controller_pets.PetProfile(pet_id)

@app.route('/petShow/<int(signed=True):pet_id>', methods=['GET', 'POST'])
def pet_show(pet_id):
    return controller_pets.PetShow(pet_id)

@app.route('/pets/history/<int(signed=True):pet_id>', methods=['GET', 'POST'])
def pet_history(pet_id):
    return controller_pets.PetHistory(pet_id)

@app.route('/profile/history/<int(signed=True):user_id>', methods=['GET', 'POST'])
def bets_history(user_id):
    return controller_requests.BetsHistory(user_id)

@app.route('/profile/ownerHistory/<int(signed=True):user_id>', methods=['GET', 'POST'])
def bets_owner_history(user_id):
    return controller_requests.BetsOwnerHistory(user_id)

@app.route('/pets/<int:pet_id>/requests/<int(signed=True):request_id>', methods=['GET', 'POST'])
def pet_request(pet_id, request_id):
    return controller_requests.RequestPage(pet_id, request_id)

@app.route('/pets/<int:pet_id>/requests/<int:request_id>/<int(signed=True):bet_id>', methods=['GET', 'POST'])
def pet_request_bet(pet_id, request_id, bet_id):
    return controller_requests.BetForRequestPage(pet_id, request_id, bet_id)

@app.route('/pets/<int(signed=True):pet_id>', methods=['DELETE'])
def archive_pet(pet_id):
    return controller_pets.ArchivePet(pet_id)

@app.route('/add_pet/<int(signed=True):pet_id>', methods=['GET', 'POST'])
def add_pet(pet_id):
    return controller_pets.AddProfile(pet_id)

@app.route('/pets',methods=['GET', 'POST'])
def pets():
    return controller_pets.AllPets()

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    become = request.args.get('become')
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if become == 'walker':
        return controller_profile.WalkerProfile(db)
    if become == 'owner':
        return controller_profile.OwnerProfile(db)
    if become == 'user':
        return controller_index.UserProfile()
    if current_user.check_role(Roles.admin):
        pass
    if current_user.check_role(Roles.moderator):
        pass
    if current_user.check_role(Roles.expert):
        pass
    if current_user.check_role(Roles.walker):
        return controller_profile.WalkerProfile(db)
    if current_user.check_role(Roles.owner):
        return controller_profile.OwnerProfile(db)
    if current_user.check_role(Roles.user): # should be checked last since everyone has it
        return controller_index.UserProfile()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return controller_index.Login()

@app.route('/register',methods=['GET', 'POST'])
def register():
    return controller_index.Register()

@app.route('/logout')
def logout():
    return controller_index.Logout()

@app.route('/confirm/<string:token>')
def confirm_email(token):
    return controller_index.Confirm(token)

@app.route('/_uploads/images/<filename>') # не используется
def send_file(filename):
    # response = send_from_directory(app.config['UPLOADED_IMAGES_DEST'], filename)
    response = send_from_directory('app/static/uploads/images/', filename)
    return response

@app.route('/current_requests')
def current_requests():
    return controller_requests.CurrentRequests()

@app.route('/map')
def map():
    return controller_map.ShowMap()

@app.route('/getCoords')
def get_coords():
    return controller_map.GetCoords()

@app.route('/review/<int(signed=True):review_id>', methods=['GET', 'POST'])
def review(review_id):
    return controller_review.AddReview(review_id)

@app.route('/violation/<int(signed=True):violation_id>', methods=['GET', 'POST'])
def violation(violation_id):
    return controller_review.AddViolation(violation_id)
