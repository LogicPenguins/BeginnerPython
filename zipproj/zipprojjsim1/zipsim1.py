from pathlib import Path
import pyinputplus as pyip
import zipfile
import os
import time
import sys

# backup_to_zip function takes a folder parameter and compresses folder and contents into .zip file in user desired path location.
def backup_to_zip(func_folder):
    folder = os.path.abspath(func_folder)
    number = 1

    # Makes a name for the zip file, adding 1 to the {number} part of the formatted string to make sure file names are not reused
    while True:
        zip_file_destination = f'{Path.home()}\\{destination_input}\\{os.path.basename(folder)}_{number}.zip'
        zip_file_name = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zip_file_destination):
            break
        number += 1
    
    print(f'Creating {zip_file_name}...')
    time.sleep(2)

    # Creates the actual zip file using path.home() to get the home path of User's computer and then the destination input that
    # the user specified beforehand. Finally the name that was created using the base of the absolute path destination for the 
    # original folder input from the user
    backup_zip = zipfile.ZipFile(f'{Path.home()}\\{destination_input}\\{zip_file_name}', 'w')

    # Uses os.walk function to go through all folders, subfolders and files in specified folder and 
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            new_base = f'{os.path.basename(folder)}_'
            # Only saves text and python files
            if filename.endswith('.txt') or filename.endswith('.py'):
                backup_zip.write(f'{foldername}\\{filename}')
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            
    backup_zip.close()
    print('Done.')


folder_input = pyip.inputStr('What folder would you like to backup?\nFolder: ', timeout=60)

destination_input = pyip.inputStr('Where in your home directory would you like to store this zip?\nDestination: ', timeout=60)

folder_location = f'C:\\{folder_input}'

if os.path.exists(folder_location):
    backup_to_zip(folder_location)
else:
    print('Folder does not exist in C: drive. Please restart program.')
    sys.exit()