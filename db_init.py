from app import app, db
from app.models import User, Pet

from sqlalchemy.sql import text as sa_text


db.engine.execute(sa_text('''DELETE FROM user''').execution_options(autocommit=True))
db.engine.execute(sa_text('''DELETE FROM pet''').execution_options(autocommit=True))


users = [
    User(username='katya', email='katya@example.com'),
    User(username='arno', email='arno@example.com'),
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
    ),
]
for pet in pets:
    db.session.add(pet)


db.session.commit()
