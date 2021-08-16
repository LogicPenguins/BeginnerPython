# This program will search for any given regex pattern in any given folder through user input

from pathlib import Path
import pyinputplus as pyip
import os
import re

file_input = pyip.inputStr('What directory would you like to search? Must be next to your home path: ')

p = Path(f'{Path.home()}\\{file_input}')


regex_pattern = re.compile(r'\w{3}\s{1}')
# Any regex pattern can be put in here. 
# I'm too lazy to put a userinput but it essentially does the same thing.

path_directories = os.listdir(p)

for directory in path_directories:
    if '.txt' in directory[-4:]:
        directory_text_file = open(f'{p}\\{directory}', 'r')
        regex_search_string = directory_text_file.read()
        patterns_found = regex_pattern.findall(regex_search_string)
        print(f"\n\n{('-' * 20)}\n\nPatterns found in text file {directory}:\n")
        for i in range(len(patterns_found)):
            print(f'Pattern #{i+1}: {patterns_found[i]}\n')
