#! python3
# This program will open all links attached to the clipboard

import re
import webbrowser
import pyperclip as pyip

link_regex = re.compile(r'''
https://\S+
''', re.VERBOSE)

text = pyip.paste()

links = link_regex.findall(text)

for link in links:
    webbrowser.open(link)