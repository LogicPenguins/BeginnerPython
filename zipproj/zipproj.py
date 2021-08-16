from pathlib import Path
import pyinputplus as pyip
import zipfile
import os
import time
import sys

def backup_to_zip(func_folder):
    folder = os.path.abspath(func_folder)

    number = 1
    while True:
        zip_file_destination = f'{Path.home()}\\{destination_input}\\{os.path.basename(folder)}_{number}.zip'
        zip_file_name = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zip_file_destination):
            break
        number += 1
        
    print(f'Creating {zip_file_name}...')
    time.sleep(2)
    backup_zip = zipfile.ZipFile(f'{Path.home()}\\{destination_input}\\{zip_file_name}', 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        time.sleep(2)
        backup_zip.write(foldername)
        for filename in filenames:
            new_base = f'{os.path.basename(folder)}_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))
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