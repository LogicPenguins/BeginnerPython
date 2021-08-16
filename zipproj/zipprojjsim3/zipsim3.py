import pyinputplus as pyip
import shutil
import sys
import os

# The function back_to_zip function will take a file path according to user input and then 
# delete whatever folder in your desired parent folder takes up the most space in bytes 
def backup_to_zip(func_folder):

    # creates a new variable assigned to the absolute path of folder passed in function parameter
    folder = os.path.abspath(func_folder)

    # list to hold values of size of each subfolder in parent folder 
    size_lst = []

    # loop that iterates through all files and subfolders of folder variable 
    # and adds sizes of each subfolder into the size_lst list
    for foldername, subfolders, filenames in os.walk(folder):
        folder_size = 0
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            folder_size += os.path.getsize(file_path)

        size_lst.append(folder_size)

    # list with first index set to 0 for later comparison use
    largest_size_lst = [0]

    # loop to iterate through each value in the list of folder sizes to find largest value in size_lst 
    # relative to largest_size_lst
    for i in range(len(size_lst)):
        if size_lst[i] > largest_size_lst[0]:
            largest_size_lst[0] = size_lst[i]
    
    # a for loop to once more walk through contents of user supplied folder and compare the individual size
    # of each folder to the value in largest_size_lst. Whichever folder size matches the value in 
    # largest_size_lst is the largest subfolder and is deleted
    for foldername, subfolders, filenames in os.walk(folder):
        folder_size_2 = 0
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            folder_size_2 += os.path.getsize(file_path)  
        if folder_size_2 == largest_size_lst[0]:
            print(foldername)
            shutil.rmtree(f'{foldername}')
    print('Task completed.')


print('What folder would you like to search?')
folder_input = pyip.inputStr('Folder: ', timeout=60)

folder_location = f'C:\\{folder_input}'

print(folder_location)
if os.path.exists(folder_location):
    backup_to_zip(folder_location)
else:
    print('Folder does not exist in C: drive. Please restart program.')
    sys.exit()