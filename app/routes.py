import json

from flask import render_template, url_for, flash, request
from werkzeug.urls import url_parse
from werkzeug.utils import redirect

from app import app, db
from app.forms import CreatePetForm, LoginForm
from app.models import User, Pet, VocationSkill
from app.pet import pet_desc

from flask_login import current_user, login_user, login_required
from flask_login import logout_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
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
                           skills=skills,
                           pet_desc=pet_desc)


@app.route('/tavern', methods=['GET', 'POST'])
@login_required
def view_tavern():
    return render_template('tavern.html',
                           title="The Tavern")


@app.route('/guild', methods=['GET', 'POST'])
@login_required
def view_pet_creation():
    pets = get_pets_by_user(current_user.username)
    if len(pets) >= 4:
        form = None
    else:
        form = CreatePetForm()
        if form.validate_on_submit():
            pet_name = form.name.data
            if Pet.query.filter_by(name=pet_name).first():
                flash('Pet name {} already exists!'.format(pet_name))
                return redirect(url_for('view_pet_creation'))
            pet = Pet(
                name=form.name.data,
                owner=current_user.username,
                species=form.species.data,
                color=form.color.data,
                gender=form.gender.data,
                level=1,
                max_health=6,
                current_health=6,
                strength=5,
                movement=7,
                defense=8,
                intelligence=11,
                hunger=6,
                mood=4,
                vocation=None
            )
            db.session.add(pet)
            db.session.commit()
            flash('Pet creation : name {}'.format(pet_name))
            return redirect(url_for('view_my_pets'))
    return render_template('guild.html',
                           title="Adventurers' Guild",
                           form=form)


@app.route('/exile')
@login_required
def view_pet_exile():
    pets = get_pets_by_user(current_user.username)
    return render_template('exile.html',
                           title="Black Market",
                           pets=pets,
                           pet_desc=pet_desc)


@app.route('/exile/pet/<string:name>')
def exile_pet(name):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    pet = Pet.query.filter_by(name=name, owner=current_user.username).first()
    if not pet:
        flash('You can only exile your own pets!')
    else:
        pet.owner = None
        db.session.commit()
    return redirect(url_for('view_my_pets'))


@app.route('/veterans')
@login_required
def view_pet_veterans():
    pets = Pet.query.filter_by(owner=None).all()
    return render_template('veterans.html',
                           title="Black Market",
                           pets=pets,
                           pet_desc=pet_desc)


@app.route('/recruit/pet/<string:name>')
def recruit_pet(name):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    pet = Pet.query.filter_by(name=name, owner=None).first()
    if not pet:
        flash('You can only recruit a pet without an owner!')
    else:
        pet.owner = current_user.username
        db.session.commit()
    return redirect(url_for('view_my_pets'))


@app.route('/party')
@login_required
def view_my_pets():
    return redirect(url_for('view_user', name=current_user.username))


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


@app.route('/pet/<string:name>', methods=['GET'])
def view_pet(name):
    pet = Pet.query.filter_by(name=name).first_or_404()

    return render_template('pet_page.html',
                           title='Pet Page',
                           pet=pet,
                           pet_desc=pet_desc)
