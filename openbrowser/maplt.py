#! python3
# mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard

import pyperclip as pyip
import webbrowser
import sys


if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyip.paste()


webbrowser.open(f'https://www.google.com/maps/place/{address}')

