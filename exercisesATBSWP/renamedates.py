# A program that changes all American styled dates in a given directory to European styled dates

from pathlib import Path
import shutil
import os
import pyinputplus as pyip
import sys
import re

def date_replacer(location):
    p = Path.home()
    location_modified = Path(p / f'{location}')
    if Path.exists(location_modified):
        american_date = re.compile(r'''
        ^(.*?)
        ((0|1)?\d)-
        ((0|1|2|3)?\d)-
        ((19|20)\d\d)
        (.*?)$
        ''', re.VERBOSE)
        location_directories = os.listdir(location_modified)    
        for directory in location_directories:
            result = american_date.search(directory)
            # result returns none if theres nothing inside, so the if statement can just be ran if the result isn't none
            if result:
                print(f'\nMatches in folder {directory}')
                before_part = result.group(1)
                month = result.group(2)
                day = result.group(4)
                year = result.group(6)
                after_part = result.group(8)
                modified_name = f'{before_part}{day}-{month}-{year}{after_part}'
                shutil.move(f'{location_modified}\\{directory}', f'{location_modified}\\spamLOLOL{modified_name}')
                print(f'{directory} succesfully renamed to {modified_name}\n')
            else:
                print(f'No matches in folder {directory}')
    else:
        print('Path does not exist. Please restart program.')
        sys.exit()

location_input = pyip.inputStr("What directory would you like to search? Directory must have home directory as parent: ", timeout=60)

date_replacer(location_input)