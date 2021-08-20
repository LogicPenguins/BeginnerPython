#! python3
# cer.py - Tabulates population and number of census tracts for each county.

import openpyxl, pprint
from pathlib import Path

print('Opening workbook...')
wb = openpyxl.load_workbook(f'{Path.home()}\\small-projects-python\\Excel_Projs\\xlsx_files\\censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

# Fill in county_data with each county's population and tracts.
print('Reading rows...')

for row in range(2, sheet.max_row + 1):

    # Each row in the spreadsheet has data for one census tract.
    state      = sheet[f'B{row}'].value
    county     = sheet[f'C{row}'].value
    population = sheet[f'D{row}'].value
    
    # Make sure the key for this state exists.
    county_data.setdefault(state, {})

    # Make sure the key for this county in this state exists.
    county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    county_data[state][county]['tracts'] += 1

    # Increase the county pop by the pop in this census tract.
    county_data[state][county]['pop'] += int(population)

# Open a new text file and write the contents of county_data to it.

print('Writing results...')
result_file = open(f'{Path.home()}\\VSCPythonProjects\\Census Excel Reader\\census2010.py', 'w')
result_file.write(f'all_data = {pprint.pformat(county_data)}')
result_file.close()
print('Done.')