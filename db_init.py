import json

from app import app, db
from app.models import User, Pet, VocationSkill

from sqlalchemy.sql import text as sa_text


db.engine.execute(sa_text('''DELETE FROM user''').execution_options(autocommit=True))
db.engine.execute(sa_text('''DELETE FROM pet''').execution_options(autocommit=True))
db.engine.execute(sa_text('''DELETE FROM vocation_skill''').execution_options(autocommit=True))


def create_basic():
    users = [
        User(id=0,
             username='katya',
             email='katya@example.com',  # pw is neopetsrulez
             password_hash='pbkdf2:sha256:50000$I4PTd3hq$ee3a77959d3ae21521ef4f1729987229144e61212f5afd316302f7545397e925'),
        User(id=1, username='arno', email='arno@example.com'),
    ]
    for user in users:
        db.session.add(user)

    pets = [
        Pet(
            name='Wulgar',
            owner='katya',
            species='Lupe',
            color='Yellow',
            gender=1,
            level=1,
            max_health=6,
            current_health=6,
            strength=5,
            movement=7,
            defense=8,
            intelligence=11,
            hunger=6,
            mood=4,
            vocation=None,
        ),
        Pet(
            name='Devon',
            owner='katya',
            species='Techo',
            color='Shadow',
            gender=1,
            level=1,
            max_health=8,
            current_health=8,
            strength=5,
            movement=12,
            defense=8,
            intelligence=9,
            hunger=6,
            mood=4,
            vocation=None,
        ),
        Pet(
            name='Katya',
            owner='katya',
            species='Cybunny',
            color='Blue',
            gender=0,
            level=1,
            max_health=10,
            current_health=10,
            strength=8,
            movement=6,
            defense=8,
            intelligence=9,
            hunger=6,
            mood=4,
            vocation=None,
        ),
    ]
    for pet in pets:
        db.session.add(pet)

    with open('data/skills.json') as f:
        skills_r = f.readlines()
        for skill in skills_r:
            skill_j = json.loads(skill)
            for level in skill_j['levels']:
                skill_db = VocationSkill(
                    skill_name=skill_j['name'],
                    level=int(level),
                    skill_level_name=skill_j['levels'][level],
                    vocation=skill_j['type'],
                    description=skill_j['desc']
                )
                db.session.add(skill_db)

    db.session.commit()


def create_with_full_party():
    create_basic()

    pets = [
        Pet(
            name='Hilga',
            owner='katya',
            species='Moehog',
            color='Green',
            gender=0,
            level=1,
            max_health=9,
            current_health=9,
            strength=8,
            movement=7,
            defense=8,
            intelligence=5,
            hunger=6,
            mood=4,
            vocation=None,
        ),
    ]
    for pet in pets:
        db.session.add(pet)

    Pet.query.filter_by(name='Wulgar', owner='katya').first().vocation = 'mage'
    Pet.query.filter_by(name='Devon', owner='katya').first().vocation = 'warrior'
    Pet.query.filter_by(name='Katya', owner='katya').first().vocation = 'cleric'
    Pet.query.filter_by(name='Hilga', owner='katya').first().vocation = 'ranger'

    db.session.commit()


if __name__ == '__main__':
    # create_basic()
    create_with_full_party()
