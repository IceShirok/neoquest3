from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from app.pet import pet_desc


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class CreatePetForm(FlaskForm):
    pet_list_form = [
        ('Acara', 'Acara'),
        ('Aisha', 'Aisha'),
        ('Blumaroo', 'Blumaroo'),
        ('Cybunny', 'Cybunny'),
        ('Draik', 'Draik'),
        ('Eyrie', 'Eyrie'),
        ('Gelert', 'Gelert'),
        ('Ixi', 'Ixi'),
        ('Jubjub', 'Jubjub'),
        ('Kacheek', 'Kacheek'),
        ('Kau', 'Kau'),
        ('Korbat', 'Korbat'),
        ('Kougra', 'Kougra'),
        ('Kyrii', 'Kyrii'),
        ('Lupe', 'Lupe'),
        ('Moehog', 'Moehog'),
        ('Nimmo', 'Nimmo'),
        ('Poogle', 'Poogle'),
        ('Quiggle', 'Quiggle'),
        ('Scorchio', 'Scorchio'),
        ('Shoyru', 'Shoyru'),
        ('Techo', 'Techo'),
        ('Uni', 'Uni'),
        ('Wocky', 'Wocky'),
        ('Xweetok', 'Xweetok'),
        ('Yurble', 'Yurble'),
        ('Zafara', 'Zafara'),
    ]
    name = StringField('Name', validators=[DataRequired()])
    species = SelectField('Species', choices=pet_list_form, validators=[DataRequired()])
    color = SelectField('Color', choices=[('Red', 'Red'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue')], validators=[DataRequired()])
    gender = SelectField('Gender', choices=[(0, 'Female'), (1, 'Male')], coerce=pet_desc.gender_desc_to_val)

    submit = SubmitField('Hire a New Adventurer!')
