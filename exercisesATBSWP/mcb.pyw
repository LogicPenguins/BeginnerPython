#! python3
# mcb.pyw - Saves and loads pieces o text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipbard to keyword.
#        py.exe mcb.pyw del <keyword> - Removes keyword from saved keyword data
#        py.exe mcb.pyw delall  - Removes all keywords from saved keyword data
#        py.exe mcb.pyw <keyword> - Loads keyword value to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

from pathlib import Path
import shelve
import pyperclip
import sys


mcb_shelf = shelve.open('mcb')

# TODO: Save Clipboard Content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'del':
        del mcb_shelf[f'{sys.argv[2]}']

elif len(sys.argv) == 2:
    # TODO: List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1].lower() == 'delall':
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    
    


mcb_shelf.close()

print(Path.cwd())