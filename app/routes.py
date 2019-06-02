import json

from flask import render_template, url_for, flash
from werkzeug.utils import redirect

from app import app
from app.forms import CreatePetForm
from app.models import User, Pet, VocationSkill
from app.pet import pet_desc


@app.route('/')
def index():
    return render_template('index.html',
                           title='NeoQuest Portal')


@app.route('/training')
def view_vocations():
    skills_raw = VocationSkill.query.all()
    skills = {}
    for skill in skills_raw:
        if skill.vocation not in skills:
            skills[skill.vocation] = {}
        vocation_skills = skills[skill.vocation]
        if skill.skill_name not in skills[skill.vocation]:
            vocation_skills[skill.skill_name] = {}
        vocation_skill = vocation_skills[skill.skill_name]
        vocation_skill['description'] = skill.description
        vocation_skill['vocation'] = skill.vocation
        if 'levels' not in vocation_skill:
            vocation_skill['levels'] = {}
        vocation_skill['levels'][skill.level] = skill.skill_level_name

        vocation_skills[skill.skill_name] = vocation_skill
        skills[skill.vocation] = vocation_skills
    print(skills)
    return render_template('training_grounds.html',
                           title='Training Grounds',
                           skills=skills)


@app.route('/guild', methods=['GET', 'POST'])
def view_pet_creation():
    form = CreatePetForm()
    if form.validate_on_submit():
        flash('Pet creation : name {}'.format(form.name.data))
        return redirect(url_for('index'))
    return render_template('guild.html',
                           title="Adventurers' Guild",
                           form=form)


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
