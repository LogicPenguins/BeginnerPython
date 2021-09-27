import send2trash
import os
from pathlib import Path

file_path = f'{Path.home()}\\small-projects-python\\Udemy Course'

for folder, sub_folders, files in os.walk(file_path):
    print(f'Currently looking at {folder}\n')
    print("The subfolders are: ")
    for sub_fold in sub_folders:
        print(f'Subfolder: {sub_fold}')
    print("\n")
    print("The files are: ")
    for f in files:
        print(f'Files: {f}')