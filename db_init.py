from app import app, db
from app.models import User, Pet

u = User(username='katya', email='katya@example.com')
db.session.add(u)
db.session.commit()

p = Pet(
    name='Wulgar',
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
)
db.session.add(p)
db.session.commit()
