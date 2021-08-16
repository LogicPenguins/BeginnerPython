import random

def class_buff(chosen_class):
    character_class = {
        'warrior': {
            'Health': random.randint(30, 45),
            'Strength': random.randint(5, 10),
            'Speed': random.randint(1, 4),
            'Intelligence': random.randint(3, 6),
            'Precision': random.randint(2, 5),
            'Magic': 0
        },
        'archer': {
            'Health': random.randint(15, 25),
            'Strength': random.randint(1, 4),
            'Speed': random.randint(5, 10),
            'Intelligence': random.randint(6, 13),
            'Precision': random.randint(5, 10),
            'Magic': 0
        },
        'mage': {
            'Health': random.randint(17, 30),
            'Strength': random.randint(1, 4),
            'Speed': random.randint(2, 4),
            'Intelligence': random.randint(12, 15),
            'Precision': random.randint(3, 9),
            'Magic': random.randint(3, 10)
        }

    }

    print(f'''
Health: {character_class[chosen_class]['Health']}
Strength: {character_class[chosen_class]['Strength']}
Speed: {character_class[chosen_class]['Speed']}
Intelligence: {character_class[chosen_class]['Intelligence']}
Precision: {character_class[chosen_class]['Precision']}
Magic: {character_class[chosen_class]['Magic']}
    ''')



