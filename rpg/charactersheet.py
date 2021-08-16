import time
import pyinputplus as pyip
import random
from characterbuffs import class_buff

def character_sheet():
    print('I would like to get to know you better before I send you off on your journey.')
    time.sleep(2)
    print('So tell me, young fellow. What shall I call you?')
    name = pyip.inputStr('Name: ')
    print(f'Wonderful. It is a pleasure to finally meet you {name}.')
    time.sleep(2)
    print("I'm sure if you've been chosen as the hero to save our world, you must be apart of a prestigous class.")
    time.sleep(3)
    print(f'''
What is your class {name}?
> Warrior
> Archer
> Mage
''')
    class_picked = False
    while class_picked is False:
        player_class = pyip.inputStr('Class: ').lower()
        if player_class == 'warrior':
            print(f'Amazing. So you are a {player_class}, {name}.')
            class_picked = True
        elif player_class == 'archer':
            print(f'Amazing. So you are a {player_class}, {name}.')
            class_picked = True
        elif player_class == 'mage':
            print(f'Amazing. So you are a {player_class}, {name}.')
            class_picked = True
        else:
            print(f'What? I have never heard of the class {player_class}! Are you sure that is a class?')
    
    print('According to this sheet Ol Eldrigar sent me... these are your current stats.')
    class_buff(player_class)

    