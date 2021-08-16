#! python3
# link-verification.py will take a URL and attempt to download every linked page on the page
# The program will flag any pages that have links which don't work

from pathlib import Path
import pyinputplus as pyip
import bs4
import requests
import time
import logging
import os


# Creating file for logging 
logging.basicConfig(filename='link_ver_logs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Getting URL input from User
url = pyip.inputStr('URL: ')

# Gets contents of page and stores in requests obj
res1 = requests.get(url)
res1.raise_for_status()

# Creates soup object to parse HTML and find all <a> elements with an href
soup = bs4.BeautifulSoup(res1.text, 'html.parser')
links_list = soup.find_all('a', href=True)

# Uses enumerate to get each link in the list of links stored in links_list. Then tries to download each link using requests
# If download fails, exception code notifies user that the link failed to give feedback to requests object, and hence is invalid
for index, link in enumerate(links_list):
    try:
        link_modified = f"https://en.wikipedia.org{link['href']}"
        print(f'Downloading {link_modified}...')

        res2 = requests.get(link_modified)
        link_file = open(f'{Path.home()}\\VSCPythonProjects\\smallprojects\\link #{index}', 'wb')
        res2.raise_for_status()

        for chunk in res2.iter_content(100000):
            link_file.write(chunk)

        link_file.close()
        print(f"{link['href']} was a valid link. Contents saved.")

    except Exception as exc:
        print(f"{link['href']} is an invalid link.")

