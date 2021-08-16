from pathlib import Path 
import pyinputplus as pyip
import time
import re 
import sys


print('''
Welcome to the madlibs program. We will ask you some questions and present 
text to you from any given existing file. You will have maximum 60 seconds 
to answer each question. If you exceed this 60 second timer, the program 
will shut off and assume you have gone idle. Thank you for using the program 
and we hope you enjoy it.
''')
time.sleep(5)

file_input = pyip.inputStr('What file would you like to recreate? ', timeout=60)

madlib_file = str(f'{file_input}.txt')
path = Path(f'{Path.home()}\\{madlib_file}')

try:
    if path.exists():
        madlib_open = open(f'{Path.home() / madlib_file}', 'r')
        print('\nCurrent text in file: \n\n')
        file_lines = madlib_open.readlines()
        final_string = ""

        for line in file_lines:
            final_string += line

        print(final_string)
        splitter = re.compile(r"[\w']+|[.,!?;]")
        first_modified_string = re.findall(splitter, final_string)
        madlib_open.close()

        print('\nProcessing...')
        time.sleep(3)
        print('\n\nNow we will begin the replacement process. Please mention what you would like to replace each type below with.')

        trigger_words = ['ADJECTIVE', 'NOUN', 'VERB']
        word_count = 0

        for word in first_modified_string:
            if word in trigger_words:
                word_count+=1
        time.sleep(2)

        for word in trigger_words:
            for count in range(word_count):
                if word in first_modified_string:
                    if word == 'ADJECTIVE':
                        word_index = first_modified_string.index(word)
                        replacement = pyip.inputStr(f'\nEnter an {word}: ', timeout=60)
                        first_modified_string[word_index] = replacement
                    if word == 'NOUN':
                        word_index = first_modified_string.index(word)
                        replacement = pyip.inputStr(f'\nEnter a {word}: ', timeout=60)
                        first_modified_string[word_index] = replacement
                    if word == 'VERB':
                        word_index = first_modified_string.index(word)
                        replacement = pyip.inputStr(f'\nEnter a {word}: ', timeout=60)
                        first_modified_string[word_index] = replacement

        for y, x in enumerate(first_modified_string):
            if x == ".":
                first_modified_string[y-1] += ".\n"
                first_modified_string.remove(x)
        
        second_modified_string = ' '.join(first_modified_string)
        third_modified_string = second_modified_string.split('\n')

        for line_num, line in enumerate(third_modified_string):
            third_modified_string[line_num] = line.strip()
        
        fourth_modified_string = ""
        for line in third_modified_string:
            fourth_modified_string += f'{line}\n'
        print(f'''
Your new modified text is: 
{fourth_modified_string}
        ''')
        
        madlib_open.close()
        time.sleep(3)
        print('What would you like to call the name of your new file?')
        new_file_name = pyip.inputStr('File Name: ', timeout=60)
        print('\nYour new file will be saved in the current workspace folder on your Desktop.')
        new_file = open(f"{new_file_name}.txt", "w")
        for line in third_modified_string:
            new_file.write(f'{line}\n')
        new_file.close()
        new_file = open(f"{new_file_name}.txt", "r")
        new_file_content = new_file.read()
        print(f'\nContents of the new file: \n\n{new_file_content}')
        new_file.close()
        print('\nThank you for using our program. We hope you enjoyed it.')
    else:
        print("That is not a valid text file.")
except TimeoutError:
    print('Input took too long to receive. Please restart the program.')
    sys.exit()