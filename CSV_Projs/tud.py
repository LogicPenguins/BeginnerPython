from pathlib import Path
import csv

file_path = f"{Path.home()}\\small-projects-python\\CSV_Projs\\csv_files\\output2.csv"

output_file = open(file_path, 'w', newline='')
output_dict_writer = csv.DictWriter(output_file, ['Name', 'Pet', 'Phone'])
output_dict_writer.writeheader()
output_dict_writer.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
output_dict_writer.writerow({'Name': 'Bob', 'Phone': '555-9999'})
output_dict_writer.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})

output_file.close()

