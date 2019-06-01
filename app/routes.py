from flask import render_template
from app import app
from app.pet.pet import Pet


@app.route('/')
def index():
    my_pet = Pet(name='Wulgar', species='Lupe', color='Desert', gender='Male')
    return render_template('index.html',
                           title='Pet Page',
                           pet=my_pet)
