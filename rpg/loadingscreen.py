import time
import pyinputplus as pyip
import os
import sys
from start import starting

def loading_screen():
    print(f"\n\n{('━' * 140)}\n{(' ' * 58)} EXPEDITION\n{('━' * 140)}")

    game_going = False

    while game_going is False:
        game_start = pyip.inputStr('''\n
What would you like to do?
> Info
> Start
> Quit
> Load
''', timeout=120).lower()
        if game_start == 'start' or game_start == 's':
            confirm = pyip.inputYesNo('You are about to begin a new game. Are you sure you want to do this?(Y/N)\n', timeout=120).lower()
            if confirm == 'yes':
                print('Creating new Expedition...')
                time.sleep(5)
                os.system('cls')
                starting('Starting')
                game_going = True
            elif confirm == 'no':
                continue

        elif game_start == 'quit' or game_start == 'q':
            print('We hope you join our expedition next time. Have a good day.')
            sys.exit()
        elif game_start == 'info' or game_start == 'i':
            print('''
---Under Construction---
            ''')
        elif game_start == 'load' or game_start == 'l':
            print('Loading an old game goes here')

    '''
    print('Welcome to the world of Tartarus.')
    time.sleep(3)
    print('A beautiful land filled with forests, mountains, plains and many other areas waiting to be discovered.')
    time.sleep(4)
    print('Though these beauties prevail as the glee and happiness of those who reside here...')
    time.sleep(4)
    print('There has been a growing emptiness screaming from the trails of burden...')
    print('within dark places that adventurers refuse to set foot in.')
    time.sleep(8)
    print('This dark place, often called Vilemourse, is a land once inhabited by kings, nobles, and many richeous individuals.')
    time.sleep(4)
    print('However, some decades ago, a mythical dragon had re-awoken as par to the prophecy of Ol Eldrigar...')
    time.sleep(4)
    print('Which stated of such an incident occuring in the near future.')
    time.sleep(3)
    print('Though no one believed him at the time, he had taken it as his duty to find an adventurer who would heed to his words...')
    time.sleep(4)
    print('This dragon reigned chaos and death upon all those who he wished to rule over for several years.')
    time.sleep(4)
    print('Turning the bodies of his opposers into his mindless servants.')
    time.sleep(3)
    print('And corrupting all that was living in his territory, to an utter rashness.')
    time.sleep(4)
    print('Now it is your turn. Expeditioner. As the one chosen by Ol Eldrigar to save this world and to stop the corruption of the dragon from spreading...')
    time.sleep(5)
    '''
    print('Do you understand? (Y/N)')
    understand = pyip.inputYesNo().lower()
    if understand == 'yes':
        os.system('cls')
    elif understand == 'no':
        print('I will give you a minute to process all that I have said')
        time.sleep(2)
        print('Then we shall move on to the next step.')
        time.sleep(60)
        os.system('cls')
