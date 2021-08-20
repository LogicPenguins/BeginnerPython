#! python3
# This is a loading screen lol

import time
import os

blank = '█'

for i in range(100):
    print('|', end='')
    print(f'{(i * blank)}', end='')
    print('|')
    time.sleep(0.000001)
    os.system('cls')