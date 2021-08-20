#! python3
# remove_csv_header.py - Removes the headers from .csv files.

from pathlib import Path
import os 
import csv

# Creates a seperate folder for modified .csv files.
os.makedirs(f'{Path.home()}\\small-projects-python\\CSV_Projs\\header_removed', exist_ok=True)

# Directory path will vary on different systems.
dirs = os.listdir(f'{Path.home()}\\small-projects-python\\CSV_Projs\\header_csvs')

# Finds all the csv files inside the directory given through the dirs variable and operate on each of them.
for dir in dirs:
    if dir.endswith('.csv'):
        print(f'Removing header from {dir}...')
        original_csv_file = open(f'{Path.home()}\\small-projects-python\\CSV_Projs\\header_csvs\\{dir}')
        file_reader = csv.reader(original_csv_file)
        csv_rows = []
        for row in file_reader:
            if file_reader.line_num == 1:
                continue
            else:
                csv_rows.append(row)
        original_csv_file.close()

        new_csv_file = open(f'{Path.home()}\\small-projects-python\\CSV_Projs\\header_removed\\modified_{dir}', 'w', newline='')
        new_csv_file_writer = csv.writer(new_csv_file)
        for csv_row in csv_rows:
            new_csv_file_writer.writerow(csv_row)
        new_csv_file.close()
    else:
        continue
    



