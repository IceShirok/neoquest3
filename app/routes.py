from flask import render_template, url_for
from werkzeug.utils import redirect

from app import app
from app.models import User, Pet
from app.pet import pet_desc


@app.route('/')
def index():
    return render_template('index.html',
                           title='NeoQuest Portal')


@app.route('/user/<string:name>')
def view_user(name):
    user = User.query.filter_by(username=name).first_or_404()
    pets = get_pets_by_user(user.username)

    return render_template('user_page.html',
                           title='Pet Page',
                           pets=pets,
                           user=user,
                           pet_desc=pet_desc)


@app.route('/user/<string:username>/pets', methods=['GET'])
def get_pets_by_user(username):
    pets_list = list()

    pets = Pet.query.filter_by(owner=username).all()
    for pet in pets:
        pets_list.append(pet)

    return pets_list


@app.route('/pet/<string:name>')
def view_pet(name):
    pet = Pet.query.filter_by(name=name).first_or_404()

    return render_template('pet_page.html',
                           title='Pet Page',
                           pet=pet,
                           pet_desc=pet_desc)
