#! python3
# searchpypi.py - Opens several search results

import requests, sys, webbrowser, bs4, time, logging, shelve
import pyinputplus as pyip
from pathlib import Path


# File initialization (Paths can be altered as needed)
pypi_log = f'{Path.home()}\\VSCPythonProjects\\logs\\searchpypi_log.txt' 
use_data = shelve.open('use_data')

# Logs and Data Setup
logging.basicConfig(filename=pypi_log, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
if len(use_data.keys()) != 0:
    value = use_data['log_num']
    value += 1
    use_data['log_num'] = value
else:
    use_data['log_num'] = 1

# Getting command prompt args and turning into request object
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Asking for amount of tabs to be opened through command prompt args
print('How many maximum search results would you like to open?')
tab_num = pyip.inputInt('Search Num: ') 

# Parsing request object with html parser and turning into soup object
# Selecting '.package-snippet' pattern in HTML and assigning to link_elems var as list of matches
# Iterating through amount of items in link_elems list and opening each individual url with a 0.5 rest period
soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.package-snippet')
num_open = min(tab_num, len(link_elems))
logging.debug(f"Program Log #{use_data['log_num']}")
print('Searching...')
for i in range(num_open):
    url_to_open = f"https://pypi.org{link_elems[i].get('href')}"
    logging.debug(f'URL #{i + 1}: {url_to_open}')
    print(f'Opening {url_to_open}...')
    time.sleep(0.5)
    webbrowser.open(url_to_open)