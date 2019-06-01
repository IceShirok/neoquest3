from flask import render_template
from app import app
from app.models import User, Pet
from app.pet import pet_desc


@app.route('/')
def index():
    user = User.query.filter_by(username='katya').first_or_404()
    pet = Pet.query.filter_by(name='Wulgar').first_or_404()

    return render_template('index.html',
                           title='Pet Page',
                           pet=pet,
                           user=user,
                           pet_desc=pet_desc)
