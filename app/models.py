from sqlalchemy import UniqueConstraint

from app import db


class User(db.Model):
    username = db.Column(db.String(64), primary_key=True, index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User={}, email={}>'.format(self.username, self.email)


class Pet(db.Model):
    name = db.Column(db.String(64), primary_key=True)
    owner = db.Column(db.String(64), index=True)
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


class VocationSkill(db.Model):
    __table_args__ = (
        UniqueConstraint("skill_name", "level", "vocation"),
    )
    skill_name = db.Column(db.String(64), index=True, primary_key=True)
    level = db.Column(db.Integer(), index=True, primary_key=True)
    vocation = db.Column(db.String(64), index=True, primary_key=True)
    skill_level_name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(256))
