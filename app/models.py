from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User={}, email={}>'.format(self.username, self.email)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    species = db.Column(db.String(64))
    color = db.Column(db.String(64))
    gender = db.Column(db.Integer())
    level = db.Column(db.Integer())
    max_health = db.Column(db.Integer())
    current_health = db.Column(db.Integer())
    strength = db.Column(db.Integer())
    movement = db.Column(db.Integer())
    defense = db.Column(db.Integer())
    intelligence = db.Column(db.Integer())
    hunger = db.Column(db.Integer())
    mood = db.Column(db.Integer())

    def __repr__(self):
        return '<id={}, name={}>'.format(self.id, self.name)
