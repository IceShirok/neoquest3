
def generate_image_url(species, color):
    return 'http://images.neopets.com/pets/{}_{}_baby.gif'.format(species.lower(), color.lower())


def get_level_desc(val):
    if 0 <= val <= 60:
        return "Normal"
    elif 61 <= val <= 90:
        return "High"
    elif 91 <= val <= 120:
        return "Very High"
    elif 121 <= val <= 180:
        return "Amazingly High"
    else:
        return "Too High to Count"


def get_strength_desc(val):
    if 1 <= val <= 1:
        return "Pathetic"
    elif 2 <= val <= 2:
        return "Weak"
    elif 3 <= val <= 4:
        return "Very Weak"
    elif 5 <= val <= 5:
        return "Frail"
    elif 6 <= val <= 6:
        return "Average"
    elif 7 <= val <= 9:
        return "Quite Strong"
    elif 10 <= val <= 11:
        return "Strong"
    elif 12 <= val <= 13:
        return "Very Strong"
    elif 14 <= val <= 14:
        return "Great"
    elif 15 <= val <= 16:
        return "Immense"
    elif 17 <= val <= 19:
        return "Titanic"
    elif 20 <= val <= 20:
        return "Herculean"
    elif 21 <= val <= 39:
        return "GREAT"
    elif 40 <= val <= 59:
        return "Excellent"
    elif 60 <= val <= 79:
        return "Awesome"
    elif 80 <= val <= 99:
        return "Amazing"
    elif 100 <= val <= 149:
        return "Legendary"
    else:
        return "Ultimate"


def get_movement_desc(val):
    if 1 <= val <= 1:
        return "Barely Moves"
    elif 2 <= val <= 2:
        return "Snail Pace"
    elif 3 <= val <= 3:
        return "Lazy"
    elif 4 <= val <= 4:
        return "Very Slow"
    elif 5 <= val <= 5:
        return "Slow"
    elif 6 <= val <= 6:
        return "Quite Slow"
    elif 7 <= val <= 8:
        return "Average"
    elif 9 <= val <= 9:
        return "Fast"
    elif 10 <= val <= 10:
        return "Speedy"
    elif 11 <= val <= 11:
        return "Super Fast"
    elif 12 <= val <= 12:
        return "Super Speedy"
    elif 13 <= val <= 13:
        return "Breakneck"
    elif 14 <= val <= 14:
        return "Cheetah"
    elif 15 <= val <= 16:
        return "Lightning"
    elif 17 <= val <= 17:
        return "Mach 1"
    elif 18 <= val <= 18:
        return "Mach 2"
    elif 19 <= val <= 19:
        return "Mach 3"
    elif 20 <= val <= 20:
        return "Mach 4"
    elif 21 <= val <= 39:
        return "Great"
    elif 40 <= val <= 59:
        return "Exellent"
    elif 60 <= val <= 79:
        return "Awesome"
    elif 80 <= val <= 99:
        return "Amazing"
    elif 100 <= val <= 149:
        return "Legendary"
    else:
        return "Ultimate"


def get_defense_desc(val):
    if 1 <= val <= 1:
        return "Defenceless"
    elif 2 <= val <= 2:
        return "Naked"
    elif 3 <= val <= 3:
        return "Vulnerable"
    elif 4 <= val <= 4:
        return "Very Poor"
    elif 5 <= val <= 5:
        return "Poor"
    elif 6 <= val <= 7:
        return "Below Average"
    elif 8 <= val <= 8:
        return "Average"
    elif 9 <= val <= 9:
        return "Armoured"
    elif 10 <= val <= 10:
        return "Tough"
    elif 11 <= val <= 12:
        return "Heavy"
    elif 13 <= val <= 14:
        return "Very Heavy"
    elif 15 <= val <= 15:
        return "Steel Plate"
    elif 16 <= val <= 16:
        return "Bullet Proof"
    elif 17 <= val <= 17:
        return "Semi-Demi Godly"
    elif 18 <= val <= 18:
        return "Demi-Godly"
    elif 19 <= val <= 19:
        return "Godly"
    elif 20 <= val <= 20:
        return "Beyond Godly"
    elif 21 <= val <= 39:
        return "Great"
    elif 40 <= val <= 59:
        return "Excellent"
    elif 60 <= val <= 79:
        return "Awesome"
    elif 80 <= val <= 99:
        return "Amazing"
    elif 100 <= val <= 149:
        return "Legendary"
    else:
        return "Ultimate"


def get_intelligence_desc(val):
    if 0 <= val <= 3:
        return "Dim Witted"
    elif 4 <= val <= 6:
        return "Dull"
    elif 7 <= val <= 10:
        return "Average"
    elif 11 <= val <= 14:
        return "Above Average"
    elif 15 <= val <= 18:
        return "Bright"
    elif 19 <= val <= 22:
        return "Clever"
    elif 23 <= val <= 26:
        return "Very Clever"
    elif 27 <= val <= 29:
        return "Brilliant"
    elif 30 <= val <= 33:
        return "Genius"
    elif 34 <= val <= 49:
        return "Super Genius"
    elif 50 <= val <= 54:
        return "Mega Genius"
    elif 55 <= val <= 59:
        return "Total Genius"
    elif 61 <= val <= 94:
        return "Master Genius"
    else:
        return "Ultimate Genius"


def get_hunger_desc(val):
    hunger_desc = {
        0: "Dying",
        1: "Starving",
        2: "Famished",
        3: "Very Hungry",
        4: "Hungry",
        5: "Not Hungry",
        6: "Fine",
        7: "Satiated",
        8: "Full Up",
        9: "Very Full",
        10: "Bloated",
        11: "Very Bloated",
    }
    return hunger_desc[val]


def get_mood_desc(val):
    mood_desc = {
        0: "Very Miserable",
        1: "Miserable",
        2: "Depressed",
        3: "Unhappy",
        4: "Content",
        5: "Happy",
        6: "Cheerful",
        7: "Extremely",
        8: "Happy",
        9: "Joyful",
        10: "Delighted!",
    }
    return mood_desc[val]