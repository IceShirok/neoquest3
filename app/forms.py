from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CreatePetForm(FlaskForm):
    pet_list = [
        'Acara', 'Aisha', 'Blumaroo', 'Bori', 'Bruce', 'Buzz', 'Chia', 'Chomby', 'Cybunny', 'Draik', 'Elephante',
        'Eyrie', 'Flotsam', 'Gelert', 'Gnorbu', 'Grarrl', 'Grundo', 'Hissi', 'Ixi', 'Jetsam', 'Jubjub', 'Kacheek',
        'Kau', 'Kiko', 'Koi', 'Korbat', 'Kougra', 'Krawk', 'Kyrii', 'Lenny', 'Lupe', 'Lutari', 'Meerca', 'Moehog',
        'Mynci', 'Nimmo', 'Ogrin', 'Peophin', 'Poogle', 'Pteri', 'Quiggle', 'Ruki', 'Scorchio', 'Shoyru', 'Skeith',
        'Techo', 'Tonu', 'Tuskaninny', 'Uni', 'Usul', 'Wocky', 'Xweetok', 'Yurble', 'Zafara',
    ]
    pet_list_form = map(lambda p: (p, p), pet_list)
    name = StringField('Name', validators=[DataRequired()])
    species = SelectField('Species', choices=pet_list_form, validators=[DataRequired()])
    color = SelectField('Color', choices=[('Red', 'Red'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue')], validators=[DataRequired()])
    gender = SelectField('Gender', choices=[(0, 'Female'), (1, 'Male')], validators=[DataRequired()])

    submit = SubmitField('Hire a New Adventurer!')
