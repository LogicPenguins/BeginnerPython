#! python3
# weburlsfinder.py - Finds the web links that begin with https:// or http:// in your clipboard

import pyperclip
import re

http_web_url = re.compile(r'https://\w+\..+|http://\w+\..+')

text = pyperclip.paste()

x = http_web_url.findall(text)

full_list = ""
for link in x:
    full_list += f"{link}\n"

if len(http_web_url.findall(text)) > 0:
    print(full_list)
else:
    print("There were no links in your clipboard.")