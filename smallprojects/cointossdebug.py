import random
import logging
from pathlib import Path

coinlogs_debug = Path(f'{Path.home()}\\VSCPythonProjects\\logs\\coinlogs.txt')
logging.basicConfig(filename=coinlogs_debug, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug(f'Toss value is: {toss}')
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')