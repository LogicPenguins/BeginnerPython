import pyinputplus
import logging
import pprint

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


random_dict = {}

for i in range(100):
    print('HUh. Oh it was a success lol')
    random_dict.setdefault(f'bob #{i}', f'dropkicked {i} women lol')

    
for x in random_dict:
    print(f'{x} {random_dict[x]}')