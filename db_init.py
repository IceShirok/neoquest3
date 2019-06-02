from app import app, db
from app.models import User, Pet

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
        color='Desert',
        gender=1,
        level=1,
        max_health=6,
        current_health=6,
        strength=6,
        movement=7,
        defense=8,
        intelligence=9,
        hunger=6,
        mood=4,
    ),
]
for pet in pets:
    db.session.add(pet)


db.session.commit()
